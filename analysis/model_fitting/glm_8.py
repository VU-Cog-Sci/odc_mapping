from nistats.first_level_model import FirstLevelModel
from nistats.second_level_model import SecondLevelModel
import pandas as pd
import argparse
from bids import BIDSLayout
import os
import os.path as op
from nilearn import image
from sklearn import decomposition
from sklearn.model_selection import KFold
import numpy as np

def main(sourcedata,
         derivatives,
         subject,
         session,
         tmp_dir):

    sourcedata_layout = BIDSLayout(sourcedata)
    sourcedata_df = sourcedata_layout.as_data_frame()
    events =  sourcedata_df[(sourcedata_df['suffix'] == 'events') &
                               (sourcedata_df['subject'] == subject) &
                               (sourcedata_df['session'] == session)]

    derivatives_layout = BIDSLayout(os.path.join(derivatives), validate=False)
    derivatives_df = derivatives_layout.as_data_frame()
    bold =  derivatives_df[(derivatives_df['suffix'] == 'preproc') &
                               (derivatives_df['subject'] == subject) &
                               (derivatives_df['session'] == session)]

    confounds =  derivatives_df[(derivatives_df['suffix'] == 'confounds') &
                               (derivatives_df['subject'] == subject) &
                               (derivatives_df['session'] == session)]

    compcor =  derivatives_df[(derivatives_df['suffix'] == 'compcor') &
                              (derivatives_df['subject'] == subject) &
                              (derivatives_df['session'] == session)]

    mask = derivatives_layout.get(subject=subject,
                                  session=session,
                                  suffix='mask',
                                  return_type='file')[0]

    df = events.merge(bold, on=['subject', 'session', 'run'],
                           suffixes=('_events','_bold'))

    confounds = confounds.rename(columns={'path':'confounds'})
    df = df.merge(confounds[['subject', 'session', 'run', 'confounds']])

    compcor = compcor.rename(columns={'path':'compcor'})
    df = df.merge(compcor[['subject', 'session', 'run', 'compcor']])

    df.sort_values('run', inplace=True)

    print(df.iloc[0])

    models = []
    for ix, row in df.iterrows():

        results_dir = os.path.join(derivatives, 
                                   'modelfitting', 
                                   'glm8',
                                   'sub-{}'.format(row['subject']))
        if 'session' in row:
            results_dir = os.path.join(results_dir, 'ses-{}'.format(row['session']))

        results_dir = op.join(results_dir, 'func')
        
        os.makedirs(results_dir, exist_ok=True)

        confounds = pd.read_table(row.confounds).fillna(method='bfill')
        compcor = pd.read_table(row.compcor).fillna(method='bfill')

        confounds = pd.concat((confounds, compcor), 1)
        confounds -= confounds.mean()
        confounds /= confounds.std()

        pca = decomposition.PCA(n_components=6)
        confounds_trans = pd.DataFrame(pca.fit_transform(confounds),
                                       columns=['pca_{}'.format(i) for i in range(6)])

        print('Fitting {}'.format(row['path_bold']))
        model = FirstLevelModel(t_r=4,
                                signal_scaling=False,
                                subject_label=int(row['run']),
                                mask_img=mask)
        paradigm = pd.read_table(row['path_events'])
        paradigm_ = paradigm.copy()
        paradigm['trial_type'] = 'stimulation'
        paradigm['modulation'] = 1
        paradigm_['modulation'] = paradigm_.trial_type.map({'eye_L':1, 
                                                            'eye_R':-1})
        paradigm_['trial_type'] = 'eye'
        paradigm = pd.concat((paradigm, paradigm_), ignore_index=True)

        model.fit(row['path_bold'], paradigm, confounds=confounds_trans)

        row['run'] = int(row['run'])
        row = dict(row)

        left_right = model.compute_contrast('eye', output_type='z_score')
        left_right.to_filename(os.path.join(results_dir,
                                            'sub-{subject}_ses-{session}_task-{task_events}_run-{run:02d}_left_over_right_zmap.nii.gz'.format(**row)))

        left_right = model.compute_contrast('eye', output_type='effect_size')
        left_right.to_filename(os.path.join(results_dir, 
                                            'sub-{subject}_ses-{session}_task-{task_events}_run-{run:02d}_left_over_right_psc.nii.gz'.format(**row)))

        stimulation = model.compute_contrast('stimulation', output_type='effect_size')
        stimulation.to_filename(os.path.join(results_dir, 
                                      'sub-{subject}_ses-{session}_task-{task_events}_run-{run:02d}_stimulation_psc.nii.gz'.format(**row)))

        stimulation = model.compute_contrast('stimulation', output_type='z_score')
        stimulation.to_filename(os.path.join(results_dir, 
                                       'sub-{subject}_ses-{session}_task-{task_events}_run-{run:02d}_stimulation_zmap.nii.gz'.format( **row)))

        models.append(model)



    second_level_model = SecondLevelModel(mask_img=mask)
    second_level_model.fit(models)

    left_right_group =second_level_model.compute_contrast(
        first_level_contrast='eye',
        output_type='z_score')
    left_right_group.to_filename(os.path.join(results_dir, 
                                              'sub-{}_ses-{}_left_over_right_zmap.nii.gz'.format(row['subject'], 
                                                                                                 row['session'])))

    left_right_group =second_level_model.compute_contrast(
        first_level_contrast='eye',
        output_type='effect_size')
    left_right_group.to_filename(os.path.join(results_dir, 
                                              'sub-{}_ses-{}_left_over_right_effect_size.nii.gz'.format(row['subject'], 
                                                                                                 row['session'])))

    stimulation_group =second_level_model.compute_contrast(
        first_level_contrast='stimulation',
        output_type='z_score')
    left_right_group.to_filename(os.path.join(results_dir, 
                                              'sub-{}_ses-{}_stimulation_zmap.nii.gz'.format(row['subject'], 
                                                                                                 row['session'])))

    stimulation_group =second_level_model.compute_contrast(
        first_level_contrast='stimulation',
        output_type='effect_size')
    left_right_group.to_filename(os.path.join(results_dir, 
                                              'sub-{}_ses-{}_stimulation_effect_size.nii.gz'.format(row['subject'], 
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

    main('/sourcedata/ds-odc', 
         '/derivatives',
         subject=args.subject,
         session=args.session,
         tmp_dir='/workflow_folders')

