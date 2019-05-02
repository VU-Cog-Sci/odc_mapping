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

    t1w = get_bids_file(derivatives, 'averaged_mp2rages', 'anat',
                         subject, 'T1w', 'anat', 'average')

    zmap1 = image.resample_to_img(zmap1, t1w, interpolation='nearest')
    zmap2 = image.resample_to_img(zmap2, t1w, interpolation='nearest')

    transform = cortex.xfm.Transform(np.identity(4), t1w)
    #transform.save(pc_subject, 'identity.t1w', 'magnet')

    mask = image.math_img('np.abs(zmap)', zmap=zmap1)
    
    images = {}
    zmap1 = zmap1.get_data().T
    zmap1[zmap1 == 0] = np.nan

    zmap2 = zmap2.get_data().T
    zmap2[zmap2 == 0] = np.nan

    mask = mask.get_data().T
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

    images['zmap_ses-odc2'] = cortex.Volume(zmap1,
                                     pc_subject,
                                     'identity.t1w', vmin=-3, vmax=3, vmin2=0, vmax2=3,
                                     cmap='BuBkRd')

    images['zmap_ses-odc3'] = cortex.Volume(zmap2,
                                     pc_subject,
                                     'identity.t1w', vmin=-3, vmax=3, vmin2=0, vmax2=3,
                                     cmap='BuBkRd')

    
    #prf_pars = np.load(op.join(derivatives, 'voxel_prf/modelfree/sub-{subject}_desc-None_prf_pars.npz').format(**locals()))

    #r2 = prf_pars['r2']
    #mask = r2 < 0.05

    #angle = prf_pars['angle']
    #angle[mask] = np.nan

    #ecc = prf_pars['ecc']
    #ecc[mask] = np.nan

    #size = prf_pars['size']
    #size[mask] = np.nan

    #images['r2'] = cortex.Vertex(prf_pars['r2'], pc_subject, cmap='inferno')
    #images['ecc'] = cortex.Vertex(ecc, pc_subject, vmin=0,vmax=15, cmap='inferno')
    #images['angle'] = cortex.Vertex(angle, pc_subject, vmin=-3.14, vmax=3.14, cmap='hsv')
    #images['size'] = cortex.Vertex(size, pc_subject, vmin=0, vmax=10)
    ##images['angle'] = cortex.Vertex2D(prf_pars['angle'], prf_pars['r2'], pc_subject)
    ##images['angle'] = cortex.Vertex(prf_pars['angle'], pc_subject)
    #images['size'] = cortex.Vertex2D(prf_pars['size'], prf_pars['r2'], pc_subject)
    #images['ecc'] = cortex.Vertex2D(prf_pars['ecc'], prf_pars['r2'], pc_subject)

    ds = cortex.Dataset(**images)
                                     
    cortex.webgl.make_static(outpath=op.join(derivatives, 'pycortex', subject),
                             data=ds)
    cortex.webshow(ds)
    #cortex.webshow(ds)




if __name__ == '__main__':


    main('/data/odc/sourcedata', 
         '/data/odc/derivatives')

