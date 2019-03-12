import argparse
from utils import get_derivative, binary_closing, largest_component
import os.path as op
from nilearn import image
import nibabel as nb
import numpy as np
import os
from subprocess import Popen

def main(sourcedata,
         derivatives,
         subject):


    manual_outside_mask = get_derivative(derivatives, 'manual_segmentation',
                                         'anat', subject, 'mask',
                                         description='outside', session='anat',
                                         check_exists=True, space='average')

    freesurfer_brainmask_auto = op.join(derivatives, 'freesurfer', 'sub-{subject}',
                                  'mri', 'brainmask.auto.mgz').format(**locals())

    freesurfer_brainmask = op.join(derivatives, 'freesurfer', 'sub-{subject}',
                                  'mri', 'brainmask.mgz').format(**locals())

    
    manual_outside_mask = image.resample_to_img(manual_outside_mask, freesurfer_brainmask_auto,
                                                interpolation='nearest')


    manual_outside_mask = nb.freesurfer.MGHImage(manual_outside_mask.get_data().astype(np.float32),
                                                 affine=manual_outside_mask.affine)


    new_brainmask = image.math_img('brain_mask * (1-outside)',
                                   brain_mask=freesurfer_brainmask_auto,
                                   outside=manual_outside_mask)

    new_brainmask.to_filename(freesurfer_brainmask)

    os.environ['SUBJECTS_DIR'] = op.join(derivatives, 'freesurfer')
    #subprocess.run(['recon-all', '-autorecon-pial', '-subjid', 'sub-{}'.format(subject)], shell=True)
    p = Popen(['recon-all', '-autorecon-pial', '-subjid', 'sub-{}'.format(subject)])




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("subject", 
                        type=str,
                        help="subject to process")

    args = parser.parse_args()

    main('/sourcedata', 
         '/derivatives',
         subject=args.subject)
