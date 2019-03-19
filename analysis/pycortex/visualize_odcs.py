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
         subject,
         session,
         dataset='odc'):

    pc_subject = '{}.{}'.format(dataset, subject)

    zmap = '{derivatives}/modelfitting/glm7/sub-{subject}/ses-{session}/sub-{subject}_ses-{session}_left_over_right_zmap.nii.gz'.format(**locals())

    #psc = '{derivatives}/modelfitting/glm7/sub-{subject}/ses-{session}/sub-{subject}_ses-{session}_left_over_right_effect_size.nii.gz'.format(**locals())

    t1w = get_bids_file(derivatives, 'averaged_mp2rages', 'anat',
                         subject, 'T1w', 'anat', 'average')

    zmap = image.resample_to_img(zmap, t1w)
    #psc = image.resample_to_img(psc, t1w)

    transform = cortex.xfm.Transform(np.identity(4), t1w)
    #transform.save(pc_subject, 'identity.t1w', 'magnet')


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
    #images['psc'] = cortex.Volume(psc.get_data().T, pc_subject, 'identity.t1w', vmin=-5, vmax=5)
    
    prf_pars = np.load(op.join(derivatives, 'prf/vertices/sub-{subject}_desc-test2_prf_optim.npz').format(**locals()))

    r2 = prf_pars['r2']
    mask = r2 < 0.05

    angle = prf_pars['angle']
    angle[mask] = np.nan

    ecc = prf_pars['ecc']
    ecc[mask] = np.nan

    size = prf_pars['size']
    size[mask] = np.nan

    images['r2'] = cortex.Vertex(prf_pars['r2'], pc_subject, cmap='inferno')
    images['ecc'] = cortex.Vertex(ecc, pc_subject, vmin=0,vmax=15, cmap='inferno')
    images['angle'] = cortex.Vertex(angle, pc_subject, vmin=-3.14, vmax=3.14, cmap='hsv')
    images['size'] = cortex.Vertex(size, pc_subject, vmin=0, vmax=10)

    ds = cortex.Dataset(**images)
                                     
    #cortex.webgl.make_static(outpath=op.join(derivatives, 'pycortex', subject),
                             #data=ds)
    cortex.webshow(ds, recache=True)
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

