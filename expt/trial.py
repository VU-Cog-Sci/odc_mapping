from exptools.core import Trial, MRITrial
from psychopy import event, visual
import itertools
import numpy as np
from stimuli import StimulusSet, StimulusSetToPosition, PRFStim, BinocularPRFStim


class StimulationTrial(MRITrial):

    def __init__(self, 
                 session=None,
                 parameters={},
                 *args, 
                 **kwargs):
        

        self.trial_duration = np.sum(session.config.get('task', 'duration_per_eye')) * 2 +\
                              session.config.get('task', 'intro_duration') + \
                              session.config.get('task', 'outro_duration')

        phase_durations = [1e6,
                           self.trial_duration]

        super(
            StimulationTrial,
            self).__init__(phase_durations=phase_durations,
                           session=session,
                           parameters=parameters,
                           *args,
                           **kwargs)

        self.setup_stimuli()

        self.flicker_frequency = self.parameters['flicker_frequency']

        self.frame = 0
        self.flicker_length_in_frames = int(self.session.framerate / self.flicker_frequency / 2.)
        self.rotation_per_frame = 360 * self.parameters['rotations_per_second'] / self.session.framerate

        self.left_stimulus.checkerboard.contrast = 1
        self.right_stimulus.checkerboard.contrast = 1


        self.directions = self._get_frame_values(self.session.framerate,
                                         self.trial_duration,
                                         self.parameters['min_direction_duration'],
                                         self.parameters['scale_direction_duration'])

        self.colors = self._get_frame_values(self.session.framerate,
                                         self.trial_duration,
                                         self.parameters['min_direction_duration'],
                                         self.parameters['scale_direction_duration'],
                                         [0, 1]).astype(int)

        self.monocularity_array = self._get_monocularity_array(self.parameters['intro_duration'],
                                                               self.parameters['monocular_durations']).astype(int)

        self.fixation_colors = np.array([[1, -1, -1],
                                         [-1, 1, -1]])



    def draw(self):

        if self.phase == 0:
            for textstim in self.wait_stims:
                textstim.draw()

        else:

            if self.frame < int(self.session.framerate * self.parameters['intro_duration']):
                self.left_stimulus.checkerboard.contrast = 0
                self.right_stimulus.checkerboard.contrast = 0
            elif self.frame == int(self.session.framerate * self.parameters['intro_duration']):
                self.left_stimulus.checkerboard.contrast = 1
                self.right_stimulus.checkerboard.contrast = 1
            elif self.frame == int(self.session.framerate * (self.trial_duration -\
                                                             self.parameters['outro_duration'])):
                self.left_stimulus.checkerboard.contrast = 0
                self.right_stimulus.checkerboard.contrast = 0

            if self.frame % self.flicker_length_in_frames == 0:
                self.left_stimulus.checkerboard.contrast *= -1
                self.right_stimulus.checkerboard.contrast *= -1

            
            self.left_stimulus.draw()
            self.right_stimulus.draw()

            self.frame += 1

            if self.monocularity_array[self.frame] == -1:
                self.left_stimulus.checkerboard.opacity = 0
                self.right_stimulus.checkerboard.opacity = 1
            elif self.monocularity_array[self.frame] == 1:
                self.left_stimulus.checkerboard.opacity = 1
                self.right_stimulus.checkerboard.opacity = 0
            else:
                self.left_stimulus.checkerboard.opacity = 0
                self.right_stimulus.checkerboard.opacity = 0


            new_ori = self.left_stimulus.checkerboard.ori + self.rotation_per_frame * self.directions[self.frame]


            self.left_stimulus.checkerboard.setOri(new_ori)
            self.right_stimulus.checkerboard.setOri(new_ori)

            self.left_stimulus.fixation.fixation_stim3.color = self.fixation_colors[self.colors[self.frame]]
            self.right_stimulus.fixation.fixation_stim3.color = self.fixation_colors[self.colors[self.frame]]

        super(StimulationTrial, self).draw()

    def setup_stimuli(self):
        """setup_stimuli creates all stimuli that do not change from trial to trial"""

        side_len = int(self.parameters['checkerboard_cycles_per_degree'] * self.parameters['left_size'] * 2.)

        self.left_stimulus = StimulusSet(self.screen,
                                         [self.parameters['left_x'],
                                          self.parameters['left_y']],
                                          self.parameters['left_size'],
                                          self.session,
                                          side_len=side_len,
                                          ori=self.parameters['left_ori'],
                                          checkerboard_type=self.parameters['checkerboard_type'])

        self.right_stimulus = StimulusSet(self.screen,
                                         [self.parameters['right_x'],
                                          self.parameters['right_y']],
                                          self.parameters['right_size'],
                                          self.session,
                                          side_len=side_len,
                                          ori=self.parameters['right_ori'],
                                          checkerboard_type=self.parameters['checkerboard_type'])

        self.wait_stims = [visual.TextStim(self.screen,
                                           'Waiting for trigger',
                                           color='red',
                                           pos=pos)
                           for pos in [self.left_stimulus.pos, self.right_stimulus.pos]]

    def event(self):
        for ev in event.getKeys():
            if (self.phase == 0) and (ev == self.session.mri_trigger_key):
                self.phase_forward()

            if ev in ['esc', 'escape', 'q']:
                self.events.append(
                    [-99, self.session.clock.getTime() - self.start_time])

                self.stopped = True
                self.session.stopped = True
                print 'run canceled by user'

            super(StimulationTrial, self).key_event(ev)

        super(StimulationTrial, self).event()

    def _get_frame_values(self,
                          framerate,
                          trial_duration,
                          min_value,
                          exp_scale,
                          values=[-1, 1],
                          safety_margin=None):

        if safety_margin is None:
            safety_margin =  5

        n_values = len(values)

        total_duration = trial_duration + safety_margin
        total_n_frames = total_duration * framerate

        result = np.zeros(total_n_frames)

        n_samples = np.ceil(total_duration * 2 / (exp_scale + min_value)).astype(int)
        durations = np.random.exponential(exp_scale, n_samples) + min_value

        frame_times = np.linspace(0, total_duration, total_n_frames, endpoint=False)

        first_index = np.random.randint(n_values)

        result[frame_times < durations[0]] = values[first_index]

        for ix, c in enumerate(np.cumsum(durations)):
            result[frame_times > c] = values[(first_index + ix) % n_values]

        return result

    def _get_monocularity_array(self,
                                intro_duration,
                                durations,
                                safety_margin=None):


        if safety_margin is None:
            safety_margin = 5

        total_duration = self.trial_duration + safety_margin
        total_n_frames = total_duration * self.session.framerate

        result = np.zeros(total_n_frames)

        start_ix = self.session.framerate * intro_duration

        for d in durations:
            result[start_ix:start_ix+d*self.session.framerate] = -1
            result[start_ix+d*self.session.framerate:start_ix + d * 2 * self.session.framerate] = 1
            start_ix = start_ix + d * 2 * self.session.framerate

        return result


class PositioningTrial(Trial):

    def __init__(self, parameters, *args, **kwargs):

        phase_durations = [100000]
                           
        super(
            PositioningTrial,
            self).__init__(parameters=parameters,
                           phase_durations=phase_durations,
                           *args,
                           **kwargs)

        self.setup_stimuli()

        self.possible_modes = list(itertools.product(['left', 'right'],
                                                     ['size', 'x', 'y', 'ori']))

        self.set_mode()

        pix2deg = self.session.pix2deg
        

    def draw(self):
        text = '{} {}\n{:.3f}'.format(self.attribute, 
                                      self.selected_stimulus,
                                      self.parameters[self.current_key])

        self.left_stimulus.set_text(text)
        self.right_stimulus.set_text(text)

        self.left_stimulus.draw()
        self.right_stimulus.draw()

        super(PositioningTrial, self).draw()



    def event(self):
        for ev in event.getKeys():
            if ev in ['esc', 'escape', 'q']:
                self.events.append(
                    [-99, self.session.clock.getTime() - self.start_time])

                self.stopped = True
                self.session.stopped = True
                print 'run canceled by user'

            elif ev in ['space']:
                self.stopped = True

            elif ev == self.session.config.get('buttons', 'keys')[3]:
                if self.left_stimulus.hide:
                    self.right_stimulus.hide = True
                    self.left_stimulus.hide = False

                    self.possible_modes = list(itertools.product(['left'],
                                                         ['size', 'x', 'y', 'ori']))
                    self.set_mode(attribute=self.attribute)

                elif self.right_stimulus.hide:
                    self.right_stimulus.hide = False

                    self.possible_modes = list(itertools.product(['left', 'right'],
                                                         ['size', 'x', 'y', 'ori']))
                    self.set_mode(attribute=self.attribute,
                                  selected_stimulus='right')

                else:
                    self.left_stimulus.hide = True

                    self.possible_modes = list(itertools.product(['right'],
                                                         ['size', 'x', 'y', 'ori']))
                    self.set_mode(attribute=self.attribute)

            elif ev ==  self.session.config.get('buttons', 'keys')[2]:
                self.mode_ix = (self.mode_ix + 1) % (len(self.possible_modes))
                self.set_mode(self.mode_ix)

            elif ev in self.session.config.get('buttons', 'keys')[:2]:
                
                if ev == self.session.config.get('buttons', 'keys')[0]:
                    self.parameters[self.current_key] -= .15
                else:
                    self.parameters[self.current_key] += .15

                
                if self.selected_stimulus == 'left':
                    self.left_stimulus = StimulusSetToPosition(self.screen,
                                                     [self.parameters['left_x'],
                                                      self.parameters['left_y']],
                                                     self.parameters['left_size'],
                                                     self.session,
                                                     ori=self.parameters['left_ori'],
                                                     hide=self.left_stimulus.hide)

                else:
                    self.right_stimulus = StimulusSetToPosition(self.screen,
                                                         [self.parameters['right_x'],
                                                          self.parameters['right_y']],
                                                         self.parameters['right_size'],
                                                         self.session,
                                                         ori=self.parameters['right_ori'],
                                                         hide=self.right_stimulus.hide)



    def set_mode(self, 
                 ix=None, 
                 attribute=None,
                 selected_stimulus=None):
        

        if ix is None:
            if selected_stimulus is None:
                selected_stimulus = self.possible_modes[0][0]

            if attribute is None:
                ix = 0
            else:
                ix = self.possible_modes.index((selected_stimulus,
                                                attribute))

        self.mode_ix = ix

        self.selected_stimulus = self.possible_modes[ix][0]
        self.attribute = self.possible_modes[ix][1]
        self.current_key = '{}_{}'.format(self.selected_stimulus,
                                          self.attribute)

    def setup_stimuli(self):
        """setup_stimuli creates all stimuli that do not change from trial to trial"""

        self.left_stimulus = StimulusSetToPosition(self.screen,
                                         [self.parameters['left_x'],
                                          self.parameters['left_y']],
                                         self.parameters['left_size'],
                                         self.session,
                                         ori=self.parameters['left_ori'])

        self.right_stimulus = StimulusSetToPosition(self.screen,
                                         [self.parameters['right_x'],
                                          self.parameters['right_y']],
                                         self.parameters['right_size'],
                                         self.session,
                                         ori=self.parameters['right_ori'])

class PRFTrial(Trial):
    def __init__(self,
                 session,
                 parameters,
                 *args,
                 **kwargs):
        

        self.frame = 0
        phase_durations = [10]
        super(PRFTrial, self).__init__(session=session,
                                       parameters=parameters,
                                       phase_durations=phase_durations,
                                       *args,
                                       **kwargs)
        self.setup_stimuli()
       
    def setup_stimuli(self):
        """setup_stimuli creates all stimuli that do not change from trial to trial"""

        self.left_frame = StimulusSet(self.screen,
                                         [self.parameters['left_x'],
                                          self.parameters['left_y']],
                                         self.parameters['left_size'],
                                         self.session,
                                         ori=self.parameters['left_ori'],
                                       checkerboard_type='none')

        self.right_frame = StimulusSet(self.screen,
                                         [self.parameters['right_x'],
                                          self.parameters['right_y']],
                                         self.parameters['right_size'],
                                         self.session,
                                         ori=self.parameters['right_ori'],
                                         checkerboard_type='none')

        self.left_prf = BinocularPRFStim(self.screen,
                                         [[self.parameters['left_x'], self.parameters['left_y']],
                                          [self.parameters['right_x'], self.parameters['right_y']]],
                                          [self.parameters['left_size'] / self.parameters['cross_circle_ratio'],
                                          self.parameters['right_size'] / self.parameters['cross_circle_ratio']],
                                          self.session,
                                          [0.25*np.pi + self.parameters['left_ori'], 0.25*np.pi + self.parameters['right_ori']],
                                          self.parameters)

    def event(self):
        for ev in event.getKeys():
            if ev in ['esc', 'escape', 'q']:
                self.events.append(
                    [-99, self.session.clock.getTime() - self.start_time])

                self.stopped = True
                self.session.stopped = True

    def draw(self):
        self.left_prf.draw(phase=float(self.frame) / (self.phase_durations[0] * self.session.framerate))
        self.left_frame.draw()
        self.right_frame.draw()
        self.frame +=1

        super(PRFTrial, self).draw()
