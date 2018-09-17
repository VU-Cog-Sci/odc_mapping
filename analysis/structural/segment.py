# NOTE: this scripts should be run in the 'nighres' conda environment
import nighres
from bids.grabbids import BIDSLayout
import argparse
import os
from nighres import brain


def main(sourcedata, 
         derivatives,
         tmp_dir,
         subject=None):

    skullstrip_layout = BIDSLayout(os.path.join(derivatives,
                                                'nighres',
                                                'skullstrip'))

    dura_layout = BIDSLayout(os.path.join(derivatives,
                                                'masks'))

    dura_mask = get_bids_file(dura_layout, subject, 'dura')
    print(dura_mask)

    t1w_masked = get_bids_file(skullstrip_layout, subject, 't1w', 'UNI')
    t1map_masked = get_bids_file(skullstrip_layout, subject, 't1map', 'T1map')
    
    output_dir = os.path.join(derivatives,
                              'nighres',
                              'segmentation',
                              'sub-{}'.format(subject))

    brain.mgdm_segmentation(contrast_image1=t1w_masked,
                            contrast_type1='Mp2rage7T',
                            contrast_image2=t1map_masked,
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
