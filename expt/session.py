from exptools.core.session import MRISession
from stimuli import StimulusSet, StimulusSetToPosition
from trial import PositioningTrial, StimulationTrial, PRFTrial
import numpy as np
import glob
import pandas as pd
from copy import copy


class ODCSession(MRISession):

    def __init__(self, reset_positions=False, *args, **kwargs):
        super(ODCSession, self).__init__(*args, **kwargs)

        if not reset_positions:
            parameters = self.find_parameters_subject()

        if reset_positions or (parameters is None):
            parameters = self.get_default_parameters()

        self.framerate = self.config.get('screen', 'framerate')

        self.positioning_trial = PositioningTrial(session=self,
                                                  parameters=parameters)

    
    def get_default_parameters(self):
        return _get_default_parameters(self)

    def find_parameters_subject(self):
        return _find_parameters_subject(self)
        
    def run(self):
        """run the session"""

        self.positioning_trial.run()

        parameters = self.positioning_trial.parameters
        parameters['framerate'] = self.framerate
        parameters['flicker_frequency'] = self.config.get('task', 'flicker_frequency')
        parameters['rotations_per_second'] = self.config.get('task', 'rotations_per_second')
        parameters['min_direction_duration'] = self.config.get('task', 'min_direction_duration')
        parameters['scale_direction_duration'] = self.config.get('task', 'scale_direction_duration')
        parameters['intro_duration'] = self.config.get('task', 'intro_duration')
        parameters['outro_duration'] = self.config.get('task', 'outro_duration')
        parameters['monocular_durations'] = self.config.get('task', 'duration_per_eye')
        parameters['checkerboard_cycles_per_degree'] = self.config.get('stimuli', 'checkerboard_cycles_per_degree')
        parameters['checkerboard_type'] = self.config.get('stimuli', 'checkerboard_type')
        parameters['cross_circle_ratio'] = self.config.get('checker_cross', 'ratio_to_circle')

        self.flicker_trial = StimulationTrial(session=self,
                                              parameters=parameters)

        np.savetxt(self.output_file + '_colors.log',
                   self.flicker_trial.colors)

        np.savetxt(self.output_file + '_directions.log',
                   self.flicker_trial.directions)

        self.flicker_trial.run()

        self.stop()
        self.close()
    



class PRFSession(MRISession):

    def __init__(self, reset_positions=False, *args, **kwargs):
        super(PRFSession, self).__init__(*args, **kwargs)

        if not reset_positions:
            parameters = self.find_parameters_subject()

        if reset_positions or (parameters is None):
            parameters = self.get_default_parameters()

        parameters['min_direction_duration'] = self.config.get('task', 'min_direction_duration')
        parameters['scale_direction_duration'] = self.config.get('task', 'scale_direction_duration')
        parameters['stim_bool'] = True

        # Put PRF parameters in parameter dict
        for par in ['num_elements',
                    'fast_speed',
                    'slow_speed',
                    'element_size',
                    'element_spatial_frequency',
                    'color_ratio',
                    'element_lifetime',
                    'bar_width_ratio',]:
            parameters[par] = self.config.get('prf', par)

        parameters['RG_color'] = 1/parameters['color_ratio']
        parameters['BY_color'] = 1

        parameters['cross_circle_ratio'] = self.config.get('checker_cross', 'ratio_to_circle')
        parameters['rim_ratio'] = self.config.get('rim', 'rim_ratio')

        self.framerate = self.config.get('screen', 'framerate')

        #for trial_color
        self.positioning_trial = PositioningTrial(session=self,
                                                  parameters=parameters)


    def get_default_parameters(self):
        return _get_default_parameters(self)

    def find_parameters_subject(self):
        return _find_parameters_subject(self)
    
    def run(self):
        """run the session"""

        self.positioning_trial.run()

        parameters = self.positioning_trial.parameters
        parameters['framerate'] = self.framerate

        stim_booleans = self.config.get('prf', 'stim_present_booleans')
        stim_direction_indices = self.config.get('prf', 'stim_direction_indices')
        stim_durations = self.config.get('prf', 'stim_durations')

        self.trials = []
        for i, (stim_present, direction, duration) in enumerate(zip(stim_booleans,
                                                                    stim_direction_indices,
                                                                    stim_durations)):
           parameters['stim_bool'] = bool(stim_present)
           parameters['bar_pass_duration'] = duration
           phase_durations = [-1e-9, duration]

           if i == 0:
               phase_durations[0] = 1000

           direction = direction / 8. * 360.
           parameters['bar_direction'] = direction

           self.trials.append(PRFTrial(parameters=parameters,
                                phase_durations=phase_durations,
                                session=self))

        for ix, trial in enumerate(self.trials):
            if not self.stopped:
                trial.run(ix)

        self.stop()
        self.close()

    
def _get_default_parameters(session):

    x_offset_left_eye = session.config.get('stimuli', 'x_offset_left_eye')
    y_offset_left_eye = session.config.get('stimuli', 'y_offset_left_eye')

    x_offset_right_eye = session.config.get('stimuli', 'x_offset_right_eye')
    y_offset_right_eye = session.config.get('stimuli', 'y_offset_right_eye')

    screen_size_deg = session.pix2deg(session.screen.size)

    left_x = -screen_size_deg[0] / 4 - x_offset_left_eye
    left_y = y_offset_left_eye

    right_x = screen_size_deg[0] / 4 + x_offset_right_eye
    right_y = y_offset_right_eye

    left_size = session.config.get('stimuli', 'left_size')
    right_size = session.config.get('stimuli', 'right_size')

    settings = {'left_x':left_x,
                'left_y':left_y,
                'left_size':left_size,
                'left_ori':0,
                'right_x':right_x,
                'right_y':right_y,
                'right_size':right_size,
                'right_ori':0}

    return settings

def _find_parameters_subject(session):

    fns = sorted(glob.glob('data/{}*.tsv'.format(session.subject_initials)))

    if len(fns) == 0:
        return None

    fn = fns[-1]

    data = pd.read_table(fn, index_col=0)

    return data.iloc[0].to_dict()
