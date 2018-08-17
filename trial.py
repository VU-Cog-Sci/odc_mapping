from exptools.core import Trial, MRITrial
from psychopy import event, visual
import itertools
import numpy as np
from stimuli import StimulusSet, StimulusSetToPosition


class StimulationTrial(MRITrial):

    def __init__(self, 
                 ID=None,
                 session=None,
                 parameters={},
                 *args, 
                 **kwargs):
        
        phase_durations = [1e6,
                           session.config.get('timing',
                                              'trial_length')]

        super(
            StimulationTrial,
            self).__init__(ID=ID,
                           phase_durations=phase_durations,
                           session=session,
                           parameters=parameters,
                           *args,
                           **kwargs)

        self.setup_stimuli()

        self.flicker_frequency = self.parameters['flicker_frequency']

        self.frame = 0
        self.flicker_length_in_frames = int(self.session.framerate / self.flicker_frequency)
        self.rotation_per_frame = 360 * self.parameters['rotations_per_second'] / self.session.framerate

        self.left_stimulus.checkerboard.contrast = 1
        self.right_stimulus.checkerboard.contrast = 1

    def draw(self):

        #if self.phase == 0:
            #for textstim in self.wait_stims:
                #textstim.draw()

        #else:
        if self.frame % self.flicker_length_in_frames == 0:
            self.left_stimulus.checkerboard.contrast *= -1
            self.right_stimulus.checkerboard.contrast *= -1


        self.left_stimulus.draw()
        self.right_stimulus.draw()

        self.frame += 1

        self.left_stimulus.checkerboard._stim.ori = self.left_stimulus.checkerboard._stim.ori + \
                                              self.rotation_per_frame

        self.right_stimulus.checkerboard._stim.ori = self.right_stimulus.checkerboard._stim.ori + \
                                              self.rotation_per_frame

        super(StimulationTrial, self).draw()

    def setup_stimuli(self):
        """setup_stimuli creates all stimuli that do not change from trial to trial"""



        self.left_stimulus = StimulusSet(self.screen,
                                         [self.parameters['left_x'],
                                          self.parameters['left_y']],
                                         self.parameters['left_size'],
                                         self.session,
                                         ori=self.parameters['left_ori'])

        self.right_stimulus = StimulusSet(self.screen,
                                         [self.parameters['right_x'],
                                          self.parameters['right_y']],
                                         self.parameters['right_size'],
                                         self.session,
                                         ori=self.parameters['right_ori'])

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

        super(StimulationTrial, self).event()

class PositioningTrial(Trial):

    def __init__(self, parameters, *args, **kwargs):

        phase_durations = [100000]
                           
        super(
            PositioningTrial,
            self).__init__(parameters=parameters,
                           ID='position',
                           phase_durations=phase_durations,
                           *args,
                           **kwargs)

        self.setup_stimuli()

        self.possible_modes = list(itertools.product(['left', 'right'],
                                                     ['size', 'x', 'y', 'ori']))

        self.set_mode()

        pix2deg = self.session.pix2deg

        left_stimulus = self.left_stimulus
        right_stimulus = self.right_stimulus
        

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

