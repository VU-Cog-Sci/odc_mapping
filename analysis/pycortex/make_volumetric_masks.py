import cortex
import argparse
import os.path as op
from utils import get_bids_file
from nilearn import image
import os

def main(subject,
         derivatives):


    dseg_l = get_bids_file(derivatives,
                              'nighres',
                              'anat',
                              subject,
                              'dseg',
                              'anat',
                              'average',
                              description='cortex',
                              hemisphere='left')

    dseg_r = get_bids_file(derivatives,
                              'nighres',
                              'anat',
                              subject,
                              'dseg',
                              'anat',
                              'average',
                              description='cortex',
                              hemisphere='right')

    dseg = image.math_img('dseg_l + dseg_r', dseg_l=dseg_l, dseg_r=dseg_r)

    t1w = get_bids_file(derivatives, 'averaged_mp2rages', 'anat',
                         subject, 'T1w', 'anat', 'average')

    mask_folder = op.join(derivatives,
                          'pycortex',
                          'masks',
                          'sub-{subject}').format(**locals())

    if not op.exists(mask_folder):
        os.makedirs(mask_folder)

    pc_subject = 'odc.{}'.format(subject)
    masks = cortex.utils.get_roi_masks(pc_subject, 'identity.t1w', gm_sampler='thick')

    for mask in masks:
        new_fn = op.join(mask_folder,
                         'sub-{subject}_desc-{mask}_mask.nii.gz').format(**locals())
        mask_im = image.new_img_like(t1w, masks[mask].T)
        mask_im.to_filename(new_fn)

        cropped_fn = op.join(mask_folder,
                         'sub-{subject}_desc-{mask}_gm_mask.nii.gz').format(**locals())
        cropped_mask_im = image.math_img('mask * (dseg == 1)',
                                         mask=mask_im,
                                         dseg=dseg)
        cropped_mask_im.to_filename(cropped_fn)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("subject", 
                        type=str,
                        help="subject to process")
    args = parser.parse_args()

    main(args.subject,
         derivatives='/derivatives')

