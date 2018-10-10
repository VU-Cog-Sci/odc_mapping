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


    fmriprep_layout = BIDSLayout(os.path.join(derivatives,
                                              'fmriprep'))
    
    manual_layout = BIDSLayout(os.path.join(derivatives,
                                              'manual_segmentation'))

    manual = {}
    manual['wm'] = get_bids_file(manual_layout, subject, 'manualsegwm')
    manual['gm'] = get_bids_file(manual_layout, subject, 'manualseggm')


    fmriprep = {}
    fmriprep['wm'] = get_bids_file(fmriprep_layout, subject, 'probtissue', 'WM')
    fmriprep['gm'] = get_bids_file(fmriprep_layout, subject, 'probtissue', 'GM')
    fmriprep['csf'] = get_bids_file(fmriprep_layout, subject, 'probtissue', 'CSF')

    
    extract_layout = BIDSLayout(os.path.join(derivatives,
                                             'nighres',
                                             'cortex_extraction'))

    output_dir = os.path.join(derivatives,
                              'nighres',
                              'cortex_extraction',
                              'sub-{}'.format(subject))

    freesurfer_seg = get_bids_file(fmriprep_layout, subject, 'roi', 'label-aseg')

    _regions = ['wm', 'csf', 'gm']

    for hemi in ['left', 'right']:

        mgdm = {}
        for r in _regions:
            mgdm[r] = get_bids_file(extract_layout, subject, 'p{}'.format(r), hemi)

        freesurfer_seg = image.resample_to_img(freesurfer_seg, 
                                               mgdm['gm'], 
                                               interpolation='nearest')

        freesurfer = {}
        if hemi == 'left':
            freesurfer['wm'] = image.math_img('(seg == 2).astype(int)', seg=freesurfer_seg)
            freesurfer['gm'] = image.math_img('(seg == 3).astype(int)', seg=freesurfer_seg)
        else:
            freesurfer['wm']  = image.math_img('(seg == 41).astype(int)', seg=freesurfer_seg)
            freesurfer['gm'] = image.math_img('(seg == 42).astype(int)', seg=freesurfer_seg)

        for key in freesurfer:
            freesurfer[key] = image.resample_to_img(freesurfer[key], mgdm['gm'], interpolation='nearest')
            

        for key in _regions:
            fmriprep[key] = image.resample_to_img(fmriprep[key], mgdm[key], interpolation='nearest')

        wm = image.math_img('fmriprep + mgdm + freesurfer + manual*5', 
                            mgdm=mgdm['wm'],
                            fmriprep=fmriprep['wm'],
                            freesurfer=freesurfer['wm'],
                            manual=manual['wm'])

        gm = image.math_img('fmriprep + mgdm + freesurfer +  manual*5', 
                            mgdm=mgdm['gm'],
                            fmriprep=fmriprep['gm'],
                            freesurfer=freesurfer['gm'],
                            manual=manual['gm'])

        csf = image.math_img('3 * mgdm', mgdm=mgdm['csf'])

        total_prob = image.math_img('wm + gm + csf',
                                    wm=wm,
                                    gm=gm,
                                    csf=csf)

        wm = image.math_img('wm / total_prob', wm=wm, total_prob=total_prob)
        gm = image.math_img('gm / total_prob', gm=gm, total_prob=total_prob)
        csf = image.math_img('csf / total_prob', csf=csf, total_prob=total_prob)

        inside_mask = image.math_img('wm > 0.45', wm=wm)
        inside_mask = image.largest_connected_component_img(inside_mask)

        cruise = nighres.cortex.cruise_cortex_extraction(
                                init_image=inside_mask,
                                wm_image=wm,
                                gm_image=gm,
                                csf_image=csf,
                                normalize_probabilities=False,
                                file_name='sub-{}_{}'.format(subject, hemi),
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

    if len(img) == 0:
        raise Exception('Found no image for {}, {}'.format(modality, 
                                                           filter))
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
