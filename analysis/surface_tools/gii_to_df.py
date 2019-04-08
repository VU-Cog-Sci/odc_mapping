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
    print(fn_template)
    fns = glob.glob(fn_template)

    rois = cortex.utils.get_roi_verts('odc.{}'.format(subject))

    reg = re.compile('.*/sub-(?P<subject>.+)_ses-(?P<session>.+)_task-(?P<task>.+)_acq-(?P<acq>.+)_run-(?P<run>.+)_desc-depth.(?P<depth>[0-9]+.[0-9]+)_hemi-lh.gii'.format(**locals()))

    results = []

    for fn in fns:

        meta = reg.match(fn).groupdict() 
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
        d_r = surface.load_surf_data(fn.replace('lhemi-lh', 'hemi-rh')).T
        d = np.concatenate((d_l, d_r), 1)
        d = pd.DataFrame(clean(d, confounds=confounds_trans.values, standardize='psc'))

        
        for key in meta:
            d[key] = meta[key]
        d['frame'] = np.arange(len(d))
        
        results.append(d)

    results = pd.concat(results)

    ix_keys = ['subject', 'session', 'task', 'acq', 'run', 'frame', 'depth']

    results_ = []

    for key in rois:
        tmp = results.loc[:, rois[key].tolist() + ix_keys]
        tmp = tmp.loc[:, (tmp != 0).any()]
        
        tmp = tmp.pivot_table(index=ix_keys[:-1], 
                        columns='depth')
        
        tmp = pd.concat([tmp], keys=[key], names=['roi'], axis=1)
        results_.append(tmp)
        
    results = pd.concat(results_, axis=1)
    results.columns.set_names('vertex', 1, inplace=True)

    verts_without_all_zeros = np.where(~(results == 0).any(0).groupby('vertex').any())[0]
    results = results.loc[:, (slice(None), verts_without_all_zeros, slice(None))]

    target_dir = op.join(derivatives,
                         'depth_sampled_surfaces',
                         'sub-{subject}').format(subject=subject)

    if not op.exists(target_dir):
        os.makedirs(target_dir)

    results.to_pickle(op.join(target_dir, 'sub-{subject}_depth_sampled_data.pkl.gz'))

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

