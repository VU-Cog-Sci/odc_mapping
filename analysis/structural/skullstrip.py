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

    layout = BIDSLayout(sourcedata)

    inv2 = get_bids_file(layout, subject, 'MP2RAGE', 'inv-2')
    t1w = get_bids_file(layout, subject, 'UNI')
    t1map = get_bids_file(layout, subject, 'T1map')
    
    output_dir = os.path.join(derivatives,
                              'nighres',
                              'skullstrip',
                              'sub-{}'.format(subject))

    brain.mp2rage_skullstripping(inv2,
                                 t1w,
                                 t1map,
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
