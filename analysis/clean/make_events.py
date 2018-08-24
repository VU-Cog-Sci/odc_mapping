import pandas as pd
from bids.grabbids import BIDSLayout
import argparse
import numpy as np
import ast


def main(bids_dir, subject):
    layout = BIDSLayout(bids_dir)
    
    trials = layout.get(type='trials', 
                        extensions='tsv')

    for trial in trials:
        print(trial)
        trial_properties = pd.read_table(trial.filename, index_col=0)

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

        print(pd.DataFrame(onsets))



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("subject", 
                        help="subject to process")
    args = parser.parse_args()

    main('/sourcedata', 
         subject=args.subject)

