import argparse
import pandas as pd
from nilearn import surface
import glob
import os.path as op
import numpy as np
from nistats.design_matrix import make_first_level_design_matrix
from nistats.first_level_model import run_glm
import os

def main(derivatives,
         subject,
         session):

    fns = glob.glob(op.join(derivatives, 'sampled_giis/sub-{subject}/ses-{session}/func/sub-{subject}_ses-{session}_*.gii'.format(**locals())))
    events = pd.read_table('/data/odc/sourcedata/sub-tk/ses-odc2/func/sub-tk_ses-odc2_task-checkerboard_acq-07_run-02_events.tsv')

    df = pd.read_pickle('/data/odc/derivatives/depth_sampled_surfaces/sub-{subject}/sub-{subject}_ses-{session}_depth_sampled_data.pkl.gz'.format(**locals()))
    df = df.droplevel('acq')

    frametimes = np.linspace(0, 66*4, 66, endpoint=False)
    X = make_first_level_design_matrix(frametimes, events, drift_order=None, drift_model=None)

    def get_contrast(d):
        labels, results = run_glm(d, X, noise_model='ols')
        
        results = results[0.0]
        
        return pd.DataFrame([results.theta[0], results.theta[1], results.t(0), results.t(1)],
                            index=pd.MultiIndex.from_product([['psc', 't'], ['eye_L', 'eye_R']],
                                                             names=['type', 'contrast']),
                            columns=d.columns)

    ts = df.groupby(['subject', 'session', 'task', 'run']).apply(get_contrast)

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

    main('/data/odc/derivatives', 
         subject=args.subject,
         session=args.session)

