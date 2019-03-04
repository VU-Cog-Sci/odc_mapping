from sys import platform as sys_pf
if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")

import argparse
import numpy as np
import cortex
import re
import matplotlib.colors as colors
import os.path as op


def main(subject,
         derivatives,
         desc='test2',
         pc_subject=None):

    if pc_subject is None:
        pc_subject = 'odc.{}'.format(subject)


    pars_grid = np.load(op.join(derivatives, 
                                'prf', 'vertices',
                                'sub-{subject}_desc-{desc}_prf_grid.npz').format(**locals()))

    pars_optim = np.load(op.join(derivatives, 
                                'prf', 'vertices',
                                'sub-{subject}_desc-{desc}_prf_optim.npz').format(**locals()))

    images = {}
    r2_grid = pars_grid['r2']
    r2_optim = pars_optim['r2']

    angle_grid = pars_grid['angle']
    angle_optim = pars_optim['angle']

    ecc_grid = pars_grid['ecc']
    ecc_optim = pars_optim['ecc']

    size_grid = pars_grid['size']
    size_optim = pars_optim['size']

    images['r2_grid'] = cortex.Vertex(r2_grid, pc_subject, vmin=0, vmax=0.65)
    images['r2_optim'] = cortex.Vertex(r2_optim, pc_subject, vmin=0, vmax=0.65)

    images['angle_grid'] = cortex.Vertex(angle_grid, pc_subject, cmap='hsv', vmin=-3.14, vmax=3.14)
    images['angle_optim'] = cortex.Vertex(angle_optim, pc_subject, cmap='hsv', vmin=-3.14, vmax=3.14)

    images['ecc_grid'] = cortex.Vertex(ecc_grid, pc_subject, vmin=0, vmax=12)
    images['ecc_optim'] = cortex.Vertex(ecc_optim, pc_subject, vmin=0, vmax=12)

    images['size_grid'] = cortex.Vertex(size_grid, pc_subject, vmin=0, vmax=12)
    images['size_optim'] = cortex.Vertex(size_optim, pc_subject, vmin=0, vmax=12)

    ds = cortex.Dataset(**images)
                                     
    cortex.webshow(ds)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("subject",
                        type=str,
                        help="subject to process")
    parser.add_argument("desc",
                        default='test2',
                        nargs='?',
                        type=str,
                        help="subject to process")
    args = parser.parse_args()

    main(args.subject,
         '/data/odc/derivatives',
         args.desc)

