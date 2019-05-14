import argparse
import os.path as op
import yaml
import cortex
from cortex.freesurfer import get_surf
import pickle as pkl
import os
import numpy as np
import pandas as pd
import statsmodels.api as sm

def main(derivatives,
         subject,
         patch='V1'):


    freesurfer_subject_dir = op.join(derivatives, 'freesurfer')

        
    for hemi in ['lh', 'rh']:
        (left_surface_pts, _), (right_surface_pts, _) = cortex.db.get_surf('odc.{}'.format(subject), 'pia')
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

        pars = np.load('/data/odc/derivatives/prf/vertices/sub-{subject}_desc-test2_prf_optim.npz'.format(subject=subject))
        ecc = pd.DataFrame(np.array([pars['ecc'], pars['r2']]).T, columns=['eccentricity', 'r2'], dtype=float)
        
        if hemi == 'lh':
            masks = dict([(m, masks[m][:size_left_surface]) for m in masks])
            ecc = ecc.iloc[:size_left_surface]
            pts = left_surface_pts
        elif hemi=='rh':
            masks = dict([(m, masks[m][size_left_surface:]) for m in masks])
            ecc = ecc.iloc[size_left_surface:]
            pts = right_surface_pts
        
        for m in masks:
            df[m] = masks[m]
            
        df.loc[(df['z'] != 0), ['x', 'y']] = np.nan

        # Store flat coordinates
        df['x_flat'] = df['x'].copy().astype(float)
        df['y_flat'] = df['y'].copy().astype(float)


        # Make new coordinate system by rotating flat coordinate system so x corresponds
        # to eccentricity gradient
        ecc.index = df.index
        df = pd.concat((df, ecc), axis=1)

        df['x'] = df['x'].astype(float)
        df['y'] = df['y'].astype(float)
        df['eccentricity'] = df['eccentricity'].astype(float)

        ix = (~df['x'].isnull()) & (df['r2'] > 0.15)
        #beta, _, _, _ = np.linalg.lstsq(df.loc[ix, ['x', 'y']].values, df.loc[ix, 'eccentricity'].values)
        X = sm.add_constant(df.loc[ix, ['x_flat', 'y_flat']])
        r = sm.WLS(df.loc[ix, ['eccentricity']], X, df.loc[ix, 'r2']).fit()
        beta = r.params[['x_flat', 'y_flat']].values
        print(beta)

        y_ = (beta[1], -beta[0]) / np.linalg.norm((beta[0], beta[1]))
        df['x'] = (beta / np.linalg.norm(beta)).dot(df[['x_flat', 'y_flat']].T)
        df['y'] = y_.dot(df[['x_flat', 'y_flat']].T)


        # Check if y goes up dorsally
        X = sm.add_constant(df.loc[ix, ['y']])

        #beta, _, _, _ = np.linalg.lstsq(X, pts[ix, [2]])
        r = sm.OLS(pts[ix, [2]], X).fit()
        beta = r.params['y']
        print(beta)

        if beta < 0.0:
            print('flip')
            df['y'] = -df['y']

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
