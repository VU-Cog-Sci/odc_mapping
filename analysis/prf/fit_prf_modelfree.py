import argparse
import numpy as np
import os
import os.path as op
from prf import PRFRidgeModel
from nilearn import image, input_data
import pandas as pd
from itertools import product
from nilearn import surface
from utils import get_voxel_data
from scipy.signal import savgol_filter, fftconvolve, resample

def main(subject,
         session,
         derivatives,
         source,
         model,
         alpha,
         description,
         rbf_kernel_size,
         out_dir):

    if not op.exists(out_dir):
        os.makedirs(out_dir)

    bold_dm = np.loadtxt(op.join(derivatives, 'prf', 'bold_dm.txt'))

    if source == 'voxels':
        data, masker = get_voxel_data(derivatives, subject, session)
    
    if source == 'vert':
        sub_dir = op.join(derivatives, 'sampled_giis/sub-{subject}/ses-prf/func').format(**locals())
        data = []
        for run in range(1,4):
            d = []
            for hemi in ['lh', 'rh']:
                d.append(surface.load_surf_data(op.join(sub_dir, 'sub-{subject}_ses-prf_task-prf_acq-10_run-{run:02d}_bold.{hemi}.gii'.format(subject=subject, run=run, hemi=hemi))).T)
    
            d = np.hstack(d)
            
            data.append(d)

        data = np.array(data)
    
    if model == 'ridge':
        m = PRFRidgeModel(bold_dm[:data.shape[1]], data)
        r2 = m.fit(alpha=alpha)

    if source == 'voxels':
        r2 = masker.inverse_transform(r2)
        mean_r2 = image.mean_img(r2)    

        r2_fn = os.path.join(out_dir, 'sub-{subject}_desc-{description}_r2.nii.gz').format(**locals())
        r2.to_filename(r2_fn)

        mean_r2_fn = os.path.join(out_dir, 'sub-{subject}_desc-{description}_mean_r2.nii.gz').format(**locals())
        mean_r2.to_filename(mean_r2_fn)
    elif source == 'vert':

        r2_fn = os.path.join(out_dir, 'sub-{subject}_desc-{description}_r2.npz').format(**locals())
        np.savez_compressed(r2_fn, r2_fn)

        mean_r2_fn = os.path.join(out_dir, 'sub-{subject}_desc-{description}_mean_r2.npz').format(**locals())
        mean_r2 = np.mean(r2, 0)
        np.savez_compressed(r2_fn, mean_r2)





if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("subject", 
                        #nargs='?',
                        type=str,
                        help="subject to process")
    parser.add_argument("session", 
                        default='prf',
                        nargs='?',
                        type=str,
                        help="subject to process")
    parser.add_argument("--out", 
                        type=str,
                        help="Where to write the data to")
    parser.add_argument("--description", 
                        type=str,
                        help="Identifier")
    parser.add_argument("--alpha", 
                        default=1.0,
                        type=float,
                        help="Identifier")
    parser.add_argument("model", 
                        default='ridge',
                        type=str,
                        nargs='?',
                        help="subject to process")
    parser.add_argument("--source", 
                        default='voxels',
                        type=str,
                        nargs='?',
                        help="Where data comes from ('voxels' or 'vertices')")
    parser.add_argument("rbf_kernel_size", 
                        default=8,
                        type=int,
                        nargs='?',
                        help="subject to process")
    args = parser.parse_args()

    main(subject=args.subject,
         session=args.session,
         derivatives='/data/odc/derivatives',
         source=args.source,
         model=args.model,
         alpha=args.alpha,
         description=args.description,
         rbf_kernel_size=args.rbf_kernel_size,
         out_dir=args.out)
