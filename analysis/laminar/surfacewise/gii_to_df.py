import argparse
import cortex
from nilearn import surface
import glob
import os
import os.path as op
import re
from nilearn.signal import clean
import pandas as pd
import numpy as np
from sklearn import decomposition

def main(derivatives,
         subject,
         session):

    fn_template = op.join(derivatives, 'sampled_giis', 'sub-{subject}', 'ses-{session}',
            'func', 'sub-{subject}_ses-{session}_task-*_acq-*_run-*desc-depth.0.*_hemi-lh.gii').format(**locals())

    fns = glob.glob(fn_template)

    rois = cortex.utils.get_roi_verts('odc.{}'.format(subject))

    reg = re.compile('.*/sub-(?P<subject>.+)_ses-(?P<session>.+)_task-(?P<task>.+)_acq-(?P<acq>.+)_run-(?P<run>.+)_desc-depth.(?P<depth>[0-9]+.[0-9]+)_hemi-lh.gii'.format(**locals()))

    results = []

    for fn in fns:

        meta = reg.match(fn).groupdict() 
        print(meta)
        meta['run'] = int(meta['run'])

        mov = pd.read_table(op.join(derivatives, 'spynoza/sub-{subject}/ses-{session}/func/sub-{subject}_ses-{session}_task-{task}_acq-{acq}_run-{run:02d}_confounds.tsv'.format(**meta)))
        compcorr = pd.read_table(op.join(derivatives,'spynoza/sub-{subject}/ses-{session}/func/sub-{subject}_ses-{session}_task-{task}_acq-{acq}_run-{run:02d}_confounds_compcor.tsv'.format(**meta)))

        confounds = pd.concat((mov, compcorr), 1).fillna(method='bfill')
        confounds -= confounds.mean()
        confounds /= confounds.std()

        pca = decomposition.PCA(n_components=6)
        confounds_trans = pd.DataFrame(pca.fit_transform(confounds),
                                       columns=['pca_{}'.format(i) for i in range(6)])


        d_l = surface.load_surf_data(fn).T
        d_r = surface.load_surf_data(fn.replace('hemi-lh', 'hemi-rh')).T
        d = np.concatenate((d_l, d_r), 1)
        print(d.shape)

        d_dirty = pd.DataFrame(d.copy())
        d_clean = pd.DataFrame(clean(d_dirty.values, confounds=confounds_trans.values, standardize=False))

        
        for key in meta:
            d_clean[key] = meta[key]
            d_dirty[key] = meta[key]
        d_clean['frame'] = np.arange(len(d))
        d_dirty['frame'] = np.arange(len(d))

        d  = pd.concat([d_clean, d_dirty], keys=['cleaned', 'psc'], names=['type', 'vertex'], axis=1)
        
        results.append(d)

    results = pd.concat(results)

    ix_keys = ['subject', 'session', 'task', 'acq', 'run', 'frame', 'depth']

    results_ = []

    for type, d in results.groupby(level='type', axis=1):
        for key in rois:
            if len(rois[key])> 0:
                tmp = d[type].loc[:, rois[key].tolist() + ix_keys]
                
                tmp = tmp.pivot_table(index=ix_keys[:-1], 
                                columns='depth')
                
                tmp = pd.concat([tmp], keys=[(type, key)], names=['type', 'roi'], axis=1)
                results_.append(tmp)
        
    results = pd.concat(results_, axis=1)

    all_depth_results = pd.concat([results.groupby(level=['type', 'roi', 'vertex'],
                                                                  axis=1).mean()],
                                                 keys=['all'],
                                                 names=['depth'],
                                                 axis=1)
    all_depth_results.columns = all_depth_results.columns.reorder_levels(results.columns.names)

    results = pd.concat([results, all_depth_results], axis=1).sort_index(axis=1)


    # Filter out vertices where one or more runs/depths has std of 0
    if subject not in ['bm']:
        ix = (~(((results.groupby('run').std() == 0).any(0)))).groupby('vertex').all()
        results = results.loc[:, results.columns.get_level_values('vertex').isin(ix[ix].index)]

    target_dir = op.join(derivatives,
                         'depth_sampled_surfaces',
                         'sub-{subject}').format(subject=subject)

    if not op.exists(target_dir):
        os.makedirs(target_dir)

    results.to_pickle(op.join(target_dir, 'sub-{subject}_ses-{session}_depth_sampled_data.pkl.gz'.format(**locals())))

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

    main('/derivatives', 
         subject=args.subject,
         session=args.session)

