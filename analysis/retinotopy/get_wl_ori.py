import argparse
import cortex
from nilearn import surface
import pandas as pd
import os.path as op
import os
import numpy as np

def main(derivatives,
         subject,
         session):

    pc_subject = 'odc.{}'.format(subject)

    left, right = cortex.db.get_surf('odc.{}'.format(subject), 'fiducial')
    left_surface = cortex.polyutils.Surface(left[0], left[1])
    right_surface = cortex.polyutils.Surface(right[0] , right[1])


    max_wavelengths = {}
    max_orientations = {}
    zmaps = {}


    for hemi, surf in zip(['lh', 'rh'], [left_surface, right_surface]):
        energies = op.join(derivatives,
                           'zmap_spatfreq',
                           'sub-{subject}',
                           'ses-{session}',
                           'func',
                           'sub-{subject}_ses-{session}_hemi-{hemi}_energies.pkl').format(subject=subject, session=session, hemi=hemi)

        energies = pd.read_pickle(energies)
        energies = energies.loc[:, ~energies.isnull().any(0)]

        max_frequency = energies.groupby(['depth', 'frequency']).sum().groupby('depth', as_index=True).apply(lambda d: d.reset_index('depth', drop=True).idxmax())

        max_wavelengths[hemi] = 1. / max_frequency

        max_orientations[hemi] = []

        zmaps[hemi] = []

        for depth, d in energies.groupby('depth'):
            tmp = d.loc[(depth, max_frequency.loc[depth]), :].idxmax()
            tmp = tmp.apply(lambda x: x[2] if not x is np.nan else None)
            tmp = pd.DataFrame(tmp,
                               columns=pd.Index([depth], name='depth')).T
            tmp.columns = energies.columns
            max_orientations[hemi].append(tmp)

            zmap = op.join(derivatives, 'sampled_giis', 'sub-{subject}', 'ses-{session}',
                           'func', 'sub-{subject}_ses-{session}_left_over_right_desc-zmap-depth-{depth}_hemi-{hemi}.gii'). \
                format(**locals())
            zmap = surface.load_surf_data(zmap)
            zmaps[hemi].append(pd.DataFrame(zmap, index=pd.MultiIndex.from_product([[depth], 
                                                                                    np.arange(len(zmap))], 
                                                                                   names=['depth', 'vertex'])))

        max_orientations[hemi] = pd.concat(max_orientations[hemi])

        zmaps[hemi] = pd.concat(zmaps[hemi])
        ss = pd.DataFrame([], columns=np.arange(surf.pts.shape[0]))
        max_wavelengths[hemi]  = pd.concat((ss, max_wavelengths[hemi]))
        max_orientations[hemi] = pd.concat((ss, max_orientations[hemi]))
        
    max_wavelengths = pd.concat((max_wavelengths['lh'], max_wavelengths['rh']), 1, keys=['lh', 'rh'], names=['hemi']).T
    max_orientations = pd.concat((max_orientations['lh'], max_orientations['rh']), 1, keys=['lh', 'rh'], names=['hemi']).T
    zmaps = pd.concat([zmaps['lh'], zmaps['rh']], axis=0, keys=['lh', 'rh'], names=['hemi'], )


    df = pd.concat((zmaps.unstack('depth').droplevel(0, 1),
                    max_wavelengths,
                    max_orientations),
                   axis=1,
                   keys=['z-value', 'wavelength', 'orientation'],
                   names=['type'])

    results_dir = op.join(derivatives, 'max_wl', f'sub-{subject}', f'ses-{session}', 'func')
    if not op.exists(results_dir):
        os.makedirs(results_dir)
    df.to_pickle(op.join(results_dir, f'sub-{subject}_ses-{session}_wavelengths.pkl.gz'))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("subject", 
                        type=str,
                        help="subject to process")
    parser.add_argument("session", 
                        type=str,
                        help="subject to process")

    args = parser.parse_args()

    main('/data/odc/derivatives',
         subject=args.subject,
         session=args.session)
