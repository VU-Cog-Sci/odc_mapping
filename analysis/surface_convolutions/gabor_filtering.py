import cortex
import yaml
import os
import os.path as op
import pandas as pd
from scipy import stats
import numpy as np
from nilearn import surface
import pandas as pd
import pickle as pkl

subject = 'tr'
session = 'odc'
derivatives = '/data/odc/derivatives'
derivatives = '/derivatives'

zmap = op.join(derivatives, 'sampled_giis', 'sub-{subject}', 'ses-{session}',
               'func', 'sub-{subject}_ses-{session}_left_over_right_desc-zmap-depth-0.571_hemi-lh.gii'). \
    format(subject=subject, session=session)

zmap = surface.load_surf_data(zmap)

left, right = cortex.db.get_surf('odc.{}'.format(subject), 'fiducial')
left_surface = cortex.polyutils.Surface(left[0], left[1])
right_surface = cortex.polyutils.Surface(right[0] , right[1])

patch_fn = op.join(derivatives, 'coordinate_patches',
                   'sub-{subject}',
                   'anat',
                   'sub-{subject}_hemi-lh_coordinatepatch.pkl').format(**locals())

with open(patch_fn, 'rb') as f:
    patch = pkl.load(f)


fwhm = 10
orientations = np.linspace(0, np.pi, 8, endpoint=False)
wavelengths = np.arange(1, 11, 1)

def make_gaussian_patches(distances,
                          fwhm):

    sd = fwhm / 2.355
    gauss = stats.norm(0, sd).pdf(distances)

    return gauss

def make_gabor_patches(coords,
                       wavelength,
                       theta=0):

    coords_ = coords[..., 0] * np.cos(theta) + coords[..., 1] * np.sin(theta)

    gabor = np.exp(1j * (2 * np.pi * coords_ / wavelength))
    gabor.real -= gabor.real.mean(axis=1)
    gabor.imag -= gabor.imag.mean(axis=1)

    gabor.real /= np.linalg.norm(gabor.real, axis=1)
    gabor.imag /= np.linalg.norm(gabor.imag, axis=1)

    return gabor

results_dir = op.join(derivatives, 'zmap_spatfreq', 'sub-{subject}', 'ses-{session}',
                      'func').format(subject=subject,
                                     session=session)

if not op.exists(results_dir):
    os.makedirs(results_dir)

ss = left_surface.create_subsurface(patch['vertex_mask'])

distances = patch['distances']
coords = patch['vertexwise_coordinate_system']


xy = pd.DataFrame({'x':patch['coordinates'][0, :],
                   'y':patch['coordinates'][1, :]})

xy_ = xy.loc[ss.subsurface_vertex_mask]
example_index = np.linalg.norm(xy_ - xy_.mean(), axis=1).argmin()

energies = []
gauss = make_gaussian_patches(distances, fwhm)

# Do gaussian convolution and remove dc-norm
zmap_gauss_norm = (gauss * zmap[np.newaxis, ss.subsurface_vertex_mask]) - (gauss * zmap[np.newaxis, ss.subsurface_vertex_mask]).mean(1)[:, np.newaxis]

example_gabors = []

for wl in wavelengths:
    for ori in orientations:
        print(wl, ori)
        gabor = make_gabor_patches(coords,
                                   wl,
                                   ori)

        energy = gabor * zmap_gauss_norm
        energy = np.linalg.norm(energy.real, axis=1) + np.linalg.norm(energy.imag, axis=1)

        example_gabors.append(np.real(gauss[example_index] * gabor[example_index]))

        index = pd.MultiIndex.from_tuples([(wl, ori)], names=['wavelength', 'orientation'])
        energy = pd.DataFrame(energy[np.newaxis, :], columns=xy_.index, index=index)
        energies.append(energy)

energies = pd.concat(energies)

#max_wavelength = energies.groupby('wavelength').sum().idxmax(0)
#max_orientation = energies.T.apply(lambda row: row[max_wavelength.loc[row.name]].idxmax(), 1)

energies.to_pickle(op.join(results_dir, 'sub-{subject}_ses-{session}_fwhm-{fwhm}_energies.pkl').format(subject=subject,
                                                                                                   fwhm=fwhm,
                                                                                           session=session))

example_gabors = pd.DataFrame(example_gabors,
                              index=energies.index,
                              columns=xy_.index)

example_gabors.to_pickle(op.join(results_dir, 'sub-{subject}_ses-{session}_fwhm-{fwhm}_example_gabors.pkl').format(subject=subject,
                                                                                                 session=session,
                                                                                                               fwhm=fwhm))

#v_dominant_orientations = cortex.Vertex(ss.lift_subsurface_data(dominant_orientations),
                                    #'odc.{}'.format(subject))
#v_dominant_wavelengths = cortex.Vertex(ss.lift_subsurface_data(dominant_wavelengths),
                                    #'odc.{}'.format(subject))
#v_example_gabors = cortex.Vertex(ss.lift_subsurface_data(np.array(example_gabors)),
                                    #'odc.{}'.format(subject))
#ds = cortex.Dataset(ori=v_dominant_orientations,
                #wl=v_dominant_wavelengths,
                #gabors=v_example_gabors)



