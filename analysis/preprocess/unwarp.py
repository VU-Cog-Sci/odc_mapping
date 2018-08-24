from spynoza.hires.workflows import init_hires_unwarping_wf
from bids.grabbids import BIDSLayout
import os
import argparse


def main(sourcedata, 
         derivatives,
         tmp_dir,
         subject=None,
         run=None):

    if run is []:
        run = '[0-9]+'

    layout = BIDSLayout(sourcedata)
    derivatives_layout = BIDSLayout(derivatives)

    bold = layout.get(subject=subject,
                      run=run,
                      type='bold', 
                      return_type='file')

    epi = layout.get(subject=subject,
                     run=run,
                     type='epi',
                     extensions='nii',
                     return_type='file')

    t1w = layout.get(type='T1w', return_type='file')[0]

    init_matrix = derivatives_layout.get(subject=subject,
                                         type='initmat',
                                         extensions='mat',
                                         return_type='file')

    if len(init_matrix) == 1:
        init_matrix = init_matrix[0]
    else:
        init_matrix = None
    print(init_matrix)

    wf = init_hires_unwarping_wf(name="unwarp_hires_{}".format(subject),
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
                              epi_to_t1_package='fsl',
                              within_epi_reg=True,
                              polish=True,
                              num_threads_ants=4)

    wf.base_dir = tmp_dir

    wf.run(plugin='MultiProc', 
           plugin_args={'n_procs' : 10})



if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("subject", 
                        help="subject to process")
    parser.add_argument("run", 
                        default=[], 
                        nargs='*', 
                        help="runs to process")
    args = parser.parse_args()

    main('/sourcedata', 
         '/derivatives',
         subject=args.subject,
         run=args.run,
         tmp_dir='/workflow_folders')

