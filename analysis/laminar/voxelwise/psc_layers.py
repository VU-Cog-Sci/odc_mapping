import argparse
import os
import os.path as op
from nilearn import image
import glob
import re
from nilearn.masking import apply_mask
import pandas as pd
import numpy as np

def main(derivatives,
         subject,
         session):

    psc = glob.glob(op.join(derivatives, 'modelfitting',
                              'glm7',
                              'sub-{subject}',
                              'ses-{session}',
                              'func',
                            'sub-{subject}_ses-{session}_task-*_run-*_psc.nii.gz').format(**locals()))

    zmap = glob.glob(op.join(derivatives, 'modelfitting',
                              'glm7',
                              'sub-{subject}',
                              'ses-{session}',
                              'func',
                            'sub-{subject}_ses-{session}_task-*_run-*_zmap.nii.gz').format(**locals()))

    print(zmap)


    masks = glob.glob(op.join(derivatives,
                              'pycortex',
                              'masks',
                              'sub-{subject}',
                              'sub-{subject}_desc-*_gm_mask.nii.gz').format(**locals()))

    depth_map_l = op.join(derivatives,
                          'nighres',
                          'sub-{subject}',
                          'ses-anat',
                          'anat',
                          'sub-{subject}_ses-anat_space-average_desc-layerdepth_hemi-left_depth.nii.gz').format(subject=subject)

    depth_map_r = op.join(derivatives,
                          'nighres',
                          'sub-{subject}',
                          'ses-anat',
                          'anat',
                          'sub-{subject}_ses-anat_space-average_desc-layerdepth_hemi-right_depth.nii.gz').format(subject=subject)
    depth_map = image.math_img('left_depth + right_depth', 
                               left_depth=depth_map_l,
                               right_depth=depth_map_r)


    psc_reg = re.compile('.*/sub-.+_task-(?P<task>[a-z]+)_run-(?P<run>[0-9\.]+)_(?P<condition>left|right)_psc\.nii\.gz')
    psc = [p for p in psc if psc_reg.match(p)]
    psc_meta = [psc_reg.match(p).groupdict() for p in psc]
    psc = [image.resample_to_img(p, depth_map) for p in psc]
    mask_reg = re.compile('.*/sub-.+_desc-(?P<mask>V1l|V1r)_gm_mask\.nii\.gz')

    df_psc = [] 

    for mask in masks:
        if mask_reg.match(mask):
            df_ = apply_mask(psc, mask)
            df_ = pd.DataFrame(df_)

            df_ = pd.concat((df_, pd.DataFrame(psc_meta)),
                           axis=1).set_index(['task',
                                              'condition',
                                              'run'])

            df_.columns = pd.MultiIndex.from_arrays([np.arange(df_.shape[1]),
                                                     apply_mask(depth_map, mask)], names=['voxel', 'depth'])
            df_psc.append(df_)

    df_psc = pd.concat(df_psc,
                   keys=[mask_reg.match(m).group(1) for m in masks if mask_reg.match(m)],
                   axis=1,
                   names=['mask', 'voxel', 'depth'])

    zmap_reg = re.compile('.*/sub-.+_task-(?P<task>[a-z]+)_run-(?P<run>[0-9\.]+)_(?P<condition>left|right)_zmap\.nii\.gz')
    zmap = [p for p in zmap if zmap_reg.match(p)]
    zmap_meta = [zmap_reg.match(p).groupdict() for p in zmap]
    zmap = [image.resample_to_img(p, depth_map) for p in zmap]

    df_zmap = [] 

    for mask in masks:
        if mask_reg.match(mask):
            df_ = apply_mask(zmap, mask)
            df_ = pd.DataFrame(df_)

            df_ = pd.concat((df_, pd.DataFrame(zmap_meta)),
                           axis=1).set_index(['task',
                                              'condition',
                                              'run'])

            df_.columns = pd.MultiIndex.from_arrays([np.arange(df_.shape[1]),
                                                     apply_mask(depth_map, mask)], names=['voxel', 'depth'])
            df_zmap.append(df_)


    df_zmap = pd.concat(df_zmap,
                       keys=[mask_reg.match(m).group(1) for m in masks if mask_reg.match(m)],
                       axis=1,
                       names=['mask', 'voxel', 'depth'])


    df = pd.concat([df_psc, df_zmap],
                   keys=['psc', 'zmap'],
                   axis=1,
                   names=['type'])

    results_dir = op.join(derivatives,
                          'laminar_analysis',
                          'sub-{subject}',
                          'ses-{session}',
                          'func',).format(**locals())

    if not op.exists(results_dir):
        os.makedirs(results_dir)

    df.to_pickle(op.join(results_dir, 'sub-{subject}_ses-{session}_desc-psc.pkl').format(**locals()))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("subject", 
                        #nargs='?',
                        type=str,
                        help="subject to process")
    parser.add_argument("session", 
                        type=str,
                        default='*',
                        help="subject to process")
    args = parser.parse_args()

    main('/data/odc/derivatives', 
         subject=args.subject,
         session=args.session)

