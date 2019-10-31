import cortex
import os.path as op
import numpy as np
from nilearn import image

subject = 'tr'
session = 'odc'
derivatives = '/data/odc/derivatives'

coordinates = op.join(derivatives,
                      'surface_voxels',
                      'coordinate_space_new.nii.gz')


pc_subject = f'odc.{subject}'


transform = cortex.xfm.Transform(np.identity(4), coordinates)
transform.save(pc_subject, 'identity.coordinates')

zmap = '{derivatives}/modelfitting/glm7/sub-{subject}/ses-{session}/func/sub-{subject}_ses-{session}_left_over_right_zmap.nii.gz'.format(
    **locals())

zmap = image.load_img(zmap)
new_shape = np.array(zmap.shape)
new_shape[1] *= 5
new_shape[0] *= 1.1
zmap = image.resample_img(zmap, zmap.affine, new_shape, fill_value=np.nan)
zmap.to_filename('/tmp/zmap.nii.gz')
transform = cortex.xfm.Transform(np.identity(4), zmap.get_filename())
transform.save(pc_subject, 'identity.zmap.extended')

mask = image.math_img('np.abs(zmap)', zmap=zmap)
mask = mask.get_data().T

zmap_vox = cortex.Volume2D(zmap.get_data().T,
                           mask, pc_subject, 'identity.zmap.extended',
                           vmin=-3.5, vmax=3.5, vmin2=0, vmax2=3,
                           cmap='BuBkRd_alpha_2D')
cds_vox = cortex.Volume(coordinates, pc_subject, 'identity.zmap.extended')

curvature_v = cortex.db.get_surfinfo(pc_subject)

random_data = np.random.rand(*curvature_v.data.shape)
random_data_v = cortex.Vertex(random_data, pc_subject)


ds = cortex.Dataset(zmap=zmap_vox, voxels=cds_vox,
                    curvature=curvature_v, random_data=random_data_v)

cortex.webshow(ds)
