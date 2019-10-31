import glob
import argparse
import os.path as op
from nilearn import surface
import numpy as np
import nibabel as nb

derivatives = '/derivatives'
subject = '06'
session = 'odc'

def main(derivatives,
         subject,
         session):

    d = op.join(derivatives, 'tsnr', f'sub-{subject}', f'ses-{session}',
                           'func')

    for hemi in ['lh', 'rh']:

        template =  op.join(d, f'sub-{subject}_ses-{session}_task-*_acq-*_run-*_desc-depth.*_hemi-{hemi}.gii')

        fns = glob.glob(template)
        print(fns)
        mean_invtsnr = np.mean([surface.load_surf_data(fn) for fn in fns], 0)

        im = nb.gifti.GiftiImage(nb.load(fns[0]).header,
                            darrays=[nb.gifti.GiftiDataArray(mean_invtsnr)])

        im.to_filename(op.join(d, f'sub-{subject}_ses-{session}_desc-depth.all_hemi-{hemi}_invtsnr.gii'))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("subject", 
                        type=str,
                        help="subject to process")
    parser.add_argument("session", 
                        type=str,
                        nargs='?',
                        default='prf',
                        help="subject to process")
    args = parser.parse_args()

    main('/derivatives',
         subject=args.subject,
         session=args.session)
