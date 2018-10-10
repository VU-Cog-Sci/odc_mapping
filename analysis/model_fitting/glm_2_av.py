from nistats.first_level_model import FirstLevelModel
from nistats.second_level_model import SecondLevelModel
import pandas as pd
import argparse
from bids.grabbids import BIDSLayout
import os
from nilearn import image
from spynoza.utils import average_over_runs

def main(sourcedata,
         derivatives,
         subject,
         session,
         tmp_dir):

    sourcedata_layout = BIDSLayout(sourcedata)
    sourcedata_df = sourcedata_layout.as_data_frame()
    events =  sourcedata_df[(sourcedata_df['type'] == 'events') &
                               (sourcedata_df['subject'] == subject) &
                               (sourcedata_df['session'] == session)]

    derivatives_layout = BIDSLayout(os.path.join(derivatives, 'spynoza'))
    derivatives_df = derivatives_layout.as_data_frame()
    bold =  derivatives_df[(derivatives_df['type'] == 'preproc') &
                               (derivatives_df['subject'] == subject) &
                               (derivatives_df['session'] == session)]

    mask = derivatives_layout.get(subject=subject,
                                  session=session,
                                  type='mask',
                                  return_type='file')[0]

    mask = image.math_img('(im > .5).astype(int)', im=mask)
    print(mask)

    row = bold.iloc[0]

    results_dir = os.path.join(derivatives, 
                               'modelfitting_av', 
                               'glm2',
                               'sub-{}'.format(row['subject']))
    os.makedirs(results_dir, exist_ok=True)

    av_bold_fn = os.path.join(results_dir, 'sub-{}_ses-{}_bold_average.nii.gz'.format(row['subject'], row['session']))
    av_bold = average_over_runs(bold.path.tolist(), output_filename=av_bold_fn)

    av_bold = image.math_img('(av_bold / av_bold.mean(-1)[..., np.newaxis])', av_bold=av_bold)
    av_bold.to_filename(av_bold_fn)
    
    model = FirstLevelModel(t_r=4,
                            mask=mask,
                            drift_model=None)

    paradigm = pd.read_table(events.iloc[0]['path'])
    model.fit(av_bold, paradigm)

    left_right = model.compute_contrast('eye_L - eye_R', output_type='z_score')
    left_right.to_filename(os.path.join(results_dir, 'sub-{}_ses-{}_left_over_right_zmap.nii.gz'.format(row['subject'], 
                                                                                                               row['session'],)))
    left_right = model.compute_contrast('eye_L - eye_R', output_type='effect_size')
    left_right.to_filename(os.path.join(results_dir, 'sub-{}_ses-{}_left_over_right_psc.nii.gz'.format(row['subject'], 
                                                                                                               row['session'])))

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

    main('/sourcedata', 
         '/derivatives',
         subject=args.subject,
         session=args.session,
         tmp_dir='/workflow_folders')

