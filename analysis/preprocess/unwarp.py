from spynoza.hires.workflows import init_hires_unwarping_wf
#from bids.grabbids import BIDSLayout
from bids import BIDSLayout
import os
import argparse
import warnings
import re

def get_dura_mask(derivatives,
                  subject,
                  space='average',
                  session=None):

    dura_folder = os.path.join(derivatives, 'masked_mp2rages')
    
    session_str = '_ses-{}'.format(session) if session else ''
    session_folder = 'ses-{}/'.format(session) if session else ''
    space_str = '_space-{}'.format(space) if session else ''

    str = 'sub-{subject}/{session_folder}anat/sub-{subject}{session_str}{space_str}_desc-dura_mask.nii.gz'.format(**locals())

    return os.path.join(dura_folder, str)

def get_averaged_image(derivatives,
                       subject,
                       space='average',
                       suffix='T1w',
                       session=None):

    folder = os.path.join(derivatives, 'averaged_mp2rages')
    
    session_str = '_ses-{}'.format(session) if session else ''
    session_folder = 'ses-{}/'.format(session) if session else ''
    space_str = '_space-{}'.format(space) if session else ''

    str = 'sub-{subject}/{session_folder}anat/sub-{subject}{session_str}{space_str}_{suffix}.nii.gz'.format(**locals())

    return os.path.join(folder, str)

def get_derivative(derivatives_folder,
                   type,
                   modality,
                   subject,
                   suffix,
                   session=None,
                   space=None,
                   acquisition=None,
                   desc=None,
                   extension='nii.gz'):

    folder = os.path.join(derivatives_folder, type)
    
    session_str = '_ses-{}'.format(session) if session else ''
    session_folder = 'ses-{}/'.format(session) if session else ''
    space_str = '_space-{}'.format(space) if space else ''
    desc_str = '_desc-{}'.format(desc) if desc else ''
    acquisition_str = '_acq-{}'.format(acquisition) if acquisition else ''

    str = 'sub-{subject}/{session_folder}{modality}/sub-{subject}{session_str}{acquisition_str}{space_str}{desc_str}_{suffix}.{extension}'.format(**locals())

    return os.path.join(folder, str)

def main(sourcedata, 
         derivatives,
         tmp_dir,
         subject=None,
         acquisition=None,
         session=None,
         run=None):

    if run is []:
        run = '[0-9]+'

    layout = BIDSLayout(sourcedata)
    derivatives_layout = BIDSLayout(derivatives)

    dtissue = get_derivative(derivatives,
                          'fmriprep',
                          'anat',
                          subject,
                          'dseg',
                          session='anat')


    dura = get_dura_mask(derivatives,
                         subject,
                         'average',
                         'anat')


    print(dura, os.path.exists(dura))

    get_wm_wf =  get_wm_seg_from_fmriprep_wf(dtissue)

    bold = []

    for acq in acquisition:
        bold += (layout.get(subject=subject,
                          session=session,
                          run=run,
                          acquisition=acq,
                          suffix='bold', 
                          return_type='file'))


    epi = []
    for b in bold:
        fmaps = layout.get_fieldmap(b, return_list=True)
        for fmap in fmaps:
            if ('type' not in fmap) or (fmap['type'] == 'epi'):
                break
        epi.append(fmap['epi'])
        print('Using {} as epi_op for {}'.format(fmap['epi'], b))


    t1w = get_derivative(derivatives,
                         'masked_mp2rages',
                         'anat',
                         subject,
                         'T1w',
                         session='anat',
                         space='average',
                         desc='masked_no_dura_no_ss',
                         extension='nii.gz')

    print(t1w, os.path.exists(t1w))

    init_matrix = get_derivative(derivatives,
                                  'manual_transformations',
                                 'func',
                                  subject,
                                  'transform',
                                  session=session,
                                  space='average',
                                  extension='mat')


    wf = init_hires_unwarping_wf(name="unwarp_hires_{}".format(subject),
                              method='topup',
                              bids_layout=layout,
                              single_warpfield=False,
                              register_to='last',
                              init_transform=init_matrix,
                              linear_registration_parameters='linear_hires.json',
                              nonlinear_registration_parameters='nonlinear_precise.json',
                              bold=bold,
                              epi_op=epi,
                              t1w_epi=None,
                              t1w=t1w,
                              dura_mask=dura,
                              wm_seg=True,
                              inv2_epi=None,
                              dof=6,
                              crop_bolds=True,
                              topup_package='afni',
                              epi_to_t1_package='fsl',
                              within_epi_reg=True,
                              polish=True,
                              num_threads_ants=4)

    wf.connect(get_wm_wf, 'outputspec.wm_seg', wf.get_node('inputspec'), 'wm_seg')
    wf.base_dir = tmp_dir

    wf.run(plugin='MultiProc', 
           plugin_args={'n_procs' : 6})

def get_wm_seg_from_fmriprep_wf(dtissue):
    from nipype.interfaces import fsl
    import nipype.interfaces.utility as util
    import nipype.pipeline.engine as pe

    wf = pe.Workflow(name='get_wm_seg')

    inputspec = pe.Node(util.IdentityInterface(fields=['fmriprep_dtissue']),
                        name='inputspec')

    inputspec.inputs.fmriprep_dtissue = dtissue

    get_wm = pe.Node(fsl.Threshold(thresh=3,
                               args='-bin'),
                     name='get_wm')

    outputspec= pe.Node(util.IdentityInterface(fields=['wm_seg']), 
                                                       name='outputspec')

    wf.connect(inputspec, 'fmriprep_dtissue', get_wm, 'in_file')
    wf.connect(get_wm, 'out_file', outputspec, 'wm_seg')

    return wf

    

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("subject", 
                        #nargs='?',
                        type=str,
                        help="subject to process")
    parser.add_argument("session", 
                        type=str,
                        nargs='?',
                        default='.*',
                        help="subject to process")
    parser.add_argument("acquisition", 
                        type=str,
                        nargs='*',
                        default='.*',
                        help="subject to process")
    parser.add_argument("run", 
                        default='.*', 
                        type=list,
                        nargs='*', 
                        help="runs to process")
    args = parser.parse_args()

    main('/sourcedata/ds-odc', 
         '/derivatives',
         subject=args.subject,
         session=args.session,
         acquisition=args.acquisition,
         run=args.run,
         tmp_dir='/workflow_folders')

