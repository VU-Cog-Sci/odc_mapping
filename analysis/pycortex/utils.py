import os

def get_bids_file(folder,
                  type,
                  modality,
                  subject,
                  suffix,
                  session=None,
                  space=None,
                  acquisition=None,
                  description=None,
                  label=None,
                  echo = None,
                  inversion=None,
                  part=None,
                  extension='nii.gz',
                  check_exists=True):

    folder = os.path.join(folder, type)
    
    session_str = '_ses-{}'.format(session) if session else ''
    session_folder = 'ses-{}/'.format(session) if session else ''
    space_str = '_space-{}'.format(space) if space else ''
    desc_str = '_desc-{}'.format(description) if description else ''
    label_str = '_label-{}'.format(label) if label else ''
    acquisition_str = '_acq-{}'.format(acquisition) if acquisition else ''
    inv_str = '_inv-{}'.format(inversion) if inversion else ''
    echo_str = '_echo-{}'.format(echo) if echo else ''
    part_str = '_part-{}'.format(part) if echo else ''

    str = 'sub-{subject}/{session_folder}{modality}/sub-{subject}{session_str}{acquisition_str}{space_str}{label_str}{desc_str}{inv_str}{echo_str}{part_str}_{suffix}.{extension}'.format(**locals())

    fn = os.path.join(folder, str)

    if not os.path.exists(fn):
        if check_exists:
            raise Exception('{} does not exists!'.format(fn))
        else:
            return None

    return fn
