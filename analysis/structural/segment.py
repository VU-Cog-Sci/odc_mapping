# NOTE: this scripts should be run in the 'nighres' conda environment
import nighres
from bids.grabbids import BIDSLayout
import argparse
import os
from nighres import brain
import warnings
from nilearn import image
from scipy import ndimage
import nibabel as nb

def main(sourcedata, 
         derivatives,
         tmp_dir,
         subject=None):

    dura_layout = BIDSLayout(os.path.join(derivatives,
                                          'masks'))
    dura_mask = get_bids_file(dura_layout, subject, 'dura')
    
    layout = BIDSLayout('/sourcedata')

    t1w = get_bids_file(layout, subject, 'UNI')
    t1map = get_bids_file(layout, subject, 'T1map')

    fmriprep_layout = BIDSLayout('/derivatives/fmriprep')
    brain_mask = get_bids_file(fmriprep_layout, subject, 'brainmask')

    brain_mask_dil = ndimage.binary_dilation(nb.load(brain_mask).get_data(), iterations=3)
    brain_mask = image.new_img_like(brain_mask, brain_mask_dil)

    brain_mask = image.resample_to_img(brain_mask, t1w)
    brain_mask.to_filename('/derivatives/mask_test.nii.gz')
    
    t1w_masked = image.math_img('brain_mask * t1w', 
                                 brain_mask=brain_mask,
                                 t1w=t1w)


    t1map_masked = image.math_img('brain_mask * t1map', 
                                  brain_mask=brain_mask,
                                  t1map=t1map)

    t1w_masked_fn = '/derivatives/fmriprep/sub-{subject}/anat/sub-{subject}_T1w_masked.nii.gz'.format(subject=subject)
    t1w_masked.to_filename(t1w_masked_fn)

    t1map_masked_fn = '/derivatives/fmriprep/sub-{subject}/anat/sub-{subject}_T1map_masked.nii.gz'.format(subject=subject)
    t1map_masked.to_filename(t1map_masked_fn)
    
    output_dir = os.path.join(derivatives,
                              'nighres',
                              'segmentation_dilation',
                              'sub-{}'.format(subject))

    brain.mgdm_segmentation(contrast_image1=t1w_masked_fn,
                            contrast_type1='Mp2rage7T',
                            contrast_image2=t1map_masked_fn,
                            contrast_type2='T1map7T',
                            contrast_image3=dura_mask,
                            contrast_type3='Filters',
                            save_data=True,
                            output_dir=output_dir)



def get_bids_file(layout,
                  subject,
                  modality,
                  filter=None):

    img = layout.get(subject=subject,
                     type=modality,
                     return_type='file')

    if filter is not None:
        img = [im for im in img if filter in im]

    if len(img) > 1:
        warnings.warn('Found more than one {}-image:\n'
                      '{}'
                       'using {}'.format(modality, img, img[0]))

    return img[0]

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("subject", 
                        #nargs='?',
                        type=str,
                        help="subject to process")

    args = parser.parse_args()

    main('/sourcedata', 
         '/derivatives',
         tmp_dir='/workflow_folders',

         subject=args.subject)
