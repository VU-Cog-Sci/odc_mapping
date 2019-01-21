import os

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


    str = 'sub-{subject}/{session_folder}{modality}/sub-{subject}{session_str}{acquisition_str}{run_str}{space_str}{label_str}{desc_str}{hemi_str}_{suffix}.{extension}'.format(**locals())

    fn = os.path.join(folder, str)

    if not os.path.exists(fn):
        if check_exists:
            raise Exception('{} does not exists!'.format(fn))
        else:
            return None

    return fn
