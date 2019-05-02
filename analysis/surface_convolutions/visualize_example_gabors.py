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

example_gabors = op.join(derivatives, 'zmap_spatfreq', 'sub-{subject}', 'ses-{session}',
               'func', 'sub-{subject}_ses-{session}_dynamicbw_example_gabors.pkl').format(subject=subject,
                                                                               session=session)
example_gabors = pd.read_pickle(example_gabors)

mask = np.zeros(len(left_surface.pts))
mask[example_gabors.columns] = True
ss = left_surface.create_subsurface(mask.astype(bool))
example_gabors = ss.lift_subsurface_data(example_gabors.values)

v_example_gabors = cortex.Vertex(example_gabors, pc_subject, vmin=-0.1, vmax=0.1, cmap='BuBkRd')


cortex.webshow(v_example_gabors)
