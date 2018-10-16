from spynoza.motion_correction.workflows import create_motion_correction_workflow
import nipype.pipeline.engine as pe
from fmriprep.interfaces import DerivativesDataSink
from spynoza.utils import pickfirst
import nipype.interfaces.utility as niu
from bids.grabbids import BIDSLayout

def select_range(in_list, i):
    return in_list[i:i+1]

subject = 'tk'
session = 'odc2'
derivatives = '/derivatives'
sourcedata = '/sourcedata'

layout = BIDSLayout(sourcedata)
derivatives_layout = BIDSLayout(derivatives)

bold = layout.get(subject=subject,
                  session=session,
                  run='[0-9]+',
                  type='bold', 
                  return_type='file')

inputnode = pe.Node(niu.IdentityInterface(fields='bold'),
                    name='inputnode')

inputnode.inputs.bold = bold

wf = pe.Workflow(name='test_mcflirt_mutualinfo', base_dir='/workflow_folders')

merge_hmc_pars = pe.Node(niu.Merge(len(bold)),
                         name='merge_hmc_pars')

for i, b in enumerate(bold):
    mcw = create_motion_correction_workflow(name='moco_{}'.format(i+1),
                                            method='FSL', lightweight=True)
    mcw.inputs.motion_correct_all.cost = 'mutualinfo'
    mcw.inputs.inputspec.which_file_is_EPI_space = 'first'

    source_file = '/sourcedata/sub-tk/ses-odc2/func/sub-tk_ses-odc2_task-checkerboard_acq-07_run-02_bold.nii'

    wf.connect(inputnode, ('bold', select_range, i), mcw, 'inputspec.in_files')
    mcw.inputs.motion_correct_EPI_space.cost = 'mutualinfo'
    mcw.inputs.motion_correct_all.cost = 'mutualinfo'

    wf.connect(mcw, 'outputspec.hmc_confounds', merge_hmc_pars, 'in{}'.format(i+1))

ds_params = pe.MapNode(DerivativesDataSink(out_path_base='analysis_experiments',
                                        suffix='hmc_confounds',
                                        base_directory='/derivatives'),
                       iterfield=['in_file', 'source_file'],
                        name='ds_pars')

wf.connect(inputnode, 'bold', ds_params, 'source_file')
wf.connect(merge_hmc_pars, 'out', ds_params, 'in_file')

wf.run(plugin='MultiProc', 
       plugin_args={'n_procs' : 10})


