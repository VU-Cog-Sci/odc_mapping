import argparse
import numpy as np
import pandas as pd
import os.path as op
from sklearn.model_selection import LeaveOneGroupOut
from nistats.design_matrix import make_first_level_design_matrix
import os
import os.path as op
import glob
from nilearn import surface
import tensorflow as tf
import logging
from braincoder.decoders import WeightedEncodingModel
import timeit

def main(sourcedata,
         derivatives,
         subject,
         session,
         n_vertices,
         masks,
         description,
         progressbar,
         verbose=False):
    
    logging.basicConfig(level=logging.INFO,
                       format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s")
    logger = logging.getLogger('fit_encoding_model')
    logger.setLevel(logging.DEBUG)
    logger.info('Checking logger, 1-2-3.')

    # get n vertices in left hemisphere
    # This is necessary to solve indexing-issue
    tmp = pd.read_pickle(op.join(derivatives,
                                 'coordinate_patches',
                                 'sub-{subject}',
                                 'anat',
                                 'sub-{subject}_hemi-lh_coordinatepatch.pkl').format(**locals()))

    n_left_vertices = tmp.shape[0]

    logger.info('Using {} vertices masks {} with description {}.'.format(n_vertices,
                                                                         masks,
                                                                         description))

    task = 'checkerboard'

    if subject == '01':
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

    df = df.loc[:, ['V1l', 'V1r']]

    df.index = df.index.droplevel(['subject', 'session', 'acq'])

    v1_both = df.loc[:, ['V1l', 'V1r']].copy()
    v1_both.columns.set_levels(
        ['V1'] * v1_both.shape[1], level=0, verify_integrity=False, inplace=True)

    df = pd.concat((df, v1_both), axis=1)

    for hemi in ['lh', 'rh']:
        energies = pd.read_pickle(op.join(derivatives,
                                          'zmap_spatfreq',
                                          'sub-{subject}',
                                          'ses-{session}',
                                          'func',
                                          'sub-{subject}_ses-{session}_hemi-{hemi}_energies.pkl').format(**locals()))
        max_frequency = energies.groupby(['depth', 'frequency']).sum().groupby(
            'depth', as_index=True).apply(lambda d: d.reset_index('depth', drop=True).idxmax())
        max_wl = 1. / max_frequency

        tmp = df.loc[:, 'V1{}'.format(hemi[:1])].T

        # Solve indexing issue (start at first vertex lh versus rh)
        if hemi == 'lh':
            tmp = tmp.loc[max_wl.loc[:, max_wl.mean() < 4].columns].T
        elif hemi == 'rh':
            tmp = tmp.loc[max_wl.loc[:, max_wl.mean() < 4].columns + n_left_vertices].T

        tmp = pd.concat([tmp],
                        axis=1,
                        keys=['V1{}_shortwl'.format(hemi[:1])],
                        names=['roi'])

        df = pd.concat((df, tmp), axis=1)

    v1_both = df.loc[:, ['V1l_shortwl', 'V1r_shortwl']].copy()
    v1_both.columns.set_levels(
        ['V1_shortwl'] * v1_both.shape[1], level=0, verify_integrity=False, inplace=True)

    df = pd.concat((df, v1_both), axis=1)
    sizes = df.groupby(level='roi', axis=1).size()
    logger.info('Size of rois:\n{}'.format(sizes))

    events_shifted = events.copy()
    events_shifted['onset'] += 4
    X_unconvolved = make_first_level_design_matrix(frametimes,
                                                   events_shifted,
                                                   drift_order=None,
                                                   drift_model=None,
                                                   hrf_model=None).values[:, :2]

    model = WeightedEncodingModel()

    runs = df.index.get_level_values("run").unique().sort_values().tolist()

    results = []
    for (roi, depth), _ in df.loc[:, masks].groupby(level=['roi', 'depth'], axis=1):
        logger.info('Working on roi {} at depth {}'.format(roi, depth))
        for n_vertices_ in n_vertices:
            for lambd in [0.1, 0.5, 0.9, 1.0]:
                logger.info('Lambda = {}'.format(lambd))
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

                    df_train = df_train.groupby(['run']).apply(lambda d: (d - d.mean()) / d.std())
                    r = (X_ * df_train).sum(0) / len(X_)

                    ix = r.abs().sort_values()[-n_vertices_:].index

                    logger.info('fitting')
                    start = timeit.default_timer()
                    model.fit(X_train, df_train.loc[:, ix].values, lambd=lambd,
                              refit_weights=False, progressbar=progressbar)
                    stop = timeit.default_timer()
                    fitting_time = stop - start
                    logger.info('done (in {:.2f} seconds)'.format(fitting_time))

                    df_test = df_test.groupby(['run']).apply(lambda d: (d - d.mean()) / d.std())

                    _, stimulus_p = model.get_stimulus_posterior(
                        df_test.loc[:, ix].values, stimulus_range=np.array([0, 1]))

                    # Bayes factor for stimulus population 1  being on and population 2 being off
                    # versus population 1 off and population 2 on.
                    bf = (stimulus_p[:, 1, 0] + stimulus_p[:, 0, 1]) / \
                        (stimulus_p[:, 1, 1] + stimulus_p[:, 0, 0])

                    map, sd = model.get_map_sd_stimulus_timeseries(
                        df_test.loc[:, ix].values, stimulus_range=np.linspace(-10, 10, 100))

                    r = pd.concat((pd.DataFrame(bf, index=df_test.index, columns=['bayes factor']),
                                   pd.DataFrame(X_test, index=df_test.index, columns=[
                                                'left eye', 'right eye']),
                                   pd.DataFrame(sd, index=df_test.index, columns=[
                                                'SD(left eye)', 'SD(right eye)']),
                                   pd.DataFrame(map, index=df_test.index, columns=['activation left eye', 'activation right eye']),
                                   pd.DataFrame(fitting_time, index=df_test.index, columns=['fitting time'])),
                                  axis=1)
                    X_ = X_test[:, 0] - X_test[:, 1]
                    accuracy = (((X_ == 1) & (bf > 1)).sum() + ((X_ == -1)
                                                                & (bf < 1)).sum()) / np.in1d(X_, [-1, 1]).sum()
                    logger.info('Accuracy: {}'.format(accuracy))

                    r['roi'] = roi
                    r['n_vertices'] = n_vertices_
                    r['depth'] = depth
                    r['fold'] = i
                    r['lambda'] = lambd

                    results.append(r)

    results = pd.concat(results, axis=0)
    results['subject'], results['session'] = subject, session
    results.loc[results['left eye'] == 1.0, 'eye'] = 'left'
    results.loc[results['right eye'] == 1.0, 'eye'] = 'right'

    out_dir = op.join(derivatives, 'encoding_model',
                      'sub-{subject}', 'ses-{session}', 'func').format(**locals())
    if not op.exists(out_dir):
        os.makedirs(out_dir)

    results.to_pickle(op.join(
        out_dir, 'sub-{subject}_desc-{description}_encodingaccuracy.pkl.gz').format(**locals()))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("subject",
                        # nargs='?',
                        type=str,
                        help="subject to process")
    parser.add_argument("session",
                        type=str,
                        default='*',
                        help="subject to process")
    parser.add_argument("--sourcedata",
                        type=str,
                        default='/sourcedata/ds-odc',
                        help="Folder where sourcedata resides")
    parser.add_argument("--derivatives",
                        type=str,
                        default='/derivatives',
                        help="Folder where derivatives reside")
    parser.add_argument('--n_vertices',
                        nargs='+',
                        type=int,
                        default=[40])
    parser.add_argument('--masks',
                        nargs='+',
                        type=str,
                        default=['V1'])
    parser.add_argument('--description',
                        type=str,
                        default='none')
    parser.add_argument('--no-progressbar',
                        dest='progressbar',
                        action='store_false')

    args = parser.parse_args()

    main(args.sourcedata,
         args.derivatives,
         subject=args.subject,
         session=args.session,
         masks=args.masks,
         n_vertices=args.n_vertices,
         description=args.description,
         progressbar=args.progressbar)
