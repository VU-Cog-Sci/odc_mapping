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
    manual_inside_mask = get_derivative(derivatives, 'manual_segmentation',
                                         'anat', subject, 'mask',
                                         description='gm', session='anat',
                                         check_exists=True, space='average')

    manual_wm_mask = get_derivative(derivatives, 'manual_segmentation',
                                         'anat', subject, 'mask',
                                         description='wm', session='anat',
                                         check_exists=False, space='average')


    freesurfer_brainmask_auto = op.join(derivatives, 'freesurfer', 'sub-{subject}',
                                  'mri', 'brainmask.auto.mgz').format(**locals())

    freesurfer_brainmask = op.join(derivatives, 'freesurfer', 'sub-{subject}',
                                  'mri', 'brainmask.mgz').format(**locals())

    freesurfer_t1w = op.join(derivatives, 'freesurfer', 'sub-{subject}',
                                  'mri', 'T1.mgz').format(**locals())

    
    manual_outside_mask = image.resample_to_img(manual_outside_mask, freesurfer_brainmask_auto,
                                                interpolation='nearest')

    manual_outside_mask = nb.freesurfer.MGHImage(manual_outside_mask.get_data().astype(np.float32),
                                                 affine=manual_outside_mask.affine)

    manual_inside_mask = image.resample_to_img(manual_inside_mask, freesurfer_brainmask_auto,
                                                interpolation='nearest')


    manual_inside_mask = nb.freesurfer.MGHImage(manual_inside_mask.get_data().astype(np.float32),
                                                 affine=manual_inside_mask.affine)

    if manual_wm_mask:
        manual_wm_mask = image.resample_to_img(manual_wm_mask, freesurfer_brainmask_auto,
                                                    interpolation='nearest')


        manual_wm_mask = nb.freesurfer.MGHImage(manual_wm_mask.get_data().astype(np.float32),
                                                     affine=manual_wm_mask.affine)


        manual_inside_mask = image.math_img('(manual_inside_mask + manual_wm_mask) > 0',
                                            manual_inside_mask=manual_inside_mask,
                                            manual_wm_mask=manual_wm_mask)

        freesurfer_wm = op.join(derivatives, 'freesurfer', 'sub-{subject}',
                                      'mri', 'wm.mgz').format(**locals())


        freesurfer_wm_new = image.math_img('freesurfer_wm * (1-manual_inside_mask) ' 
                                           '* (1 - manual_outside_mask)' 
                                           '+ manual_wm_mask * 255',
                                       manual_inside_mask=manual_inside_mask,
                                       manual_wm_mask=manual_wm_mask,
                                       manual_outside_mask=manual_outside_mask,
                                       freesurfer_wm=freesurfer_wm)

        # Get rid of any weird small components
        freesurfer_wm_new_ =  nb.Nifti1Image(freesurfer_wm_new.get_data(), freesurfer_wm_new.affine)
        largest_component = image.largest_connected_component_img(freesurfer_wm_new_)
        largest_component = nb.MGHImage(largest_component.get_data(), freesurfer_wm_new.affine, freesurfer_wm_new.header)

        freesurfer_wm_new = image.math_img('freesurfer_wm * largest_component',
                                           freesurfer_wm=freesurfer_wm_new,
                                           largest_component=largest_component)

        freesurfer_wm_new.to_filename(freesurfer_wm)


    new_brainmask = image.math_img('(((brain_mask > 0) + inside - outside ) > 0) * t1w',
                                   brain_mask=freesurfer_brainmask_auto,
                                   outside=manual_outside_mask,
                                   t1w=freesurfer_t1w,
                                   inside=manual_inside_mask)

    new_brainmask.to_filename(freesurfer_brainmask)

    new_brainmask.to_filename(op.join(derivatives, 'freesurfer', 'sub-{subject}',
                                  'mri', 'brain.finalsurfs.manedit.mgz').format(**locals()))

    #os.environ['SUBJECTS_DIR'] = op.join(derivatives, 'freesurfer')
    ##subprocess.run(['recon-all', '-autorecon-pial', '-subjid', 'sub-{}'.format(subject)], shell=True)
    ##p = Popen(['recon-all', '-autorecon-pial', '-subjid', 'sub-{}'.format(subject)])




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("subject", 
                        type=str,
                        help="subject to process")

    args = parser.parse_args()

    main('/sourcedata', 
         '/derivatives',
         subject=args.subject)
