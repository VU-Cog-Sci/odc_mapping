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
from nilearn._utils.ndimage import largest_connected_component

def main(sourcedata, 
         derivatives,
         tmp_dir,
         subject=None):


    cruise_layout = BIDSLayout(os.path.join(derivatives,
                                             'nighres',
                                             'cortex_extraction_combine_manual_freesurfer'))


    for hemi in ['right', 'left']:
        csf_gm_boundary = get_bids_file(cruise_layout, subject, 'cgb', hemi)
        gm_wm_boundary = get_bids_file(cruise_layout, subject, 'gwb', hemi)

        output_dir = os.path.join(derivatives, 'nighres', 'layers')

        depth = nighres.laminar.volumetric_layering(
                                                inner_levelset=gm_wm_boundary,
                                                outer_levelset=csf_gm_boundary,
                                                n_layers=4,
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
