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

    mask1 = image.math_img('np.abs(zmap)', zmap=zmap1)
    mask2 = image.math_img('np.abs(zmap)', zmap=zmap2)
    mask3 = image.math_img('np.abs(zmap)', zmap=zmap3)
    
    images = {}
    zmap1 = zmap1.get_data().T
    zmap1[zmap1 == 0] = np.nan

    zmap2 = zmap2.get_data().T
    zmap2[zmap2 == 0] = np.nan

    zmap3 = zmap3.get_data().T
    zmap3[zmap3 == 0] = np.nan

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

    images['zmap_ses-odc2'] = cortex.Volume2D(zmap1,
                                              mask1.get_data().T,
                                              pc_subject,
                                              'identity.t1w', vmin=-3, vmax=3, vmin2=0, vmax2=3,
                                     cmap='BuBkRd_alpha_2D')

    images['zmap_ses-odc3'] = cortex.Volume2D(zmap2,
                                              mask2.get_data().T,
                                              pc_subject,
                                              'identity.t1w', vmin=-3, vmax=3, vmin2=0, vmax2=3,
                                     cmap='BuBkRd_alpha_2D')

    images['zmap_ses-cas'] = cortex.Volume2D(zmap3,
                                             mask3.get_data().T,
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

