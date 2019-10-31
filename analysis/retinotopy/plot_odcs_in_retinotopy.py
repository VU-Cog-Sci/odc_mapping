from nilearn import surface
import os.path as op
import numpy as np



derivatives = '/data/odc/derivatives'

subject = '06'
session = 'odc'
depth = .571

prf_fn = op.join(derivatives, 'prf', 'vertices', 'sub-{subject}_desc-test2_prf_optim.npz').format(**locals())
prf_pars = np.load(prf_fn)

zmaps = []
for hemi in ['lh', 'rh']:
    zmap = surface.load_surf_data(op.join(derivatives,
                                          'sampled_giis/sub-{subject}/ses-odc/func/sub-{subject}_ses-{session}_left_over_right_desc-zmap-depth-{depth}_hemi-{hemi}.gii'.format(**locals()))
                                  )

    zmaps.append(zmap)
zmaps = np.concatenate(zmaps)

masks = cortex.utils.get_roi_verts('odc.{}'.format(subject))

for mask in ['V1l', 'V1r']:

