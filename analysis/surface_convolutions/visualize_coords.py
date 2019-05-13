import argparse
import cortex
import os.path as op
import pickle as pkl
import numpy as np
import pandas as pd
import matplotlib.colors as colors

def main(derivatives,
         subject):

    pc_subject = 'odc.{}'.format(subject)

    coordinates = []
    for hemi in ['lh', 'rh']:
        coordinates.append(pd.read_pickle(op.join(derivatives,
                                                  'coordinate_patches',
                                                  'sub-{subject}',
                                                  'anat',
                                                  'sub-{subject}_hemi-{hemi}_coordinatepatch.pkl').format(**locals())))


    coordinates = pd.concat(coordinates, axis=0, ignore_index=True)
    print(coordinates.shape)
    print(coordinates.head())
    print(coordinates['x'].dtype)

    images = {}
    images['x'] = cortex.Vertex(coordinates['x'].values, 'odc.{}'.format(subject),
                      cmap='BROYG', vmin=-35, vmax=35)
    images['y'] = cortex.Vertex(coordinates['y'].values, 'odc.{}'.format(subject),
                      cmap='BROYG', vmin=-35, vmax=35)

    # PRFs
    prf_pars = np.load(op.join(derivatives, 'prf/vertices/sub-{subject}_desc-test2_prf_optim.npz').format(**locals()))

    r2 = prf_pars['r2']
    mask = r2 < 0.1

    angle = prf_pars['angle']
    angle[mask] = np.nan

    ecc = prf_pars['ecc']
    ecc[mask] = np.nan

    size = prf_pars['size']
    size[mask] = np.nan

    r2_max = np.max(r2)
    r2_max = 0.3
    r2_min = 0.05

    hsv_angle = np.ones((len(r2), 3))
    hsv_angle[:, 0] = angle.copy()
    hsv_angle[:, 1] = np.clip(r2 / r2_max * 2, 0, 1)
    hsv_angle[:, 2] = r2 > r2_min

    left_index = cortex.db.get_surfinfo(pc_subject).left.shape[0]
    angle_ = hsv_angle[:left_index, 0]
    hsv_angle[:left_index, 0] = np.clip(((angle_ + np.pi) - 0.25 * np.pi) / (1.5 * np.pi), 0, 1)
    angle_ = -hsv_angle[left_index:, 0].copy()
    angle_[hsv_angle[left_index:, 0] > 0] += 2 * np.pi
    angle_ = np.clip((angle_ - 0.25 * np.pi) / 1.5 / np.pi, 0, 1)
    hsv_angle[left_index:, 0] = angle_

    rgb_angle = colors.hsv_to_rgb(hsv_angle)

    alpha_angle = np.clip(r2 / r2_max * 2, r2_min/r2_max, 1)
    alpha_angle[alpha_angle < r2_min/r2_max] = 0
    alpha_angle = hsv_angle[:, 2]

    images['angle'] = cortex.VertexRGB(rgb_angle[:, 0], rgb_angle[:, 1], rgb_angle[:, 2],
                                       #alpha=np.ones(len(rgb_angle)),
                                       alpha=alpha_angle,
                                       subject=pc_subject)
    #images['r2'] = cortex.Vertex(prf_pars['r2'], pc_subject, cmap='inferno')
    images['ecc'] = cortex.Vertex(ecc, pc_subject, vmin=0,vmax=15, cmap='inferno')
    #images['angle_1d'] = cortex.Vertex(angle, pc_subject, vmin=-3.14, vmax=3.14, cmap='hsv')
    #images['size'] = cortex.Vertex(size, pc_subject, vmin=0, vmax=10)
    cortex.webshow(cortex.Dataset(**images))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("subject", 
                        type=str,
                        help="subject to process")

    args = parser.parse_args()

    main('/data/odc/derivatives',
         subject=args.subject)
