from skimage import measure
from utils import save_mesh_geometry
from nilearn import image
import numpy as np
import nibabel as nb

wgb = '/data/odc/derivatives/nighres/sub-de/ses-anat/anat/sub-de_ses-anat_space-average_desc-cgb_hemi-left_levelset.nii.gz'

wgb = image.load_img(wgb)

coords, faces, _, _ = measure.marching_cubes_lewiner(wgb.get_data(), 0)

#coords = np.dot(np.linalg.inv(wgb.affine),
                #np.concatenate((coords,
                                #np.ones((coords.shape[0], 1))), 1).T).T

correct_matrix = np.array([[1, 0, 0, 0],
                           [0, 0, 1, 0],
                           [0, 1, 0, 0],
                           [0, 0, 0, 1]])
correct_matrix = np.identity(4)
coords = np.dot(correct_matrix.dot(wgb.affine),
                np.concatenate((coords,
                                np.ones((coords.shape[0], 1))), 1).T).T
#coords = np.dot(wgb.affine,
                #np.concatenate((coords,
                                #np.ones((coords.shape[0], 1))), 1).T).T

#correct_matrix = np.array([[-1, 0, 0, 0],
                           #[0, 0, -1, 0],
                           #[0, -1, 0, 0],
                           #[0, 0, 0, 1]])
coords = correct_matrix.dot(coords.T).T
coords = coords[:, :3]
surf_dict = {'coords':coords,
             'faces':faces}

meta = { 'VolGeomX_R': '-1.000000',
 'VolGeomX_A': '0.000000',
 'VolGeomX_S': '-0.000000',
 'VolGeomY_R': '-0.000000',
 'VolGeomY_A': '0.000000',
 'VolGeomY_S': '-1.000000',
 'VolGeomZ_R': '0.000000',
 'VolGeomZ_A': '1.000000',
 'VolGeomZ_S': '-0.000000',
 'VolGeomC_R': '0.000000',
 'VolGeomC_A': '0.000000',
 'VolGeomC_S': '0.000000'}


coord_array = nb.gifti.GiftiDataArray(data=coords,
                                      intent=nb.nifti1.intent_codes[
                                          'NIFTI_INTENT_POINTSET'],
                                      meta=meta)
face_array = nb.gifti.GiftiDataArray(data=faces,
                                     intent=nb.nifti1.intent_codes[
                                         'NIFTI_INTENT_TRIANGLE'])
gii = nb.gifti.GiftiImage(darrays=[coord_array, face_array])
#nb.gifti.write(gii, surf_mesh)

pointset = gii.get_arrays_from_intent('NIFTI_INTENT_POINTSET')[0]

nb.gifti.write(gii, '/data/odc/zooi/test.gii',)




#save_mesh_geometry('/data/odc/zooi/test.gii', surf_dict)
