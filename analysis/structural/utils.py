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
                   extension='nii.gz',
                   check_exists=True):

    folder = os.path.join(derivatives_folder, type)
    
    session_str = '_ses-{}'.format(session) if session else ''
    session_folder = 'ses-{}/'.format(session) if session else ''
    space_str = '_space-{}'.format(space) if space else ''
    desc_str = '_desc-{}'.format(description) if description else ''
    label_str = '_label-{}'.format(label) if label else ''
    acquisition_str = '_acq-{}'.format(acquisition) if acquisition else ''

    str = 'sub-{subject}/{session_folder}{modality}/sub-{subject}{session_str}{acquisition_str}{space_str}{label_str}{desc_str}_{suffix}.{extension}'.format(**locals())

    fn = os.path.join(folder, str)

    if not os.path.exists(fn):
        if check_exists:
            raise Exception('{} does not exists!'.format(fn))
        else:
            return None

    return fn


def binary_closing(input_image, iterations):
    from scipy.ndimage import binary_closing
    from nilearn import image
    from nipype.utils.filemanip import split_filename
    import os

    _, fn, ext = split_filename(input_image)

    input_image = image.load_img(input_image)
    output_image = image.new_img_like(input_image,
                                      binary_closing(input_image.get_data(), 
                                                     iterations=iterations))

    output_image.to_filename(os.path.abspath('{fn}_closed{ext}'.format(fn=fn, ext=ext)))

    return output_image.get_filename()

def largest_component(input_image):
    from nilearn import image
    from nipype.utils.filemanip import split_filename
    import os

    _, fn, ext = split_filename(input_image)

    output_image = image.largest_connected_component_img(input_image)

    output_image.to_filename(os.path.abspath('{fn}_largestcomponent{ext}'.format(fn=fn, ext=ext)))

    return output_image.get_filename()
