from nistats.first_level_model import FirstLevelModel
import pandas as pd


#def main():

model = FirstLevelModel(t_r=4)

paradigm = pd.read_table('/sourcedata/sub-tk/ses-odc2/func/sub-tk_ses-odc2_task-fixation_acq-07_run-01_events.tsv')
bold = '/sourcedata/sub-tk/ses-odc2/func/sub-tk_ses-odc2_task-fixation_acq-07_run-01_bold.nii'

model.fit(bold, paradigm)

#if __name__ == '__main__':
    
    #main()
