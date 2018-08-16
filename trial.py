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
                                             pos=[0, -self.screen.size[1] / 10 * 4],
                                             #pos=[0, 0],
                                             color='white',
                                             )

        self.left_stimulus = self.session.left_stimulus
        self.right_stimulus = self.session.right_stimulus

        self.selected_stimulus = 'left'
        self.mode = 'size'
        self.current_key = 'left_size'

        self.possible_modes = list(itertools.product(['left', 'right'],
                                                     ['size', 'x', 'y', 'ori']))
        self.mode_ix = 0

        self.parameters.update({'left_size':self.left_stimulus.size,
                               'left_x':self.left_stimulus.pos[0],
                               'left_y':self.left_stimulus.pos[1],
                               'left_ori':self.left_stimulus.ori,
                               'right_size':self.right_stimulus.size,
                               'right_x':self.right_stimulus.pos[0],
                               'right_y':self.right_stimulus.pos[1],
                               'right_ori':self.right_stimulus.ori})
        

    def draw(self):
        self.session.left_stimulus.draw()
        self.session.right_stimulus.draw()

        self.text_stimulus.text = '{} {}\n{}'.format(self.mode, 
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
                self.session.stopped = True
                print 'run canceled by user'

            elif ev == self.session.config.get('buttons', 'keys')[3]:
                if self.left_stimulus.hide:
                    self.right_stimulus.hide = True
                    self.left_stimulus.hide = False
                elif self.right_stimulus.hide:
                    self.right_stimulus.hide = False
                else:
                    self.left_stimulus.hide = True

            elif ev ==  self.session.config.get('buttons', 'keys')[2]:
                self.mode_ix = (self.mode_ix + 1) % (len(self.possible_modes))
                self.selected_stimulus = self.possible_modes[self.mode_ix][0]
                self.mode = self.possible_modes[self.mode_ix][1]
                self.current_key = '{}_{}'.format(self.selected_stimulus,
                                                  self.mode)

            elif ev in self.session.config.get('buttons', 'keys')[:2]:
                
                if ev == self.session.config.get('buttons', 'keys')[0]:
                    self.parameters[self.current_key] -= 1
                else:
                    self.parameters[self.current_key] += 1

                
                if self.selected_stimulus == 'left':
                    self.session.left_stimulus = StimulusSet(self.screen, 
                                                     [self.parameters['left_x'],
                                                      self.parameters['left_y']],
                                                     self.parameters['left_size'],
                                                     self.session,
                                                     ori=self.parameters['left_ori'])

                else:
                    self.session.right_stimulus = StimulusSet(self.screen, 
                                                     [self.parameters['right_x'],
                                                      self.parameters['right_y']],
                                                     self.parameters['right_size'],
                                                     self.session,
                                                     ori=self.parameters['right_ori'])
