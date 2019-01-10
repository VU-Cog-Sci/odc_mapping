import argparse
from utils import get_derivative
from nipype.interfaces import freesurfer as fs
from fmriprep.interfaces import DerivativesDataSink
import nipype.pipeline.engine as pe
import nipype.interfaces.utility as util
import os

def main(derivatives,
         subject,
         session,
         task,
         acquisition,
         run,
         workflow_folder='/tmp/workflow_folders'):

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
                                  extension='lta')


    wf = pe.Workflow(name='sample_fs',
                     base_dir=workflow_folder)

    inputnode = pe.Node(util.IdentityInterface('preproc_bold',
                                               'registration'
                                               'subject'),
                        name='inputnode')
    inputnode.inputs.preproc_bold = preproc_bold
    inputnode.inputs.subject = subject
    inputnode.inputs.registration = registration

    sampler = pe.Node(fs.SampleToSurface(sampling_method='average', sampling_range=(0, 1, 0.2),
                                         sampling_units='frac', interp_method='trilinear', cortex_mask=True,
                                         subjects_dir=os.path.join(derivatives,'freesurfer'),
                                         out_type='gii'),
                      iterables=('hemi', ['lh', 'rh']),
                      name='sampler')
    wf.connect(inputnode, 'preproc_bold', sampler, 'source_file')
    wf.connect(inputnode, 'registration', sampler, 'reg_file')


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

    main('/data/odc/derivatives',
         subject=args.subject,
         session=args.session,
         acquisition=args.acquisition,
         run=args.run,
         task=args.task)
         

