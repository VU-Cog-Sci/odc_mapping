from bids import BIDSLayout
import nipype.pipeline.engine as pe
from spynoza.motion_correction.workflows import create_motion_correction_workflow
import argparse
from fmriprep.interfaces import DerivativesDataSink
from nipype.interfaces import fsl, ants
import nipype.interfaces.utility as niu

def pickfirst(input):
    return input[0]

def main(sourcedata,
         derivatives,
         subject,
         session,
         run,
         wf_dir):

    layout = BIDSLayout(sourcedata)

    bolds = layout.get(subject=subject,
                       session=session,
                       run=run,
                       suffix='bold',
                       return_type='file')

    
    bold = bolds 
    for bold in bolds:
        print('Making reference image of {}'.format(bold))

    inputnode = pe.Node(niu.IdentityInterface(fields=['bold']),
                        name='inputnode')
    inputnode.inputs.bold = bolds

    wf = pe.Workflow(name='make_ref_{}_{}_{}'.format(subject,
                                                     session,
                                                     run))

    wf.base_dir = wf_dir

    mc_wf_bold = create_motion_correction_workflow(name='mc_wf_bold',
                                                   method='FSL',
                                                   lightweight=True)

                                              

    wf.connect(inputnode, 'bold', mc_wf_bold, 'inputspec.in_files')
    wf.connect(inputnode, ('bold', pickfirst), mc_wf_bold, 'inputspec.which_file_is_EPI_space')

    mean_bold = pe.MapNode(fsl.MeanImage(dimension='T'), 
                                 iterfield=['in_file'],
                                 name='mean_bold1')

    n4_correct = pe.MapNode(ants.N4BiasFieldCorrection(), 
                            iterfield=['input_image'],
                            name='n4_correct')
    wf.connect(mean_bold, 'out_file', n4_correct, 'input_image')
    
    ds = pe.MapNode(DerivativesDataSink(out_path_base='simple_bold_ref',
                                        suffix='reference',
                                        base_directory=derivatives),
                                iterfield=['in_file', 'source_file'],
                                name='ds_reg_report')
    
    wf.connect(mc_wf_bold, 'outputspec.motion_corrected_files', mean_bold, 'in_file')
    wf.connect(n4_correct, 'output_image', ds, 'in_file')
    wf.connect(inputnode, 'bold', ds, 'source_file')
    

    wf.run()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("subject", 
                        help="subject to process")
    parser.add_argument("session", 
                        default='*',
                        nargs='?',
                        help="Session to process")
    parser.add_argument("run", 
                        default='1',
                        nargs='?',
                        help="Session to process")
    args = parser.parse_args()

    main('/sourcedata/ds-odc', 
         '/derivatives',
         subject=args.subject,
         session=args.session,
         run=args.run,
         wf_dir='/workflow_folders')

