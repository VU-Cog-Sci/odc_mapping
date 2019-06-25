import cortex
from nilearn import surface
import os.path as op
import numpy as np
import argparse

def main(derivatives,
         subject,
         session):

    all_depth_zmap_l = op.join(derivatives, 'sampled_giis', f'sub-{subject}', 
                             f'ses-{session}', 'func', 
                             f'sub-{subject}_ses-{session}_left_over_right_desc-zmap-depth-all_hemi-lh.gii')
    all_depth_zmap_r = op.join(derivatives, 'sampled_giis', f'sub-{subject}', 
                             f'ses-{session}', 'func', 
                             f'sub-{subject}_ses-{session}_left_over_right_desc-zmap-depth-all_hemi-rh.gii')
    all_depth_zmap = np.hstack((surface.load_surf_data(all_depth_zmap_l),
                                surface.load_surf_data(all_depth_zmap_r)))

    abs_zmap_l = op.join(derivatives, 'sampled_giis', f'sub-{subject}', 
                             f'ses-{session}', 'func', 
                             f'sub-{subject}_ses-{session}_left_over_right_desc-abszmap-depth-all_hemi-lh_smoothed.gii')
    abs_zmap_r = op.join(derivatives, 'sampled_giis', f'sub-{subject}', 
                             f'ses-{session}', 'func', 
                             f'sub-{subject}_ses-{session}_left_over_right_desc-abszmap-depth-all_hemi-rh_smoothed.gii')
    abs_zmap = np.hstack((surface.load_surf_data(abs_zmap_l), surface.load_surf_data(abs_zmap_r)))

    images ={}
    images['all_depth_zmap'] = cortex.Vertex(all_depth_zmap, f'odc.{subject}')
    images['abs_zmap_smooth'] = cortex.Vertex(abs_zmap, f'odc.{subject}')

    ds = cortex.Dataset(**images)

    cortex.webshow(ds)

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

    main('/data/odc/derivatives',
         subject=args.subject,
         session=args.session)

