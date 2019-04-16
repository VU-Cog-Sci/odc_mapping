import cortex
import os.path as op
import pandas as pd
import numpy as np
from nilearn import surface
from bids import BIDSLayout
from nilearn import image

derivatives = '/data/odc/derivatives'
subject = 'tr'
pc_subject = 'odc.{}'.format(subject)
session = 'odc'

left, right = cortex.db.get_surf('odc.{}'.format(subject), 'fiducial')
left_surface = cortex.polyutils.Surface(left[0], left[1])
right_surface = cortex.polyutils.Surface(right[0] , right[1])


zmap = op.join(derivatives, 'sampled_giis', 'sub-{subject}', 'ses-{session}',
               'func', 'sub-{subject}_ses-{session}_left_over_right_desc-zmap-depth-0.571_hemi-lh.gii'). \
    format(subject=subject, session=session)
zmap = surface.load_surf_data(zmap)
zmap = pd.DataFrame(zmap)


energies = op.join(derivatives, 'zmap_spatfreq', 'sub-{subject}', 'ses-{session}',
               'func', 'sub-{subject}_ses-{session}_dynamicbw_energies.pkl').format(subject=subject,
                                                                          session=session)
#energies = op.join(derivatives, 'zmap_spatfreq', 'sub-{subject}', 'ses-{session}',
               #'func', 'sub-{subject}_ses-{session}_energies.pkl').format(subject=subject,
                                                                          #session=session)
energies = pd.read_pickle(energies)
#energies = energies[(energies.index.get_level_values('wavelength')>1) & (energies.index.get_level_values('wavelength')<8)]

#example_gabors = op.join(derivatives, 'zmap_spatfreq', 'sub-{subject}', 'ses-{session}',
               #'func', 'sub-{subject}_ses-{session}_fwhm-10_example_gabors.pkl').format(subject=subject,
                                                                               #session=session)
example_gabors = op.join(derivatives, 'zmap_spatfreq', 'sub-{subject}', 'ses-{session}',
               'func', 'sub-{subject}_ses-{session}_dynamicbw_example_gabors.pkl').format(subject=subject,
                                                                               session=session)
example_gabors = pd.read_pickle(example_gabors)


mask = np.zeros(len(left_surface.pts))
mask[energies.columns] = True
ss = left_surface.create_subsurface(mask.astype(bool))
example_gabors = ss.lift_subsurface_data(example_gabors.values)

wl_grouped_energy = energies.groupby('wavelength').sum()
max_wavelength = energies.groupby('wavelength').sum().idxmax(0)
max_orientation = energies.T.apply(lambda row: row[max_wavelength.loc[row.name]].idxmax(), 1)

mean_wavelength = energies.groupby('wavelength').mean()
mean_wavelength = (mean_wavelength / mean_wavelength.sum(0) * mean_wavelength.index.values[:, np.newaxis]).sum(0)

max_wavelength = ss.lift_subsurface_data(max_wavelength.values.astype(float))
max_wavelength[(zmap == 0).values.ravel()] = np.nan

max_orientation = ss.lift_subsurface_data(max_orientation.values)
max_orientation[(zmap == 0).values.ravel()] = np.nan

mean_wavelength = ss.lift_subsurface_data(mean_wavelength.values)
mean_wavelength[(zmap == 0).values.ravel()] = np.nan

v_mwl = cortex.Vertex(max_wavelength, pc_subject,
                     vmin=0, vmax=15)
v_meanwl = cortex.Vertex(mean_wavelength, pc_subject,
                     vmin=0, vmax=15)
v_ori = cortex.Vertex(max_orientation, pc_subject,
                      cmap='hsv',
                     vmin=0, vmax=np.pi)

v_zmap = cortex.Vertex(zmap.values.T, pc_subject, vmin=-3, vmax=3, cmap='BuBkRd')
v_example_gabors = cortex.Vertex(example_gabors, pc_subject, vmin=-0.1, vmax=0.1, cmap='BuBkRd')

layout = BIDSLayout(op.join(derivatives, 'tsnr'),
                    validate=False)
veins = layout.get(subject=subject,
                   session='prf',
                   suffix='invtsnr',
                   return_type='file')
veins = image.mean_img(veins)

t1w = cortex.db.get_anat(pc_subject, 'raw')
veins = image.resample_to_img(veins,
                              t1w)

veins = cortex.Volume(veins.get_data().T,
                                subject=pc_subject,
                                xfmname='identity',
                                vmin=0,
                                vmax=2)

ds = cortex.Dataset(max_wavelength=v_mwl,
                    mean_wavelength=v_meanwl,
                    example_gabors=v_example_gabors,
                    orientation=v_ori,
                    veins=veins,
                    zmap=v_zmap)
#cortex.webshow(v_mwl)
cortex.webshow(ds)
