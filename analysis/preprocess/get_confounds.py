import argparse
from nilearn import image
import nipype.pipeline.engine as pe
from bids import BIDSLayout
import nipype.interfaces.utility as niu
from nipype.algorithms.confounds import ACompCor, ComputeDVARS
from fmriprep.interfaces.utils import AddTPMs
import os
from fmriprep.interfaces import DerivativesDataSink
from fmriprep.interfaces import GatherConfounds, AddTSVHeader
from utils import get_derivative


def main(sourcedata, 
         derivatives,
         tmp_dir,
         subject=None,
         session=None,

         run=None):

    layout = BIDSLayout(sourcedata)
    derivatives_layout = BIDSLayout('/derivatives')

    cortex_l = get_derivative(derivatives, 'nighres', 'anat', subject, 'dseg',
                              session='anat', space='average', description='cortex',
                              hemi='left')

    cortex_r = get_derivative(derivatives, 'nighres', 'anat', subject, 'dseg',
                              session='anat', space='average', description='cortex',
                              hemi='left')

    mask = derivatives_layout.get(subject=subject,
                                       session=session,
                                       suffix='mask',
                                       return_type='file')
    mask = sorted(mask)
    assert(len(mask) == 1)
    mask = mask[0]

    bold = derivatives_layout.get(subject=subject,
                                  session=session,
                                  suffix='preproc',
                                  return_type='file')
    bold = sorted(bold)
    print('BOLD: {}'.format(bold))
    print('MASK: {}'.format(mask))

    inputnode = pe.Node(niu.IdentityInterface(fields=['cortex_l',
                                                     'cortex_r',
                                                      'bold',
                                                      'mask']),
                        name='inputnode')


    inputnode.inputs.cortex_l = cortex_l
    inputnode.inputs.cortex_r = cortex_r
    inputnode.inputs.bold = bold
    inputnode.inputs.mask = mask

    get_masks = pe.MapNode(niu.Function(function=get_brain_regions_cruise,
                                   input_names=['cortex_l', 'cortex_r', 'type'],
                                   output_names=['out']),
                           iterfield=['type'],
                      name='get_masks')
    get_masks.inputs.type = ['csf', 'wm']


    wf = pe.Workflow(name='get_confounds',
                     base_dir='/workflow_folders')
    wf.connect(inputnode, 'cortex_l', get_masks, 'cortex_l')
    wf.connect(inputnode, 'cortex_r', get_masks, 'cortex_r')

    resampler = pe.MapNode(niu.Function(function=resample_img,
                                        input_names=['input_image',
                                                     'ref_image',
                                                     'interpolation'],
                                        output_names=['resampled_image'],
                                        ),
                           iterfield=['input_image'],
                           name='resampler')

    wf.connect(inputnode, ('bold', pickfirst), resampler, 'ref_image')
    wf.connect(get_masks, 'out', resampler, 'input_image')

    compcorr = pe.MapNode(ACompCor(merge_method='union'),
                          iterfield=['realigned_file'],
                          name='acompcorr')
    
    wf.connect(resampler, 'resampled_image', compcorr, 'mask_files')
    wf.connect(inputnode, 'bold', compcorr, 'realigned_file')


    dvars = pe.MapNode(ComputeDVARS(),
                       iterfield=['in_file'],
                       name='dvars')
    wf.connect(inputnode, 'mask', dvars, 'in_mask')
    wf.connect(inputnode, 'bold', dvars, 'in_file')

    add_header = pe.MapNode(AddTSVHeader(columns=["dvars"]),
                            iterfield=['in_file'],
                            name="add_header_dvars")
    wf.connect(dvars, 'out_std', add_header, 'in_file')

    concat = pe.MapNode(GatherConfounds(),
                     iterfield=['acompcor', 'dvars'],
                     name="concat")
    wf.connect(add_header, 'out_file', concat, 'dvars')
    wf.connect(compcorr, 'components_file', concat, 'acompcor')

    ds_confounds = pe.MapNode(DerivativesDataSink(out_path_base='spynoza',
                                                    suffix='confounds_compcor',
                                                    base_directory=derivatives),
                                iterfield=['in_file', 'source_file'],
                                name='ds_reg_report')

    wf.connect(inputnode, 'bold', ds_confounds, 'source_file')
    wf.connect(concat, 'confounds_file', ds_confounds, 'in_file')

    wf.run(plugin='MultiProc', 
           plugin_args={'n_procs' : 10})


def get_brain_regions_cruise(cortex_l, 
                             cortex_r,
                             type):

    from nilearn import image
    import os
    from nipype.utils.filemanip import split_filename
    from scipy import ndimage
    
    _, fn_l, _ = split_filename(cortex_l)
    _, fn_r, _ = split_filename(cortex_l)

    cortex_l = image.load_img(cortex_l)
    cortex_r = image.load_img(cortex_r)

    new_fn = os.path.abspath('{}.nii.gz'.format(fn_l)).replace('left_', '')

    if type == 'wm':
        wm = image.math_img('(cortex_l == 2) + (cortex_r == 2)', cortex_l=cortex_l, cortex_r=cortex_r)
        wm = image.new_img_like(wm, ndimage.binary_erosion(wm.get_data()))
        wm.to_filename(new_fn)

    elif type == 'csf':
        csf = image.math_img('(cortex_l + cortex_r) == 0', cortex_l=cortex_l, cortex_r=cortex_r)
        csf = image.new_img_like(csf, ndimage.binary_erosion(csf.get_data()))
        csf.to_filename(new_fn)

    return new_fn

def resample_img(input_image,
                 ref_image,
                 interpolation='nearest'):
    from nilearn import image
    import os
    from nipype.utils.filemanip import split_filename

    _, fn, ext = split_filename(input_image)

    new_img = image.resample_to_img(input_image,
                                    ref_image,
                                    interpolation=interpolation)

    new_fn = os.path.abspath('{}_resampled{}'.format(fn, ext))

    new_img.to_filename(new_fn)

    return new_fn


def get_bids_file(layout,
                  subject,
                  modality,
                  filter=None):

    img = layout.get(subject=subject,
                     type=modality,
                     return_type='file')

    if filter is not None:
        img = [im for im in img if filter in im]

    if len(img) == 0:
        raise Exception('Found no image for {}, {}'.format(modality, 
                                                           filter))
    if len(img) > 1:
        warnings.warn('Found more than one {}-image, using {}'.format(modality,
                                                                      img[0]))

    return img[0]


def get_bids_files(layout,
                  subject,
                  modality,
                  filter=None):

    img = layout.get(subject=subject,
                     type=modality,
                     return_type='file')

    if filter is not None:
        img = [im for im in img if filter in im]


    return img

def pickfirst(in_list):
    return in_list[0]

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("subject", 
                        #nargs='?',
                        type=str,
                        help="subject to process")
    parser.add_argument("session", 
                        type=str,
                        default='*',
                        help="subject to process")
    parser.add_argument("run", 
                        default=[], 
                        type=list,
                        nargs='*', 
                        help="runs to process")
    args = parser.parse_args()

    main('/sourcedata/ds-odc', 
         '/derivatives',
         subject=args.subject,
         session=args.session,
         run=args.run,
         tmp_dir='/workflow_folders')

