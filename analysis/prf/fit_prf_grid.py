import argparse
from utils import get_voxel_data, get_vertex_data
import numpy as np
from prf import PRFGridSearch
import os.path as op
import numpy as np


def main(subject,
         session,
         derivatives,
         source,
         description,
         out_dir,
         distance_screen=15,
         size_cm=6,
         TR=2.7,
         n_pixels=50):

    dm = np.load(op.join(derivatives, 'prf/dm.npy'))

    grid_searcher = PRFGridSearch(dm, distance_screen, size_cm, 1.0)

    eccs = np.hstack(([0], np.geomspace(1, 30, 30)))
    angles = np.linspace(-np.pi, np.pi, 30, endpoint=False)
    sizes = np.geomspace(2, 30, 30)

    print('making predictions')
    grid_searcher.make_predictions(angles, eccs, sizes)

    if source == 'vertices':

        print('loading data')
        #data = np.load('/data/odc/zooi/bm.npy')
        #data = np.load('/data/odc/zooi/de.npy')
        data = get_vertex_data(derivatives, 
                               subject, 
                               session)

        data = np.mean(data, 0)
        mask = (data != 0).all(0)


        print('searching')
        pars = grid_searcher.fit(data[:, mask])


        r2 = np.zeros(data.shape[1])
        size = np.zeros(data.shape[1])
        angle = np.zeros(data.shape[1])
        ecc = np.zeros(data.shape[1])

        r2[mask] = pars['r2']
        size[mask] = pars['size']
        angle[mask] = pars['angle']
        ecc[mask] = pars['ecc']

        np.savez(op.join(out_dir, 'sub-{subject}_desc-{description}_prf_pars'.format(**locals())), 
                 r2=r2,
                 size=size,
                 angle=angle,
                 ecc=ecc)
 
    elif source == 'voxels':
        print('getting data')
        data, masker = get_voxel_data(derivatives, subject, session)
        data = np.mean(data, 0)
        print(data.shape)
        
        print('Searching for model')
        pars = grid_searcher.fit(data)

        for thing in ['r2', 'size', 'angle', 'ecc']:
            fn = op.join(out_dir, 'sub-{subject}_desc-{description}_prf_{thing}.nii'.format(**locals()))
            masker.inverse_transform(pars[thing]).to_filename(fn)


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
    parser.add_argument("--source", 
                        default='voxels',
                        type=str,
                        nargs='?',
                        help="Where data comes from ('voxels' or 'vertices')")
    args = parser.parse_args()

    main(subject=args.subject,
         session=args.session,
         derivatives='/data/odc/derivatives',
         source=args.source,
         description=args.description,
         out_dir=args.out)
