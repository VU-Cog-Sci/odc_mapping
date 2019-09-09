import argparse
from nilearn import surface
import pickle as pkl
import numpy as np
import os.path as op
import os
import pandas as pd
from scipy import interpolate
from itertools import product
from tqdm import tqdm
from skimage.filters import gabor_kernel
from skimage.io import imsave
import scipy.ndimage as ndi
import sharedmem


def main(derivatives,
         subject,
         session):

    grid_resolution = .35
    max_frequency = 1.
    min_frequency = 1/10.
    n_frequencies = 50
    n_orientations = 16
    scale_factor = (min_frequency/max_frequency)**(-1/(n_frequencies-1))
    frequencies_mm = scale_factor**-np.arange(0, n_frequencies) * max_frequency
    orientations = np.linspace(0, np.pi, n_orientations, endpoint=False)

    frequencies_pix = frequencies_mm * grid_resolution

    for hemi in ['lh', 'rh']:

        xy = pd.read_pickle(op.join(derivatives, 'coordinate_patches', 'sub-{subject}',
                            'anat', 'sub-{subject}_hemi-{hemi}_coordinatepatch.pkl').format(**locals()))

        depths = np.round(np.linspace(0, 1, 8), 3)[1:-1]

        pb = tqdm(total=len(frequencies_pix) * len(orientations) * len(depths))

        mask_name = 'V1'+hemi[:1]

        results = []

        for depth in depths:
            zmap = op.join(derivatives, 'sampled_giis', 'sub-{subject}', 'ses-{session}',
                           'func',
                           'sub-{subject}_ses-{session}_left_over_right_desc-zmap-depth-{depth}_hemi-{hemi}.gii'). \
                format(**locals())
            zmap_v = surface.load_surf_data(zmap)
            zmap = pd.DataFrame(zmap_v, columns=['z_value'])
            df = zmap.merge(xy, left_index=True, right_index=True)
            df = df.loc[(df.z == 0) & df[mask_name]]

            x_grid, y_grid = np.meshgrid(np.arange(df['x'].min(), df['x'].max(), grid_resolution),
                                         np.arange(df['y'].min(), df['y'].max(), grid_resolution))


            data = interpolate.griddata(df[['x', 'y']],
                                        df['z_value'],
                                        np.vstack((x_grid.ravel(), y_grid.ravel())).T,
                                        fill_value=0,
                                        method='linear').reshape(x_grid.shape)

            results_dir = op.join(derivatives, 'zmap_spatfreq',
                                             'sub-{subject}',
                                             'ses-{session}',
                                             'func').format(**locals())

            if not op.exists(results_dir):
                os.makedirs(results_dir)

            print('Writing zmap...')
            imsave(op.join(results_dir, f'sub-{subject}_ses-{session}_hemi-{hemi}_depth-{depth}_desc-zmap2d_image.png'), data)

            pars = [(freq, ori) for freq, ori in product(frequencies_pix, orientations)]

            n_jobs = 16

            with sharedmem.MapReduce(np=n_jobs) as pool:
                def reduce(r):
                    pb.update()
                    return r

                def get_power(pars):
                    freq, ori = pars
                    kernel = gabor_kernel(freq, ori, n_stds=3)
                    filtered_real = ndi.convolve(data, np.real(kernel), mode='wrap')
                    filtered_imag = ndi.convolve(data, np.imag(kernel), mode='wrap')
                    power = np.sqrt(filtered_real**2 + filtered_imag**2)
                    power[data == 0] = np.nan

                    power = pd.DataFrame([power.ravel()],
                                         index=pd.MultiIndex.from_tuples([(depth, freq/grid_resolution, ori)], names=['depth', 'frequency', 'orientation']))

                    return power

                results += pool.map(get_power, pars, reduce)

        results = pd.concat(results, axis=0)

        results_vertex = interpolate.griddata(np.vstack((x_grid.ravel(),
                                                         y_grid.ravel())).T,
                                              results.T,
                                              df[['x', 'y']])

        results_vertex = pd.DataFrame(results_vertex.T,
                                      index=results.index,
                                      columns=df.index)
        results_vertex.loc[:, df[df['z_value'] == 0].index] = np.nan


        results_vertex.to_pickle(op.join(results_dir,
                                         'sub-{subject}_ses-{session}_hemi-{hemi}_energies.pkl').format(**locals()))



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("subject", 
                        type=str,
                        help="subject to process")
    parser.add_argument("session", 
                        type=str,
                        help="subject to process")
    parser.add_argument("--derivatives", 
                        type=str,
                        default='/derivatives',
                        help="Folder where derivatives reside")
    args = parser.parse_args()

    main(derivatives=args.derivatives,
         subject=args.subject,
         session=args.session)
