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


    segment_layout = BIDSLayout(os.path.join(derivatives,
                                             'nighres',
                                             'segmentation_dilation'))

    fmriprep_layout = BIDSLayout(os.path.join(derivatives,
                                              'fmriprep'))
    
    manual_layout = BIDSLayout(os.path.join(derivatives,
                                              'manual_segmentation'))

    wm_manual = get_bids_file(manual_layout, subject, 'manualsegwm')
    gm_manual = get_bids_file(manual_layout, subject, 'manualseggm')


    wm_fmriprep = get_bids_file(fmriprep_layout, subject, 'probtissue', 'WM')
    gm_fmriprep = get_bids_file(fmriprep_layout, subject, 'probtissue', 'GM')
    csf_fmriprep = get_bids_file(fmriprep_layout, subject, 'probtissue', 'CSF')
    print(csf_fmriprep)

    segmentation = get_bids_file(segment_layout, 
                                 subject,
                                 'seg')

    boundary_dist = get_bids_file(segment_layout, 
                                 subject,
                                 'dist')

    max_labels = get_bids_file(segment_layout, 
                                 subject,
                                 'lbls')

    max_probas = get_bids_file(segment_layout, 
                               subject,
                               'mems')


    output_dir = os.path.join(derivatives,
                              'nighres',
                              'cortex_extraction_combine_manual',
                              'sub-{}'.format(subject))

    extract_layout = BIDSLayout(os.path.join(derivatives,
                                             'nighres',
                                             'cortex_extraction'))
    # RIGHT
    cortex_right = nighres.brain.extract_brain_region(segmentation=segmentation,
                                               levelset_boundary=boundary_dist,
                                               maximum_membership=max_probas,
                                               maximum_label=max_labels,
                                               extracted_region='right_cerebrum',
                                               file_name='sub-{}'.format(subject),
                                               save_data=True,
                                               output_dir=output_dir)

    wm_fmriprep = image.resample_to_img(wm_fmriprep, cortex_right['inside_proba'], interpolation='nearest')
    gm_fmriprep = image.resample_to_img(gm_fmriprep, cortex_right['inside_proba'], interpolation='nearest')
    csf_fmriprep = image.resample_to_img(csf_fmriprep, cortex_right['inside_proba'], interpolation='nearest')

    wm_seg_right = image.math_img('fmriprep + cbs + manual*5', 
                                 cbs=cortex_right['inside_proba'],
                                 fmriprep=wm_fmriprep,
                                 manual=wm_manual)

    gm_seg_right = image.math_img('fmriprep + cbs + manual*5', 
                                 cbs=cortex_right['region_proba'],
                                 fmriprep=gm_fmriprep,
                                 manual=gm_manual)

    csf_seg_right = image.math_img('2 * cbs', 
                                 cbs=cortex_right['background_proba'],
                                 fmriprep=csf_fmriprep)

    total_prob = image.math_img('wm_seg_right + gm_seg_right + csf_seg_right',
                                wm_seg_right=wm_seg_right,
                                gm_seg_right=gm_seg_right,
                                csf_seg_right=csf_seg_right)

    wm_seg_right = image.math_img('wm_seg_right / total_prob',
                                 wm_seg_right=wm_seg_right,
                                 total_prob=total_prob)
    wm_seg_right.to_filename('/derivatives/zooi/wm_seg_right.nii.gz')

    gm_seg_right = image.math_img('gm_seg_right / total_prob',
                                 gm_seg_right=gm_seg_right,
                                 total_prob=total_prob)
    gm_seg_right.to_filename('/derivatives/zooi/gm_seg_right.nii.gz')

    csf_seg_right = image.math_img('csf_seg_right / total_prob',
                                  csf_seg_right=csf_seg_right,
                                  total_prob=total_prob)
    csf_seg_right.to_filename('/derivatives/zooi/csf_seg_right.nii.gz')

    cruise = nighres.cortex.cruise_cortex_extraction(
                            init_image=cortex_right['inside_mask'],
                            wm_image=wm_seg_right,
                            gm_image=gm_seg_right,
                            csf_image=csf_seg_right,
                            normalize_probabilities=False,
                            file_name='sub-{}_right'.format(subject),
                            save_data=True,
                            output_dir=output_dir)


    # LEFT
    cortex = nighres.brain.extract_brain_region(segmentation=segmentation,
                                       levelset_boundary=boundary_dist,
                                       maximum_membership=max_probas,
                                       maximum_label=max_labels,
                                       extracted_region='left_cerebrum',
                                       file_name='sub-{}'.format(subject),
                                       save_data=True,
                                       output_dir=output_dir)


    wm_seg_left = image.math_img('fmriprep + cbs + manual*5', 
                                 cbs=cortex['inside_proba'],
                                 fmriprep=wm_fmriprep,
                                 manual=wm_manual)

    gm_seg_left = image.math_img('fmriprep + cbs + manual*5', 
                                 cbs=cortex['region_proba'],
                                 fmriprep=gm_fmriprep,
                                 manual=gm_manual)

    csf_seg_left = image.math_img('2 * cbs', 
                                 cbs=cortex['background_proba'],
                                 fmriprep=csf_fmriprep)

    total_prob = image.math_img('wm_seg_left + gm_seg_left + csf_seg_left',
                                wm_seg_left=wm_seg_left,
                                gm_seg_left=gm_seg_left,
                                csf_seg_left=csf_seg_left)

    wm_seg_left = image.math_img('wm_seg_left / total_prob',
                                 wm_seg_left=wm_seg_left,
                                 total_prob=total_prob)
    wm_seg_left.to_filename('/derivatives/zooi/wm_seg_left.nii.gz')

    gm_seg_left = image.math_img('gm_seg_left / total_prob',
                                 gm_seg_left=gm_seg_left,
                                 total_prob=total_prob)
    gm_seg_left.to_filename('/derivatives/zooi/gm_seg_left.nii.gz')

    csf_seg_left = image.math_img('csf_seg_left / total_prob',
                                  csf_seg_left=csf_seg_left,
                                  total_prob=total_prob)
    csf_seg_left.to_filename('/derivatives/zooi/csf_seg_left.nii.gz')

    cruise = nighres.cortex.cruise_cortex_extraction(
                            init_image=cortex['inside_mask'],
                            wm_image=wm_seg_left,
                            gm_image=gm_seg_left,
                            csf_image=csf_seg_left,
                            normalize_probabilities=False,
                            file_name='sub-{}_left'.format(subject),
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
        warnings.warn('Found more than one {}-image, using {}'.format(modality,
                                                                      img[0]))

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
