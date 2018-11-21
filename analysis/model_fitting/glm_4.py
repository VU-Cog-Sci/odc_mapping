from nistats.first_level_model import FirstLevelModel
from nistats.second_level_model import SecondLevelModel
import pandas as pd
import argparse
from bids.grabbids import BIDSLayout
import os
from nilearn import image

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

    derivatives_layout = BIDSLayout(os.path.join(derivatives, 'spynoza_mc_mutualinfo'))
    derivatives_df = derivatives_layout.as_data_frame()
    bold =  derivatives_df[(derivatives_df['type'] == 'preproc') &
                               (derivatives_df['subject'] == subject) &
                               (derivatives_df['session'] == session)]

    confounds =  derivatives_df[(derivatives_df['type'] == 'confounds') &
                               (derivatives_df['subject'] == subject) &
                               (derivatives_df['session'] == session)]

    print(derivatives_df.type.unique())

    mask = derivatives_layout.get(subject=subject,
                                  session=session,
                                  type='mask',
                                  return_type='file')[0]

    df = events.merge(bold, on=['subject', 'session', 'run'],
                           suffixes=('_events','_bold'))

    confounds = confounds.rename(columns={'path':'confounds'})
    df = df.merge(confounds[['subject', 'session', 'run', 'confounds']])
    
    models = []
    for ix, row in df.iterrows():

        results_dir = os.path.join(derivatives, 
                                   'modelfitting', 
                                   'glm4',
                                   'sub-{}'.format(row['subject']))
        if 'session' in row:
            results_dir = os.path.join(results_dir, 'ses-{}'.format(row['session']))
        
        os.makedirs(results_dir, exist_ok=True)

        confounds = pd.read_table(row.confounds).fillna(method='bfill')

        print('Fitting {}'.format(row['path_bold']))
        model = FirstLevelModel(t_r=4,
                                mask=mask)
        paradigm = pd.read_table(row['path_events'])
        model.fit(row['path_bold'], paradigm, confounds=confounds)

        left_right = model.compute_contrast('eye_L - eye_R', output_type='z_score')
        left_right.to_filename(os.path.join(results_dir, 'sub-{}_ses-{}_run-{}_left_over_right_zmap.nii.gz'.format(row['subject'], 
                                                                                                                   row['session'],
                                                                                                                   row['run'])))
        left_right = model.compute_contrast('eye_L - eye_R', output_type='effect_size')
        left_right.to_filename(os.path.join(results_dir, 'sub-{}_ses-{}_run-{}_left_over_right_psc.nii.gz'.format(row['subject'], 
                                                                                                                   row['session'],
                                                                                                                   row['run'])))
        models.append(model)

    second_level_model = SecondLevelModel(mask=mask)
    second_level_model.fit(models)

    left_right_group =second_level_model.compute_contrast(
        first_level_contrast='eye_L - eye_R',
        output_type='z_score')
    left_right_group.to_filename(os.path.join(results_dir, 
                                              'sub-{}_ses-{}_left_over_right_zmap.nii.gz'.format(row['subject'], 
                                                                                                 row['session'])))

    left_right_group =second_level_model.compute_contrast(
        first_level_contrast='eye_L - eye_R',
        output_type='effect_size')
    left_right_group.to_filename(os.path.join(results_dir, 
                                              'sub-{}_ses-{}_left_over_right_effect_size.nii.gz'.format(row['subject'], 
                                                                                                 row['session'])))
    
    left_right_group =second_level_model.compute_contrast(
        first_level_contrast='eye_L - eye_R',
        output_type='z_score')
    left_right_group.to_filename(os.path.join(results_dir, 
                                              'sub-{}_ses-{}_left_over_right_zmap.nii.gz'.format(row['subject'], 
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

