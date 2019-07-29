import argparse
from bids import BIDSLayout
import os.path as op
import nipype.pipeline.engine as pe
import nipype.interfaces.utility as niu
from nipype.algorithms.confounds import TSNR
from niworkflows.interfaces.bids import DerivativesDataSink
from nipype.interfaces import fsl

derivatives = '/derivatives'
workflow_dirs = '/tmp/workflow_folders'

parser = argparse.ArgumentParser()
parser.add_argument("subject", 
                    #nargs='?',
                    type=str,
                    help="subject to process")
parser.add_argument("session", 
                    type=str,
                    default='*',
                    help="subject to process")



args = parser.parse_args()
subject = args.subject
session = args.session

layout = BIDSLayout(op.join(derivatives, 'spynoza'),
                    absolute_paths=True,
                    validate=False)

preproc = layout.get(subject=subject,
                     session=session,
                     return_type='file',
                     suffix='preproc')

reference = layout.get(subject=subject,
                     session=session,
                     return_type='file',
                     suffix='reference')


wf = pe.Workflow(base_dir=workflow_dirs,
                 name='tsnr_{}_{}'.format(subject, session))

inputnode = pe.Node(niu.IdentityInterface(fields=['preproc', 'reference']),
                    name='inputnode')

inputnode.inputs.preproc = preproc
inputnode.inputs.reference = reference

adder = pe.MapNode(fsl.ImageMaths(op_string='-add'),
                iterfield=['in_file', 'in_file2'],
                name='adder')
wf.connect(inputnode, 'preproc', adder, 'in_file')
wf.connect(inputnode, 'reference', adder, 'in_file2')

tsnr = pe.MapNode(TSNR(),
                  iterfield=['in_file'],
                  name='tsnr')

wf.connect(adder, 'out_file', tsnr, 'in_file')

def invert(in_file):
    from nilearn import image
    from nipype.utils.filemanip import split_filename
    import os.path as op
    _, fn, ext = split_filename(in_file)

    inverse = image.math_img('1 / tsnr', tsnr=in_file)

    new_fn = op.abspath('{}_inverse{}'.format(fn, ext))
    inverse.to_filename(new_fn)

    return new_fn

invert_tsnr = pe.MapNode(niu.Function(function=invert,
                                   input_names=['in_file'],
                                   output_names=['out_file']),
                         iterfield=['in_file'],
                         name='invert_tsnr')
wf.connect(tsnr, 'tsnr_file', invert_tsnr, 'in_file')

ds_tsnr = pe.MapNode(DerivativesDataSink(base_directory=derivatives,
                                 suffix='tsnr',
                                 out_path_base='tsnr'),
             iterfield=['in_file', 'source_file'],
             name='datasink_tsnr')

wf.connect(inputnode, 'preproc', ds_tsnr, 'source_file')
wf.connect(tsnr, 'tsnr_file', ds_tsnr, 'in_file')

ds_std = pe.MapNode(DerivativesDataSink(base_directory=derivatives,
                                 suffix='stddev',
                                 out_path_base='tsnr'),
             iterfield=['in_file', 'source_file'],
             name='datasink_std')

wf.connect(inputnode, 'preproc', ds_std, 'source_file')
wf.connect(tsnr, 'tsnr_file', ds_std, 'in_file')

ds_invtsnr = pe.MapNode(DerivativesDataSink(base_directory=derivatives,
                                 suffix='invtsnr',
                                 out_path_base='tsnr'),
             iterfield=['in_file', 'source_file'],
             name='datasink_invtsnr')

wf.connect(inputnode, 'preproc', ds_invtsnr, 'source_file')
wf.connect(invert_tsnr, 'out_file', ds_invtsnr, 'in_file')

wf.run(plugin='MultiProc',
       plugin_args={'n_procs':4})

