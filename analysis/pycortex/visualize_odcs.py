import cortex
import argparse
import os
import os.path as op
from utils import get_bids_file
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from nilearn import image
from bids import BIDSLayout
import matplotlib.colors as colors

def main(sourcedata,
         derivatives,
         subject,
         session,
         cache=False,
         dataset='odc'):


    if subject in []:
        trans_str = '_trans'
    else:
        trans_str = ''

    pc_subject = '{}.{}'.format(dataset, subject)

    zmap = '{derivatives}/modelfitting/glm7/sub-{subject}/ses-{session}/func/sub-{subject}_ses-{session}_left_over_right_zmap{trans_str}.nii.gz'.format(**locals())

    #zmap_task = '{derivatives}/modelfitting/glm7/sub-{subject}/ses-{session}/sub-{subject}_ses-{session}_left_over_right_task_zmap.nii.gz'.format(**locals())

    if subject == 'bm':
        mean_epi = '{derivatives}/spynoza/sub-{subject}/ses-{session}/func/sub-{subject}_ses-{session}_task-checkerboard_acq-07_run-03_reference{trans_str}.nii.gz'.format(**locals())
    else:
        mean_epi = '{derivatives}/spynoza/sub-{subject}/ses-{session}/func/sub-{subject}_ses-{session}_task-fixation_acq-07_run-03_reference{trans_str}.nii.gz'.format(**locals())

    #psc = '{derivatives}/modelfitting/glm7/sub-{subject}/ses-{session}/sub-{subject}_ses-{session}_left_over_right_effect_size.nii.gz'.format(**locals())

    t1w = get_bids_file(derivatives, 'averaged_mp2rages', 'anat',
                         subject, 'T1w', 'anat', 'average')

    zmap = image.resample_to_img(zmap, t1w)
    #zmap_task = image.resample_to_img(zmap_task, t1w)
    mean_epi = image.resample_to_img(mean_epi, t1w)

    transform = cortex.xfm.Transform(np.identity(4), t1w)
    if not np.in1d(subject, ['bm', 'tk']):
        transform.save(pc_subject, 'identity.t1w', 'magnet')


    mask = image.math_img('np.abs(zmap)', zmap=zmap)

    
    images = {}
    zmap = zmap.get_data().T
    zmap[zmap == 0] = np.nan
    mask = mask.get_data().T
    images['zmap'] = cortex.Volume2D(zmap,
                                     mask,
                                     pc_subject,
                                     'identity.t1w', vmin=-3, vmax=3, vmin2=0, vmax2=3,
                                     cmap='BuBkRd_alpha_2D')
    images['abs_zmap'] = cortex.Volume(np.abs(zmap),
                                     pc_subject,
                                     'identity.t1w', vmin=-3, vmax=3, vmin2=0, vmax2=3)
                                     #cmap='BuBkRd_alpha_2D')
    #zmap_task = zmap_task.get_data().T
    #zmap_task[zmap_task == 0] = np.nan
    #images['zmap_task'] = cortex.Volume2D(zmap_task,
                                     #mask,
                                     #pc_subject,
                                     #'identity.t1w', vmin=-3, vmax=3, vmin2=0, vmax2=3,
                                     #cmap='BuBkRd_alpha_2D')

    #images['mean_epi'] = cortex.Volume(mean_epi.get_data().T,
                                       #pc_subject,
                                       #'identity.t1w')

    
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

    # VEIN MASK
    layout = BIDSLayout(op.join(derivatives, 'tsnr'),
                        validate=False)

    veins = layout.get(subject=subject,
                       session=session,
                       suffix='invtsnr',
                       return_type='file')

    if len(veins) > 0:
        veins = image.mean_img(veins)
        t1w = cortex.db.get_anat(pc_subject, 'raw')
        veins = image.resample_to_img(veins,
                                      t1w)
        images['veins'] = cortex.Volume(veins.get_data().T,
                                        subject=pc_subject,
                                        xfmname='identity',
                                        vmin=0,
                                        vmax=2)
    ds = cortex.Dataset(**images)
                                     
    cortex.webgl.make_static(outpath=op.join(derivatives, 'pycortex', subject),
                             data=ds)
    cortex.webgl.make_static(outpath=op.join(derivatives, 'pycortex', subject, 'light'),
                             data=images['zmap'])
    cortex.webshow(ds, recache=cache)
    #cortex.webshow(ds)




if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("subject", 
                        #nargs='?',
                        type=str,
                        help="subject to process")
    parser.add_argument("session", 
                        nargs='?',
                        default='odc',
                        type=str,
                        help="subject to process")
    args = parser.parse_args()

    main('/data/odc/sourcedata', 
         '/data/odc/derivatives',
         subject=args.subject,
         session=args.session)

