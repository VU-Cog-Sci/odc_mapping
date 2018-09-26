from spynoza.hires.workflows import init_hires_unwarping_wf
from bids.grabbids import BIDSLayout
import os
import argparse
import warnings


def main(sourcedata, 
         derivatives,
         tmp_dir,
         subject=None,
         session=None,
         run=None):

    if run is []:
        run = '[0-9]+'

    print('Processing subject {subject}, session {session}, run {run}'.format(**locals()))

    layout = BIDSLayout(sourcedata)
    derivatives_layout = BIDSLayout(derivatives)

    dtissue = derivatives_layout.get(subject=subject,
                                    type='dtissue',
                                    return_type='file')



    dura = derivatives_layout.get(subject=subject,
                                    type='dura',
                                    return_type='file')


    if len(dtissue) > 1:
        warnings.warn('Found more than one white-matter segmentation! {} '\
                      'Using {}'.format(dtissue, dtissue[0]))

    dtissue = dtissue[0]
    print(dtissue)
    dura = dura[0]

    get_wm_wf =  get_wm_seg_from_fmriprep_wf(dtissue)

    bold = layout.get(subject=subject,
                      session=session,
                      run=run,
                      type='bold', 
                      return_type='file')

    
    epi = []
    for b in bold:
        fmaps = layout.get_fieldmap(b, return_list=True)
        for fmap in fmaps:
            if fmap['type'] == 'epi':
                break
        epi.append(fmap['epi'])
        print('Using {} as epi_op for {}'.format(fmap['epi'], b))


    t1w = layout.get(subject=subject, type='T1w', return_type='file')[0]

    init_matrix = derivatives_layout.get(subject=subject,
                                         type='initmat',
                                         extensions='mat',
                                         return_type='file')

    if len(init_matrix) == 1:
        init_matrix = init_matrix[0]
    else:
        init_matrix = None
    print(init_matrix)

    wf = init_hires_unwarping_wf(name="unwarp_hires_{}_onefield".format(subject),
                              method='topup',
                              bids_layout=layout,
                              single_warpfield=True,
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
           plugin_args={'n_procs' : 12})

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
                        default='*',
                        help="subject to process")
    parser.add_argument("run", 
                        default=[], 
                        type=list,
                        nargs='*', 
                        help="runs to process")
    args = parser.parse_args()

    main('/sourcedata', 
         '/derivatives',
         subject=args.subject,
         session=args.session,
         run=args.run,
         tmp_dir='/workflow_folders')

