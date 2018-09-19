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


    segment_layout = BIDSLayout(os.path.join('/derivatives',
                                             'nighres',
                                             'segmentation_dilation'))

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
                              'cortex_extraction',
                              'sub-{}'.format(subject))

    # RIGHT
    #cortex = nighres.brain.extract_brain_region(segmentation=segmentation,
                                       #levelset_boundary=boundary_dist,
                                       #maximum_membership=max_probas,
                                       #maximum_label=max_labels,
                                       #extracted_region='right_cerebrum',
                                       #file_name='sub-{}'.format(subject),
                                       #save_data=True,
                                       #output_dir=output_dir)

    #extract_layout = BIDSLayout(os.path.join('/derivatives',
                                             #'nighres',
                                             #'cortex_extraction'))

    #cruise = nighres.cortex.cruise_cortex_extraction(
                            #init_image=cortex['inside_mask'],
                            #wm_image=cortex['inside_proba'],
                            #gm_image=cortex['region_proba'],
                            #csf_image=cortex['background_proba'],
                            #normalize_probabilities=True,
                            #file_name='sub-{}_right'.format(subject),
                            #save_data=True,
                            #output_dir=output_dir)


    # LEFT
    cortex = nighres.brain.extract_brain_region(segmentation=segmentation,
                                       levelset_boundary=boundary_dist,
                                       maximum_membership=max_probas,
                                       maximum_label=max_labels,
                                       extracted_region='left_cerebrum',
                                       file_name='sub-{}'.format(subject),
                                       save_data=True,
                                       output_dir=output_dir)

    extract_layout = BIDSLayout(os.path.join('/derivatives',
                                             'nighres',
                                             'cortex_extraction'))

    manual_wm_seg_left = '/derivatives/manual_segmentation/sub-tk/sub-tk_manualsegwml.nii.gz'
    #wm_seg_left = image.math_img('np.min((manual + auto, np.ones_like(auto)*0.99), 0)', 
    wm_seg_left = image.math_img('manual*20 + auto', 
                                 auto=cortex['inside_proba'],
                                 manual=manual_wm_seg_left)

    manual_gm_seg_left = '/derivatives/manual_segmentation/sub-tk/sub-tk_manualseggml.nii.gz'
    gm_seg_left = image.math_img('manual*20 + auto', 
                                 auto=cortex['region_proba'],
                                 manual=manual_gm_seg_left)

    total_prob = image.math_img('wm_seg_left + gm_seg_left + csf_seg_left',
                                wm_seg_left=wm_seg_left,
                                gm_seg_left=gm_seg_left,
                                csf_seg_left=cortex['background_proba'])

    wm_seg_left = image.math_img('np.clip(np.nan_to_num(wm_seg_left / total_prob), 0, 1)',
                                 wm_seg_left=wm_seg_left,
                                 total_prob=total_prob)

    gm_seg_left = image.math_img('np.clip(np.nan_to_num(gm_seg_left / total_prob), 0, 1)',
                                 gm_seg_left=gm_seg_left,
                                 total_prob=total_prob)

    csf_seg_left = image.math_img('np.clip(np.nan_to_num(csf_seg_left / total_prob), 0, 1)',
                                  csf_seg_left=cortex['background_proba'],
                                  total_prob=total_prob)

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
