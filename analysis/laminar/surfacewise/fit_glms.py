import argparse
import pandas as pd
from nilearn import surface
import glob
import os.path as op
import numpy as np
from nistats.design_matrix import make_first_level_design_matrix
from nistats.first_level_model import run_glm
import os
from bids import BIDSLayout
from sklearn import decomposition


def main(sourcedata,
         derivatives,
         subject,
         session):
    derivatives_layout = BIDSLayout(op.join(derivatives), validate=False)
    derivatives_df = derivatives_layout.as_data_frame()

    confounds =  derivatives_df[(derivatives_df['suffix'] == 'confounds') &
                               (derivatives_df['subject'] == subject) &
                               (derivatives_df['session'] == session)].set_index(['subject', 'session', 'task', 'run'])

    compcor =  derivatives_df[(derivatives_df['suffix'] == 'compcor') &
                              (derivatives_df['subject'] == subject) &
                              (derivatives_df['session'] == session)].set_index(['subject', 'session', 'task', 'run'])

    fns = glob.glob(op.join(derivatives, 'sampled_giis/sub-{subject}/ses-{session}/func/sub-{subject}_ses-{session}_*.gii'.format(**locals())))
    # Events are the same for all subjects
    events = pd.read_table(op.join(sourcedata,
                                   'sub-tk/ses-odc2/func/sub-tk_ses-odc2_task-checkerboard_acq-07_run-02_events.tsv'))

    df = pd.read_pickle(op.join(derivatives,
                                'depth_sampled_surfaces/sub-{subject}/sub-{subject}_ses-{session}_depth_sampled_data.pkl.gz'.format(**locals())))
    print(df.head())
    df = df.loc[:, 'psc']

    df.index = df.index.droplevel('acq')

    frametimes = np.linspace(0, 66*4, 66, endpoint=False)
    X = make_first_level_design_matrix(frametimes, events, drift_order=None, drift_model=None)

    ts = []
    for ix, d in df.loc[:, ['V1l', 'V1r']].groupby(['subject', 'session', 'task', 'run']):
        print(ix)
        conf = pd.read_table(confounds.loc[ix].path).fillna(method='bfill')
        comc = pd.read_table(compcor.loc[ix].path).fillna(method='bfill')

        conf = pd.concat((conf, comc), 1)
        conf -= conf.mean()
        conf /= conf.std()

        pca = decomposition.PCA(n_components=6)
        confounds_trans = pd.DataFrame(pca.fit_transform(conf),
                                       columns=['pca_{}'.format(i) for i in range(6)])

        confounds_trans.index = X.index

        X_ = pd.concat((X, confounds_trans), axis=1)
        labels, results = run_glm(d, X, noise_model='ols')


        results = results[0.0]
        
        ts.append(pd.DataFrame([results.theta[0], results.theta[1], results.t(0), results.t(1)],
                            index=pd.MultiIndex.from_product([[e] for e in ix] + [['psc', 't'], ['eye_L', 'eye_R']],
                                                             names=['subject',
                                                                    'session',
                                                                    'task',
                                                                    'run',
                                                                    'type',
                                                                    'contrast']),
                            columns=d.columns))

    ts = pd.concat(ts, axis=0)


    results_dir = op.join(derivatives, 'surfacewise_glms', 'sub-{subject}', 'ses-{session}', 'func').format(**locals())
    if not op.exists(results_dir):
        os.makedirs(results_dir)

    ts.to_pickle(op.join(results_dir, 'sub-{subject}_ses-{session}_desc-laminarglms.pkl').format(**locals()))


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

    main('/sourcedata/ds-odc',
         '/derivatives', 
         subject=args.subject,
         session=args.session)

