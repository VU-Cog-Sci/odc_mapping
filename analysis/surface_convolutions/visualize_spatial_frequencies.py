import argparse
import cortex
import os.path as op
import pandas as pd
import numpy as np
from nilearn import surface
from bids import BIDSLayout
from nilearn import image

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
        xy = pd.read_pickle(op.join(derivatives, 'coordinate_patches', 'sub-{subject}',
                            'anat', 'sub-{subject}_hemi-{hemi}_coordinatepatch.pkl').format(**locals()))

        energies = pd.read_pickle(energies)

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
            zmaps[hemi].append(surface.load_surf_data(zmap))

        zmaps[hemi] = np.array(zmaps[hemi])
        max_orientations[hemi] = pd.concat(max_orientations[hemi])

        ss = pd.DataFrame([], columns=np.arange(surf.pts.shape[0]))
        max_wavelengths[hemi]  = pd.concat((ss, max_wavelengths[hemi])).values
        max_orientations[hemi] = pd.concat((ss, max_orientations[hemi])).values

    print(max_wavelengths['lh'].shape, max_wavelengths['rh'].shape)
    max_wavelengths = np.concatenate([max_wavelengths['lh'], 
                                      max_wavelengths['rh']],
                                     axis=-1)
    max_orientations = np.concatenate([max_orientations['lh'], 
                                       max_orientations['rh']],
                                      axis=-1)

    print(zmaps['lh'].shape, zmaps['rh'].shape)
    zmaps = np.concatenate([zmaps['lh'], 
                            zmaps['rh']],
                           axis=-1)

    images = {}
    images['wavelength'] = cortex.Vertex(max_wavelengths, 'odc.{}'.format(subject),
                                         vmin=0,
                                         vmax=10)
    images['orientation'] = cortex.Vertex(max_orientations, 'odc.{}'.format(subject),
                                          vmin=0,
                                          vmax=np.pi,
                                          cmap='hsv')

    images['zmap'] = cortex.Vertex(zmaps, 'odc.{}'.format(subject), vmin=-3,
                                          vmax=3)

    layout = BIDSLayout(op.join(derivatives, 'tsnr'),
                        validate=False)
    veins = layout.get(subject=subject,
                       session=session,
                       suffix='invtsnr',
                       return_type='file')
    veins = image.mean_img(veins)

    t1w = cortex.db.get_anat(pc_subject, 'raw')
    veins = image.resample_to_img(veins,
                                  t1w)

    images['veins'] = cortex.Volume(veins.get_data().T,
                                    subject=pc_subject,
                                    xfmname='identity',
                                    vmin=0,
                                    vmax=2)

    ds = cortex.Dataset(**images)

    cortex.webshow(ds)

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
