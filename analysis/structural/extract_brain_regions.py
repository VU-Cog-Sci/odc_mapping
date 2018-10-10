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
                              'extract_brain_regions',
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


    # LEFT
    cortex = nighres.brain.extract_brain_region(segmentation=segmentation,
                                       levelset_boundary=boundary_dist,
                                       maximum_membership=max_probas,
                                       maximum_label=max_labels,
                                       extracted_region='left_cerebrum',
                                       file_name='sub-{}'.format(subject),
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
                        type=str,
                        help="subject to process")

    args = parser.parse_args()

    main('/sourcedata', 
         '/derivatives',
         tmp_dir='/workflow_folders',
         subject=args.subject)
