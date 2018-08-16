from exptools.core.session import MRISession
from stimuli import StimulusSet
from trial import PositioningTrial
import numpy as np

class ODCSession(MRISession):

    def __init__(self, *args, **kwargs):
        super(MRISession, self).__init__(*args, **kwargs)
        print(self.config.config_dict)

        self.setup_stimuli()

        self.positioning_trial = PositioningTrial(session=self)


    
    def setup_stimuli(self):
        """setup_stimuli creates all stimuli that do not change from trial to trial"""

        x_offset_left_eye = self.config.get('positions', 'x_offset_left_eye')
        y_offset_left_eye = self.config.get('positions', 'y_offset_left_eye')

        x_offset_right_eye = self.config.get('positions', 'x_offset_right_eye')
        y_offset_right_eye = self.config.get('positions', 'y_offset_right_eye')

        self.left_pos = [-self.screen.size[0]/4 + self.deg2pix(x_offset_left_eye), 
                        self.deg2pix(y_offset_left_eye)]

        self.right_pos = [self.screen.size[0]/4 + self.deg2pix(x_offset_right_eye), 
                        self.deg2pix(y_offset_right_eye)]

        self.left_size = self.deg2pix(self.config.get('positions',
                                                      'left_size'))

        self.right_size = self.deg2pix(self.config.get('positions',
                                                      'right_size'))

        self.left_stimulus = StimulusSet(self.screen, 
                                         self.left_pos,
                                         self.left_size,
                                         self)

        self.right_stimulus = StimulusSet(self.screen,
                                         self.right_pos,
                                         self.right_size,
                                         self)

    def run(self):
        """run the session"""

        self.positioning_trial.run()
        
