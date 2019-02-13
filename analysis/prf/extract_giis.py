import argparse
from utils import get_derivative
from nipype.interfaces import freesurfer as fs
from fmriprep.interfaces import DerivativesDataSink
import nipype.pipeline.engine as pe
import nipype.interfaces.utility as niu
import os

def main(derivatives,
         subject,
         session,
         task,
         acquisition,
         run,
         workflow_folder='/tmp/workflow_folders'):

    os.environ['SUBJECTS_DIR'] = os.path.join(derivatives, 'freesurfer')

    preproc_bold = get_derivative(derivatives,
                                    'spynoza',
                                    'func',
                                    subject=subject,
                                    session=session,
                                    suffix='preproc',
                                    acquisition=acquisition,
                                    run=run,
                                    task=task
                                    )

    registration = get_derivative(derivatives,
                                  'manual_registrations',
                                  'func',
                                  subject=subject,
                                  session=session,
                                  description='spynoza2t1w',
                                  suffix='transform',
                                  extension='lta',
                                  check_exists=False)


    wf = pe.Workflow(name='sample_fs',
                     base_dir=workflow_folder)

    inputnode = pe.Node(niu.IdentityInterface(fields=['preproc_bold', 'registration' 'subject']), name='inputnode')
    inputnode.inputs.preproc_bold = preproc_bold
    inputnode.inputs.subject = 'sub-{}'.format(subject)
    inputnode.inputs.registration = registration

    sampler = pe.Node(fs.SampleToSurface(sampling_method='average', sampling_range=(0, 1, 0.2),
                                         sampling_units='frac', interp_method='trilinear', cortex_mask=True,
                                         subjects_dir=os.path.join(derivatives,'freesurfer'),
                                         override_reg_subj=True,
                                         out_type='gii'),
                      iterables=('hemi', ['lh', 'rh']),
                      name='sampler')

    wf.connect(inputnode, 'preproc_bold', sampler, 'source_file')
    if registration is not None:
        wf.connect(inputnode, 'registration', sampler, 'reg_file')
    else:
        sampler.inputs.reg_header = True
    wf.connect(inputnode, 'subject', sampler, 'subject_id')

    merger = pe.JoinNode(niu.Merge(1, ravel_inputs=True), name='merger',
                                  joinsource='sampler', joinfield=['in1'])
    wf.connect(sampler, 'out_file', merger, 'in1')

    ds = pe.MapNode(DerivativesDataSink(base_directory=derivatives,
                                        out_path_base='sampled_giis',
                                        ),
                    iterfield=['in_file', 'suffix'],
                 name='datasink')

    ds.inputs.suffix = ['bold.lh', 'bold.rh']

    wf.connect(merger, 'out', ds, 'in_file')
    wf.connect(inputnode, 'preproc_bold', ds, 'source_file')


    wf.run()



if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("subject", 
                        #nargs='?',
                        type=str,
                        help="subject to process")
    parser.add_argument("session", 
                        type=str,
                        nargs='?',
                        default='prf',
                        help="subject to process")
    parser.add_argument("task", 
                        type=str,
                        nargs='?',
                        default='prf',
                        help="task to process")
    parser.add_argument("acquisition", 
                        type=str,
                        nargs='?',
                        default='.*',
                        help="Acquisition to process")
    parser.add_argument("run", 
                        type=str,
                        nargs='?',
                        default='.*',
                        help="Run to process")
    args = parser.parse_args()

    main('/derivatives',
         subject=args.subject,
         session=args.session,
         acquisition=args.acquisition,
         run=args.run,
         task=args.task)
         

