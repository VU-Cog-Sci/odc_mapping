from exptools.core import Trial
from psychopy import event, visual
import itertools
import numpy as np
from stimuli import StimulusSet, StimulusSetToPosition


class StimulationTrial(Trial):

    def __init__(self, 
                 ID=None,
                 flicker_frequency=8,
                 eyes='both',
                 session=None,
                 settings=None,
                 *args, 
                 **kwargs):
        
        phase_durations = [session.config.get('timing',
                                              'stimulus_length')]

        super(
            StimulationTrial,
            self).__init__(ID=ID,
                           phase_durations=phase_durations,
                           session=session,
                           *args,
                           **kwargs)

        self.setup_stimuli(settings)

        self.flicker_frequency = flicker_frequency
        self.eye = eyes
        self.frame = 0
        self.flicker_length_in_frames = int(self.session.framerate / flicker_frequency)

        self.session.left_stimulus.checkerboard.contrast = 1
        self.session.right_stimulus.checkerboard.contrast = 1

        if eyes == 'both':
            self.session.left_stimulus.checkerboard.hide = False
            self.session.right_stimulus.checkerboard.hide = False
        elif eyes == 'left':
            self.session.left_stimulus.checkerboard.hide = False
            self.session.right_stimulus.checkerboard.hide = True
        elif eyes == 'right':
            self.session.left_stimulus.checkerboard.hide = True
            self.session.right_stimulus.checkerboard.hide = False


    def draw(self):

        if self.frame % self.flicker_length_in_frames == 0:
            self.session.left_stimulus.checkerboard.contrast *= -1
            self.session.right_stimulus.checkerboard.contrast *= -1

        self.session.left_stimulus.draw()
        self.session.right_stimulus.draw()

        print(self.session.left_stimulus.checkerboard.contrast)

        self.frame += 1

        super(StimulationTrial, self).draw()

    def setup_stimuli(self, settings):
        """setup_stimuli creates all stimuli that do not change from trial to trial"""


        self.left_stimulus = StimulusSet(self.screen,
                                         [settings['left_x'],
                                          settings['left_y']],
                                         settings['left_size'],
                                         self.session,
                                         ori=settings['left_ori'])

        self.right_stimulus = StimulusSet(self.screen,
                                         [settings['right_x'],
                                          settings['right_y']],
                                         settings['right_size'],
                                         self.session,
                                         ori=settings['right_ori'])

class PositioningTrial(Trial):

    def __init__(self, settings, *args, **kwargs):

        phase_durations = [100000]
                           
        super(
            PositioningTrial,
            self).__init__(ID='position',
                           phase_durations=phase_durations,
                           *args,
                           **kwargs)

        self.setup_stimuli(settings)

        self.possible_modes = list(itertools.product(['left', 'right'],
                                                     ['size', 'x', 'y', 'ori']))

        self.set_mode()

        pix2deg = self.session.pix2deg

        left_stimulus = self.session.left_stimulus
        right_stimulus = self.session.right_stimulus

        self.parameters.update({'left_size':pix2deg(left_stimulus.size),
                               'left_x':pix2deg(left_stimulus.pos[0]),
                               'left_y':pix2deg(left_stimulus.pos[1]),
                               'left_ori':left_stimulus.ori,
                               'right_size':pix2deg(right_stimulus.size),
                               'right_x':pix2deg(right_stimulus.pos[0]),
                               'right_y':pix2deg(right_stimulus.pos[1]),
                               'right_ori':right_stimulus.ori})

        
        

    def draw(self):
        text = '{} {}\n{:.3f}'.format(self.attribute, 
                                      self.selected_stimulus,
                                      self.parameters[self.current_key])

        self.session.left_stimulus.set_text(text)
        self.session.right_stimulus.set_text(text)

        self.session.left_stimulus.draw()
        self.session.right_stimulus.draw()

        super(PositioningTrial, self).draw()



    def event(self):
        for ev in event.getKeys():
            if ev in ['esc', 'escape', 'q']:
                self.events.append(
                    [-99, self.session.clock.getTime() - self.start_time])

                self.stopped = True
                self.session.stopped = True
                print 'run canceled by user'

            elif ev == self.session.config.get('buttons', 'keys')[3]:
                if self.session.left_stimulus.hide:
                    self.session.right_stimulus.hide = True
                    self.session.left_stimulus.hide = False

                    self.possible_modes = list(itertools.product(['left'],
                                                         ['size', 'x', 'y', 'ori']))
                    self.set_mode(attribute=self.attribute)

                elif self.session.right_stimulus.hide:
                    self.session.right_stimulus.hide = False

                    self.possible_modes = list(itertools.product(['left', 'right'],
                                                         ['size', 'x', 'y', 'ori']))
                    self.set_mode(attribute=self.attribute,
                                  selected_stimulus='right')

                else:
                    self.session.left_stimulus.hide = True

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
                    self.session.left_stimulus = StimulusSetToPosition(self.screen,
                                                     [self.parameters['left_x'],
                                                      self.parameters['left_y']],
                                                     self.parameters['left_size'],
                                                     self.session,
                                                     ori=self.parameters['left_ori'],
                                                     hide=self.session.left_stimulus.hide)

                else:
                    self.session.right_stimulus = StimulusSetToPosition(self.screen,
                                                         [self.parameters['right_x'],
                                                          self.parameters['right_y']],
                                                         self.parameters['right_size'],
                                                         self.session,
                                                         ori=self.parameters['right_ori'],
                                                         hide=self.session.right_stimulus.hide)


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

    def setup_stimuli(self, settings):
        """setup_stimuli creates all stimuli that do not change from trial to trial"""


        self.session.left_stimulus = StimulusSetToPosition(self.screen,
                                         [settings['left_x'],
                                          settings['left_y']],
                                         settings['left_size'],
                                         self.session,
                                         ori=settings['left_ori'])

        self.session.right_stimulus = StimulusSetToPosition(self.screen,
                                         [settings['right_x'],
                                          settings['right_y']],
                                         settings['right_size'],
                                         self.session,
                                         ori=settings['right_ori'])
