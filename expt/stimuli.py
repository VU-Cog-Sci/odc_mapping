import numpy as np
import psychopy
from psychopy.visual import Line, GratingStim, TextStim, RadialStim, ElementArrayStim
from psychopy.visual.filters import makeMask
from psychopy.tools.unittools import radians
from psychopy.tools.attributetools import setAttribute, attributeSetter

class ImageBased(object):

    def __init__(self,
                 win,
                 size,
                 pos,
                 ori=0,
                 contrast=1,
                 hide=False,
                 *args,
                 **kwargs):

        self.win = win
        self.size = size

        self._array, self._mask = self._get_array()

        self._stim = psychopy.visual.ImageStim(
            self.win,
            self._array,
            size=size,
            pos=pos,
            mask=self._mask,
            ori=ori,
            *args,
            **kwargs)

        self.contrast = contrast

        self.hide = hide
        self.autoLog = False

    def draw(self):
        if not self.hide:
            self._stim.draw()

    def _get_array(self):
        pass

    @attributeSetter
    def opacity(self, opacity):
        self._stim.opacity = opacity

    @property
    def contrast(self):
        return self._stim.contrast

    @contrast.setter
    def contrast(self, value):
        self._stim.contrast = value

    @property
    def ori(self):
        return self._stim.ori

    @ori.setter
    def ori(self, value):
        self._stim.ori = value

    def setOri(self, value):
        self.ori = value

class CheckerBoard(ImageBased):
    """Create an instance of a `Checkerboard` object.
    Parameters
    ----------
    win : (psychopy.visual.Window) window in which to display stimulus
    side_len : (int) number of rings in radial checkerboard
    inverted : (bool) if true, invert black and white squares
    size : (numeric) size of checkerboard
    kwds : keyword arguments to psychopy.visual.ImageStim
    """

    def __init__(self,
                 win,
                 pos,
                 side_len=8,
                 inverted=False,
                 size=16,
                 mask=None,
                 ori=0,
                 *args,
                 **kwargs):

        self.side_len = side_len
        self.inverted = inverted

        super(CheckerBoard, self).__init__(win, size, pos, ori=ori, *args, **kwargs)

    def _get_array(self, mask='circle', upscale=None):
        """Return square `np.ndarray` of alternating ones and negative ones
        with shape `(self.side_len, self.side_len)`."""
        board = np.ones((self.side_len, self.side_len), dtype=np.int32)
        board[::2, ::2] = -1
        board[1::2, 1::2] = -1

        if upscale is None:
            upscale = np.ceil(self.size / self.side_len)

        if upscale != 1:
            board = np.repeat(np.repeat(board, upscale, axis=0),
                              upscale, axis=1)

        if mask is not None:
            mask = makeMask(board.shape[0],
                            'raisedCosine')


        board = board if not self.inverted else board * -1

        return board, mask


class Rim(ImageBased):

    def __init__(self, win,
                 inner_radius,
                 outer_radius,
                 n_bars,
                 pos,
                 *args,
                 **kwargs):

        self.inner_radius = inner_radius
        self.outer_radius = outer_radius
        self.n_bars = n_bars

        super(Rim, self).__init__(win, 
                                  size=outer_radius*2+1,
                                  pos=pos,
                                  *args,
                                  **kwargs)

    def _get_array(self):
        x = np.linspace(-self.outer_radius,
                        self.outer_radius,
                        int(2*self.outer_radius+1))

        y = np.linspace(-self.outer_radius,
                        self.outer_radius,
                        int(2*self.outer_radius+1))

        xv, yv = np.meshgrid(x, y)
        
        rim = np.round(np.arctan2(xv, yv) / np.pi * self.n_bars/2) % 2 * 2 - 1


        rad = xv**2+yv**2
        mask = (rad > self.inner_radius**2) & (rad < self.outer_radius**2)
        mask = mask.astype(float)

        mask = mask * 2 - 1

        return rim, mask

class Cross(object):

    def __init__(self,
                 win,
                 width, 
                 pos=[0,0],
                 ori=0,
                 height=None, 
                 lineWidth=1,
                 *args,
                 **kwargs):

        if height is None:
            height = width
        
        #if ori != 0:
            #raise NotImplementedError()

        ori = radians(ori)

        pos1 = np.array([-np.cos(ori)*width/2, np.sin(ori)*height/2])
        pos1 += pos
        pos2 = np.array([np.cos(ori)*width/2, -np.sin(ori)*height/2])
        pos2 += pos

        pos3 = np.array([np.sin(ori)*width/2, np.cos(ori)*height/2])
        pos3 += pos
        pos4 = np.array([-np.sin(ori)*width/2, -np.cos(ori)*height/2])
        pos4 += pos

        self.line1 = Line(win,
                          start=pos1,
                          end=pos2,
                          lineWidth=lineWidth,
                          *args,
                          **kwargs)

        self.line2 = Line(win,
                          start=pos3,
                          end=pos4,
                          lineWidth=lineWidth,
                          *args,
                          **kwargs)

    def draw(self):
        self.line1.draw()
        self.line2.draw()


class CheckerBoardCross(ImageBased):

    def __init__(self,
                 win,
                 size,
                 pos=[0,0],
                 ori=0,
                 side_len=16,
                 n_blocks=2,
                 inverted=False,
                 ratio_inner_circle=1.5,
                 height=None):
       
        if (side_len % 2 == 0) & (n_blocks % 2 == 1):
            raise ValueError('side_len should be even!')

        if (side_len % 2 == 1) & (n_blocks % 2 == 0):
            raise ValueError('side_len should be uneven!')
        
        self.side_len = side_len
        self.n_blocks = n_blocks
        self.inverted = inverted

        self.ratio_inner_circle = ratio_inner_circle
        
        super(CheckerBoardCross, self).__init__(win,
                                                size,
                                                pos,
                                                ori)
        

    def _get_array(self, upscale=None):
        """Return square `np.ndarray` of alternating ones and negative ones
        with shape `(self.side_len, self.side_len)`."""
        board = np.ones((self.side_len, self.side_len), dtype=np.int32)
        board[::2, ::2] = -1
        board[1::2, 1::2] = -1

        cross = np.ones((self.side_len, self.side_len)) * -1

        low_ix = self.side_len / 2 - self.n_blocks / 2
        high_ix = low_ix + self.n_blocks

        cross[low_ix:high_ix, :] = 1
        cross[:, low_ix:high_ix] = 1

        if upscale is None:
            upscale = np.ceil(self.size / self.side_len)

        if upscale != 1:
            board = np.repeat(np.repeat(board, upscale, axis=0),
                              upscale, axis=1)
            cross = np.repeat(np.repeat(cross, upscale, axis=0),
                              upscale, axis=1)

        x = np.linspace(-1, 1, board.shape[0])
        y = np.linspace(-1, 1, board.shape[1])

        xv, yv = np.meshgrid(x, y)
        mask = (xv**2 + yv**2 > self.ratio_inner_circle)

        board[cross == -1] = -1
        board = board if not self.inverted else board * -1

        mask = mask * 2 - 1

        return board, mask

class FixationPoint(object):

    def __init__(self,
                 win,
                 pos,
                 size,
                 color=(1,0,0)):

        self.screen = win

        self.fixation_stim1 = GratingStim(win,
                                          sf=0,
                                          color=[1, 1, 1],
                                          mask='circle',
                                          pos=pos,
                                          size=size)

        self.fixation_stim2 = GratingStim(win,
                                          sf=0,
                                          color=[-1, -1, -1],
                                          mask='circle',
                                          pos=pos,
                                          size=0.66*size)



        self.fixation_stim3 = GratingStim(win,
                                          sf=0,
                                          color=color,
                                          mask='circle',
                                          pos=pos,
                                          size=0.33*size)
    def draw(self):
        self.fixation_stim1.draw()
        self.fixation_stim2.draw()
        self.fixation_stim3.draw()

class StimulusSet(object):


    def __init__(self,
                 win,
                 pos,
                 size,
                 session,
                 ori=0,
                 side_len=12,
                 checkerboard_type='square',
                 hide=False):

        self.screen = win
        self.config = session.config
        self.session = session

        self.size = self.session.deg2pix(size)
        self.pos = [self.session.deg2pix(pos[0]), self.session.deg2pix(pos[1])]

        self.ori = ori

        self.hide = hide

        checkerboard_size = self.size / self.config.get('checker_cross', 'ratio_to_circle')


        if checkerboard_type == 'square':
            self.checkerboard = CheckerBoard(self.screen,
                                             size=checkerboard_size,
                                             side_len=side_len,
                                             pos=self.pos,
                                             ori=ori)
        elif checkerboard_type == 'radial':
            mask = makeMask(checkerboard_size,
                            'raisedCosine',
                            range=(0,1))

            mask = mask[int(checkerboard_size/2), int(checkerboard_size/2):]
            self.checkerboard = RadialStim(self.screen,
                                           mask=mask,
                                           pos=self.pos,
                                           size=checkerboard_size,
                                           angularCycles=side_len,
                                           radialCycles=side_len /4)

        elif checkerboard_type == 'none':
            self.checkerboard = GratingStim(self.screen,
                                          opacity=0)

        else:
            ValueError('{} is not a valid checkerboard type'.format(checkerboard_type))


        rim_radius = self.size / 2 / self.config.get('checker_cross',
                                                     'ratio_to_circle') - 1

        self.rim = Rim(self.screen,
                       rim_radius,
                       rim_radius * self.config.get('rim', 'rim_ratio'),
                       self.config.get('rim', 'n_parts'),
                       pos=self.pos,
                       contrast=self.config.get('rim', 'contrast'),
                       ori=ori)

        ratio_inner_circle = 1 / self.config.get('checker_cross', 'ratio_to_circle') /\
                             self.config.get('rim', 'rim_ratio') 

        self.check_cross = CheckerBoardCross(self.screen,
                                             self.size,
                                             side_len=32,
                                             n_blocks=4,
                                             pos=self.pos,
                                             ratio_inner_circle=ratio_inner_circle,
                                             ori=ori)

        fixation_size = self.config.get('fixation', 'proportion') * self.size

        self.fixation = FixationPoint(self.screen,
                                      self.pos,
                                      fixation_size)

    def draw(self):
        if not self.hide:
            self.check_cross.draw()
            self.checkerboard.draw()
            self.rim.draw()
            self.fixation.draw()

class StimulusSetToPosition(StimulusSet):

    def __init__(self,
                 win,
                 pos,
                 size,
                 session,
                 ori=0,
                 hide=False,
                 text=''):

        super(StimulusSetToPosition, self).__init__(win,
                                              pos=pos,
                                              size=size,
                                              session=session,
                                              ori=ori,
                                              hide=hide)

        lw = self.session.deg2pix(self.config.get('cross', 'linewidth'))

        self.cross = Cross(self.screen,
                           self.size,
                           pos=self.pos,
                           lineColor=self.config.get('cross', 'color'),
                           lineWidth=lw,
                           ori=ori,
                           )

        self.text_stimulus = TextStim(self.screen,
                                      'size left',
                                      pos=[self.pos[0],
                                           self.pos[1] + 0.1 * self.size],
                                      height=self.size*0.05,
                                      ori=self.ori,
                                      color='green')

        self.checkerboard.contrast = 0


    def draw(self):
        super(StimulusSetToPosition, self).draw()
        if not self.hide:
            self.cross.draw()
            self.text_stimulus.draw()

    def set_text(self, text):
        self.text_stimulus.text = text

class PRFStim(object):
    def __init__(self,
                 screen,
                 pos,
                 size,
                 session,
                 orientation,
                 parameters,
                 aperture='circle'):

        self.session = session
        self.screen = screen

        self.aperture = aperture

        self.size_pix = self.session.deg2pix(size)
        self.pos = [self.session.deg2pix(pos[0]), self.session.deg2pix(pos[1])]

        self.orientation = radians(orientation)    # convert to radians immediately, and use to calculate rotation matrix
        self.rotation_matrix = np.array([[np.cos(self.orientation), -np.sin(self.orientation)],
                                          [np.sin(self.orientation), np.cos(self.orientation)]])

        self.parameters = parameters

        self.RG_color = self.parameters['RG_color']
        self.BY_color = self.parameters['BY_color']

        self.fast_speed = self.parameters['fast_speed']
        self.slow_speed = self.parameters['slow_speed']
        
        self.bar_width = self.parameters['bar_width_ratio'] * self.size_pix
        self.bar_length = self.size_pix

        self.num_elements = self.parameters['num_elements']
        
        self.bar_pass_duration = self.parameters['bar_pass_duration']

        self.full_width = self.size_pix + self.bar_width + self.parameters['element_size']
        self.midpoint = np.array(self.pos)

        # this is for determining ecc, which we make dependent on largest screen dimension

        self.phase = 0
        # bookkeeping variables
        self.eccentricity_bin = -1
        self.redraws = 0
        self.frames = 0

        # psychopy stimuli
        self.populate_stimulus()

        # create the stimulus
        self.element_array = ElementArrayStim(screen,
                                              nElements=self.parameters['num_elements'],
                                              sizes=self.element_sizes,
                                              sfs=self.element_sfs,
                                              xys=self.element_positions,
                                              colors=self.colors,
                                              colorSpace='rgb')


    def convert_sample(self,in_sample):
        return 1 - (1/(np.e**in_sample+1))
    
    def populate_stimulus(self):

        RG_ratio = 0.5
        BY_ratio = 0.5
        fast_ratio = 0.5
        slow_ratio = 0.5

        # set the default colors
        self.colors = np.ones((self.num_elements,3)) * 0.5
        self.fix_gray_value = self.session.background_color

        # and change them if a pulse is wanted

        # Now set the actual stimulus parameters
        self.colors = np.concatenate((np.ones((int(np.round(self.num_elements*RG_ratio/2.0)),3)) * np.array([1,-1,0]) * self.RG_color,  # red/green - red
                                    np.ones((int(np.round(self.num_elements*RG_ratio/2.0)),3)) * np.array([-1,1,0]) * self.RG_color,  # red/green - green
                                    np.ones((int(np.round(self.num_elements*BY_ratio/2.0)),3)) * np.array([-1,-1,1]) * self.BY_color,  # blue/yellow - blue
                                    np.ones((int(np.round(self.num_elements*BY_ratio/2.0)),3)) * np.array([1,1,-1]) * self.BY_color))  # blue/yellow - yellow

    
        np.random.shuffle(self.colors)

        # but do update all other stim parameters (regardless of pulse)
        self.element_speeds = np.concatenate((np.ones(int(np.round(self.num_elements*fast_ratio))) * self.parameters['fast_speed'],
                                            np.ones(int(np.round(self.num_elements*slow_ratio))) * self.parameters['slow_speed']))
        np.random.shuffle(self.element_speeds)

        self.element_positions = np.random.rand(self.num_elements, 2) * \
            np.array([self.bar_length, self.bar_width]) - \
            np.array([self.bar_length/2.0, self.bar_width/2.0])

        # self.element_sfs = np.ones((self.num_elements)) * self.session.element_spatial_frequency']
        self.element_sfs = np.random.rand(self.num_elements) * self.session.deg2pix(self.parameters['element_spatial_frequency'])
        self.element_sizes = np.ones(self.num_elements) * self.session.deg2pix(self.parameters['element_size'])
        self.element_phases = np.zeros(self.num_elements)
        self.element_orientations = np.random.rand(self.num_elements) * 720.0 - 360.0

        self.lifetimes = np.random.rand(self.num_elements) * self.parameters['element_lifetime']

    def draw(self, phase=0):

        self.phase = phase
        self.frames += 1

        to_be_redrawn = self.lifetimes < phase
        self.element_positions[to_be_redrawn] = np.random.rand(to_be_redrawn.sum(), 2) \
            * np.array([self.bar_length, self.bar_width]) \
            - np.array([self.bar_length/2.0, self.bar_width/2.0])

        self.lifetimes[to_be_redrawn] += np.random.rand(to_be_redrawn.sum()) * self.parameters['element_lifetime']

        # define midpoint
        self.midpoint = phase * self.full_width - 0.5 * self.full_width

        self.element_array.setSfs(self.element_sfs)
        self.element_array.setSizes(self.element_sizes)
        self.element_array.setColors(self.colors)
        self.element_array.setOris(self.element_orientations)
        delta_pos = np.array([0, -self.midpoint]).dot(self.rotation_matrix)

        xys = self.element_positions.dot(self.rotation_matrix) + delta_pos
        self.element_array.setXYs(xys + self.pos)

        if self.aperture == 'circle':
            self.element_array.setOpacities(np.sqrt((xys**2).sum(1)) < self.full_width / 2)

        self.element_array.setPhases(self.element_speeds * self.phase * self.bar_pass_duration + self.element_phases)

        if self.parameters['stim_bool']:
            self.element_array.draw()

class BinocularPRFStim(PRFStim):
    def __init__(self,
                 screen,
                 pos,
                 size,
                 session,
                 orientation,
                 parameters):

        super(BinocularPRFStim, self).__init__(screen,
                                               pos[0],
                                              size[0],
                                              session,
                                              orientation[0],
                                              parameters)

        self.pos2 = [self.session.deg2pix(pos[1][0]), self.session.deg2pix(pos[1][1])]
        self.size_pix2 = self.session.deg2pix(size[1])
        self.orientation2 = radians(orientation[1])

        self.rotation_matrix2 = np.array([[np.cos(self.orientation2), -np.sin(self.orientation2)],
                                         [np.sin(self.orientation2), np.cos(self.orientation2)]])


        self.scaling = self.size_pix2 / self.size_pix

        self.rotation_matrix2 = self.rotation_matrix2 * self.scaling


    def draw(self, phase=0):

        super(BinocularPRFStim, self).draw(phase=phase)

        self.element_array.setSfs(self.element_sfs * self.scaling)
        self.element_array.setSizes(self.element_sizes * self.scaling)
        self.element_array.setOris(self.element_orientations)

        delta_pos = np.array([0, -self.midpoint]).dot(self.rotation_matrix2)

        self.element_array.setXYs(self.element_positions.dot(self.rotation_matrix2) + delta_pos + self.pos2)
        self.element_array.setPhases(self.element_speeds * self.phase * self.bar_pass_duration + self.element_phases)

        if self.parameters['stim_bool']:
            self.element_array.draw()
