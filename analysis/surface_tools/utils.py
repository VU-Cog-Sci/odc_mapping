import os
from nilearn import image, input_data
import os.path as op
import pandas as pd
import numpy as np
from scipy.signal import savgol_filter
from nilearn import surface
from nilearn.signal import clean
import glob

def get_derivative(derivatives_folder,
                   type,
                   modality,
                   subject,
                   suffix,
                   session=None,
                   space=None,
                   acquisition=None,
                   description=None,
                   label=None,
                   hemi=None,
                   task=None,
                   run=None,
                   extension='nii.gz',
                   check_exists=True,
                   **kwargs):

    folder = os.path.join(derivatives_folder, type)
    
    session_str = '_ses-{}'.format(session) if session else ''
    session_folder = 'ses-{}/'.format(session) if session else ''
    space_str = '_space-{}'.format(space) if space else ''
    desc_str = '_desc-{}'.format(description) if description else ''
    label_str = '_label-{}'.format(label) if label else ''
    acquisition_str = '_acq-{}'.format(acquisition) if acquisition else ''
    hemi_str = '_hemi-{}'.format(hemi) if hemi else ''
    run_str = '_run-{}'.format(run) if run else ''
    task_str = '_task-{}'.format(task) if task else ''


    str = 'sub-{subject}/{session_folder}{modality}/sub-{subject}{session_str}{task_str}{acquisition_str}{run_str}{space_str}{label_str}{desc_str}{hemi_str}_{suffix}.{extension}'.format(**locals())

    fn = os.path.join(folder, str)

    if '*' in fn:
        fn = glob.glob(fn)
    
    else:
        if not os.path.exists(fn):
            if check_exists:
                raise Exception('{} does not exists!'.format(fn))
            else:
                return None

    return fn


def _write_gifti(surf_mesh, points, faces, data=None):
    coord_array = nb.gifti.GiftiDataArray(data=points,
                                          intent=nb.nifti1.intent_codes[
                                              'NIFTI_INTENT_POINTSET'])
    face_array = nb.gifti.GiftiDataArray(data=faces,
                                         intent=nb.nifti1.intent_codes[
                                             'NIFTI_INTENT_TRIANGLE'])
    if data is not None:
        data_array = nb.gifti.GiftiDataArray(data=data,
                                         intent=nb.nifti1.intent_codes[
                                             'NIFTI_INTENT_ESTIMATE'])
        gii = nb.gifti.GiftiImage(darrays=[coord_array, face_array, data_array])
    else:
        gii = nb.gifti.GiftiImage(darrays=[coord_array, face_array])
        
    nb.gifti.write(gii, surf_mesh)


def get_voxel_data(derivatives,
                   subject,
                   session,
                   filter=True,
                   regress_confounds=True,
                   window_length=47,
                   polyorder=3):

    masks = image.load_img(op.join(derivatives, 'nighres/sub-{subject}/ses-anat/anat/sub-{subject}_ses-anat_space-average_desc-cortex_hemi-left_dseg.nii.gz'.format(subject=subject))), image.load_img(op.join(derivatives, 'nighres/sub-{subject}/ses-anat/anat/sub-{subject}_ses-anat_space-average_desc-cortex_hemi-right_dseg.nii.gz'.format(subject=subject)))

    gm = image.math_img('(mask1+ mask2) == 1', mask1=masks[0], mask2=masks[1])
    im = image.load_img('/data/odc/derivatives/spynoza/sub-de/ses-prf/func/sub-de_ses-prf_task-prf_acq-10_run-{run:02d}_preproc.nii.gz'.format(run=1))
    gm = image.resample_to_img(gm, im, interpolation='nearest')
    masker = input_data.NiftiMasker(gm)

    data = []

    for ix in range(1,4):
        mov = pd.read_table(op.join(derivatives, 'spynoza/sub-{subject}/ses-prf/func/sub-{subject}_ses-{session}_task-prf_acq-10_run-{run:02d}_confounds.tsv'.format(subject=subject, run=ix, session=session)))
        compcorr = pd.read_table(op.join(derivatives,'spynoza/sub-{subject}/ses-prf/func/sub-{subject}_ses-{session}_task-prf_acq-10_run-{run:02d}_confounds_compcor.tsv'.format(subject=subject, run=ix, session=session)))
        confounds = pd.concat((mov, compcorr), 1).fillna(method='bfill')
        im = image.load_img('/data/odc/derivatives/spynoza/sub-de/ses-prf/func/sub-de_ses-prf_task-prf_acq-10_run-{run:02d}_preproc.nii.gz'.format(run=ix))
        
        confounds_to_include = ['framewise_displacement', 'x', 'y', 'z', 'rot_x', 'rot_y', 'rot_z',
           'a_comp_cor00', 'a_comp_cor01', 'a_comp_cor02', 'a_comp_cor03', 'a_comp_cor04', 'a_comp_cor05']

        if regress_confounds:
            d = masker.fit_transform(im, confounds=confounds[confounds_to_include].values)
        else:
            d = masker.fit_transform(im)
        
        if filter:
            d -= savgol_filter(d, window_length, polyorder, axis=0)

        data.append(d)

    return np.array(data), masker

def get_vertex_data(derivatives,
                    subject,
                    session,
                   filter=True,
                   regress_confounds=True,
                   window_length=47,
                   polyorder=3):

    sub_dir = op.join(derivatives, 'sampled_giis/sub-{subject}/ses-{session}/func').format(**locals())
    data = []
    runs = range(1,4)
    if (subject == 'tk') & (session == 'prf'):
        runs = range(1, 6)

    for run in runs:
        d = []
        for hemi in ['lh', 'rh']:
            d.append(surface.load_surf_data(op.join(sub_dir, 'sub-{subject}_ses-{session}_task-prf_acq-10_run-{run:02d}_bold.{hemi}.gii'.format(**locals()))).T)


        d = np.hstack(d)

        if regress_confounds:
            mov = pd.read_table(op.join(derivatives, 'spynoza/sub-{subject}/ses-prf/func/sub-{subject}_ses-{session}_task-prf_acq-10_run-{run:02d}_confounds.tsv'.format(subject=subject, run=run, session=session)))
            compcorr = pd.read_table(op.join(derivatives,'spynoza/sub-{subject}/ses-prf/func/sub-{subject}_ses-{session}_task-prf_acq-10_run-{run:02d}_confounds_compcor.tsv'.format(subject=subject, run=run, session=session)))
            confounds = pd.concat((mov, compcorr), 1).fillna(method='bfill')
            d = clean(d, confounds=confounds.values, standardize=False)
        
        if filter:
            d -= savgol_filter(d, window_length, polyorder, axis=0)

        data.append(d)

    return np.array(data)


