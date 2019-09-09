import os
import nibabel as nb
import os.path as op
import glob
import numpy as np
from nipype.utils.filemanip import split_filename
from nipype.interfaces import freesurfer
from nibabel import gifti
import argparse

def main(derivatives,
         subject,
         session):

    for hemi in ['lh', 'rh']:
        template = op.join(derivatives, 'sampled_giis', f'sub-{subject}',
                                  f'ses-{session}', 'func',
                                  f'sub-{subject}_ses-{session}_left_over_right_desc-zmap-depth-*_hemi-{hemi}.gii')
        print(template)
        zmaps = glob.glob(template)

        print(zmaps)

        mean_zmap = np.mean([nb.load(fn).darrays[0].data for fn in zmaps], 0)
        zmap_im = nb.load(zmaps[0])
        mean_zmap_im = gifti.GiftiImage(header=zmap_im.header,
                                        extra=zmap_im.extra)
        mean_zmap_im.add_gifti_data_array(gifti.GiftiDataArray(mean_zmap))
        mean_zmap_im.to_filename(op.join(derivatives, 'sampled_giis', f'sub-{subject}',
                                  f'ses-{session}', 'func',
                                  f'sub-{subject}_ses-{session}_left_over_right_desc-zmap-depth-all_hemi-{hemi}.gii'))


        mean_zmap_abs = np.abs(mean_zmap)
        mean_zmap_abs_im = gifti.GiftiImage(header=zmap_im.header,
                                        extra=zmap_im.extra)
        mean_zmap_abs_im.add_gifti_data_array(gifti.GiftiDataArray(mean_zmap_abs))
        mean_zmap_abs_im.to_filename(op.join(derivatives, 'sampled_giis', f'sub-{subject}',
                                  f'ses-{session}', 'func',
                                  f'sub-{subject}_ses-{session}_left_over_right_desc-abszmap-depth-all_hemi-{hemi}.gii'))

        os.environ['SUBJECTS_DIR'] = op.join(derivatives, 'freesurfer')
        smoother = freesurfer.SurfaceSmooth()
        smoother.inputs.in_file = mean_zmap_abs_im.get_filename()
        smoother.inputs.fwhm = 2.0
        smoother.inputs.subject_id = f'sub-{subject}'
        smoother.inputs.hemi = hemi
        smoother.inputs.out_file = op.join(derivatives, 'sampled_giis', f'sub-{subject}',
                                  f'ses-{session}', 'func',
                                  f'sub-{subject}_ses-{session}_left_over_right_desc-abszmap-depth-all_hemi-{hemi}_smoothed.gii')

        r = smoother.run()


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
