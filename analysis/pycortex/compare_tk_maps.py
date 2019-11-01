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
from scipy import ndimage
import matplotlib.colors as colors

def main(sourcedata,
         derivatives,
         subject='tk',
         dataset='odc'):

    pc_subject = '{}.{}'.format(dataset, subject)
    template = '{derivatives}/modelfitting/glm7/sub-{subject}/ses-{session}/func/sub-{subject}_ses-{session}_left_over_right_zmap.nii.gz'

    session = 'odc2'
    zmap1 = template.format(**locals())

    session = 'odc3'
    zmap2 = template.format(**locals())

    session = 'cas'
    zmap3 = template.format(**locals())

    t1w = get_bids_file(derivatives, 'averaged_mp2rages', 'anat',
                         subject, 'T1w', 'anat', 'average')

    zmap1 = image.resample_to_img(zmap1, t1w, interpolation='nearest')
    zmap2 = image.resample_to_img(zmap2, t1w, interpolation='nearest')
    zmap3 = image.resample_to_img(zmap3, t1w, interpolation='nearest')

    transform = cortex.xfm.Transform(np.identity(4), t1w)
    #transform.save(pc_subject, 'identity.t1w', 'magnet')

    mask1 = image.math_img('np.abs(zmap)', zmap=zmap1).get_data().T
    mask2 = image.math_img('np.abs(zmap)', zmap=zmap2).get_data().T
    mask3 = image.math_img('np.abs(zmap) > 2', zmap=zmap3).get_data().T

    print(mask3.sum())

    mask3 = ndimage.binary_closing(mask3, iterations=2)
    print(mask3.sum())

    prf_pars = np.load(op.join(derivatives, 'prf/vertices/sub-{subject}_desc-test2_prf_optim.npz').format(**locals()))

    r2 = prf_pars['r2']
    mask = r2 < 0.1

    angle = prf_pars['angle']
    #angle[mask] = np.nan

    ecc = prf_pars['ecc']
    ecc[mask] = np.nan

    size = prf_pars['size']
    size[mask] = np.nan

    r2_max = np.max(r2)
    r2_max = 0.3
    r2_min = 0.15


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

    
    images = {}
    zmap1 = zmap1.get_data().T
    zmap1[zmap1 == 0] = np.nan

    zmap2 = zmap2.get_data().T
    zmap2[zmap2 == 0] = np.nan

    zmap3 = zmap3.get_data().T
    zmap3[zmap3 == 0] = np.nan

    images['PRF polar angle'] = cortex.VertexRGB(rgb_angle[:, 0], rgb_angle[:, 1], rgb_angle[:, 2],
                                       alpha=alpha_angle,
                                       subject=pc_subject)

    #images['zmap_ses-odc2'] = cortex.Volume2D(zmap1,
                                     #mask,
                                     #pc_subject,
                                     #'identity.t1w', vmin=-3, vmax=3, vmin2=0, vmax2=3,
                                     #cmap='BuBkRd_alpha_2D')

    #images['zmap_ses-odc3'] = cortex.Volume2D(zmap2,
                                     #mask,
                                     #pc_subject,
                                     #'identity.t1w', vmin=-3, vmax=3, vmin2=0, vmax2=3,
                                     #cmap='BuBkRd_alpha_2D')

    images['ODCs Amsterdam 1'] = cortex.Volume2D(zmap1,
                                              mask3,
                                              pc_subject,
                                              'identity.t1w', vmin=-3, vmax=3, vmin2=0, vmax2=3,
                                     cmap='BuBkRd_alpha_2D')

    images['ODCs Amsterdam 2'] = cortex.Volume2D(zmap2,
                                              mask3,
                                              pc_subject,
                                              'identity.t1w', vmin=-3, vmax=3, vmin2=0, vmax2=3,
                                     cmap='BuBkRd_alpha_2D')

    images['ODCs Beijing'] = cortex.Volume2D(zmap3,
                                             mask3,
                                             pc_subject,
                                             'identity.t1w', vmin=-3, vmax=3, vmin2=0, vmax2=3,
                                     cmap='BuBkRd_alpha_2D')
    
    ds = cortex.Dataset(**images)
                                     
    cortex.webgl.make_static(outpath=op.join(derivatives, 'pycortex', subject),
                             data=ds)
    cortex.webshow(ds)
    #cortex.webshow(ds)




if __name__ == '__main__':


    main('/data/odc/sourcedata', 
         '/data/odc/derivatives')

