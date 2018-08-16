from exptools.core import Trial
from psychopy import event

class PositioningTrial(Trial):

    def __init__(self,  *args, **kwargs):

        phase_durations = [100000]
                           
        super(
            PositioningTrial,
            self).__init__(ID='position',
            phase_durations=phase_durations,
            *args,
            **kwargs)


    def draw(self):
        self.session.left_rim.draw()
        self.session.right_rim.draw()
        self.session.left_grating.draw()
        #self.session.right_grating.draw()

        self.session.left_cross.draw()
        self.session.right_cross.draw()

        super(PositioningTrial, self).draw()

    def event(self):
        for ev in event.getKeys():
            if ev in ['esc', 'escape', 'q']:
                self.events.append(
                    [-99, self.session.clock.getTime() - self.start_time])
                self.stopped = True
                self.session.stopped = True
                print 'run canceled by user'
