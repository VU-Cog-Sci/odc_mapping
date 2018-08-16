import numpy as np
import psychopy
from psychopy.visual import Line
from psychopy.tools.unittools import radians


class ImageBased(object):

    def __init__(self,
                 win,
                 size,
                 pos,
                 ori=0,
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

    def draw(self):
        self._stim.draw()

    def _get_array(self):
        pass

class Checkerboard(ImageBased):
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
                 ori=0):

        self.side_len = side_len
        self.inverted = inverted

        super(Checkerboard, self).__init__(win, size, pos, ori=ori)

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

    def draw(self):
        """Draw checkerboard object."""
        self._stim.draw()


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


