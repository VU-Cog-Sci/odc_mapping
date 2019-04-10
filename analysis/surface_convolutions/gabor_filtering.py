import cortex
import yaml
import os.path as op
import pandas as pd
from scipy import stats
import numpy as np
from nilearn import surface
import pandas as pd

subject = 'tk'
session = 'odc2'
derivatives = '/data/odc/derivatives'

with open(op.abspath('coordinate_vertices.yml')) as f:
    db = yaml.load(f)

if 'sub-{}'.format(subject) not in db:
    raise Exception('Subject {} not present in coordinate_vertices.yml'.format(subject))

meta = db['sub-{}'.format(subject)]



zmap = op.join(derivatives, 'sampled_giis', 'sub-{subject}', 'ses-{session}',
               'func', 'sub-{subject}_ses-{session}_left_over_right_desc-zmap-depth-0.571_hemi-rh.gii'). \
    format(subject=subject, session=session)

zmap = surface.load_surf_data(zmap)

left, right = cortex.db.get_surf(subject, 'fiducial')
left_surface = cortex.polyutils.Surface(left[0], left[1])
right_surface = cortex.polyutils.Surface(right[0] , right[1])

right_patch = right_surface.get_geodesic_strip_patch(v0=meta['rh']['start'],
                                                     v1=meta['rh']['end'],
                                                     m=2.5,
                                                     method='whole_surface',
                                                     radius=20)

fwhm = 5
orientations = np.linspace(0, np.pi, 8, endpoint=False)

max_frequency = 1
min_frequency = 1/20.
n_frequencies = 8
scale_factor = (min_frequency/max_frequency)**(-1/(n_frequencies-1))
spatial_frequencies = scale_factor**-np.arange(0, n_frequencies) * max_frequency
wavelengths = 1./spatial_frequencies

def make_gabor_patches(coords,
                       distances,
                       fwhm,
                       wavelength,
                       theta=0):

    sd = fwhm / 2.355

    gauss = stats.norm(0, sd).pdf(distances)

    coords_ = coords[..., 0] * np.cos(theta) + coords[..., 1] * np.sin(theta)
    gabor = gauss * np.exp(1j * (2 * np.pi * coords_ / wavelength))
    gabor.real /= np.linalg.norm(gabor.real, axis=1)
    gabor.imag /= np.linalg.norm(gabor.imag, axis=1)

    return gabor

results_dir = op.join(derivatives, 'zmap_spatfreq', 'sub-{subject}', 'ses-{session}',
                      'func').format(subject=subject,
                                     session=session)

if not op.exists(results_dir):
    os.makedirs(results_dir)

xy = pd.DataFrame({'x':patch['coordinates'][0, :],
                   'y':patch['coordinates'][1, :]})

patch_indices = xy[patch['vertex_mask']].index

ss = patch['subsurface']
distances = np.array([ss.geodesic_distance(ss.subsurface_vertex_map[ix]) for ix in patch_indices])

# rows correspond to centers of coordinate system
coords = (xy.loc[patch_indices].values[np.newaxis, :, :] - xy.loc[patch_indices].values[:, np.newaxis, :])


energies = np.zeros((len(patch_indices), len(wavelengths), len(orientations)))
example_gabors = []

xy_ = xy.loc[ss.subsurface_vertex_mask]
example_index = np.linalg.norm(xy_ - xy_.mean(), axis=1).argmin()

energies = []

for i, wl in enumerate(wavelengths):
    for j, ori in enumerate(orientations):
        print(wl, ori)
        gabor = make_gabor_patches(coords,
                                   distances,
                                   fwhm,
                                   wl,
                                   ori)

        energy = gabor * zmap[ss.subsurface_vertex_mask]
        energy = np.linalg.norm(energy.real, axis=1) + np.linalg.norm(energy.imag, axis=1)

        example_gabors.append(np.real(gabor[example_index]))

        index = pd.MultiIndex.from_tuples([(wl, ori)], names=['wavelength', 'orientation'])
        energy = pd.DataFrame(energy[np.newaxis, :], columns=xy_.index, index=index)
        energies.append(energy)

energies = pd.concat(energies)

max_wavelength = energies.groupby('wavelength').sum().idxmax(0)
max_orientation = energies.T.apply(lambda row: row[max_wavelength.loc[row.name]].idxmax(), 1)

energies.to_pickle(op.join(results_dir, 'sub-{subject}_ses-{session}_energies.pkl'))


#v_dominant_orientations = cortex.Vertex(ss.lift_subsurface_data(dominant_orientations),
                                    #'odc.{}'.format(subject))
#v_dominant_wavelengths = cortex.Vertex(ss.lift_subsurface_data(dominant_wavelengths),
                                    #'odc.{}'.format(subject))
#v_example_gabors = cortex.Vertex(ss.lift_subsurface_data(np.array(example_gabors)),
                                    #'odc.{}'.format(subject))
#ds = cortex.Dataset(ori=v_dominant_orientations,
                #wl=v_dominant_wavelengths,
                #gabors=v_example_gabors)



