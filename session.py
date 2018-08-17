from exptools.core.session import MRISession
from stimuli import StimulusSet, StimulusSetToPosition
from trial import PositioningTrial, StimulationTrial
import numpy as np
import glob
import pandas as pd

class ODCSession(MRISession):

    def __init__(self, *args, **kwargs):
        super(MRISession, self).__init__(*args, **kwargs)

        parameters = self.find_parameters_subject()

        if parameters is None:
            parameters = self.get_default_parameters()

        self.framerate = self.config.get('screen', 'framerate')

        self.positioning_trial = PositioningTrial(session=self,
                                                  parameters=parameters)

        
    def run(self):
        """run the session"""

        self.positioning_trial.run()

        self.stop()
        self.close()
    

    def find_parameters_subject(self):

        fns = sorted(glob.glob('data/{}*.tsv'.format(self.subject_initials)))

        if len(fns) == 0:
            return None

        fn = fns[-1]

        data = pd.read_table(fn, index_col=0)
        print(data)

        return data.iloc[0].to_dict()

    
    def get_default_parameters(self):

        x_offset_left_eye = self.config.get('stimuli', 'x_offset_left_eye')
        y_offset_left_eye = self.config.get('stimuli', 'y_offset_left_eye')

        x_offset_right_eye = self.config.get('stimuli', 'x_offset_right_eye')
        y_offset_right_eye = self.config.get('stimuli', 'y_offset_right_eye')

        screen_size_deg = self.pix2deg(self.screen.size)

        left_x = -screen_size_deg[0] / 4 - x_offset_left_eye
        left_y = y_offset_left_eye

        right_x = screen_size_deg[0] / 4 + x_offset_right_eye
        right_y = y_offset_right_eye

        left_size = self.config.get('stimuli', 'left_size')
        right_size = self.config.get('stimuli', 'right_size')

        settings = {'left_x':left_x,
                    'left_y':left_y,
                    'left_size':left_size,
                    'left_ori':0,
                    'right_x':right_x,
                    'right_y':right_y,
                    'right_size':right_size,
                    'right_ori':0}

        return settings
