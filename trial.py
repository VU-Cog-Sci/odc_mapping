from exptools.core import Trial
from psychopy import event, visual
import itertools
from stimuli import StimulusSet

class PositioningTrial(Trial):

    def __init__(self,  *args, **kwargs):

        phase_durations = [100000]
                           
        super(
            PositioningTrial,
            self).__init__(ID='position',
            phase_durations=phase_durations,
            *args,
            **kwargs)


        self.text_stimulus = visual.TextStim(self.screen,
                                             'size left',
                                             #pos=[0, -self.screen.size[1] / 10 * 4],
                                             pos=[0, 0],
                                             color='red',
                                             )


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
        self.session.left_stimulus.checkerboard.contrast = 0
        self.session.right_stimulus.checkerboard.contrast = 0

        self.session.left_stimulus.draw()
        self.session.right_stimulus.draw()

        self.text_stimulus.text = '{} {}\n{:.3f}'.format(self.attribute, 
                                                     self.selected_stimulus,
                                                     self.parameters[self.current_key])
        self.text_stimulus.draw()

        super(PositioningTrial, self).draw()



    def event(self):
        for ev in event.getKeys():
            if ev in ['esc', 'escape', 'q']:
                self.events.append(
                    [-99, self.session.clock.getTime() - self.start_time])

                self.stopped = True
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
                    self.session.left_stimulus = StimulusSet(self.screen, 
                                                     [self.parameters['left_x'],
                                                      self.parameters['left_y']],
                                                     self.parameters['left_size'],
                                                     self.session,
                                                     ori=self.parameters['left_ori'],
                                                     hide=self.session.left_stimulus.hide)

                else:
                    self.session.right_stimulus = StimulusSet(self.screen, 
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


