from __future__ import division
from math import *
import numpy as np


class PRFModelTrial(object):
    """docstring for PRFModelTrial"""

    def __init__(self, orientation, n_elements, n_samples, sample_duration, bar_width=0.1, ecc_test=1.0):
        super(PRFModelTrial, self).__init__()
        self.orientation = orientation
        self.n_elements = n_elements
        self.n_samples = n_samples
        self.sample_duration = sample_duration
        self.bar_width = bar_width * 2.

        self.rotation_matrix = np.matrix(
            [[cos(self.orientation), -sin(self.orientation)], [sin(self.orientation), cos(self.orientation)]])

        x, y = np.meshgrid(np.linspace(-1, 1, self.n_elements, endpoint = True),
                           np.linspace(-1, 1, self.n_elements, endpoint = True))
        self.xy = np.matrix([x.ravel(), y.ravel()])
        self.rotated_xy = np.array(self.rotation_matrix * self.xy)

        if ecc_test == None:
            self.ecc_test = np.ones_like(x.ravel(), dtype=bool)
        else:
            self.ecc_test = np.sqrt((np.array(self.xy) ** 2).sum(axis=0)) <= ecc_test


    def in_bar(self, time=0):
        """in_bar, a method, not Ralph."""
        # a bar of self.bar_width width
        position = 2.0 * ((time * (1.0 + self.bar_width / 2.0)
                           ) - (0.5 + self.bar_width / 4.0))
        # position = 2.0 * ((time * (1.0 + self.bar_width)) - (0.5 + self.bar_width / 2.0))
        extent = [-self.bar_width / 2.0 + position,
                  self.bar_width / 2.0 + position]
        # rotating the xy matrix itself allows us to test only the x component
        return ((self.rotated_xy[0, :] >= extent[0]) * (self.rotated_xy[0, :] <= extent[1]) * self.ecc_test).reshape((self.n_elements, self.n_elements))
        # return ((self.rotated_xy[0,:] >= extent[0]) * (self.rotated_xy[0,:] <= extent[1])).reshape((self.n_elements, self.n_elements))

    def pass_through(self):
        """pass_through models a single pass-through of the bar, 
        with padding as in the padding list for start and end."""

        self.pass_matrix = np.array(
            [self.in_bar(i) for i in np.linspace(0.0, 1.0, self.n_samples, endpoint=True)])


def create_visual_designmatrix_all(
        bar_dur_in_TR=32,
        iti_duration=2,
        bar_width=0.1,
        n_pixels=100,
        thetas=[-1, 0, -1, 45, 270, -1,  315,
                180, -1,  135,   90, -1,  225, -1],
        nr_timepoints=462):
    ITIs = np.zeros((iti_duration, n_pixels, n_pixels))
    all_bars = []
    for x in thetas:
        all_bars.extend(ITIs)
        if x == -1:
            all_bars.extend(np.zeros((bar_dur_in_TR, n_pixels, n_pixels)))
        else:
            pmt = PRFModelTrial(orientation=-np.radians(x) - np.pi / 2.0, n_elements=n_pixels,
                                n_samples=bar_dur_in_TR + 1, sample_duration=1, bar_width=bar_width)
            pmt.pass_through()
            pmt.pass_matrix = pmt.pass_matrix[:-1]
            all_bars.extend(pmt.pass_matrix)

    # swap axes for popeye:
    visual_dm = np.transpose(np.array(all_bars), [1, 2, 0])
    visual_dm = np.round(visual_dm[:, :, :nr_timepoints]).astype(np.int16)

    return visual_dm


def create_bd_designmatrix_all(
        bar_dur_in_TR=32,
        iti_duration=2,
        bar_width=0.1,
        n_pixels=100,
        thetas=[-1, 0, -1, 45, 270, -1,  315,
                180, -1,  135,   90, -1,  225, -1],
        nr_timepoints=462,
        TR=0.945,
        dm_upscale_factor=10,
        window_length=1000,
        polyorder=2):

    import numpy as np
    from scipy.signal import fftconvolve
    from hrf_estimation.hrf import spmt, dspmt, ddspmt
    from scipy.signal import savgol_filter

    kernel = spmt(np.linspace(
        0, 35, dm_upscale_factor * 35 / TR, endpoint=False))

    visual_designmatrix = create_visual_designmatrix_all(
        bar_dur_in_TR=bar_dur_in_TR,
        iti_duration=iti_duration,
        bar_width=bar_width,
        n_pixels=n_pixels,
        thetas=thetas,
        nr_timepoints=nr_timepoints)
    # create the blockdesign design matrix
    blocks = np.sign(visual_designmatrix.sum(axis=0).sum(axis=0))
    raw_dm = np.repeat(blocks, dm_upscale_factor)

    # convolve, subsample and reshape
    cr = fftconvolve(raw_dm, kernel)[::dm_upscale_factor]
    conv_dm = cr[:nr_timepoints]
    conv_dm = conv_dm.reshape((-1, nr_timepoints))

    # normalize regressor amplitude
    conv_dm = (conv_dm.T / conv_dm.std(axis=-1)).T

    # Window must be odd
    if window_length % 2 == 0:
        window_length += 1
    conv_dm_filt = conv_dm - savgol_filter(conv_dm, window_length=window_length, polyorder=polyorder,
                                           deriv=0, axis=1, mode='nearest')
    # the resulting visual design matrix
    visual_dm = np.vstack((np.ones((1, nr_timepoints)), conv_dm, conv_dm_filt))

    return visual_dm


def create_visual_designmatrix_nprf(
        bar_dur_in_TR_hor=32, # 49 for nprf2 expt
        bar_dur_in_TR_vert=57, # 49 for nprf2 expt
        iti_duration=1,
        bar_width=0.1,
        n_pixels=192,
        thetas=[-1, 0, 90, -1,  270, 180, -1],
        nr_timepoints=290 # 351 for nprf2 expt
        ):

    from scipy.misc.pilutil import imresize

    all_bars_square = np.zeros((nr_timepoints, n_pixels, n_pixels))
    bar_pass_hor = PRFModelTrial(orientation=-np.radians(0) - np.pi / 2.0,
                             n_elements=n_pixels,
                             n_samples=bar_dur_in_TR_hor + 1,
                             sample_duration=1,
                             bar_width=bar_width,
                             ecc_test=None)
    bar_pass_hor.pass_through()
    bar_pass_hor.pass_matrix = bar_pass_hor.pass_matrix[:-1]

    bar_pass_vert = PRFModelTrial(orientation=-np.radians(0) - np.pi / 2.0,
                             n_elements=n_pixels,
                             n_samples=bar_dur_in_TR_vert + 1,
                             sample_duration=1,
                             bar_width=bar_width,
                             ecc_test=None)
    bar_pass_vert.pass_through()
    bar_pass_vert.pass_matrix = bar_pass_vert.pass_matrix[:-1]

    start_tr = 1
    for i, th in enumerate(thetas):
        if th == -1:
            start_tr += bar_dur_in_TR_hor + iti_duration
            continue
        else:
            if th == 0:
                mov_direction = 1
                ori_direction = (0, 1, 2)
                bar_pass = bar_pass_hor
            if th == 270:
                mov_direction = 1
                ori_direction = (0, 2, 1)
                bar_pass = bar_pass_vert
            if th == 180:
                mov_direction = -1
                ori_direction = (0, 1, 2)
                bar_pass = bar_pass_hor
            if th == 90:
                mov_direction = -1
                ori_direction = (0, 2, 1)
                bar_pass = bar_pass_vert
            # create square DM
            all_bars_square[start_tr:start_tr +
                            bar_pass.pass_matrix.shape[0]] = bar_pass.pass_matrix[::mov_direction, :, :].transpose(ori_direction)
            # fix the timing of the next trial
            start_tr += bar_pass.pass_matrix.shape[0] + iti_duration

    all_bar_rect = np.zeros_like(all_bars_square)
    pix_h = int(9 * n_pixels / 16)
    border = int((n_pixels - pix_h) / 2)
    for i, sq in enumerate(all_bars_square):
        all_bar_rect[i, border:-border,
                     :] = imresize(sq, (pix_h, n_pixels), 'nearest')

    # swap axes for popeye:
    visual_dm = np.transpose(np.array(all_bar_rect), [1, 2, 0])
    visual_dm = np.round(visual_dm[:, :, :nr_timepoints]).astype(np.int16)

    # import matplotlib.pyplot as pl
    # import seaborn as sn
    # import matplotlib.animation as animation
    # f = pl.figure(figsize = (6,6))
    # ims = []
    # for x in range(visual_dm.shape[-1]):
    #     im = pl.imshow(visual_dm[:,:,x], animated=True, clim = [0, 1], cmap = 'viridis', alpha = 0.95, extent = [-n_pixels/2,n_pixels/2,-n_pixels/2,n_pixels/2])
    #     pl.axis('off')
    #     ims.append([im])

    # ani = animation.ArtistAnimation(f, ims, interval = 25, blit = True, repeat_delay = 150)
    # pl.show()

    return visual_dm


def create_bd_designmatrix_nprf(
        bar_dur_in_TR_hor=32, # 49 for nprf2 expt
        bar_dur_in_TR_vert=57, # 49 for nprf2 expt
        iti_duration=1,
        bar_width=0.1,
        n_pixels=192,
        thetas=[-1, 0, 90, -1,  270, 180, -1],
        nr_timepoints=290, # 351 for nprf2 expt
        TR=0.945,
        dm_upscale_factor=10,
        window_length=1000,
        polyorder=2):

    import numpy as np
    from scipy.signal import fftconvolve
    from hrf_estimation.hrf import spmt, dspmt, ddspmt
    from scipy.signal import savgol_filter

    kernel = spmt(np.linspace(
        0, 35, dm_upscale_factor * 35 / TR, endpoint=False))

    visual_designmatrix = create_visual_designmatrix_nprf(
        bar_dur_in_TR_hor=bar_dur_in_TR_hor,
        bar_dur_in_TR_vert=bar_dur_in_TR_vert,
        iti_duration=iti_duration,
        bar_width=bar_width,
        n_pixels=n_pixels,
        thetas=thetas,
        nr_timepoints=nr_timepoints)
    # create the blockdesign design matrix
    blocks = np.sign(visual_designmatrix.sum(axis=0).sum(axis=0))
    raw_dm = np.repeat(blocks, dm_upscale_factor)

    # convolve, subsample and reshape
    cr = fftconvolve(raw_dm, kernel)[::dm_upscale_factor]
    conv_dm = cr[:nr_timepoints]
    conv_dm = conv_dm.reshape((-1, nr_timepoints))

    # normalize regressor amplitude
    conv_dm = (conv_dm.T / conv_dm.std(axis=-1)).T

    # Window must be odd
    if window_length % 2 == 0:
        window_length += 1
    conv_dm_filt = conv_dm - savgol_filter(conv_dm, window_length=window_length, polyorder=polyorder,
                                           deriv=0, axis=1, mode='nearest')
    # the resulting visual design matrix
    visual_dm = np.vstack((np.ones((1, nr_timepoints)), conv_dm, conv_dm_filt))
    # pl.plot(visual_dm.T)
    # pl.show()

    return visual_dm
