import numpy as np
import psychopy
from psychopy.visual import Line, GratingStim, TextStim
from psychopy.tools.unittools import radians


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

    def draw(self):
        if not self.hide:
            self._stim.draw()

    def _get_array(self):
        pass

    @property
    def contrast(self):
        return self._stim.contrast

    @contrast.setter
    def contrast(self, value):
        self._stim.contrast = value

    @property
    def ori(self):
        return self._stim.ori

    @contrast.setter
    def ori(self, value):
        self._stim.ori = value


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
                 cyclesperdegree=1,
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
            if mask == 'circle':
                x = np.linspace(-1, 1, board.shape[0])
                y = np.linspace(-1, 1, board.shape[1])

                xv, yv = np.meshgrid(x, y)
                mask = (xv**2 + yv**2 < 1).astype(float) * 2 - 1

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
        mask = (xv**2 + yv**2 < self.ratio_inner_circle)

        board[mask] = -1

        board = board if not self.inverted else board * -1

        return board, cross

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
                 hide=False):

        self.screen = win
        self.config = session.config
        self.session = session

        self.size = self.session.deg2pix(size)
        self.pos = [self.session.deg2pix(pos[0]), self.session.deg2pix(pos[1])]

        self.ori = ori

        self.hide = hide

        self.checkerboard = CheckerBoard(self.screen,
                                         size=self.size /
                                              self.config.get('checker_cross', 
                                                         'ratio_to_circle'),
                                         pos=self.pos,
                                         ori=ori)


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
                                              pos,
                                              size,
                                              session,
                                              ori,
                                              hide)

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
