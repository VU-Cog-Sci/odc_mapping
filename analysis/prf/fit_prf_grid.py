import argparse
from utils import get_voxel_data, get_vertex_data
import numpy as np
from prf import PRFGridSearch
import os
import os.path as op
import numpy as np
from scipy import signal


def main(subject,
         session,
         derivatives,
         source,
         description,
         out_dir,
         n_jobs=8,
         r2_threshold=0.3,
         distance_screen=15,
         size_cm=6,
         TR=2.7,
         n_pixels=50):

    print("loading design matrix")
    dm = np.load(op.join(derivatives, 'prf/dm.npy'))

    dm = signal.resample(dm, 118, axis=-1)

    grid_searcher = PRFGridSearch(dm, distance_screen, size_cm, TR)

    eccs = np.hstack(([0], np.geomspace(.25, 20, 25)))
    angles = np.linspace(-np.pi, np.pi, 32, endpoint=False)
    sizes = np.geomspace(.25, 15, 25)

    print('making predictions')
    grid_searcher.make_predictions(angles, eccs, sizes)

    if source == 'vertices':

        print('loading data')
        data = get_vertex_data(derivatives,
                               subject,
                               session)

        print('Found {} runs'.format(data.shape[0]))

        data = np.mean(data, 0)
        mask = (data != 0).all(0)

        print('searching')
        pars = grid_searcher.fit(data[:, mask],
                                 include_predictions=True)

        r2 = np.zeros(data.shape[1])
        size = np.zeros(data.shape[1])
        angle = np.zeros(data.shape[1])
        ecc = np.zeros(data.shape[1])

        r2[mask] = pars['r2']
        size[mask] = pars['size']
        angle[mask] = pars['angle']
        ecc[mask] = pars['ecc']

        if not os.path.exists(out_dir):
            os.makedirs(out_dir)

        np.savez(op.join(out_dir, 'sub-{subject}_desc-{description}_prf_grid'.format(**locals())), 
                 r2=r2,
                 size=size,
                 angle=angle,
                 ecc=ecc)

        optim_pars = grid_searcher.refine_parameters(pars[pars['r2'] > r2_threshold],
                                                     n_jobs=n_jobs)
                                                     

        r2[optim_pars.index] = optim_pars['r2_opt']
        size[optim_pars.index] = optim_pars['size_opt']
        angle[optim_pars.index] = optim_pars['angle_opt']
        ecc[optim_pars.index] = optim_pars['ecc_opt']


        np.savez(op.join(out_dir, 'sub-{subject}_desc-{description}_prf_optim'.format(**locals())), 
                 r2=r2,
                 size=size,
                 angle=angle,
                 ecc=ecc)


 

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("subject", 
                        #nargs='?',
                        type=str,
                        help="subject to process")
    parser.add_argument("session", 
                        default='prf',
                        nargs='?',
                        type=str,
                        help="subject to process")
    parser.add_argument("--out", 
                        type=str,
                        help="Where to write the data to")
    parser.add_argument("--description", 
                        type=str,
                        help="Identifier")
    parser.add_argument("--njobs", 
                        default=8,
                        type=int,
                        help="Number of processes to use for optimization")
    parser.add_argument("--source", 
                        default='voxels',
                        type=str,
                        nargs='?',
                        help="Where data comes from ('voxels' or 'vertices')")
    parser.add_argument("--r2thr", 
                        default=0.3,
                        type=float,
                        nargs='?',
                        help="Which threshold to choose to refine parameters in.")
    args = parser.parse_args()

    main(subject=args.subject,
         session=args.session,
         derivatives='/home/shared/2018/visual/7T_BR/ODC/',
         source=args.source,
         description=args.description,
         out_dir=args.out,
         n_jobs=args.njobs,
         r2_threshold=args.r2thr)
