import argparse
import os.path as op
import yaml
import cortex
from cortex.freesurfer import get_surf
import pickle as pkl
import os
import numpy as np
import pandas as pd

def main(derivatives,
         subject,
         patch='V1'):


    freesurfer_subject_dir = op.join(derivatives, 'freesurfer')

        
    for hemi in ['lh', 'rh'][:1]:
        (left_surface_pts, _), _ = cortex.db.get_surf('odc.{}'.format(subject), 'pia')
        size_left_surface = len(left_surface_pts)
        
        # Get 2D coordinates
        pts, _, _ = get_surf('sub-{}'.format(subject), 
                             hemi, 
                             "patch", 
                             patch+".flat", 
                             freesurfer_subject_dir=freesurfer_subject_dir)
        flat = pts[:, [1, 0, 2]]
        flat[:, 1] = -flat[:, 1]
        
        df = pd.DataFrame(pts, columns=['x', 'y', 'z'])

        masks = cortex.utils.get_roi_verts('odc.{}'.format(subject), mask=True)
        
        if hemi == 'lh':
            masks = dict([(m, masks[m][:size_left_surface]) for m in masks])
        elif hemi=='rh':
            masks = dict([(m, masks[m][size_left_surface:]) for m in masks])
        
        for m in masks:
            df[m] = masks[m]
            
        df.loc[(df['z'] != 0), ['x', 'y']] = np.nan
        target_dir = op.join(derivatives, 'coordinate_patches', 'sub-{subject}', 'anat').format(**locals())

        if not op.exists(target_dir):
            os.makedirs(target_dir)


        df.to_pickle(op.join(target_dir, 'sub-{subject}_hemi-{hemi}_coordinatepatch.pkl').format(**locals()))
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("subject", 
                        type=str,
                        help="subject to process")

    args = parser.parse_args()

    main('/derivatives',
         subject=args.subject)
