import cortex
import argparse
import os
import os.path as op
from utils import get_bids_file
import numpy as np
from nilearn import image

def main(sourcedata,
         derivatives,
         subject,
         session):

    zmap = '{derivatives}/modelfitting/glm7/sub-{subject}/ses-{session}/sub-{subject}_ses-{session}_left_over_right_zmap.nii.gz'.format(**locals())

    psc = '{derivatives}/modelfitting/glm7/sub-{subject}/ses-{session}/sub-{subject}_ses-{session}_left_over_right_effect_size.nii.gz'.format(**locals())

    t1w = get_bids_file(derivatives, 'averaged_mp2rages', 'anat',
                         subject, 'T1w', 'anat', 'average')

    zmap = image.resample_to_img(zmap, t1w)
    psc = image.resample_to_img(psc, t1w)

    zmap = image.math_img('zmap * (np.abs(zmap) > 1)', zmap=zmap)

    transform = cortex.xfm.Transform(np.identity(4), t1w)
    transform.save(subject, 'identity.t1w', 'magnet')

    
    images = {}
    zmap = zmap.get_data().T
    zmap[zmap == 0] = np.nan
    images['zmap'] = cortex.Volume(zmap, subject, 'identity', vmin=-3, vmax=3)
    images['psc'] = cortex.Volume(psc.get_data().T, subject, 'identity', vmin=-5, vmax=5)


    ds = cortex.Dataset(**images)
                                     
    cortex.webshow(ds)




if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("subject", 
                        #nargs='?',
                        type=str,
                        help="subject to process")
    args = parser.parse_args()

    main('/sourcedata', 
         '/derivatives',
         subject=args.subject,
         session='odc1')

