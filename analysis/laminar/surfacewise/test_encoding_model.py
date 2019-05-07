import argparse
import numpy as np
import pandas as pd
from encoding import BinocularModelFitter
import os.path as op
from sklearn.model_selection import LeaveOneGroupOut
from nistats.design_matrix import make_first_level_design_matrix
import os

def main(sourcedata,
         derivatives,
         subject,
         session):
    task = 'checkerboard'

    run = '02'

    if subject == 'bm':
        task = 'fixation'

    events = pd.read_csv(op.join(sourcedata, 
                                   'sub-{subject}', 
                                   'ses-{session}',
                                   'func',
                                   'sub-{subject}_ses-{session}_task-{task}_acq-07_run-02_events.tsv').format(**locals()),
                         sep='\t')

    frametimes = np.linspace(0, 66*4, 66, endpoint=False)

    df = pd.read_pickle(op.join(derivatives,
                                'depth_sampled_surfaces/sub-{subject}/sub-{subject}_ses-{session}_depth_sampled_data.pkl.gz'.format(**locals())))
    df = df.loc[:, 'cleaned']

    df.index = df.index.droplevel(['subject' ,'session', 'acq'])

    events_shifted = events.copy()
    events_shifted['onset'] += 4
    X_unconvolved = make_first_level_design_matrix(frametimes,
                                                   events_shifted,
                                                   drift_order=None,
                                                   drift_model=None,
                                                   hrf_model=None).values[:, :2]

    fitter = BinocularModelFitter()

    runs = df.index.get_level_values("run").unique().sort_values().tolist()

    results = []
    for (roi, depth), _ in df.loc[:, ['V1l', 'V1r']].groupby(level=['roi', 'depth'], axis=1):
        print(roi, depth)
        for n_vertices in [25, 50, 100, 250, 500]:
            print(n_vertices)
            for i, run in enumerate(runs[::2]):
                train = [run, run+1]
                test = runs.copy()
                test.remove(run)
                test.remove(run+1)

                X_train = np.tile(X_unconvolved, (len(train), 1))
                X_test = np.tile(X_unconvolved, (len(test), 1))

                df_test = df.loc[(slice(None),
                                   test),
                                  (roi, slice(None), depth)]

                df_train = df.loc[(slice(None),
                                   train),
                                  (roi, slice(None), depth)]

                X_ = (X_train[:, 0] - X_train[:, 1])[:, np.newaxis]
                X_ = (X_ - X_.mean(0))/X_.std()

                df_train =  (df_train - df_train.mean()) / df_train.std()
                r = (X_ * df_train).sum(0) / len(X_)

                ix = r.abs().sort_values()[-n_vertices:].index

                print('fitting')
                fitter.fit(df_train.loc[:, ix].values, X_train)
                print('done')


                df_test = (df_test - df_test.mean()) / df_test.std()
                _, map = fitter.decode(df_test.loc[:, ix].values, stimulus_range=np.array([0, 1]))

                # Bayes factor for stimulus population 1  being on and population 2 being off
                # versus population 1 off and population 2 on.
                bf = (map[:, 1, 0] + map[:, 0, 1]) / (map[:, 0, 1] + map[:, 0, 0])


                X_ = X_test[:, 0] - X_test[:, 1]
                accuracy = (((X_ == 1) & (bf > 1)).sum() + ((X_ == -1) & (bf < 1)).sum()) / np.in1d(X_, [-1,1]).sum()
                print(accuracy)


                r = pd.concat((pd.DataFrame(bf, index=df_test.index, columns=['bayes factor']),
                               pd.DataFrame(X_test, index=df_test.index, columns=['left eye', 'right eye'])),
                              axis=1)

                r['roi'] = roi
                r['n_vertices'] = n_vertices
                r['depth'] = depth
                r['fold'] = i+i

                results.append(r)


    results = pd.concat(results, axis=0)
    results['subject'], results['session'] = subject, session
    results.loc[results['left eye'] == 1.0, 'eye'] = 'left'
    results.loc[results['right eye'] == 1.0, 'eye'] = 'right'


    out_dir = op.join(derivatives, 'encoding_model', 'sub-{subject}', 'ses-{session}', 'func').format(**locals())
    if not op.exists(out_dir):
        os.makedirs(out_dir)

    results.to_pickle(op.join(out_dir, 'sub-{subject}_desc-encodingaccuracy.pkl.gz').format(**locals()))


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


    
