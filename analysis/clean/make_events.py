import pandas as pd
from bids import BIDSLayout
import argparse
import numpy as np
import ast
import os
import glob
import os.path as op


def main(bids_dir, subject, session):
    layout = BIDSLayout(bids_dir)
    
    trials = layout.get(suffix='trials', 
                        session=session,
                        subject=subject,
                        extensions='tsv')

    trials = glob.glob(op.join(bids_dir, 'sub-{subject}/ses-{session}/beh/*.tsv'.format(**locals())))
    print(trials)

    onset_dir = os.path.join(bids_dir, 
                      'sub-{}'.format(subject))
    
    if session is not None:
        onset_dir = os.path.join(onset_dir, 'ses-{}'.format(session))

    onset_dir = os.path.join(onset_dir, 'func')

    for trial in trials:
        print(trial)
        trial_properties = pd.read_table(trial, index_col=0)

        eye_onsets = []

        eyes = ['R', 'L']
        
        intro_duration = trial_properties.loc[0, 'intro_duration']
        start_durations = ast.literal_eval(trial_properties.loc[0, 'monocular_durations'])
        
        current_time = intro_duration

        onsets = []

        for duration in start_durations:
            for eye in eyes:
                d = {'trial_type':'eye_{}'.format(eye),
                     'onset':current_time,
                     'duration':duration}

                onsets.append(d)
                current_time += duration

        onsets = pd.DataFrame(onsets)


        if session is not None:
            session_str = '_ses-{}'.format(session)
        else:
            session_str = ''
        _, fn = op.split(trial)
        fn = fn.replace('_trials', '_events')
        fn = os.path.join(onset_dir, fn)
        print(fn)
        
        onsets.to_csv(fn, sep='\t', index=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("subject", 
                        help="subject to process")
    parser.add_argument("session", 
                        help="session to process")
    args = parser.parse_args()

    main('/sourcedata/ds-odc', 
         subject=args.subject,
         session=args.session)

