import numpy as np
import psychopy

class Checkerboard(object):
    """Create an instance of a `Checkerboard` object.
    Parameters
    ----------
    win : (psychopy.visual.Window) window in which to display stimulus
    side_len : (int) number of rings in radial checkerboard
    inverted : (bool) if true, invert black and white squares
    size : (numeric) size of checkerboard
    kwds : keyword arguments to psychopy.visual.ImageStim
    """

    def __init__(self, win, side_len=8, inverted=False, size=16, mask=None, **kwds):
        self.win = win
        self.side_len = side_len
        self.inverted = inverted
        self.size = size

        self._array, self._mask = self._get_array()

        print(self.size)

        self._stim = psychopy.visual.ImageStim(
            self.win,
            self._array,
            size=size,
            mask=self._mask,
        **kwds)

        print('board', self._array.shape)

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


class Rim(object):

    def __init__(self, win,
                 inner_radius,
                 outer_radius,
                 n_bars,
                 *args,
                 **kwargs):

        self.win = win
        
        self.inner_radius = inner_radius
        self.outer_radius = outer_radius
        self.n_bars = n_bars

        self._array, self._mask = self._get_array()
        
        self._stim = psychopy.visual.ImageStim(
            self.win,
            self._array,
            size=self._array.shape,
            mask=self._mask,
            contrast=0.5,
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

    def draw(self):
        """Draw Rim object."""
        self._stim.draw()
