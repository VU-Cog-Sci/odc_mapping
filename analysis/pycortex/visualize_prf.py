from sys import platform as sys_pf
if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")

import argparse
import numpy as np
import cortex
import re
import matplotlib.colors as colors
import seaborn as sns
import os.path as op
from bids import BIDSLayout
from nilearn import image
from utils import get_bids_file


def main(pars,
         make_svg,
         derivatives,
         old=False,
         recache=False,
         pc_subject=None):

    if pc_subject is None:
        reg = re.compile('.*/sub-(?P<subject>[a-z0-9]+)_.*')

        subject = reg.match(pars).group(1)
        pc_subject = 'odc.{}'.format(subject)

        if old:
            pc_subject += '.old'


    #mean_epi = '{derivatives}/spynoza/ses-prffunc/sub-subject/.nii.gz'.format(**locals())

    prf_pars = np.load(pars)

    images = {}

    r2 = prf_pars['r2']
    mask = r2 < 0.05

    angle = prf_pars['angle']
    #angle[mask] = np.nan


    ecc = prf_pars['ecc']
    ecc[mask] = np.nan

    size = prf_pars['size']
    size[mask] = np.nan

    images['ecc'] = cortex.Vertex(ecc, pc_subject, vmin=0, vmax=15)

    r2_max = np.max(r2)
    r2_max = 0.3
    r2_min = 0.1


    hsv_angle = np.ones((len(r2), 3))
    hsv_angle[:, 0] = angle
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

    #alpha_angle = np.clip(r2 / r2_max * 2, r2_min/r2_max, 1)
    #alpha_angle[alpha_angle < r2_min/r2_max] = 0
    alpha_angle = hsv_angle[:, 2]

    images['angle'] = cortex.VertexRGB(rgb_angle[:, 0], rgb_angle[:, 1], rgb_angle[:, 2],
                                       #alpha=np.ones(len(rgb_angle)),
                                       alpha=alpha_angle,
                                       subject=pc_subject)

    images['angle_1d'] = cortex.Vertex(angle, pc_subject, vmin=-3.14, vmax=3.14, cmap='hsv')

    images['r2'] = cortex.Vertex(r2, pc_subject, vmin=0, vmax=r2_max)
    #images['ecc'] = cortex.Vertex2D(ecc/15, r2/r2_max, cmap='BuBkRd_alpha_2D', subject=pc_subject, vmin=.15, vmax=1)

    v1_ix, v1_values = cortex.freesurfer.get_label(pc_subject,
                                              'V1_exvivo',
                                              'sub-{}'.format(subject),
                                              fs_dir=op.join(derivatives, 'freesurfer'))

    vt_v1 = np.zeros_like(r2)
    vt_v1[v1_ix] = v1_values
    images['fs_v1'] = cortex.Vertex(vt_v1, pc_subject)

    v2_ix, v2_values = cortex.freesurfer.get_label(pc_subject,
                                              'V2_exvivo',
                                              'sub-{}'.format(subject),
                                              fs_dir=op.join(derivatives, 'freesurfer'))
    vt_v2 = np.zeros_like(r2)
    vt_v2[v2_ix] = v2_values

    images['fs_v2'] = cortex.Vertex(vt_v2, pc_subject)

    layout = BIDSLayout(op.join(derivatives, 'tsnr'),
                        validate=False)

    veins = layout.get(subject=subject,
                       session='prf',
                       suffix='invtsnr',
                       return_type='file')
    veins = image.mean_img(veins)

    t1w = cortex.db.get_anat(pc_subject, 'raw')
    veins = image.resample_to_img(veins,
                                  t1w)

    images['veins'] = cortex.Volume(veins.get_data().T,
                                    subject=pc_subject,
                                    xfmname='identity',
                                    vmin=0,
                                    vmax=2)



    if make_svg:
        cortex.utils.add_roi(data=images['angle'], name='prf_angle', open_inkscape=False)
        cortex.utils.add_roi(data=images['angle_1d'], name='prf_angle_1d', open_inkscape=False)
        cortex.utils.add_roi(data=images['ecc'], name='prf_ecc', open_inkscape=False)
        cortex.utils.add_roi(data=images['fs_v1'], name='Freesurfer V1', open_inkscape=False)
        cortex.utils.add_roi(data=images['fs_v2'], name='Freesurfer V2', open_inkscape=False)
    else:
        ds = cortex.Dataset(**images)
        cortex.webshow(ds, recache=recache)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("pars", 
                        #nargs='?',
                        type=str,
                        help="subject to process")
    parser.add_argument('--make-svg', dest='make_svg', action='store_true')
    parser.add_argument('--recache', dest='recache', action='store_true')
    parser.add_argument('--old', dest='old', action='store_true')
    args = parser.parse_args()

    main(args.pars,
         args.make_svg,
         '/data/odc/derivatives',
         args.old,
         args.recache)

