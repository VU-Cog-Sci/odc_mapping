import nibabel as nb

def save_mesh_geometry(filename, surf_dict):
    '''
    Saves surface mesh geometry to file
    Parameters
    ----------
    filename: str
        Full path and filename under which surfaces data should be saved. The
        extension determines the file format. Currently supported are
        freesurfer geometry formats, gii and ASCII-coded vtk, obj, ply'
    surf_dict: dict
        Surface mesh geometry to be saved. Dictionary with a numpy array with
        key "coords" for a Numpy array of the x-y-z coordinates of the mesh
        vertices and key "faces2 for a Numpy array of the the indices
        (into coords) of the mesh faces
    Notes
    ----------
    Originally created as part of Laminar Python [1]_
    References
    -----------
    .. [1] Huntenburg et al. (2017), Laminar Python: Tools for cortical
       depth-resolved analysis of high-resolution brain imaging data in
       Python. DOI: 10.3897/rio.3.e12346
    '''
    if isinstance(filename, str) and isinstance(surf_dict, dict):
        if (filename.endswith('orig') or filename.endswith('pial') or
                filename.endswith('white') or filename.endswith('sphere') or
                filename.endswith('inflated')):
            nb.freesurfer.io.write_geometry(filename, surf_dict['coords'],
                                            surf_dict['faces'])
            print("\nSaving {}".format(filename))
        elif filename.endswith('gii'):
            _write_gifti(filename, surf_dict['coords'], surf_dict['faces'])
            print("\nSaving {}".format(filename))
        elif filename.endswith('vtk'):
            if 'data' in surf_dict.keys():
                _write_vtk(filename, surf_dict['coords'], surf_dict['faces'],
                           surf_dict['data'])
                print("\nSaving {}".format(filename))
            else:
                _write_vtk(filename, surf_dict['coords'], surf_dict['faces'])
                print("\nSaving {}".format(filename))
        elif filename.endswith('ply'):
            _write_ply(filename, surf_dict['coords'], surf_dict['faces'])
            print("\nSaving {}".format(filename))
        elif filename.endswith('obj'):
            _write_obj(filename, surf_dict['coords'], surf_dict['faces'])
            print("\nSaving {}".format(filename))
            print('To view mesh in brainview, run the command:\n')
            print('average_objects ' + filename + ' ' + filename)
    else:
        raise ValueError('Filename must be a string and surf_dict must be a '
                         'dictionary with keys "coords" and "faces"')


def _write_gifti(surf_mesh, coords, faces):
    coord_array = nb.gifti.GiftiDataArray(data=coords,
                                          intent=nb.nifti1.intent_codes[
                                              'NIFTI_INTENT_POINTSET'])
    face_array = nb.gifti.GiftiDataArray(data=faces,
                                         intent=nb.nifti1.intent_codes[
                                             'NIFTI_INTENT_TRIANGLE'])
    gii = nb.gifti.GiftiImage(darrays=[coord_array, face_array])
    nb.gifti.write(gii, surf_mesh)
