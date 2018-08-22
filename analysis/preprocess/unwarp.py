from spynoza.hires.workflows import init_hires_unwarping_wf
from bids.grabbids import BIDSLayout
import os


def main(sourcedata, 
         derivatives,
         tmp_dir):

    layout = BIDSLayout(sourcedata)

    bold = layout.get(run=2,type='bold', return_type='file' )
    epi = layout.get(run=2,type='epi', extensions='nii', return_type='file' )

    t1w = layout.get(type='T1w', return_type='file')[0]

    init_matrix = os.path.join(derivatives,
                               'matrices',
                               'sub-tk',
                               'sub-tk_session-odc1_run-02_to_acq-avg_T1w.h5')

    print(bold, epi, t1w)


    wf = init_hires_unwarping_wf(name="unwarp_hires",
                              method='topup',
                              bids_layout=layout,
                              single_warpfield=False,
                              register_to='last',
                              init_reg_file=init_matrix,
                              linear_registration_parameters='linear_hires.json',
                              nonlinear_registration_parameters='nonlinear_precise.json',
                              bold_epi=bold,
                              epi_op=epi,
                              t1w_epi=None,
                              t1w=t1w,
                              inv2_epi=None,
                              crop_bold_epis=True,
                              topup_package='afni',
                              within_epi_reg=True,
                              polish=True,
                              num_threads_ants=4)

    wf.base_dir = tmp_dir


    wf.run(plugin='MultiProc', 
           plugin_args={'n_procs' : 10})



if __name__ == '__main__':

    bids_dir = '/home/raw_data/2018/visual/7T_BR/ODC'

    sourcedata  = os.path.join(bids_dir, 'sourcedata')
    derivatives = '/home/shared/2018/visual/7T_BR/ODC/derivatives'

    main(sourcedata, 
         derivatives,
         tmp_dir='/tmp/workflow_folders')

