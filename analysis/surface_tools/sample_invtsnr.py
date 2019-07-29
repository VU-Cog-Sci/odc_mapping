import argparse
from utils import get_derivative
import nipype.pipeline.engine as pe
import nipype.interfaces.freesurfer as fs
import nipype.interfaces.utility as niu
import os
import os.path as op
import numpy as np
from niworkflows.interfaces.bids import DerivativesDataSink


def main(derivatives,
         subject,
         session,
         workflow_folder,
         n_procs=8):

    fn = get_derivative(derivatives,
                        'tsnr',
                        'func',
                        subject=subject,
                        session=session,
                        run='*',
                        acquisition='*',
                        task='*',
                        suffix='invtsnr')

    os.environ['SUBJECTS_DIR'] = op.join(derivatives, 'freesurfer')

    wf = pe.Workflow(name='sample_fs_invtsnt_{}_{}'.format(subject, session),
                     base_dir=workflow_folder)

    input_node = pe.Node(niu.IdentityInterface(fields=['source_file']),
                        name='input_node')
    input_node.inputs.source_file = fn

    config_node = pe.Node(niu.IdentityInterface(fields=['depth',
                                                     'hemisphere']),
                       name='config_node')
    config_node.iterables = [('depth', np.arange(1, 7)),
                          ('hemisphere', ['lh', 'rh'])]


    def get_surf_name(depth, n_surfs=8):
        return 'equi{}.pial'.format(str(float(depth)/(n_surfs-1)))

    sampler = pe.MapNode(fs.SampleToSurface(subjects_dir=os.path.join(derivatives,'freesurfer'),
                                            override_reg_subj=True,
                                            reg_header=True,
                                            subject_id='sub-{}'.format(subject),
                                            interp_method='trilinear',
                                            projection_stem='',
                                         out_type='gii'),
                         iterfield=['source_file'],
                         name='sampler')

    wf.connect(input_node, 'source_file', sampler, 'source_file')
    wf.connect(config_node, ('depth', get_surf_name), sampler, 'surface')
    wf.connect(config_node, 'hemisphere', sampler, 'hemi')

    def get_desc(depth, n_surfs=8):
        return 'depth.{:.03f}'.format(float(depth)/(n_surfs-1))

    def get_extra_values(hemi):
        return ['hemi-{}'.format(hemi)]

    ds = pe.MapNode(DerivativesDataSink(base_directory=derivatives,
                                        out_path_base='tsnr',
                                        ),
                    iterfield=['in_file', 'source_file'],
                 name='datasink')

    wf.connect(input_node, 'source_file', ds, 'source_file')
    wf.connect(sampler, 'out_file', ds, 'in_file')
    wf.connect(config_node, ('depth', get_desc), ds, 'desc')
    wf.connect(config_node, ('hemisphere', get_extra_values), ds, 'extra_values')

    wf.run(plugin='MultiProc',
           plugin_args={'n_procs':n_procs})


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("subject", 
                        type=str,
                        help="subject to process")
    parser.add_argument("session", 
                        type=str,
                        nargs='?',
                        default='prf',
                        help="subject to process")
    args = parser.parse_args()

    main('/derivatives',
         subject=args.subject,
         session=args.session,
         workflow_folder='/workflow_folders',)
         



