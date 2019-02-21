Node: bbregister_N (freesurfer)
===============================


 Hierarchy : reg_test.bbregister_N
 Exec ID : bbregister_N


Original Inputs
---------------


* args : <undefined>
* contrast_type : bold
* dof : <undefined>
* environ : {'SUBJECTS_DIR': '/derivatives/freesurfer/'}
* epi_mask : <undefined>
* fsldof : <undefined>
* init : <undefined>
* init_cost_file : <undefined>
* init_reg_file : <undefined>
* intermediate_file : <undefined>
* out_fsl_file : True
* out_lta_file : <undefined>
* out_reg_file : <undefined>
* reg_frame : <undefined>
* reg_middle_frame : <undefined>
* registered_file : <undefined>
* source_file : /workflow_folders/unwarp_hires_bm/unwarp_reg_wf_0/mean_bold2/sub-bm_ses-odc_task-checkerboard_acq-07_run-03_bold_mcf_roi_mean_av.nii.gz
* spm_nifti : <undefined>
* subject_id : sub-bm
* subjects_dir : /derivatives/freesurfer

Execution Inputs
----------------


* args : <undefined>
* contrast_type : bold
* dof : <undefined>
* environ : {'SUBJECTS_DIR': '/derivatives/freesurfer'}
* epi_mask : <undefined>
* fsldof : <undefined>
* init : <undefined>
* init_cost_file : <undefined>
* init_reg_file : <undefined>
* intermediate_file : <undefined>
* out_fsl_file : True
* out_lta_file : <undefined>
* out_reg_file : <undefined>
* reg_frame : <undefined>
* reg_middle_frame : <undefined>
* registered_file : <undefined>
* source_file : /workflow_folders/reg_test/bbregister_N/sub-bm_ses-odc_task-checkerboard_acq-07_run-03_bold_mcf_roi_mean_av.nii.gz
* spm_nifti : <undefined>
* subject_id : sub-bm
* subjects_dir : /derivatives/freesurfer


Execution Outputs
-----------------


* init_cost_file : <undefined>
* min_cost_file : <undefined>
* out_fsl_file : /workflow_folders/reg_test/bbregister_N/sub-bm_ses-odc_task-checkerboard_acq-07_run-03_bold_mcf_roi_mean_av_bbreg_sub-bm.mat
* out_lta_file : <undefined>
* out_reg_file : /workflow_folders/reg_test/bbregister_N/sub-bm_ses-odc_task-checkerboard_acq-07_run-03_bold_mcf_roi_mean_av_bbreg_sub-bm.dat
* registered_file : <undefined>


Runtime info
------------


* command : bbregister --bold --fslmat /workflow_folders/reg_test/bbregister_N/sub-bm_ses-odc_task-checkerboard_acq-07_run-03_bold_mcf_roi_mean_av_bbreg_sub-bm.mat --reg /workflow_folders/reg_test/bbregister_N/sub-bm_ses-odc_task-checkerboard_acq-07_run-03_bold_mcf_roi_mean_av_bbreg_sub-bm.dat --mov /workflow_folders/reg_test/bbregister_N/sub-bm_ses-odc_task-checkerboard_acq-07_run-03_bold_mcf_roi_mean_av.nii.gz --s sub-bm
* duration : 213.747391
* hostname : 9958f5fd3ba7
* prev_wd : /src
* working_dir : /workflow_folders/reg_test/bbregister_N


Terminal output
~~~~~~~~~~~~~~~


 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 3
 4
 .
 6
 2
 8
 9
 7
 9
 :
 t
 m
 p
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 3
 4
 .
 6
 2
 9
 4
 8
 4
 :
 L
 o
 g
  
 f
 i
 l
 e
  
 i
 s
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 _
 b
 b
 r
 e
 g
 _
 s
 u
 b
 -
 b
 m
 .
 d
 a
 t
 .
 l
 o
 g
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 3
 4
 .
 6
 3
 2
 0
 9
 8
 :
 T
 u
 e
  
 D
 e
 c
  
 1
 1
  
 1
 5
 :
 3
 3
 :
 3
 4
  
 U
 T
 C
  
 2
 0
 1
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 3
 4
 .
 6
 3
 4
 9
 6
 8
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 3
 4
 .
 6
 3
 7
 9
 6
 9
 :
 s
 e
 t
 e
 n
 v
  
 S
 U
 B
 J
 E
 C
 T
 S
 _
 D
 I
 R
  
 /
 d
 e
 r
 i
 v
 a
 t
 i
 v
 e
 s
 /
 f
 r
 e
 e
 s
 u
 r
 f
 e
 r
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 3
 4
 .
 6
 4
 2
 0
 2
 0
 :
 c
 d
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 3
 4
 .
 6
 4
 4
 7
 1
 1
 :
 /
 o
 p
 t
 /
 f
 r
 e
 e
 s
 u
 r
 f
 e
 r
 -
 6
 .
 0
 .
 1
 /
 b
 i
 n
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
  
 -
 -
 b
 o
 l
 d
  
 -
 -
 f
 s
 l
 m
 a
 t
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 _
 b
 b
 r
 e
 g
 _
 s
 u
 b
 -
 b
 m
 .
 m
 a
 t
  
 -
 -
 r
 e
 g
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 _
 b
 b
 r
 e
 g
 _
 s
 u
 b
 -
 b
 m
 .
 d
 a
 t
  
 -
 -
 m
 o
 v
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 .
 n
 i
 i
 .
 g
 z
  
 -
 -
 s
  
 s
 u
 b
 -
 b
 m
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 3
 4
 .
 6
 4
 7
 4
 2
 0
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 3
 4
 .
 6
 5
 0
 1
 3
 2
 :
 $
 I
 d
 :
  
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 ,
 v
  
 1
 .
 7
 5
  
 2
 0
 1
 6
 /
 0
 5
 /
 1
 0
  
 2
 0
 :
 0
 2
 :
 2
 8
  
 g
 r
 e
 v
 e
  
 E
 x
 p
  
 $
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 3
 4
 .
 6
 5
 2
 7
 4
 3
 :
 L
 i
 n
 u
 x
  
 9
 9
 5
 8
 f
 5
 f
 d
 3
 b
 a
 7
  
 3
 .
 1
 0
 .
 0
 -
 6
 9
 3
 .
 1
 7
 .
 1
 .
 e
 l
 7
 .
 x
 8
 6
 _
 6
 4
  
 #
 1
  
 S
 M
 P
  
 T
 h
 u
  
 J
 a
 n
  
 2
 5
  
 2
 0
 :
 1
 3
 :
 5
 8
  
 U
 T
 C
  
 2
 0
 1
 8
  
 x
 8
 6
 _
 6
 4
  
 G
 N
 U
 /
 L
 i
 n
 u
 x
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 3
 4
 .
 6
 5
 5
 3
 9
 5
 :
 F
 R
 E
 E
 S
 U
 R
 F
 E
 R
 _
 H
 O
 M
 E
  
 /
 o
 p
 t
 /
 f
 r
 e
 e
 s
 u
 r
 f
 e
 r
 -
 6
 .
 0
 .
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 3
 4
 .
 6
 5
 8
 8
 4
 2
 :
 m
 r
 i
 _
 c
 o
 n
 v
 e
 r
 t
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 .
 n
 i
 i
 .
 g
 z
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 t
 e
 m
 p
 l
 a
 t
 e
 .
 n
 i
 i
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 3
 4
 .
 6
 8
 3
 4
 1
 9
 :
 m
 r
 i
 _
 c
 o
 n
 v
 e
 r
 t
 .
 b
 i
 n
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 .
 n
 i
 i
 .
 g
 z
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 t
 e
 m
 p
 l
 a
 t
 e
 .
 n
 i
 i
  
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 3
 4
 .
 8
 1
 0
 2
 0
 4
 :
 $
 I
 d
 :
  
 m
 r
 i
 _
 c
 o
 n
 v
 e
 r
 t
 .
 c
 ,
 v
  
 1
 .
 2
 2
 6
  
 2
 0
 1
 6
 /
 0
 2
 /
 2
 6
  
 1
 6
 :
 1
 5
 :
 2
 4
  
 m
 r
 e
 u
 t
 e
 r
  
 E
 x
 p
  
 $
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 3
 4
 .
 8
 1
 0
 2
 0
 4
 :
 T
 R
 =
 4
 0
 0
 0
 .
 0
 0
 ,
  
 T
 E
 =
 0
 .
 0
 0
 ,
  
 T
 I
 =
 0
 .
 0
 0
 ,
  
 f
 l
 i
 p
  
 a
 n
 g
 l
 e
 =
 0
 .
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 3
 4
 .
 8
 1
 0
 2
 0
 4
 :
 i
 _
 r
 a
 s
  
 =
  
 (
 -
 1
 ,
  
 0
 ,
  
 0
 )
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 3
 4
 .
 8
 1
 0
 2
 0
 4
 :
 j
 _
 r
 a
 s
  
 =
  
 (
 0
 ,
  
 0
 .
 9
 9
 9
 9
 8
 6
 ,
  
 0
 .
 0
 0
 5
 3
 4
 0
 6
 8
 )
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 3
 4
 .
 8
 1
 0
 2
 0
 4
 :
 k
 _
 r
 a
 s
  
 =
  
 (
 0
 ,
  
 -
 0
 .
 0
 0
 5
 3
 4
 0
 6
 8
 ,
  
 0
 .
 9
 9
 9
 9
 8
 6
 )
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 3
 4
 .
 8
 1
 0
 2
 0
 4
 :
 r
 e
 a
 d
 i
 n
 g
  
 f
 r
 o
 m
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 .
 n
 i
 i
 .
 g
 z
 .
 .
 .
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 3
 4
 .
 8
 1
 0
 2
 0
 4
 :
 w
 r
 i
 t
 i
 n
 g
  
 t
 o
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 t
 e
 m
 p
 l
 a
 t
 e
 .
 n
 i
 i
 .
 .
 .
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 3
 4
 .
 8
 1
 5
 9
 9
 5
 :
 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 -
 -
 s
  
 s
 u
 b
 -
 b
 m
  
 -
 -
 m
 o
 v
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 t
 e
 m
 p
 l
 a
 t
 e
 .
 n
 i
 i
  
 -
 -
 r
 e
 g
 d
 a
 t
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 r
 e
 g
 .
 i
 n
 i
 t
 .
 d
 a
 t
  
 -
 -
 r
 e
 g
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 m
 r
 i
 _
 c
 o
 r
 e
 g
 .
 l
 t
 a
  
 -
 -
 n
 t
 h
 r
 e
 a
 d
 s
  
 1
  
 -
 -
 d
 o
 f
  
 6
  
 -
 -
 s
 e
 p
  
 4
  
 -
 -
 f
 t
 o
 l
  
 .
 0
 0
 0
 1
  
 -
 -
 l
 i
 n
 m
 i
 n
 t
 o
 l
  
 .
 0
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 6
 .
 5
 1
 2
 0
 7
 0
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 6
 .
 5
 1
 2
 0
 7
 0
 :
 $
 I
 d
 :
  
 m
 r
 i
 _
 c
 o
 r
 e
 g
 .
 c
 ,
 v
  
 1
 .
 2
 7
  
 2
 0
 1
 6
 /
 0
 4
 /
 3
 0
  
 1
 5
 :
 1
 1
 :
 4
 9
  
 g
 r
 e
 v
 e
  
 E
 x
 p
  
 $
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 6
 .
 5
 1
 2
 0
 7
 0
 :
 C
 r
 e
 a
 t
 i
 n
 g
  
 r
 a
 n
 d
 o
 m
  
 n
 u
 m
 b
 e
 r
 s
  
 f
 o
 r
  
 c
 o
 o
 r
 d
 i
 n
 a
 t
 e
  
 d
 i
 t
 h
 e
 r
 i
 n
 g
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 6
 .
 5
 1
 2
 0
 7
 0
 :
 M
 o
 v
 O
 O
 B
  
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 6
 .
 5
 1
 2
 0
 7
 0
 :
 P
 e
 r
 f
 o
 r
 m
 i
 n
 g
  
 i
 n
 t
 e
 n
 s
 i
 t
 y
  
 d
 i
 t
 h
 e
 r
 i
 n
 g
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 6
 .
 5
 1
 2
 0
 7
 0
 :
 R
 e
 a
 d
 i
 n
 g
  
 i
 n
  
 a
 n
 d
  
 a
 p
 p
 l
 y
 i
 n
 g
  
 r
 e
 f
 m
 a
 s
 k
  
 /
 d
 e
 r
 i
 v
 a
 t
 i
 v
 e
 s
 /
 f
 r
 e
 e
 s
 u
 r
 f
 e
 r
 /
 s
 u
 b
 -
 b
 m
 /
 m
 r
 i
 /
 a
 p
 a
 r
 c
 +
 a
 s
 e
 g
 .
 m
 g
 z
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 6
 .
 5
 1
 2
 0
 7
 0
 :
 R
 e
 a
 d
 i
 n
 g
  
 i
 n
  
 m
 o
 v
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 t
 e
 m
 p
 l
 a
 t
 e
 .
 n
 i
 i
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 6
 .
 5
 1
 2
 0
 7
 0
 :
 R
 e
 a
 d
 i
 n
 g
  
 i
 n
  
 r
 e
 f
  
 /
 d
 e
 r
 i
 v
 a
 t
 i
 v
 e
 s
 /
 f
 r
 e
 e
 s
 u
 r
 f
 e
 r
 /
 s
 u
 b
 -
 b
 m
 /
 m
 r
 i
 /
 b
 r
 a
 i
 n
 m
 a
 s
 k
 .
 m
 g
 z
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 6
 .
 5
 1
 2
 0
 7
 0
 :
 S
 a
 t
 P
 c
 t
  
  
  
  
 9
 9
 .
 9
 9
 0
 0
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 6
 .
 5
 1
 2
 0
 7
 0
 :
 S
 e
 t
 t
 i
 n
 g
  
 c
 r
 a
 s
  
 t
 r
 a
 n
 s
 l
 a
 t
 i
 o
 n
  
 p
 a
 r
 a
 m
 e
 t
 e
 r
 s
  
 t
 o
  
 a
 l
 i
 g
 n
  
 c
 e
 n
 t
 e
 r
 s
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 6
 .
 5
 1
 2
 0
 7
 0
 :
 S
 m
 o
 o
 t
 h
 R
 e
 f
  
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 6
 .
 5
 1
 2
 0
 7
 0
 :
 b
 f
  
  
  
  
  
  
  
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 6
 .
 5
 1
 2
 0
 7
 0
 :
 b
 f
 l
 i
 m
  
  
  
  
 3
 0
 .
 0
 0
 0
 0
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 6
 .
 5
 1
 2
 0
 7
 0
 :
 b
 f
 n
 s
 a
 m
 p
  
  
  
  
 3
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 6
 .
 5
 1
 2
 0
 7
 0
 :
 c
 m
 d
 l
 i
 n
 e
  
 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 -
 -
 s
  
 s
 u
 b
 -
 b
 m
  
 -
 -
 m
 o
 v
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 t
 e
 m
 p
 l
 a
 t
 e
 .
 n
 i
 i
  
 -
 -
 r
 e
 g
 d
 a
 t
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 r
 e
 g
 .
 i
 n
 i
 t
 .
 d
 a
 t
  
 -
 -
 r
 e
 g
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 m
 r
 i
 _
 c
 o
 r
 e
 g
 .
 l
 t
 a
  
 -
 -
 n
 t
 h
 r
 e
 a
 d
 s
  
 1
  
 -
 -
 d
 o
 f
  
 6
  
 -
 -
 s
 e
 p
  
 4
  
 -
 -
 f
 t
 o
 l
  
 .
 0
 0
 0
 1
  
 -
 -
 l
 i
 n
 m
 i
 n
 t
 o
 l
  
 .
 0
 1
  
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 6
 .
 5
 1
 2
 0
 7
 0
 :
 c
 r
 a
 s
 0
  
  
  
  
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 6
 .
 5
 1
 2
 0
 7
 0
 :
 c
 w
 d
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 6
 .
 5
 1
 2
 0
 7
 0
 :
 d
 o
 f
  
  
  
  
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 6
 .
 5
 1
 2
 0
 7
 0
 :
 f
 t
 o
 l
  
  
  
  
 0
 .
 0
 0
 0
 1
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 6
 .
 5
 1
 2
 0
 7
 0
 :
 h
 o
 s
 t
 n
 a
 m
 e
  
 9
 9
 5
 8
 f
 5
 f
 d
 3
 b
 a
 7
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 6
 .
 5
 1
 2
 0
 7
 0
 :
 l
 i
 n
 m
 i
 n
 t
 o
 l
  
  
  
  
 0
 .
 0
 1
 0
 0
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 6
 .
 5
 1
 2
 0
 7
 0
 :
 m
 a
 c
 h
 i
 n
 e
  
  
 x
 8
 6
 _
 6
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 6
 .
 5
 1
 2
 0
 7
 0
 :
 n
 s
 e
 p
  
  
  
  
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 6
 .
 5
 1
 2
 0
 7
 0
 :
 o
 p
 t
 s
 c
 h
 e
 m
 a
  
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 6
 .
 5
 1
 2
 0
 7
 0
 :
 s
 y
 s
 n
 a
 m
 e
  
  
 L
 i
 n
 u
 x
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 6
 .
 5
 1
 2
 0
 7
 0
 :
 u
 s
 e
 r
  
  
  
  
  
 r
 o
 o
 t
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 8
 .
 0
 0
 6
 8
 3
 3
 :
 D
 o
 C
 o
 o
 r
 d
 D
 i
 t
 h
 e
 r
  
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 8
 .
 0
 0
 6
 8
 3
 3
 :
 D
 o
 I
 n
 t
 e
 n
 s
 i
 t
 y
 D
 i
 t
 h
 e
 r
  
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 8
 .
 0
 0
 6
 8
 3
 3
 :
 D
 o
 S
 m
 o
 o
 t
 h
 i
 n
 g
  
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 8
 .
 0
 0
 6
 8
 3
 3
 :
 H
 i
 s
 t
  
 F
 W
 H
 M
  
 7
 .
 0
 0
 0
 0
 0
 0
  
 7
 .
 0
 0
 0
 0
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 8
 .
 0
 0
 6
 8
 3
 3
 :
 I
 n
 i
 t
 i
 a
 l
  
 p
 a
 r
 a
 m
 e
 t
 e
 r
 s
  
  
 6
 .
 0
 0
 5
 9
  
 -
 1
 0
 5
 .
 7
 5
 8
 5
  
 -
 9
 .
 6
 4
 2
 9
  
  
 0
 .
 0
 0
 0
 0
  
  
 0
 .
 0
 0
 0
 0
  
  
 0
 .
 0
 0
 0
 0
  
  
 1
 .
 0
 0
 0
 0
  
  
 1
 .
 0
 0
 0
 0
  
  
 1
 .
 0
 0
 0
 0
  
  
 0
 .
 0
 0
 0
 0
  
  
 0
 .
 0
 0
 0
 0
  
  
 0
 .
 0
 0
 0
 0
  
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 8
 .
 0
 0
 6
 8
 3
 3
 :
 S
 a
 t
 P
 c
 t
  
 9
 9
 .
 9
 9
 0
 0
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 8
 .
 0
 0
 6
 8
 3
 3
 :
 S
 e
 p
 a
 r
 a
 t
 i
 o
 n
  
 l
 i
 s
 t
  
 (
 1
 )
 :
  
  
 4
  
  
  
 m
 i
 n
  
 =
  
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 8
 .
 0
 0
 6
 8
 3
 3
 :
 S
 m
 o
 o
 t
 h
 i
 n
 g
  
 m
 o
 v
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 8
 .
 0
 0
 6
 8
 3
 3
 :
 f
 t
 o
 l
  
 1
 .
 0
 0
 0
 e
 -
 0
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 8
 .
 0
 0
 6
 8
 3
 3
 :
 l
 i
 n
 m
 i
 n
 t
 o
 l
  
 1
 .
 0
 0
 0
 e
 -
 0
 2
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 8
 .
 0
 0
 6
 8
 3
 3
 :
 m
 o
 v
  
 g
 s
 t
 d
  
 1
 .
 9
 2
 4
 8
  
 1
 .
 9
 2
 3
 3
  
 1
 .
 9
 2
 4
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 8
 .
 0
 0
 6
 8
 3
 3
 :
 m
 o
 v
 s
 a
 t
  
 =
  
 2
 3
 0
 5
 .
 5
 0
 9
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 8
 .
 0
 0
 6
 8
 3
 3
 :
 n
 i
 t
 e
 r
 s
 m
 a
 x
  
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 3
 :
 5
 8
 .
 0
 0
 6
 8
 3
 3
 :
 n
 t
 h
 r
 e
 a
 d
 s
  
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 4
 :
 4
 7
 .
 1
 7
 7
 4
 6
 5
 :
 S
 m
 o
 o
 t
 h
 i
 n
 g
  
 r
 e
 f
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 4
 :
 4
 7
 .
 1
 7
 7
 4
 6
 5
 :
 r
 e
 f
  
 g
 s
 t
 d
  
 1
 .
 9
 2
 8
 3
  
 1
 .
 9
 2
 8
 3
  
 1
 .
 9
 2
 8
 3
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 4
 :
 4
 7
 .
 1
 7
 7
 4
 6
 5
 :
 r
 e
 f
 s
 a
 t
  
 =
  
 1
 1
 6
 .
 0
 0
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 4
 :
 4
 7
 .
 2
 5
 6
 5
 2
 8
 :
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 .
 0
 0
 0
 0
 0
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 4
 :
 4
 7
 .
 2
 5
 6
 5
 2
 8
 :
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 .
 0
 0
 0
 0
 0
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 4
 :
 4
 7
 .
 2
 5
 6
 5
 2
 8
 :
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 .
 0
 0
 0
 0
 0
  
  
 -
 9
 .
 6
 4
 2
 8
 7
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 4
 :
 4
 7
 .
 2
 5
 6
 5
 2
 8
 :
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
 -
 1
 0
 5
 .
 7
 5
 8
 5
 4
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 4
 :
 4
 7
 .
 2
 5
 6
 5
 2
 8
 :
  
 0
 .
 0
 0
 0
 0
 0
  
  
 -
 0
 .
 0
 0
 4
 8
 8
  
  
  
 0
 .
 9
 1
 4
 2
 7
  
  
 -
 1
 2
 8
 .
 5
 4
 7
 6
 7
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 4
 :
 4
 7
 .
 2
 5
 6
 5
 2
 8
 :
  
 0
 .
 0
 0
 0
 0
 0
  
  
 -
 0
 .
 9
 3
 8
 4
 0
  
  
 -
 0
 .
 0
 0
 5
 0
 1
  
  
  
 2
 4
 5
 .
 9
 7
 4
 6
 6
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 4
 :
 4
 7
 .
 2
 5
 6
 5
 2
 8
 :
  
 0
 .
 9
 3
 8
 4
 2
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
 -
 5
 4
 .
 1
 7
 7
 4
 5
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 4
 :
 4
 7
 .
 2
 5
 6
 5
 2
 8
 :
  
 1
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 6
 .
 0
 0
 5
 9
 0
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 4
 :
 4
 7
 .
 2
 5
 6
 5
 2
 8
 :
 C
 O
 R
 E
 G
 p
 r
 e
 p
 r
 o
 c
 (
 )
  
 d
 o
 n
 e
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 4
 :
 4
 7
 .
 2
 5
 6
 5
 2
 8
 :
 I
 n
 i
 t
  
 c
 o
 s
 t
  
  
  
 -
 1
 .
 0
 2
 0
 0
 6
 3
 2
 4
 1
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 4
 :
 4
 7
 .
 2
 5
 6
 5
 2
 8
 :
 I
 n
 i
 t
 i
 a
 l
  
  
 R
 e
 f
 R
 A
 S
 -
 t
 o
 -
 M
 o
 v
 R
 A
 S
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 4
 :
 4
 7
 .
 2
 5
 6
 5
 2
 8
 :
 I
 n
 i
 t
 i
 a
 l
  
  
 R
 e
 f
 V
 o
 x
 -
 t
 o
 -
 M
 o
 v
 V
 o
 x
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 4
 :
 4
 7
 .
 2
 5
 6
 5
 2
 8
 :
 T
 e
 s
 t
 i
 n
 g
  
 i
 f
  
 m
 o
 v
  
 a
 n
 d
  
 t
 a
 r
 g
 e
 t
  
 o
 v
 e
 r
 l
 a
 p
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 4
 :
 4
 7
 .
 2
 5
 6
 5
 2
 8
 :
 n
 h
 i
 t
 s
  
 =
  
 2
 3
 3
 5
 4
  
 o
 u
 t
  
 o
 f
  
 3
 2
 7
 6
 8
 0
 0
 0
 ,
  
 P
 e
 r
 c
 e
 n
 t
  
 O
 v
 e
 r
 l
 a
 p
 :
  
  
  
 4
 .
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 0
 7
 .
 4
 0
 3
 9
 8
 9
 :
 #
 B
 F
 #
  
 s
 e
 p
 =
  
 4
  
 i
 t
 e
 r
 =
 0
  
 l
 i
 m
 =
 3
 0
 .
 0
  
 d
 e
 l
 t
 a
 =
 2
 .
 0
 0
  
  
 -
 7
 .
 9
 9
 4
 1
 0
  
 -
 9
 7
 .
 7
 5
 8
 5
 4
  
 -
 2
 1
 .
 6
 4
 2
 8
 7
  
  
 -
 4
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 0
 5
 6
 0
 7
 9
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 0
 7
 .
 4
 0
 3
 9
 8
 9
 :
 C
 O
 R
 E
 G
 o
 p
 t
 B
 r
 u
 t
 e
 F
 o
 r
 c
 e
 (
 )
  
 3
 0
  
 1
  
 3
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 0
 7
 .
 4
 0
 3
 9
 8
 9
 :
 T
 u
 r
 n
 i
 n
 g
  
 o
 n
  
 M
 o
 v
 O
 O
 B
  
 f
 o
 r
  
 B
 r
 u
 t
 e
 F
 o
 r
 c
 e
  
 S
 e
 a
 r
 c
 h
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 0
 7
 .
 4
 0
 3
 9
 8
 9
 :
 s
 e
 p
  
 =
  
 4
  
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 0
 7
 .
 4
 6
 6
 0
 1
 5
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 0
 7
 .
 4
 6
 6
 0
 1
 5
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 0
 7
 .
 4
 6
 6
 0
 1
 5
 :
 #
 @
 #
  
  
 4
  
  
 1
 8
 8
  
  
 -
 7
 .
 9
 9
 4
 1
 0
  
 -
 9
 7
 .
 7
 5
 8
 5
 4
  
 -
 2
 1
 .
 6
 4
 2
 8
 7
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 5
 0
 5
 6
 9
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 0
 7
 .
 4
 6
 6
 0
 1
 5
 :
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 0
 7
 .
 4
 6
 6
 0
 1
 5
 :
 I
 n
 i
 t
  
 P
 o
 w
 e
 l
  
 P
 a
 r
 a
 m
 s
  
 d
 o
 f
  
 =
  
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 0
 7
 .
 4
 6
 6
 0
 1
 5
 :
 I
 n
 i
 t
 i
 a
 l
 C
 o
 s
 t
  
  
  
  
  
  
  
  
 -
 1
 .
 0
 3
 5
 0
 5
 6
 9
 4
 8
 7
  
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 0
 7
 .
 4
 6
 6
 0
 1
 5
 :
 S
 t
 a
 r
 t
 i
 n
 g
  
 O
 p
 e
 n
 P
 o
 w
 e
 l
 2
 (
 )
 ,
  
 s
 e
 p
  
 =
  
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 0
 7
 .
 4
 6
 6
 0
 1
 5
 :
 T
 u
 r
 n
 i
 n
 g
  
  
 M
 o
 v
 O
 O
 B
  
 b
 a
 c
 k
  
 o
 f
 f
  
 a
 f
 t
 e
 r
  
 b
 r
 u
 t
 e
  
 f
 o
 r
 c
 e
  
 s
 e
 a
 r
 c
 h
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 0
 7
 .
 6
 5
 3
 0
 1
 7
 :
  
  
 f
 t
 o
 l
  
  
  
 0
 .
 0
 0
 0
 1
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 0
 7
 .
 6
 5
 3
 0
 1
 7
 :
  
  
 l
 i
 n
 m
 i
 n
 _
 x
 t
 o
 l
 _
  
  
  
 0
 .
 0
 1
 0
 0
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 0
 7
 .
 6
 5
 3
 0
 1
 7
 :
  
  
 m
 a
 x
 f
 e
 v
  
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 0
 7
 .
 6
 5
 3
 0
 1
 7
 :
  
  
 n
 p
 a
 r
 a
 m
 s
  
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 0
 7
 .
 6
 5
 3
 0
 1
 7
 :
  
  
 p
 o
 w
 e
 l
 l
  
 n
 t
 h
 i
 t
 e
 r
  
 0
 :
  
 f
 r
 e
 t
  
 =
  
 -
 1
 .
 0
 3
 5
 0
 5
 7
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 0
 7
 .
 6
 5
 3
 0
 1
 7
 :
 #
 @
 #
  
  
 4
  
  
 1
 9
 1
  
  
 -
 9
 .
 6
 1
 2
 1
 4
  
 -
 9
 7
 .
 7
 5
 8
 5
 4
  
 -
 2
 1
 .
 6
 4
 2
 8
 7
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 5
 3
 4
 4
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 0
 7
 .
 6
 5
 3
 0
 1
 7
 :
 f
 s
 _
 p
 o
 w
 e
 l
 l
 :
 :
 m
 i
 n
 i
 m
 i
 z
 e
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 0
 7
 .
 7
 1
 4
 4
 5
 1
 :
 #
 @
 #
  
  
 4
  
  
 1
 9
 2
  
  
 -
 9
 .
 9
 7
 3
 7
 0
  
 -
 9
 7
 .
 7
 5
 8
 5
 4
  
 -
 2
 1
 .
 6
 4
 2
 8
 7
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 5
 3
 6
 2
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 0
 7
 .
 9
 5
 3
 3
 9
 3
 :
 #
 @
 #
  
  
 4
  
  
 1
 9
 6
  
  
 -
 1
 0
 .
 0
 4
 6
 3
 5
  
 -
 9
 7
 .
 7
 5
 8
 5
 4
  
 -
 2
 1
 .
 6
 4
 2
 8
 7
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 5
 3
 6
 8
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 0
 8
 .
 0
 1
 4
 4
 6
 4
 :
 #
 @
 #
  
  
 4
  
  
 1
 9
 7
  
  
 -
 1
 0
 .
 0
 9
 1
 2
 5
  
 -
 9
 7
 .
 7
 5
 8
 5
 4
  
 -
 2
 1
 .
 6
 4
 2
 8
 7
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 5
 3
 7
 3
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 0
 8
 .
 1
 3
 4
 4
 4
 3
 :
 #
 @
 #
  
  
 4
  
  
 1
 9
 9
  
  
 -
 1
 0
 .
 0
 8
 1
 2
 1
  
 -
 9
 7
 .
 7
 5
 8
 5
 4
  
 -
 2
 1
 .
 6
 4
 2
 8
 7
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 5
 3
 7
 4
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 0
 8
 .
 1
 9
 4
 3
 3
 5
 :
 #
 @
 #
  
  
 4
  
  
 2
 0
 0
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 9
 7
 .
 7
 5
 8
 5
 4
  
 -
 2
 1
 .
 6
 4
 2
 8
 7
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 5
 3
 7
 6
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 0
 8
 .
 4
 3
 3
 4
 6
 4
 :
 #
 @
 #
  
  
 4
  
  
 2
 0
 4
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 9
 9
 .
 3
 7
 6
 5
 7
  
 -
 2
 1
 .
 6
 4
 2
 8
 7
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 6
 5
 1
 1
 9
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 0
 8
 .
 4
 9
 4
 0
 2
 3
 :
 #
 @
 #
  
  
 4
  
  
 2
 0
 5
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 1
 .
 9
 9
 4
 6
 1
  
 -
 2
 1
 .
 6
 4
 2
 8
 7
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 8
 1
 0
 1
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 0
 8
 .
 5
 5
 4
 4
 8
 0
 :
 #
 @
 #
  
  
 4
  
  
 2
 0
 6
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 1
 4
 .
 2
 1
 3
 2
 3
  
 -
 2
 1
 .
 6
 4
 2
 8
 7
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 9
 0
 2
 1
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 0
 8
 .
 6
 1
 4
 8
 1
 0
 :
 #
 @
 #
  
  
 4
  
  
 2
 0
 7
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 1
 5
 4
 3
 2
  
 -
 2
 1
 .
 6
 4
 2
 8
 7
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 9
 6
 0
 7
 2
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 0
 8
 .
 9
 1
 2
 3
 0
 2
 :
 #
 @
 #
  
  
 4
  
  
 2
 1
 2
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 9
 2
 4
 1
  
 -
 2
 1
 .
 6
 4
 2
 8
 7
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 9
 7
 0
 6
 2
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 0
 9
 .
 0
 3
 1
 5
 9
 7
 :
 #
 @
 #
  
  
 4
  
  
 2
 1
 4
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 7
 9
 8
 5
 1
  
 -
 2
 1
 .
 6
 4
 2
 8
 7
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 9
 7
 2
 7
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 0
 9
 .
 2
 7
 0
 3
 5
 7
 :
 #
 @
 #
  
  
 4
  
  
 2
 1
 8
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 1
 .
 6
 4
 2
 8
 7
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 9
 7
 2
 8
 2
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 0
 9
 .
 4
 5
 0
 0
 0
 6
 :
 #
 @
 #
  
  
 4
  
  
 2
 2
 1
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 3
 .
 2
 6
 0
 9
 0
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 9
 7
 9
 2
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 0
 9
 .
 8
 0
 7
 9
 5
 4
 :
 #
 @
 #
  
  
 4
  
  
 2
 2
 7
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 3
 .
 1
 2
 0
 7
 1
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 9
 7
 9
 6
 5
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 0
 9
 .
 8
 6
 7
 7
 0
 9
 :
 #
 @
 #
  
  
 4
  
  
 2
 2
 8
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 3
 .
 0
 1
 9
 3
 7
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 9
 7
 9
 8
 3
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 1
 0
 .
 0
 5
 8
 4
 6
 0
 :
 #
 @
 #
  
  
 4
  
  
 2
 3
 1
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 6
 4
 4
 4
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 9
 8
 0
 1
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 1
 0
 .
 2
 9
 6
 6
 4
 8
 :
 #
 @
 #
  
  
 4
  
  
 2
 3
 5
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 7
 4
 4
 4
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 9
 8
 0
 1
 2
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 1
 0
 .
 4
 1
 6
 6
 4
 1
 :
 #
 @
 #
  
  
 4
  
  
 2
 3
 7
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 7
 4
 4
 4
  
 -
 3
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 4
 0
 0
 4
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 1
 0
 .
 4
 7
 6
 8
 6
 8
 :
 #
 @
 #
  
  
 4
  
  
 2
 3
 8
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 7
 4
 4
 4
  
 -
 1
 .
 3
 8
 1
 9
 7
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 4
 0
 1
 2
 5
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 1
 0
 .
 5
 9
 7
 3
 0
 2
 :
 #
 @
 #
  
  
 4
  
  
 2
 4
 0
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 7
 4
 4
 4
  
 1
 .
 2
 3
 6
 0
 7
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 4
 0
 4
 6
 0
 3
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 1
 0
 .
 6
 5
 7
 4
 9
 2
 :
 #
 @
 #
  
  
 4
  
  
 2
 4
 1
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 7
 4
 4
 4
  
 5
 .
 4
 7
 2
 1
 4
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 4
 0
 6
 9
 3
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 1
 0
 .
 8
 9
 5
 9
 5
 9
 :
 #
 @
 #
  
  
 4
  
  
 2
 4
 5
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 7
 4
 4
 4
  
 4
 .
 8
 5
 4
 1
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 4
 0
 7
 2
 9
 9
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 1
 1
 .
 0
 7
 6
 8
 5
 2
 :
 #
 @
 #
  
  
 4
  
  
 2
 4
 8
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 7
 4
 4
 4
  
 4
 .
 7
 0
 8
 2
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 4
 0
 7
 3
 5
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 1
 1
 .
 3
 1
 4
 7
 3
 9
 :
 #
 @
 #
  
  
 4
  
  
 2
 5
 2
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 7
 4
 4
 4
  
 4
 .
 7
 3
 1
 3
 4
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 4
 0
 7
 3
 7
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 1
 1
 .
 4
 3
 3
 8
 5
 4
 :
 #
 @
 #
  
  
 4
  
  
 2
 5
 4
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 7
 4
 4
 4
  
 4
 .
 7
 2
 1
 3
 4
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 4
 0
 7
 4
 3
 9
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 1
 1
 .
 5
 5
 4
 0
 1
 7
 :
 #
 @
 #
  
  
 4
  
  
 2
 5
 6
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 7
 4
 4
 4
  
 4
 .
 7
 2
 1
 3
 4
  
 1
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 4
 0
 7
 5
 5
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 1
 1
 .
 7
 9
 2
 7
 9
 6
 :
 #
 @
 #
  
  
 4
  
  
 2
 6
 0
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 7
 4
 4
 4
  
 4
 .
 7
 2
 1
 3
 4
  
 0
 .
 6
 1
 8
 0
 3
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 4
 0
 7
 7
 5
 9
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 1
 2
 .
 0
 9
 0
 4
 3
 8
 :
 #
 @
 #
  
  
 4
  
  
 2
 6
 5
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 7
 4
 4
 4
  
 4
 .
 7
 2
 1
 3
 4
  
 0
 .
 6
 0
 7
 4
 5
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 4
 0
 7
 7
 8
 3
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 1
 2
 .
 5
 6
 9
 4
 2
 5
 :
 #
 @
 #
  
  
 4
  
  
 2
 7
 3
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 7
 4
 4
 4
  
 4
 .
 7
 2
 1
 3
 4
  
 0
 .
 6
 0
 7
 4
 5
  
 0
 .
 3
 8
 1
 9
 7
  
  
  
 -
 1
 .
 0
 4
 0
 7
 8
 1
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 1
 2
 .
 6
 8
 9
 3
 0
 5
 :
 #
 @
 #
  
  
 4
  
  
 2
 7
 5
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 7
 4
 4
 4
  
 4
 .
 7
 2
 1
 3
 4
  
 0
 .
 6
 0
 7
 4
 5
  
 0
 .
 6
 1
 8
 0
 3
  
  
  
 -
 1
 .
 0
 4
 0
 8
 0
 1
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 1
 2
 .
 7
 4
 9
 0
 7
 2
 :
 #
 @
 #
  
  
 4
  
  
 2
 7
 6
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 7
 4
 4
 4
  
 4
 .
 7
 2
 1
 3
 4
  
 0
 .
 6
 0
 7
 4
 5
  
 0
 .
 7
 6
 3
 9
 3
  
  
  
 -
 1
 .
 0
 4
 0
 8
 1
 5
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 1
 3
 .
 2
 2
 7
 9
 5
 8
 :
  
  
 p
 o
 w
 e
 l
 l
  
 n
 t
 h
 i
 t
 e
 r
  
 1
 :
  
 f
 r
 e
 t
  
 =
  
 -
 1
 .
 0
 4
 0
 8
 1
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 1
 3
 .
 2
 2
 7
 9
 5
 8
 :
 #
 @
 #
  
  
 4
  
  
 2
 8
 4
  
  
 -
 9
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 7
 4
 4
 4
  
 4
 .
 7
 2
 1
 3
 4
  
 0
 .
 6
 0
 7
 4
 5
  
 0
 .
 7
 6
 3
 9
 3
  
  
  
 -
 1
 .
 0
 4
 0
 9
 0
 9
 2
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 1
 3
 .
 4
 6
 5
 7
 7
 2
 :
 #
 @
 #
  
  
 4
  
  
 2
 8
 8
  
  
 -
 9
 .
 4
 5
 3
 1
 8
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 7
 4
 4
 4
  
 4
 .
 7
 2
 1
 3
 4
  
 0
 .
 6
 0
 7
 4
 5
  
 0
 .
 7
 6
 3
 9
 3
  
  
  
 -
 1
 .
 0
 4
 0
 9
 1
 3
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 1
 3
 .
 5
 2
 6
 0
 8
 1
 :
 #
 @
 #
  
  
 4
  
  
 2
 8
 9
  
  
 -
 9
 .
 3
 1
 6
 2
 2
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 7
 4
 4
 4
  
 4
 .
 7
 2
 1
 3
 4
  
 0
 .
 6
 0
 7
 4
 5
  
 0
 .
 7
 6
 3
 9
 3
  
  
  
 -
 1
 .
 0
 4
 0
 9
 2
 1
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 1
 4
 .
 5
 3
 8
 1
 5
 0
 :
 #
 @
 #
  
  
 4
  
  
 3
 0
 6
  
  
 -
 9
 .
 3
 1
 6
 2
 2
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 4
 .
 5
 9
 2
 4
 7
  
 4
 .
 7
 2
 1
 3
 4
  
 0
 .
 6
 0
 7
 4
 5
  
 0
 .
 7
 6
 3
 9
 3
  
  
  
 -
 1
 .
 0
 4
 1
 2
 5
 1
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 1
 5
 .
 5
 4
 8
 7
 4
 1
 :
 #
 @
 #
  
  
 4
  
  
 3
 2
 3
  
  
 -
 9
 .
 3
 1
 6
 2
 2
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 4
 .
 5
 9
 2
 4
 7
  
 4
 .
 6
 6
 0
 4
 4
  
 0
 .
 6
 0
 7
 4
 5
  
 0
 .
 7
 6
 3
 9
 3
  
  
  
 -
 1
 .
 0
 4
 1
 2
 6
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 1
 5
 .
 6
 0
 8
 5
 7
 2
 :
 #
 @
 #
  
  
 4
  
  
 3
 2
 4
  
  
 -
 9
 .
 3
 1
 6
 2
 2
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 4
 .
 5
 9
 2
 4
 7
  
 4
 .
 6
 8
 0
 4
 1
  
 0
 .
 6
 0
 7
 4
 5
  
 0
 .
 7
 6
 3
 9
 3
  
  
  
 -
 1
 .
 0
 4
 1
 2
 7
 2
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 1
 5
 .
 9
 6
 6
 6
 2
 2
 :
 #
 @
 #
  
  
 4
  
  
 3
 3
 0
  
  
 -
 9
 .
 3
 1
 6
 2
 2
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 4
 .
 5
 9
 2
 4
 7
  
 4
 .
 6
 8
 0
 4
 1
  
 -
 0
 .
 0
 1
 0
 5
 8
  
 0
 .
 7
 6
 3
 9
 3
  
  
  
 -
 1
 .
 0
 4
 1
 3
 0
 7
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 1
 6
 .
 9
 1
 7
 9
 8
 7
 :
 #
 @
 #
  
  
 4
  
  
 3
 4
 6
  
  
 -
 9
 .
 3
 1
 6
 2
 2
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 4
 .
 5
 9
 2
 4
 7
  
 4
 .
 6
 8
 0
 4
 1
  
 -
 0
 .
 0
 1
 0
 5
 8
  
 0
 .
 8
 0
 9
 6
 7
  
  
  
 -
 1
 .
 0
 4
 1
 3
 2
 5
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 1
 7
 .
 9
 3
 2
 9
 2
 6
 :
 #
 @
 #
  
  
 4
  
  
 3
 6
 3
  
  
 -
 9
 .
 3
 0
 8
 6
 7
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 4
 .
 6
 0
 8
 6
 5
  
 4
 .
 6
 8
 0
 0
 0
  
 -
 0
 .
 0
 1
 6
 7
 7
  
 0
 .
 8
 1
 0
 1
 2
  
  
  
 -
 1
 .
 0
 4
 1
 3
 3
 3
 9
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 1
 8
 .
 2
 9
 0
 7
 8
 7
 :
  
  
 p
 o
 w
 e
 l
 l
  
 n
 t
 h
 i
 t
 e
 r
  
 2
 :
  
 f
 r
 e
 t
  
 =
  
 -
 1
 .
 0
 4
 1
 3
 3
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 1
 8
 .
 2
 9
 0
 7
 8
 7
 :
 #
 @
 #
  
  
 4
  
  
 3
 6
 9
  
  
 -
 8
 .
 9
 2
 6
 7
 0
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 4
 .
 6
 0
 8
 6
 5
  
 4
 .
 6
 8
 0
 0
 0
  
 -
 0
 .
 0
 1
 6
 7
 7
  
 0
 .
 8
 1
 0
 1
 2
  
  
  
 -
 1
 .
 0
 4
 1
 3
 4
 3
 9
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 1
 8
 .
 3
 5
 0
 6
 6
 1
 :
 #
 @
 #
  
  
 4
  
  
 3
 7
 0
  
  
 -
 9
 .
 0
 4
 6
 2
 3
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 4
 .
 6
 0
 8
 6
 5
  
 4
 .
 6
 8
 0
 0
 0
  
 -
 0
 .
 0
 1
 6
 7
 7
  
 0
 .
 8
 1
 0
 1
 2
  
  
  
 -
 1
 .
 0
 4
 1
 3
 5
 1
 7
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 1
 8
 .
 4
 7
 0
 1
 5
 6
 :
 #
 @
 #
  
  
 4
  
  
 3
 7
 2
  
  
 -
 9
 .
 0
 0
 4
 6
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 4
 .
 6
 0
 8
 6
 5
  
 4
 .
 6
 8
 0
 0
 0
  
 -
 0
 .
 0
 1
 6
 7
 7
  
 0
 .
 8
 1
 0
 1
 2
  
  
  
 -
 1
 .
 0
 4
 1
 3
 5
 9
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 2
 2
 4
 5
 0
 9
 :
 #
 @
 #
  
  
 4
  
  
 4
 3
 5
  
  
 -
 8
 .
 9
 9
 7
 0
 6
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 4
 .
 6
 2
 4
 8
 3
  
 4
 .
 6
 7
 9
 5
 9
  
 -
 0
 .
 0
 2
 2
 9
 5
  
 0
 .
 8
 1
 0
 5
 8
  
  
  
 -
 1
 .
 0
 4
 1
 3
 6
 1
 9
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 2
 8
 4
 4
 5
 2
 :
 O
 p
 t
 T
 i
 m
 e
 M
 i
 n
  
  
 0
 .
 2
 5
  
 m
 i
 n
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 2
 8
 4
 4
 5
 2
 :
 O
 p
 t
 T
 i
 m
 e
 S
 e
 c
  
 1
 4
 .
 9
  
 s
 e
 c
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 2
 8
 4
 4
 5
 2
 :
 P
 o
 w
 e
 l
 l
  
 d
 o
 n
 e
  
 n
 i
 t
 e
 r
 s
  
 t
 o
 t
 a
 l
  
 =
  
 2
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 2
 8
 4
 4
 5
 2
 :
 n
 E
 v
 a
 l
 s
  
 4
 3
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 4
 6
 3
 7
 3
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 4
 6
 3
 7
 3
 :
  
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 4
 6
 3
 7
 3
 :
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 .
 0
 0
 0
 0
 0
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 4
 6
 3
 7
 3
 :
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 .
 0
 0
 0
 0
 0
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 4
 6
 3
 7
 3
 :
  
 0
 .
 0
 0
 1
 5
 5
  
  
 -
 0
 .
 0
 8
 1
 5
 7
  
  
  
 0
 .
 9
 9
 6
 6
 7
  
  
 -
 2
 4
 .
 6
 2
 4
 8
 3
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 4
 6
 3
 7
 3
 :
  
 0
 .
 0
 1
 2
 8
 5
  
  
 -
 0
 .
 0
 7
 9
 4
 6
  
  
  
 0
 .
 9
 1
 0
 7
 4
  
  
 -
 1
 2
 4
 .
 3
 7
 7
 1
 1
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 4
 6
 3
 7
 3
 :
  
 0
 .
 9
 3
 8
 3
 2
  
  
 -
 0
 .
 0
 0
 0
 3
 8
  
  
 -
 0
 .
 0
 1
 3
 2
 8
  
  
 -
 2
 9
 .
 8
 0
 9
 5
 2
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 4
 6
 3
 7
 3
 :
  
 0
 .
 9
 9
 9
 9
 0
  
  
  
 0
 .
 0
 1
 4
 1
 5
  
  
 -
 0
 .
 0
 0
 0
 4
 0
  
  
 -
 8
 .
 9
 9
 7
 0
 6
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 4
 6
 3
 7
 3
 :
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 4
 6
 3
 7
 3
 :
 -
 0
 .
 0
 0
 1
 5
 3
  
  
 -
 0
 .
 9
 3
 4
 8
 7
  
  
 -
 0
 .
 0
 8
 1
 5
 4
  
  
  
 2
 3
 6
 .
 9
 7
 4
 9
 6
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 4
 6
 3
 7
 3
 :
 -
 0
 .
 0
 1
 4
 0
 7
  
  
  
 0
 .
 9
 9
 6
 5
 7
  
  
  
 0
 .
 0
 8
 1
 5
 8
  
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 4
 6
 3
 7
 3
 :
 F
 i
 n
 a
 l
  
  
 R
 e
 f
 R
 A
 S
 -
 t
 o
 -
 M
 o
 v
 R
 A
 S
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 4
 6
 3
 7
 3
 :
 F
 i
 n
 a
 l
  
  
 R
 e
 f
 V
 o
 x
 -
 t
 o
 -
 M
 o
 v
 V
 o
 x
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 4
 6
 3
 7
 3
 :
 F
 i
 n
 a
 l
  
 c
 o
 s
 t
  
  
  
 -
 1
 .
 0
 4
 1
 3
 6
 1
 9
 3
 9
 8
 3
 0
 2
 5
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 4
 6
 3
 7
 3
 :
 F
 i
 n
 a
 l
  
 p
 a
 r
 a
 m
 e
 t
 e
 r
 s
  
  
 -
 8
 .
 9
 9
 7
 0
 5
 6
 9
 6
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 0
 9
 8
 3
  
 -
 2
 4
 .
 6
 2
 4
 8
 3
 2
 1
 5
  
  
  
 4
 .
 6
 7
 9
 5
 9
 3
 0
 9
  
  
 -
 0
 .
 0
 2
 2
 9
 4
 5
 4
 8
  
  
  
 0
 .
 8
 1
 0
 5
 8
 0
 7
 3
  
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 4
 6
 3
 7
 3
 :
 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 r
 u
 _
 i
 d
 r
 s
 s
  
  
  
  
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 4
 6
 3
 7
 3
 :
 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 r
 u
 _
 i
 n
 b
 l
 o
 c
 k
  
  
 1
 9
 5
 6
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 4
 6
 3
 7
 3
 :
 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 r
 u
 _
 i
 s
 r
 s
 s
  
  
  
  
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 4
 6
 3
 7
 3
 :
 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 r
 u
 _
 i
 x
 r
 s
 s
  
  
  
  
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 4
 6
 3
 7
 3
 :
 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 r
 u
 _
 m
 a
 j
 f
 l
 t
  
  
  
 3
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 4
 6
 3
 7
 3
 :
 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 r
 u
 _
 m
 a
 x
 r
 s
 s
  
  
  
 8
 5
 5
 4
 9
 2
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 4
 6
 3
 7
 3
 :
 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 r
 u
 _
 m
 i
 n
 f
 l
 t
  
  
  
 6
 4
 6
 7
 8
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 4
 6
 3
 7
 3
 :
 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 r
 u
 _
 m
 s
 g
 r
 c
 v
  
  
  
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 4
 6
 3
 7
 3
 :
 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 r
 u
 _
 m
 s
 g
 s
 n
 d
  
  
  
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 4
 6
 3
 7
 3
 :
 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 r
 u
 _
 n
 i
 v
 c
 s
 w
  
  
  
 7
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 4
 6
 3
 7
 3
 :
 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 r
 u
 _
 n
 s
 i
 g
 n
 a
 l
 s
  
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 4
 6
 3
 7
 3
 :
 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 r
 u
 _
 n
 s
 w
 a
 p
  
  
  
  
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 4
 6
 3
 7
 3
 :
 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 r
 u
 _
 n
 v
 c
 s
 w
  
  
  
  
 4
 2
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 4
 6
 3
 7
 3
 :
 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 r
 u
 _
 o
 u
 b
 l
 o
 c
 k
  
  
 1
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 4
 6
 3
 7
 3
 :
 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 s
 t
 i
 m
 e
 s
 e
 c
  
  
  
  
 0
 .
 7
 7
 3
 9
 9
 5
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 4
 6
 3
 7
 3
 :
 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 u
 t
 i
 m
 e
 s
 e
 c
  
  
  
  
 1
 0
 6
 .
 6
 7
 4
 4
 2
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 5
 2
 9
 0
 0
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 5
 2
 9
 0
 0
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 5
 2
 9
 0
 0
 :
  
  
  
 t
 k
 r
 e
 g
 i
 s
 t
 e
 r
 f
 v
  
 -
 -
 m
 o
 v
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 t
 e
 m
 p
 l
 a
 t
 e
 .
 n
 i
 i
  
 -
 -
 t
 a
 r
 g
  
 /
 d
 e
 r
 i
 v
 a
 t
 i
 v
 e
 s
 /
 f
 r
 e
 e
 s
 u
 r
 f
 e
 r
 /
 s
 u
 b
 -
 b
 m
 /
 m
 r
 i
 /
 b
 r
 a
 i
 n
 m
 a
 s
 k
 .
 m
 g
 z
  
 -
 -
 r
 e
 g
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 m
 r
 i
 _
 c
 o
 r
 e
 g
 .
 l
 t
 a
  
 -
 -
 s
  
 s
 u
 b
 -
 b
 m
  
 -
 -
 s
 u
 r
 f
 s
  
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 5
 2
 9
 0
 0
 :
 F
 i
 n
 a
 l
  
 p
 a
 r
 a
 m
 e
 t
 e
 r
 s
  
 -
 8
 .
 9
 9
 7
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
  
 -
 2
 4
 .
 6
 2
 4
 8
  
  
 4
 .
 6
 7
 9
 6
  
 -
 0
 .
 0
 2
 2
 9
  
  
 0
 .
 8
 1
 0
 6
  
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 5
 2
 9
 0
 0
 :
 T
 o
  
 c
 h
 e
 c
 k
  
 r
 u
 n
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 5
 2
 9
 0
 0
 :
 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 R
 u
 n
 T
 i
 m
 e
 S
 e
 c
  
 1
 0
 7
 .
 5
  
 s
 e
 c
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 5
 2
 9
 0
 0
 :
 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 d
 o
 n
 e
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 3
 5
 2
 9
 0
 0
 :
 n
 h
 i
 t
 s
  
 =
  
 2
 3
 2
 9
 1
  
 o
 u
 t
  
 o
 f
  
 3
 2
 7
 6
 8
 0
 0
 0
 ,
  
 P
 e
 r
 c
 e
 n
 t
  
 O
 v
 e
 r
 l
 a
 p
 :
  
  
  
 4
 .
 5
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 1
 6
 8
 5
 5
 :
 m
 r
 i
 _
 s
 e
 g
 r
 e
 g
  
 -
 -
 m
 o
 v
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 t
 e
 m
 p
 l
 a
 t
 e
 .
 n
 i
 i
  
 -
 -
 i
 n
 i
 t
 -
 r
 e
 g
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 r
 e
 g
 .
 i
 n
 i
 t
 .
 d
 a
 t
  
 -
 -
 o
 u
 t
 -
 r
 e
 g
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 b
 b
 r
 .
 p
 a
 s
 s
 1
 .
 d
 a
 t
  
 -
 -
 s
 u
 b
 s
 a
 m
 p
 -
 b
 r
 u
 t
 e
  
 1
 0
 0
  
 -
 -
 s
 u
 b
 s
 a
 m
 p
  
 1
 0
 0
  
 -
 -
 t
 o
 l
  
 1
 e
 -
 4
  
 -
 -
 t
 o
 l
 1
 d
  
 1
 e
 -
 3
  
 -
 -
 b
 r
 u
 t
 e
  
 -
 4
  
 4
  
 4
  
 -
 -
 s
 u
 r
 f
  
 w
 h
 i
 t
 e
  
 -
 -
 g
 m
 -
 p
 r
 o
 j
 -
 f
 r
 a
 c
  
 0
 .
 5
  
 -
 -
 g
 m
 -
 g
 t
 -
 w
 m
  
 0
 .
 5
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 .
 0
 0
 0
 0
 0
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
  
 0
 .
 0
 0
 1
 6
 3
  
  
 -
 0
 .
 0
 8
 6
 8
 9
  
  
  
 0
 .
 9
 9
 6
 2
 2
  
  
 -
 1
 4
 .
 9
 3
 1
 9
 6
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
  
 0
 .
 0
 1
 4
 0
 6
  
  
 -
 0
 .
 9
 9
 6
 1
 2
  
  
 -
 0
 .
 0
 8
 6
 9
 1
  
  
  
 4
 .
 4
 2
 1
 0
 7
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
  
 0
 .
 9
 9
 9
 9
 0
  
  
  
 0
 .
 0
 1
 4
 1
 5
  
  
 -
 0
 .
 0
 0
 0
 4
 0
  
  
 -
 1
 5
 .
 0
 9
 8
 0
 3
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 $
 I
 d
 :
  
 m
 r
 i
 _
 s
 e
 g
 r
 e
 g
 .
 c
 ,
 v
  
 1
 .
 1
 1
 3
  
 2
 0
 1
 6
 /
 0
 5
 /
 1
 0
  
 0
 3
 :
 2
 3
 :
 2
 0
  
 g
 r
 e
 v
 e
  
 E
 x
 p
  
 $
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 A
 d
 d
 N
 o
 i
 s
 e
  
  
 0
  
 (
 0
 )
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 G
 M
 P
 r
 o
 j
 F
 r
 a
 c
  
 0
 .
 5
 0
 0
 0
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 G
 d
 i
 a
 g
 _
 n
 o
  
  
 -
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 I
 n
 p
 u
 t
  
 r
 e
 g
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 P
 e
 n
 a
 l
 t
 y
 C
 e
 n
 t
 e
 r
  
 0
 .
 0
 0
 0
 0
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 P
 e
 n
 a
 l
 t
 y
 S
 i
 g
 n
  
  
 -
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 P
 e
 n
 a
 l
 t
 y
 S
 l
 o
 p
 e
  
 0
 .
 5
 0
 0
 0
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 P
 r
 o
 f
 i
 l
 e
  
  
  
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 R
 o
 t
 R
 a
 n
 d
 M
 a
 x
  
 0
 .
 0
 0
 0
 0
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 R
 o
 t
 a
 t
 i
 o
 n
 s
  
  
  
 0
 .
 0
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 S
 y
 n
 t
 h
 S
 e
 e
 d
  
 1
 5
 4
 4
 9
 8
 3
 2
 0
 5
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 T
 o
 l
 P
 o
 w
 e
 l
 l
  
 0
 .
 0
 0
 0
 1
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 T
 r
 a
 n
 s
 R
 a
 n
 d
 M
 a
 x
  
 0
 .
 0
 0
 0
 0
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 T
 r
 a
 n
 s
 l
 a
 t
 i
 o
 n
 s
  
 0
 .
 0
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 U
 s
 e
 L
 H
  
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 U
 s
 e
 M
 a
 s
 k
  
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 U
 s
 e
 R
 H
  
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 W
 M
 P
 r
 o
 j
 A
 b
 s
  
 2
 .
 0
 0
 0
 0
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 c
 d
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 d
 o
 f
  
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 f
 r
 a
 m
 e
  
  
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 h
 o
 s
 t
 n
 a
 m
 e
  
 9
 9
 5
 8
 f
 5
 f
 d
 3
 b
 a
 7
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 i
 n
 t
 e
 r
 p
  
  
 t
 r
 i
 l
 i
 n
 e
 a
 r
  
 (
 1
 )
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 l
 h
 c
 o
 s
 t
 f
 i
 l
 e
  
 (
 n
 u
 l
 l
 )
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 m
 a
 c
 h
 i
 n
 e
  
  
 x
 8
 6
 _
 6
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 m
 o
 v
 v
 o
 l
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 t
 e
 m
 p
 l
 a
 t
 e
 .
 n
 i
 i
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 m
 r
 i
 _
 s
 e
 g
 r
 e
 g
  
 -
 -
 m
 o
 v
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 t
 e
 m
 p
 l
 a
 t
 e
 .
 n
 i
 i
  
 -
 -
 i
 n
 i
 t
 -
 r
 e
 g
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 r
 e
 g
 .
 i
 n
 i
 t
 .
 d
 a
 t
  
 -
 -
 o
 u
 t
 -
 r
 e
 g
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 b
 b
 r
 .
 p
 a
 s
 s
 1
 .
 d
 a
 t
  
 -
 -
 s
 u
 b
 s
 a
 m
 p
 -
 b
 r
 u
 t
 e
  
 1
 0
 0
  
 -
 -
 s
 u
 b
 s
 a
 m
 p
  
 1
 0
 0
  
 -
 -
 t
 o
 l
  
 1
 e
 -
 4
  
 -
 -
 t
 o
 l
 1
 d
  
 1
 e
 -
 3
  
 -
 -
 b
 r
 u
 t
 e
  
 -
 4
  
 4
  
 4
  
 -
 -
 s
 u
 r
 f
  
 w
 h
 i
 t
 e
  
 -
 -
 g
 m
 -
 p
 r
 o
 j
 -
 f
 r
 a
 c
  
 0
 .
 5
  
 -
 -
 g
 m
 -
 g
 t
 -
 w
 m
  
 0
 .
 5
  
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 n
 1
 d
 m
 i
 n
  
  
 3
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 n
 M
 a
 x
 I
 t
 e
 r
 s
 P
 o
 w
 e
 l
 l
  
 3
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 n
 s
 u
 b
 s
 a
 m
 p
  
 1
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 o
 u
 t
 r
 e
 g
 f
 i
 l
 e
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 b
 b
 r
 .
 p
 a
 s
 s
 1
 .
 d
 a
 t
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 r
 e
 g
 f
 i
 l
 e
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 r
 e
 g
 .
 i
 n
 i
 t
 .
 d
 a
 t
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 r
 h
 c
 o
 s
 t
 f
 i
 l
 e
  
 (
 n
 u
 l
 l
 )
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 s
 e
 t
 e
 n
 v
  
 S
 U
 B
 J
 E
 C
 T
 S
 _
 D
 I
 R
  
 /
 d
 e
 r
 i
 v
 a
 t
 i
 v
 e
 s
 /
 f
 r
 e
 e
 s
 u
 r
 f
 e
 r
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 s
 u
 b
 j
 e
 c
 t
  
 s
 u
 b
 -
 b
 m
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 s
 u
 r
 f
 n
 a
 m
 e
  
 w
 h
 i
 t
 e
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 s
 y
 s
 n
 a
 m
 e
  
  
 L
 i
 n
 u
 x
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 4
 1
 1
 3
 6
 :
 u
 s
 e
 r
  
  
  
  
  
 r
 o
 o
 t
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 2
 .
 4
 5
 0
 2
 0
 7
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 9
 .
 3
 6
 2
 3
 2
 9
 :
 L
 o
 a
 d
 i
 n
 g
  
 l
 h
 .
 t
 h
 i
 c
 k
 n
 e
 s
 s
  
 f
 o
 r
  
 G
 M
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 9
 .
 3
 6
 2
 3
 2
 9
 :
 L
 o
 a
 d
 i
 n
 g
  
 l
 h
 .
 w
 h
 i
 t
 e
  
 s
 u
 r
 f
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 9
 .
 3
 6
 2
 3
 2
 9
 :
 L
 o
 a
 d
 i
 n
 g
  
 m
 o
 v
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 2
 9
 .
 3
 6
 2
 3
 2
 9
 :
 P
 r
 o
 j
 e
 c
 t
 i
 n
 g
  
 L
 H
  
 S
 u
 r
 f
 s
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 4
 .
 3
 1
 3
 6
 2
 8
 :
 G
 M
  
 P
 r
 o
 j
 :
  
 1
  
 0
 .
 5
 0
 0
 0
 0
 0
  
 2
 .
 0
 0
 0
 0
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 4
 .
 3
 1
 3
 6
 2
 8
 :
 L
 o
 a
 d
 i
 n
 g
  
 r
 h
 .
 t
 h
 i
 c
 k
 n
 e
 s
 s
  
 f
 o
 r
  
 G
 M
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 4
 .
 3
 1
 3
 6
 2
 8
 :
 L
 o
 a
 d
 i
 n
 g
  
 r
 h
 .
 w
 h
 i
 t
 e
  
 s
 u
 r
 f
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 4
 .
 3
 1
 3
 6
 2
 8
 :
 P
 r
 o
 j
 e
 c
 t
 i
 n
 g
  
 R
 H
  
 S
 u
 r
 f
 s
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 4
 .
 3
 1
 3
 6
 2
 8
 :
 W
 M
  
 P
 r
 o
 j
 :
  
 0
  
 0
 .
 5
 0
 0
 0
 0
 0
  
 2
 .
 0
 0
 0
 0
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 4
 .
 9
 7
 3
 2
 5
 1
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 4
 .
 9
 7
 3
 2
 5
 1
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 4
 .
 9
 7
 3
 2
 5
 1
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 4
 .
 9
 7
 3
 2
 5
 1
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 4
 .
 9
 7
 3
 2
 5
 1
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 4
 .
 9
 7
 3
 2
 5
 1
 :
  
 0
  
  
 -
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
  
 1
 .
 1
 2
 3
 3
 9
 7
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 4
 .
 9
 7
 3
 2
 5
 1
 :
  
 1
  
  
 -
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
  
 1
 .
 1
 1
 9
 1
 7
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 4
 .
 9
 7
 3
 2
 5
 1
 :
  
 2
  
  
 -
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
  
 1
 .
 0
 4
 2
 8
 4
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 4
 .
 9
 7
 3
 2
 5
 1
 :
  
 3
  
  
 -
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
  
 1
 .
 0
 1
 5
 8
 8
 7
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 4
 .
 9
 7
 3
 2
 5
 1
 :
  
 4
  
  
  
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
  
 0
 .
 9
 9
 8
 6
 8
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 4
 .
 9
 7
 3
 2
 5
 1
 :
  
 5
  
  
  
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
  
 1
 .
 0
 5
 0
 3
 5
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 4
 .
 9
 7
 3
 2
 5
 1
 :
  
 6
  
  
  
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
  
 1
 .
 0
 1
 7
 1
 4
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 4
 .
 9
 7
 3
 2
 5
 1
 :
  
 7
  
  
  
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
  
 1
 .
 0
 5
 6
 2
 3
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 4
 .
 9
 7
 3
 2
 5
 1
 :
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 4
 .
 9
 7
 3
 2
 5
 1
 :
 B
 r
 u
 t
 e
  
 f
 o
 r
 c
 e
  
 p
 r
 e
 o
 p
 t
  
 -
 4
  
 4
  
 4
 ,
  
 n
  
 =
  
 7
 2
 9
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 4
 .
 9
 7
 3
 2
 5
 1
 :
 C
 o
 m
 p
 u
 t
 i
 n
 g
  
 r
 e
 l
 a
 t
 i
 v
 e
  
 c
 o
 s
 t
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 4
 .
 9
 7
 3
 2
 5
 1
 :
 C
 o
 s
 t
  
  
  
 1
 .
 1
 0
 9
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 4
 .
 9
 7
 3
 2
 5
 1
 :
 C
 t
 x
  
 I
 n
 t
 e
 n
 s
 i
 t
 y
  
  
  
 1
 3
 8
 .
 4
 9
 6
 3
  
 +
 /
 -
  
 2
 1
 7
 .
 2
 5
 7
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 4
 .
 9
 7
 3
 2
 5
 1
 :
 I
 f
  
 t
 h
 e
  
 m
 o
 v
  
 d
 a
 t
 a
  
 h
 a
 s
  
 a
  
 T
 1
  
 c
 o
 n
 t
 r
 a
 s
 t
 ,
  
 r
 e
 -
 r
 u
 n
  
 w
 i
 t
 h
  
 -
 -
 T
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 4
 .
 9
 7
 3
 2
 5
 1
 :
 I
 n
 i
 t
 i
 a
 l
  
 c
 o
 s
 t
 s
  
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 4
 .
 9
 7
 3
 2
 5
 1
 :
 N
 u
 m
 b
 e
 r
  
 o
 f
  
 s
 u
 r
 f
 a
 c
 e
  
 h
 i
 t
 s
  
 8
 7
 9
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 4
 .
 9
 7
 3
 2
 5
 1
 :
 P
 c
 t
  
 C
 o
 n
 t
 r
 a
 s
 t
  
  
  
  
  
 -
 7
 .
 7
 7
 2
 1
  
 +
 /
 -
  
  
 7
 3
 .
 1
 1
 7
 5
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 4
 .
 9
 7
 3
 2
 5
 1
 :
 P
 r
 o
 j
 e
 c
 t
 i
 n
 g
  
 R
 H
  
 S
 u
 r
 f
 s
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 4
 .
 9
 7
 3
 2
 5
 1
 :
 R
 E
 L
 :
  
  
 8
  
  
 1
 .
 1
 0
 9
 0
 3
 2
  
  
  
  
 8
 .
 4
 2
 3
 7
 2
 3
  
  
 1
 .
 0
 5
 2
 9
 6
 5
  
 r
 e
 l
  
 =
  
 1
 .
 0
 5
 3
 2
 5
  
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 4
 .
 9
 7
 3
 2
 5
 1
 :
 R
 e
 l
 C
 o
 s
 t
  
  
  
 1
 .
 0
 5
 3
 2
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 4
 .
 9
 7
 3
 2
 5
 1
 :
 U
 s
 i
 n
 g
  
 l
 h
 .
 c
 o
 r
 t
 e
 x
 .
 l
 a
 b
 e
 l
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 4
 .
 9
 7
 3
 2
 5
 1
 :
 U
 s
 i
 n
 g
  
 r
 h
 .
 c
 o
 r
 t
 e
 x
 .
 l
 a
 b
 e
 l
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 4
 .
 9
 7
 3
 2
 5
 1
 :
 W
 A
 R
 N
 I
 N
 G
 :
  
 i
 n
 i
 t
 i
 a
 l
  
 G
 -
 W
  
 c
 o
 n
 t
 r
 a
 s
 t
  
 i
 s
  
 n
 e
 g
 a
 t
 i
 v
 e
 ,
  
 b
 u
 t
  
 e
 x
 p
 e
 c
 t
 i
 n
 g
  
 p
 o
 s
 i
 t
 i
 v
 e
 .
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 4
 .
 9
 7
 3
 2
 5
 1
 :
 W
 M
  
  
 I
 n
 t
 e
 n
 s
 i
 t
 y
  
  
  
 1
 4
 5
 .
 3
 8
 3
 4
  
 +
 /
 -
  
 2
 3
 2
 .
 7
 4
 9
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 4
 .
 9
 7
 6
 2
 5
 2
 :
  
  
  
  
  
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
  
  
  
  
 1
 .
 0
 6
 2
 9
  
  
  
 1
 .
 0
 6
 2
 9
  
  
 0
 .
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 4
 .
 9
 8
 0
 5
 3
 9
 :
  
  
  
  
  
 2
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
  
 4
 .
 0
 0
 0
 0
  
  
  
  
  
  
 1
 .
 0
 4
 6
 3
  
  
  
 1
 .
 0
 4
 6
 3
  
  
 0
 .
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 4
 .
 9
 9
 6
 1
 2
 9
 :
  
  
  
  
  
 9
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
  
  
  
  
 1
 .
 0
 2
 0
 3
  
  
  
 1
 .
 0
 2
 0
 3
  
  
 0
 .
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 5
 .
 0
 0
 0
 6
 4
 6
 :
  
  
  
  
 1
 1
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
  
 4
 .
 0
 0
 0
 0
  
  
  
  
  
  
 1
 .
 0
 1
 0
 0
  
  
  
 1
 .
 0
 1
 0
 0
  
  
 0
 .
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 5
 .
 0
 8
 7
 0
 0
 0
 :
  
  
  
  
 5
 2
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
  
 4
 .
 0
 0
 0
 0
  
  
  
 4
 .
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
  
  
  
  
 1
 .
 0
 0
 2
 9
  
  
  
 1
 .
 0
 0
 2
 9
  
  
 0
 .
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 5
 .
 1
 0
 6
 5
 4
 1
 :
  
  
  
  
 6
 1
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
  
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
  
 4
 .
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
  
  
  
  
 0
 .
 9
 9
 4
 3
  
  
  
 0
 .
 9
 9
 4
 3
  
  
 0
 .
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 5
 .
 2
 0
 9
 4
 3
 2
 :
  
  
  
 1
 1
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
  
 4
 .
 0
 0
 0
 0
  
  
  
  
  
  
 0
 .
 9
 8
 9
 4
  
  
  
 0
 .
 9
 8
 9
 4
  
  
 0
 .
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 5
 .
 4
 0
 9
 2
 6
 5
 :
  
  
  
 2
 0
 6
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
  
 4
 .
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
  
 4
 .
 0
 0
 0
 0
  
  
  
 4
 .
 0
 0
 0
 0
  
  
  
  
  
  
 0
 .
 9
 6
 8
 2
  
  
  
 0
 .
 9
 6
 8
 2
  
  
 0
 .
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 5
 .
 4
 4
 1
 0
 2
 9
 :
  
  
  
 2
 2
 1
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
  
 4
 .
 0
 0
 0
 0
  
  
  
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
  
 4
 .
 0
 0
 0
 0
  
  
  
  
  
  
 0
 .
 9
 6
 6
 3
  
  
  
 0
 .
 9
 6
 6
 3
  
  
 0
 .
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 5
 .
 5
 2
 0
 3
 7
 2
 :
  
  
  
 2
 5
 9
  
  
  
 0
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
  
 4
 .
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
  
  
  
  
 0
 .
 9
 6
 4
 3
  
  
  
 0
 .
 9
 6
 4
 3
  
  
 0
 .
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 0
 0
 8
 4
 1
 0
 :
  
  
  
 4
 8
 6
  
  
  
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
  
  
  
  
 0
 .
 9
 5
 7
 0
  
  
  
 0
 .
 9
 5
 7
 0
  
  
 0
 .
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 0
 3
 2
 3
 0
 7
 :
  
  
  
 4
 9
 7
  
  
  
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
  
 4
 .
 0
 0
 0
 0
  
  
  
  
  
  
 0
 .
 9
 4
 8
 5
  
  
  
 0
 .
 9
 4
 8
 5
  
  
 0
 .
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 5
 3
 7
 8
 4
 6
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 5
 3
 7
 8
 4
 6
 :
  
  
  
 8
  
  
 3
 .
 9
 8
 7
  
 -
 4
 .
 0
 0
 0
  
 -
 4
 .
 0
 0
 0
  
  
 0
 .
 0
 0
 0
  
 -
 4
 .
 0
 0
 0
  
  
 4
 .
 0
 0
 0
  
  
  
 0
 .
 9
 4
 8
 0
 3
 2
 1
 3
 1
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 5
 3
 7
 8
 4
 6
 :
  
  
 4
 .
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
  
  
 0
 .
 0
 0
 0
  
 -
 4
 .
 0
 0
 0
  
  
 4
 .
 0
 0
 0
  
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 5
 3
 7
 8
 4
 6
 :
  
  
 f
 t
 o
 l
  
  
  
 0
 .
 0
 0
 0
 1
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 5
 3
 7
 8
 4
 6
 :
  
  
 l
 i
 n
 m
 i
 n
 _
 x
 t
 o
 l
 _
  
  
  
 0
 .
 0
 0
 1
 0
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 5
 3
 7
 8
 4
 6
 :
  
  
 m
 a
 x
 f
 e
 v
  
 3
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 5
 3
 7
 8
 4
 6
 :
  
  
 n
 p
 a
 r
 a
 m
 s
  
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 5
 3
 7
 8
 4
 6
 :
  
  
 p
 o
 w
 e
 l
 l
  
 n
 t
 h
 i
 t
 e
 r
  
 0
 :
  
 f
 r
 e
 t
  
 =
  
 0
 .
 9
 4
 8
 5
 3
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 5
 3
 7
 8
 4
 6
 :
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 5
 3
 7
 8
 4
 6
 :
 0
  
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 5
 3
 7
 8
 4
 6
 :
 1
  
 -
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 5
 3
 7
 8
 4
 6
 :
 2
  
 -
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 5
 3
 7
 8
 4
 6
 :
 3
  
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 5
 3
 7
 8
 4
 6
 :
 4
  
 -
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 5
 3
 7
 8
 4
 6
 :
 5
  
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 5
 3
 7
 8
 4
 6
 :
 B
 r
 u
 t
 e
  
 F
 o
 r
 c
 e
  
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 5
 3
 7
 8
 4
 6
 :
 I
 n
 i
 t
  
 P
 o
 w
 e
 l
  
 P
 a
 r
 a
 m
 s
  
 d
 o
 f
  
 =
  
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 5
 3
 7
 8
 4
 6
 :
 M
 i
 n
  
 c
 o
 s
 t
  
 w
 a
 s
  
 0
 .
 9
 4
 8
 5
 3
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 5
 3
 7
 8
 4
 6
 :
 N
 u
 m
 b
 e
 r
  
 o
 f
  
 i
 t
 e
 r
 a
 t
 i
 o
 n
 s
  
  
  
 7
 2
 9
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 5
 3
 7
 8
 4
 6
 :
 P
 a
 r
 a
 m
 e
 t
 e
 r
 s
  
 a
 t
  
 b
 e
 s
 t
  
 (
 t
 r
 a
 n
 s
 m
 m
 ,
  
 r
 o
 t
 d
 e
 g
 )
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 5
 3
 7
 8
 4
 6
 :
 S
 e
 a
 r
 c
 h
  
 t
 i
 m
 e
  
 1
 .
 5
 4
 7
 0
 0
 0
  
 s
 e
 c
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 5
 3
 7
 8
 4
 6
 :
 S
 t
 a
 r
 t
 i
 n
 g
  
 P
 o
 w
 e
 l
 l
  
 M
 i
 n
 i
 m
 i
 z
 a
 t
 i
 o
 n
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 5
 3
 7
 8
 4
 6
 :
 f
 s
 _
 p
 o
 w
 e
 l
 l
 :
 :
 m
 i
 n
 i
 m
 i
 z
 e
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 5
 4
 6
 9
 0
 0
 :
  
  
 1
 2
  
  
 3
 .
 9
 8
 9
  
 -
 4
 .
 0
 0
 0
  
 -
 4
 .
 0
 0
 0
  
  
 0
 .
 0
 0
 0
  
 -
 4
 .
 0
 0
 0
  
  
 4
 .
 0
 0
 0
  
  
  
 0
 .
 9
 4
 8
 0
 2
 5
 0
 7
 1
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 5
 6
 6
 6
 6
 4
 :
  
  
 2
 1
  
  
 3
 .
 9
 8
 9
  
 -
 3
 .
 9
 8
 6
  
 -
 4
 .
 0
 0
 0
  
  
 0
 .
 0
 0
 0
  
 -
 4
 .
 0
 0
 0
  
  
 4
 .
 0
 0
 0
  
  
  
 0
 .
 9
 4
 7
 2
 3
 9
 5
 6
 8
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 5
 7
 1
 1
 3
 0
 :
  
  
 2
 3
  
  
 3
 .
 9
 8
 9
  
 -
 3
 .
 9
 3
 2
  
 -
 4
 .
 0
 0
 0
  
  
 0
 .
 0
 0
 0
  
 -
 4
 .
 0
 0
 0
  
  
 4
 .
 0
 0
 0
  
  
  
 0
 .
 9
 4
 7
 0
 9
 7
 6
 2
 1
 2
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 6
 4
 3
 4
 0
 6
 :
  
  
 5
 7
  
  
 3
 .
 9
 8
 9
  
 -
 3
 .
 9
 3
 2
  
 -
 4
 .
 0
 0
 0
  
 -
 0
 .
 0
 0
 5
  
 -
 4
 .
 0
 0
 0
  
  
 4
 .
 0
 0
 0
  
  
  
 0
 .
 9
 4
 7
 0
 3
 5
 6
 1
 0
 2
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 6
 5
 8
 4
 6
 1
 :
  
  
 6
 4
  
  
 3
 .
 9
 8
 9
  
 -
 3
 .
 9
 3
 2
  
 -
 4
 .
 0
 0
 0
  
 -
 0
 .
 0
 0
 5
  
 -
 4
 .
 6
 1
 8
  
  
 4
 .
 0
 0
 0
  
  
  
 0
 .
 9
 4
 2
 0
 1
 1
 4
 7
 1
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 6
 7
 1
 1
 9
 5
 :
  
  
 7
 0
  
  
 3
 .
 9
 8
 9
  
 -
 3
 .
 9
 3
 2
  
 -
 4
 .
 0
 0
 0
  
 -
 0
 .
 0
 0
 5
  
 -
 4
 .
 5
 8
 5
  
  
 4
 .
 0
 0
 0
  
  
  
 0
 .
 9
 3
 7
 3
 0
 9
 7
 8
 4
 7
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 6
 7
 5
 6
 7
 1
 :
  
  
 7
 2
  
  
 3
 .
 9
 8
 9
  
 -
 3
 .
 9
 3
 2
  
 -
 4
 .
 0
 0
 0
  
 -
 0
 .
 0
 0
 5
  
 -
 4
 .
 5
 8
 7
  
  
 4
 .
 0
 0
 0
  
  
  
 0
 .
 9
 3
 7
 2
 6
 0
 3
 3
 1
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 6
 7
 7
 9
 2
 4
 :
  
  
 7
 3
  
  
 3
 .
 9
 8
 9
  
 -
 3
 .
 9
 3
 2
  
 -
 4
 .
 0
 0
 0
  
 -
 0
 .
 0
 0
 5
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 0
 0
  
  
  
 0
 .
 9
 3
 7
 2
 5
 2
 4
 0
 7
 2
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 7
 0
 1
 2
 4
 9
 :
  
  
 8
 4
  
  
 3
 .
 9
 8
 9
  
 -
 3
 .
 9
 3
 2
  
 -
 4
 .
 0
 0
 0
  
 -
 0
 .
 0
 0
 5
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 1
 6
  
  
  
 0
 .
 9
 3
 7
 2
 4
 1
 8
 7
 1
 7
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 7
 0
 3
 5
 4
 0
 :
  
  
 8
 5
  
  
 3
 .
 9
 8
 9
  
 -
 3
 .
 9
 3
 2
  
 -
 4
 .
 0
 0
 0
  
 -
 0
 .
 0
 0
 5
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 0
 8
  
  
  
 0
 .
 9
 3
 7
 0
 8
 1
 2
 7
 8
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 7
 0
 8
 0
 4
 7
 :
  
  
 8
 7
  
  
 3
 .
 9
 8
 9
  
 -
 3
 .
 9
 3
 2
  
 -
 4
 .
 0
 0
 0
  
 -
 0
 .
 0
 0
 5
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 1
 0
  
  
  
 0
 .
 9
 3
 7
 0
 6
 9
 9
 7
 5
 2
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 7
 3
 8
 2
 7
 4
 :
  
  
 p
 o
 w
 e
 l
 l
  
 n
 t
 h
 i
 t
 e
 r
  
 1
 :
  
 f
 r
 e
 t
  
 =
  
 0
 .
 9
 3
 7
 0
 7
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 7
 3
 8
 2
 7
 4
 :
  
 1
 0
 1
  
  
 4
 .
 0
 0
 0
  
 -
 3
 .
 9
 3
 2
  
 -
 4
 .
 0
 0
 0
  
 -
 0
 .
 0
 0
 5
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 1
 0
  
  
  
 0
 .
 9
 3
 6
 2
 3
 8
 2
 0
 4
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 7
 4
 2
 8
 7
 5
 :
  
 1
 0
 3
  
  
 3
 .
 9
 9
 8
  
 -
 3
 .
 9
 3
 2
  
 -
 4
 .
 0
 0
 0
  
 -
 0
 .
 0
 0
 5
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 1
 0
  
  
  
 0
 .
 9
 3
 6
 2
 1
 3
 7
 8
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 7
 4
 5
 1
 5
 6
 :
  
 1
 0
 4
  
  
 3
 .
 9
 9
 7
  
 -
 3
 .
 9
 3
 2
  
 -
 4
 .
 0
 0
 0
  
 -
 0
 .
 0
 0
 5
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 1
 0
  
  
  
 0
 .
 9
 3
 6
 2
 1
 2
 4
 6
 2
 5
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 7
 7
 0
 6
 7
 6
 :
  
 1
 1
 6
  
  
 3
 .
 9
 9
 7
  
 -
 3
 .
 9
 3
 8
  
 -
 4
 .
 0
 0
 0
  
 -
 0
 .
 0
 0
 5
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 1
 0
  
  
  
 0
 .
 9
 3
 5
 9
 1
 0
 9
 0
 7
 2
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 7
 7
 3
 0
 0
 2
 :
  
 1
 1
 7
  
  
 3
 .
 9
 9
 7
  
 -
 3
 .
 9
 3
 9
  
 -
 4
 .
 0
 0
 0
  
 -
 0
 .
 0
 0
 5
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 1
 0
  
  
  
 0
 .
 9
 3
 5
 9
 1
 0
 3
 1
 4
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 8
 0
 4
 9
 6
 9
 :
  
 1
 3
 2
  
  
 3
 .
 9
 9
 7
  
 -
 3
 .
 9
 3
 9
  
 -
 3
 .
 9
 9
 7
  
 -
 0
 .
 0
 0
 5
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 1
 0
  
  
  
 0
 .
 9
 3
 5
 8
 7
 0
 9
 8
 4
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 8
 2
 8
 6
 7
 0
 :
  
 1
 4
 3
  
  
 3
 .
 9
 9
 7
  
 -
 3
 .
 9
 3
 9
  
 -
 3
 .
 9
 9
 7
  
 -
 0
 .
 0
 0
 1
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 1
 0
  
  
  
 0
 .
 9
 3
 5
 7
 2
 3
 2
 1
 8
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 8
 3
 5
 1
 0
 2
 :
  
 1
 4
 6
  
  
 3
 .
 9
 9
 7
  
 -
 3
 .
 9
 3
 9
  
 -
 3
 .
 9
 9
 7
  
  
 0
 .
 0
 0
 3
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 1
 0
  
  
  
 0
 .
 9
 3
 5
 5
 4
 4
 4
 7
 0
 7
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 8
 3
 7
 3
 8
 1
 :
  
 1
 4
 7
  
  
 3
 .
 9
 9
 7
  
 -
 3
 .
 9
 3
 9
  
 -
 3
 .
 9
 9
 7
  
  
 0
 .
 0
 0
 7
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 1
 0
  
  
  
 0
 .
 9
 3
 5
 3
 7
 0
 0
 0
 3
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 8
 3
 9
 6
 4
 8
 :
  
 1
 4
 8
  
  
 3
 .
 9
 9
 7
  
 -
 3
 .
 9
 3
 9
  
 -
 3
 .
 9
 9
 7
  
  
 0
 .
 0
 1
 0
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 1
 0
  
  
  
 0
 .
 9
 3
 5
 2
 8
 9
 3
 9
 7
 7
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 8
 9
 6
 4
 7
 7
 :
  
 1
 7
 5
  
  
 3
 .
 9
 9
 7
  
 -
 3
 .
 9
 3
 9
  
 -
 3
 .
 9
 9
 7
  
  
 0
 .
 0
 1
 0
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 0
 7
  
  
  
 0
 .
 9
 3
 5
 2
 7
 5
 3
 2
 6
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 8
 9
 8
 7
 0
 6
 :
  
 1
 7
 6
  
  
 3
 .
 9
 9
 7
  
 -
 3
 .
 9
 3
 9
  
 -
 3
 .
 9
 9
 7
  
  
 0
 .
 0
 1
 0
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 0
 8
  
  
  
 0
 .
 9
 3
 5
 2
 7
 2
 0
 1
 0
 3
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 9
 0
 0
 9
 4
 3
 :
  
 1
 7
 7
  
  
 4
 .
 0
 0
 6
  
 -
 3
 .
 9
 4
 5
  
 -
 3
 .
 9
 9
 3
  
  
 0
 .
 0
 2
 5
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 0
 6
  
  
  
 0
 .
 9
 3
 4
 7
 2
 9
 7
 3
 3
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 9
 1
 6
 2
 6
 6
 :
  
 1
 8
 4
  
  
 4
 .
 0
 0
 6
  
 -
 3
 .
 9
 4
 5
  
 -
 3
 .
 9
 9
 3
  
  
 0
 .
 0
 2
 4
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 0
 6
  
  
  
 0
 .
 9
 3
 4
 7
 1
 5
 1
 3
 1
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 9
 1
 8
 5
 1
 4
 :
  
 1
 8
 5
  
  
 4
 .
 0
 0
 6
  
 -
 3
 .
 9
 4
 5
  
 -
 3
 .
 9
 9
 3
  
  
 0
 .
 0
 2
 4
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 0
 6
  
  
  
 0
 .
 9
 3
 4
 7
 1
 2
 7
 3
 8
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 9
 2
 0
 8
 7
 1
 :
  
 1
 8
 6
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 4
 4
  
 -
 3
 .
 9
 9
 4
  
  
 0
 .
 0
 2
 2
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 0
 6
  
  
  
 0
 .
 9
 3
 4
 7
 1
 0
 1
 7
 3
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 9
 2
 3
 2
 1
 3
 :
  
 1
 8
 7
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 4
 4
  
 -
 3
 .
 9
 9
 3
  
  
 0
 .
 0
 2
 3
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 0
 6
  
  
  
 0
 .
 9
 3
 4
 7
 0
 4
 5
 3
 5
 7
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 9
 2
 5
 5
 1
 5
 :
  
 1
 8
 8
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 4
 4
  
 -
 3
 .
 9
 9
 4
  
  
 0
 .
 0
 2
 3
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 0
 6
  
  
  
 0
 .
 9
 3
 4
 7
 0
 3
 6
 0
 1
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 9
 6
 1
 5
 8
 5
 :
  
  
 p
 o
 w
 e
 l
 l
  
 n
 t
 h
 i
 t
 e
 r
  
 2
 :
  
 f
 r
 e
 t
  
 =
  
 0
 .
 9
 3
 4
 7
 0
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 9
 6
 1
 5
 8
 5
 :
  
 2
 0
 5
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 4
 4
  
 -
 3
 .
 9
 9
 4
  
  
 0
 .
 0
 2
 3
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 0
 5
  
  
  
 0
 .
 9
 3
 4
 6
 9
 8
 5
 2
 2
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 9
 8
 5
 3
 1
 5
 :
  
 2
 1
 6
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 5
 3
  
 -
 3
 .
 9
 9
 4
  
  
 0
 .
 0
 2
 3
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 0
 5
  
  
  
 0
 .
 9
 3
 4
 4
 6
 1
 1
 9
 4
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 9
 8
 7
 5
 2
 4
 :
  
 2
 1
 7
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 4
 9
  
 -
 3
 .
 9
 9
 4
  
  
 0
 .
 0
 2
 3
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 0
 5
  
  
  
 0
 .
 9
 3
 4
 4
 0
 6
 9
 4
 3
 7
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 6
 .
 9
 9
 1
 8
 5
 8
 :
  
 2
 1
 9
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 4
 7
  
 -
 3
 .
 9
 9
 4
  
  
 0
 .
 0
 2
 3
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 0
 5
  
  
  
 0
 .
 9
 3
 4
 3
 5
 3
 4
 8
 2
 2
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 0
 2
 6
 0
 0
 6
 :
  
 2
 3
 5
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 4
 7
  
 -
 3
 .
 9
 9
 5
  
  
 0
 .
 0
 2
 3
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 0
 5
  
  
  
 0
 .
 9
 3
 3
 9
 3
 4
 5
 4
 4
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 0
 5
 7
 9
 0
 8
 :
  
 2
 5
 0
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 4
 7
  
 -
 3
 .
 9
 9
 5
  
  
 0
 .
 0
 2
 0
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 0
 5
  
  
  
 0
 .
 9
 3
 3
 8
 7
 6
 2
 7
 9
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 0
 6
 4
 5
 9
 3
 :
  
 2
 5
 3
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 4
 7
  
 -
 3
 .
 9
 9
 5
  
  
 0
 .
 0
 1
 9
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 0
 5
  
  
  
 0
 .
 9
 3
 3
 8
 7
 2
 8
 8
 4
 2
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 0
 9
 6
 3
 6
 9
 :
  
 2
 6
 8
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 4
 7
  
 -
 3
 .
 9
 9
 5
  
  
 0
 .
 0
 1
 9
  
 -
 4
 .
 5
 9
 0
  
  
 4
 .
 0
 0
 5
  
  
  
 0
 .
 9
 3
 3
 7
 5
 6
 6
 5
 0
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 1
 1
 3
 6
 4
 7
 :
  
 2
 7
 6
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 4
 7
  
 -
 3
 .
 9
 9
 5
  
  
 0
 .
 0
 1
 9
  
 -
 4
 .
 5
 9
 0
  
  
 4
 .
 0
 0
 5
  
  
  
 0
 .
 9
 3
 3
 7
 5
 4
 5
 4
 8
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 1
 5
 2
 2
 3
 4
 :
  
  
 p
 o
 w
 e
 l
 l
  
 n
 t
 h
 i
 t
 e
 r
  
 3
 :
  
 f
 r
 e
 t
  
 =
  
 0
 .
 9
 3
 3
 7
 5
 5
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 1
 5
 2
 2
 3
 4
 :
  
 2
 9
 4
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 4
 7
  
 -
 3
 .
 9
 9
 5
  
  
 0
 .
 0
 1
 9
  
 -
 4
 .
 5
 9
 0
  
  
 4
 .
 0
 0
 1
  
  
  
 0
 .
 9
 3
 3
 7
 0
 7
 1
 3
 6
 5
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 1
 5
 4
 5
 3
 3
 :
  
 2
 9
 5
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 4
 7
  
 -
 3
 .
 9
 9
 5
  
  
 0
 .
 0
 1
 9
  
 -
 4
 .
 5
 9
 0
  
  
 4
 .
 0
 0
 2
  
  
  
 0
 .
 9
 3
 3
 6
 9
 4
 6
 9
 8
 5
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 2
 1
 3
 9
 5
 4
 :
  
 3
 2
 2
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 4
 7
  
 -
 3
 .
 9
 9
 7
  
  
 0
 .
 0
 1
 9
  
 -
 4
 .
 5
 9
 0
  
  
 4
 .
 0
 0
 2
  
  
  
 0
 .
 9
 3
 3
 4
 2
 0
 9
 1
 4
 5
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 2
 4
 3
 9
 6
 3
 :
  
 3
 3
 6
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 4
 7
  
 -
 3
 .
 9
 9
 7
  
  
 0
 .
 0
 2
 0
  
 -
 4
 .
 5
 9
 0
  
  
 4
 .
 0
 0
 2
  
  
  
 0
 .
 9
 3
 3
 4
 0
 7
 7
 7
 7
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 2
 6
 5
 4
 9
 3
 :
  
 3
 4
 6
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 4
 7
  
 -
 3
 .
 9
 9
 7
  
  
 0
 .
 0
 2
 0
  
 -
 4
 .
 5
 9
 3
  
  
 4
 .
 0
 0
 2
  
  
  
 0
 .
 9
 3
 3
 1
 8
 0
 9
 7
 6
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 2
 7
 2
 1
 6
 6
 :
  
 3
 4
 9
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 4
 7
  
 -
 3
 .
 9
 9
 7
  
  
 0
 .
 0
 2
 0
  
 -
 4
 .
 5
 9
 4
  
  
 4
 .
 0
 0
 2
  
  
  
 0
 .
 9
 3
 3
 1
 2
 0
 4
 2
 1
 9
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 2
 7
 4
 3
 8
 8
 :
  
 3
 5
 0
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 4
 7
  
 -
 3
 .
 9
 9
 7
  
  
 0
 .
 0
 2
 0
  
 -
 4
 .
 5
 9
 6
  
  
 4
 .
 0
 0
 2
  
  
  
 0
 .
 9
 3
 3
 0
 2
 9
 6
 0
 0
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 2
 9
 5
 5
 6
 5
 :
  
 3
 6
 0
  
  
 4
 .
 0
 0
 6
  
 -
 3
 .
 9
 4
 8
  
 -
 3
 .
 9
 9
 7
  
  
 0
 .
 0
 2
 1
  
 -
 4
 .
 5
 9
 6
  
  
 4
 .
 0
 0
 2
  
  
  
 0
 .
 9
 3
 3
 0
 1
 2
 2
 9
 8
 2
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 2
 9
 7
 7
 9
 1
 :
  
 3
 6
 1
  
  
 4
 .
 0
 0
 6
  
 -
 3
 .
 9
 4
 8
  
 -
 3
 .
 9
 9
 7
  
  
 0
 .
 0
 2
 1
  
 -
 4
 .
 5
 9
 6
  
  
 4
 .
 0
 0
 2
  
  
  
 0
 .
 9
 3
 2
 9
 9
 8
 0
 1
 7
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 3
 9
 8
 1
 1
 2
 :
  
  
 p
 o
 w
 e
 l
 l
  
 n
 t
 h
 i
 t
 e
 r
  
 4
 :
  
 f
 r
 e
 t
  
 =
  
 0
 .
 9
 3
 2
 9
 9
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 3
 9
 8
 1
 1
 2
 :
  
 4
 0
 8
  
  
 4
 .
 0
 0
 6
  
 -
 3
 .
 9
 4
 8
  
 -
 3
 .
 9
 9
 8
  
  
 0
 .
 0
 2
 1
  
 -
 4
 .
 5
 9
 6
  
  
 4
 .
 0
 0
 2
  
  
  
 0
 .
 9
 3
 2
 8
 5
 5
 8
 6
 9
 2
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 4
 5
 9
 5
 1
 6
 :
  
 4
 3
 7
  
  
 4
 .
 0
 0
 6
  
 -
 3
 .
 9
 4
 8
  
 -
 3
 .
 9
 9
 8
  
  
 0
 .
 0
 2
 1
  
 -
 4
 .
 5
 9
 7
  
  
 4
 .
 0
 0
 2
  
  
  
 0
 .
 9
 3
 2
 8
 2
 6
 3
 2
 7
 5
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 4
 7
 6
 3
 7
 6
 :
  
 4
 4
 5
  
  
 4
 .
 0
 0
 6
  
 -
 3
 .
 9
 4
 8
  
 -
 3
 .
 9
 9
 8
  
  
 0
 .
 0
 2
 2
  
 -
 4
 .
 5
 9
 7
  
  
 4
 .
 0
 0
 2
  
  
  
 0
 .
 9
 3
 2
 8
 2
 5
 0
 1
 6
 9
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 4
 7
 8
 5
 5
 3
 :
  
 4
 4
 6
  
  
 4
 .
 0
 0
 6
  
 -
 3
 .
 9
 4
 8
  
 -
 3
 .
 9
 9
 8
  
  
 0
 .
 0
 2
 1
  
 -
 4
 .
 5
 9
 7
  
  
 4
 .
 0
 0
 2
  
  
  
 0
 .
 9
 3
 2
 8
 2
 0
 9
 8
 6
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 4
 8
 0
 7
 8
 8
 :
  
 4
 4
 7
  
  
 4
 .
 0
 0
 6
  
 -
 3
 .
 9
 4
 8
  
 -
 3
 .
 9
 9
 8
  
  
 0
 .
 0
 2
 1
  
 -
 4
 .
 5
 9
 7
  
  
 4
 .
 0
 0
 2
  
  
  
 0
 .
 9
 3
 2
 8
 1
 8
 9
 2
 0
 2
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 3
 7
 1
 1
 0
 :
  
  
 p
 o
 w
 e
 l
 l
  
 n
 t
 h
 i
 t
 e
 r
  
 5
 :
  
 f
 r
 e
 t
  
 =
  
 0
 .
 9
 3
 2
 8
 1
 9
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 3
 7
 1
 1
 0
 :
  
 5
 2
 1
  
  
 4
 .
 0
 0
 6
  
 -
 3
 .
 9
 4
 8
  
 -
 3
 .
 9
 9
 8
  
  
 0
 .
 0
 2
 1
  
 -
 4
 .
 5
 9
 8
  
  
 4
 .
 0
 0
 2
  
  
  
 0
 .
 9
 3
 2
 7
 9
 7
 8
 0
 8
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 5
 6
 6
 5
 8
 :
  
 5
 3
 0
  
  
 4
 .
 0
 0
 6
  
 -
 3
 .
 9
 4
 8
  
 -
 3
 .
 9
 9
 8
  
  
 0
 .
 0
 2
 1
  
 -
 4
 .
 5
 9
 8
  
  
 4
 .
 0
 0
 2
  
  
  
 0
 .
 9
 3
 2
 7
 9
 6
 2
 6
 9
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 8
 7
 0
 9
 5
 :
  
 0
  
  
 -
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
  
 1
 .
 1
 0
 6
 6
 4
 7
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 8
 7
 0
 9
 5
 :
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 .
 0
 0
 0
 0
 0
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 8
 7
 0
 9
 5
 :
  
 0
 .
 0
 7
 1
 1
 0
  
  
 -
 0
 .
 0
 7
 9
 7
 5
  
  
  
 0
 .
 9
 9
 4
 2
 8
  
  
 -
 1
 9
 .
 9
 2
 0
 1
 9
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 8
 7
 0
 9
 5
 :
  
 0
 .
 0
 9
 4
 1
 7
  
  
 -
 0
 .
 9
 9
 1
 8
 1
  
  
 -
 0
 .
 0
 8
 6
 2
 9
  
  
 -
 0
 .
 8
 0
 7
 2
 0
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 8
 7
 0
 9
 5
 :
  
 0
 .
 9
 9
 3
 0
 1
  
  
  
 0
 .
 0
 9
 9
 7
 7
  
  
 -
 0
 .
 0
 6
 3
 0
 1
  
  
 -
 1
 0
 .
 3
 1
 7
 5
 5
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 8
 7
 0
 9
 5
 :
  
 1
  
  
 -
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
  
 1
 .
 0
 3
 9
 0
 6
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 8
 7
 0
 9
 5
 :
  
 2
  
  
 -
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
  
 1
 .
 0
 3
 0
 7
 1
 7
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 8
 7
 0
 9
 5
 :
  
 3
  
  
 -
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
  
 0
 .
 9
 9
 9
 4
 8
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 8
 7
 0
 9
 5
 :
  
 4
  
  
  
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
  
 1
 .
 0
 2
 5
 5
 2
 7
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 8
 7
 0
 9
 5
 :
  
 5
  
  
  
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
  
 1
 .
 0
 1
 4
 6
 9
 7
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 8
 7
 0
 9
 5
 :
  
 6
  
  
  
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
  
 1
 .
 0
 2
 6
 6
 2
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 8
 7
 0
 9
 5
 :
  
 7
  
  
  
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
  
 1
 .
 0
 2
 1
 2
 6
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 8
 7
 0
 9
 5
 :
 C
 o
 m
 p
 u
 t
 i
 n
 g
  
 r
 e
 l
 a
 t
 i
 v
 e
  
 c
 o
 s
 t
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 8
 7
 0
 9
 5
 :
 C
 o
 s
 t
  
  
  
 0
 .
 9
 3
 2
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 8
 7
 0
 9
 5
 :
 C
 t
 x
  
 I
 n
 t
 e
 n
 s
 i
 t
 y
  
  
  
 1
 3
 5
 .
 5
 8
 7
 7
  
 +
 /
 -
  
 2
 0
 4
 .
 5
 2
 5
 2
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 8
 7
 0
 9
 5
 :
 F
 i
 n
 a
 l
  
 c
 o
 s
 t
 s
  
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 8
 7
 0
 9
 5
 :
 M
 i
 n
  
 c
 o
 s
 t
  
 w
 a
 s
  
 0
 .
 9
 3
 2
 7
 9
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 8
 7
 0
 9
 5
 :
 N
 u
 m
 b
 e
 r
  
 o
 f
  
 F
 u
 n
 c
 t
 i
 o
 n
 C
 a
 l
 l
 s
  
  
  
 5
 3
 3
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 8
 7
 0
 9
 5
 :
 N
 u
 m
 b
 e
 r
  
 o
 f
  
 i
 t
 e
 r
 a
 t
 i
 o
 n
 s
  
  
  
  
  
 5
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 8
 7
 0
 9
 5
 :
 N
 u
 m
 b
 e
 r
  
 o
 f
  
 s
 u
 r
 f
 a
 c
 e
  
 h
 i
 t
 s
  
 9
 1
 7
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 8
 7
 0
 9
 5
 :
 O
 p
 t
 i
 m
 i
 z
 a
 t
 i
 o
 n
 T
 i
 m
 e
  
 1
 .
 1
 4
 4
 0
 0
 0
  
 s
 e
 c
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 8
 7
 0
 9
 5
 :
 P
 a
 r
 a
 m
 e
 t
 e
 r
 s
  
 a
 t
  
 o
 p
 t
 i
 m
 u
 m
  
 (
 r
 o
 t
 d
 e
 g
 )
  
  
 0
 .
 0
 2
 1
 4
 0
  
 -
 4
 .
 5
 9
 8
 2
 7
  
  
 4
 .
 0
 0
 2
 0
 0
  
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 8
 7
 0
 9
 5
 :
 P
 a
 r
 a
 m
 e
 t
 e
 r
 s
  
 a
 t
  
 o
 p
 t
 i
 m
 u
 m
  
 (
 t
 r
 a
 n
 s
 m
 m
 )
  
  
 4
 .
 0
 0
 6
 0
 8
  
 -
 3
 .
 9
 4
 7
 9
 7
  
 -
 3
 .
 9
 9
 8
 0
 9
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 8
 7
 0
 9
 5
 :
 P
 c
 t
  
 C
 o
 n
 t
 r
 a
 s
 t
  
  
  
  
  
  
 3
 .
 6
 2
 1
 7
  
 +
 /
 -
  
  
 7
 4
 .
 4
 1
 4
 9
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 8
 7
 0
 9
 5
 :
 P
 o
 w
 e
 l
 l
  
 d
 o
 n
 e
  
 n
 i
 t
 e
 r
 s
  
 =
  
 5
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 8
 7
 0
 9
 5
 :
 R
 E
 L
 :
  
  
 8
  
  
 0
 .
 9
 3
 2
 7
 9
 6
  
  
  
  
 8
 .
 2
 6
 4
 0
 2
 1
  
  
 1
 .
 0
 3
 3
 0
 0
 3
  
 r
 e
 l
  
 =
  
 0
 .
 9
 0
 2
 9
 9
 5
  
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 8
 7
 0
 9
 5
 :
 R
 e
 g
  
 a
 t
  
 m
 i
 n
  
 c
 o
 s
 t
  
 w
 a
 s
  
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 8
 7
 0
 9
 5
 :
 R
 e
 l
 C
 o
 s
 t
  
  
  
 1
 .
 0
 5
 3
 2
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 8
 7
 0
 9
 5
 :
 T
 o
 l
 P
 o
 w
 e
 l
 l
  
 0
 .
 0
 0
 0
 1
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 8
 7
 0
 9
 5
 :
 W
 M
  
  
 I
 n
 t
 e
 n
 s
 i
 t
 y
  
  
  
 1
 3
 4
 .
 2
 1
 8
 8
  
 +
 /
 -
  
 2
 2
 9
 .
 0
 9
 5
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 8
 7
 0
 9
 5
 :
 n
 M
 a
 x
 I
 t
 e
 r
 s
 P
 o
 w
 e
 l
 l
  
 3
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 9
 4
 1
 9
 0
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 9
 4
 1
 9
 0
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 9
 4
 1
 9
 0
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 9
 4
 1
 9
 0
 :
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 9
 4
 1
 9
 0
 :
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 .
 0
 0
 0
 0
 0
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 9
 4
 1
 9
 0
 :
  
 0
 .
 0
 0
 1
 6
 3
  
  
 -
 0
 .
 0
 8
 6
 8
 9
  
  
  
 0
 .
 9
 9
 6
 2
 2
  
  
 -
 1
 4
 .
 9
 3
 1
 9
 6
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 9
 4
 1
 9
 0
 :
  
 0
 .
 0
 0
 6
 8
 9
  
  
 -
 0
 .
 0
 8
 5
 6
 2
  
  
  
 0
 .
 0
 6
 2
 6
 1
  
  
 -
 4
 .
 7
 8
 0
 4
 8
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 9
 4
 1
 9
 0
 :
  
 0
 .
 0
 1
 4
 0
 6
  
  
 -
 0
 .
 9
 9
 6
 1
 2
  
  
 -
 0
 .
 0
 8
 6
 9
 1
  
  
  
 4
 .
 4
 2
 1
 0
 7
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 9
 4
 1
 9
 0
 :
  
 0
 .
 9
 9
 9
 9
 0
  
  
  
 0
 .
 0
 1
 4
 1
 5
  
  
 -
 0
 .
 0
 0
 0
 4
 0
  
  
 -
 1
 5
 .
 0
 9
 8
 0
 3
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 9
 4
 1
 9
 0
 :
 -
 0
 .
 0
 6
 9
 4
 7
  
  
 -
 0
 .
 0
 0
 7
 1
 4
  
  
  
 0
 .
 0
 0
 1
 9
 4
  
  
  
 4
 .
 9
 8
 8
 2
 3
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 9
 4
 1
 9
 0
 :
 -
 0
 .
 0
 8
 0
 1
 2
  
  
 -
 0
 .
 0
 0
 4
 3
 1
  
  
 -
 0
 .
 0
 0
 0
 6
 2
  
  
  
 5
 .
 2
 2
 8
 2
 7
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 9
 4
 1
 9
 0
 :
 O
 r
 i
 g
 i
 n
 a
 l
  
 R
 e
 g
  
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 9
 4
 1
 9
 0
 :
 O
 r
 i
 g
 i
 n
 a
 l
  
 R
 e
 g
  
 -
  
 O
 p
 t
 i
 m
 a
 l
  
 R
 e
 g
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 6
 9
 4
 1
 9
 0
 :
 W
 r
 i
 t
 i
 n
 g
  
 o
 p
 t
 i
 m
 a
 l
  
 r
 e
 g
  
 t
 o
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 b
 b
 r
 .
 p
 a
 s
 s
 1
 .
 d
 a
 t
 ,
  
 t
 y
 p
 e
  
 =
  
 1
 4
  
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 8
 9
 6
 1
 2
 6
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 8
 9
 6
 1
 2
 6
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 8
 9
 6
 1
 2
 6
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 8
 9
 6
 1
 2
 6
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 8
 9
 6
 1
 2
 6
 :
 C
 o
 m
 p
 u
 t
 i
 n
 g
  
 c
 h
 a
 n
 g
 e
  
 i
 n
  
 l
 h
  
 p
 o
 s
 i
 t
 i
 o
 n
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 8
 9
 6
 1
 2
 6
 :
 C
 o
 m
 p
 u
 t
 i
 n
 g
  
 c
 h
 a
 n
 g
 e
  
 i
 n
  
 r
 h
  
 p
 o
 s
 i
 t
 i
 o
 n
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 8
 9
 6
 1
 2
 6
 :
 I
 f
  
 t
 h
 e
  
 m
 o
 v
  
 d
 a
 t
 a
  
 h
 a
 s
  
 a
  
 T
 1
  
 c
 o
 n
 t
 r
 a
 s
 t
 ,
  
 r
 e
 -
 r
 u
 n
  
 w
 i
 t
 h
  
 -
 -
 T
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 8
 9
 6
 1
 2
 6
 :
 L
 H
  
 r
 m
 s
 D
 i
 f
 f
 M
 e
 a
 n
  
 1
 0
 .
 9
 7
 8
 6
 0
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 8
 9
 6
 1
 2
 6
 :
 S
 u
 r
 f
 a
 c
 e
 -
 R
 M
 S
 -
 D
 i
 f
 f
 -
 m
 m
  
 8
 .
 5
 8
 7
 8
 3
 2
  
 3
 .
 0
 7
 6
 6
 2
 2
  
 1
 4
 .
 6
 4
 3
 2
 3
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 8
 9
 6
 1
 2
 6
 :
 W
 A
 R
 N
 I
 N
 G
 :
  
 i
 n
 i
 t
 i
 a
 l
  
 G
 -
 W
  
 c
 o
 n
 t
 r
 a
 s
 t
  
 w
 a
 s
  
 n
 e
 g
 a
 t
 i
 v
 e
 ,
  
 b
 u
 t
  
 e
 x
 p
 e
 c
 t
 e
 d
  
 p
 o
 s
 i
 t
 i
 v
 e
 .
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 7
 .
 8
 9
 6
 1
 2
 6
 :
 m
 r
 i
 _
 s
 e
 g
 r
 e
 g
  
 d
 o
 n
 e
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 7
 2
 7
 1
 2
 :
 m
 r
 i
 _
 s
 e
 g
 r
 e
 g
  
 -
 -
 m
 o
 v
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 t
 e
 m
 p
 l
 a
 t
 e
 .
 n
 i
 i
  
 -
 -
 i
 n
 i
 t
 -
 r
 e
 g
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 b
 b
 r
 .
 p
 a
 s
 s
 1
 .
 d
 a
 t
  
 -
 -
 o
 u
 t
 -
 r
 e
 g
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 _
 b
 b
 r
 e
 g
 _
 s
 u
 b
 -
 b
 m
 .
 d
 a
 t
  
 -
 -
 i
 n
 t
 e
 r
 p
  
 t
 r
 i
 l
 i
 n
 e
 a
 r
  
 -
 -
 w
 m
 -
 p
 r
 o
 j
 -
 a
 b
 s
  
 2
  
 -
 -
 t
 o
 l
  
 1
 e
 -
 8
  
 -
 -
 t
 o
 l
 1
 d
  
 1
 e
 -
 3
  
 -
 -
 c
 0
  
 0
  
 -
 -
 m
 i
 n
 c
 o
 s
 t
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 _
 b
 b
 r
 e
 g
 _
 s
 u
 b
 -
 b
 m
 .
 d
 a
 t
 .
 m
 i
 n
 c
 o
 s
 t
  
 -
 -
 d
 o
 f
  
 6
  
 -
 -
 n
 m
 a
 x
  
 3
 6
  
 -
 -
 p
 a
 r
 a
 m
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 _
 b
 b
 r
 e
 g
 _
 s
 u
 b
 -
 b
 m
 .
 d
 a
 t
 .
 p
 a
 r
 a
 m
  
 -
 -
 s
 u
 r
 f
  
 w
 h
 i
 t
 e
  
 -
 -
 b
 r
 u
 t
 e
  
 -
 0
 .
 1
  
 0
 .
 1
  
 0
 .
 1
  
 -
 -
 c
 u
 r
 -
 r
 e
 g
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 r
 e
 g
 .
 c
 u
 r
 o
 p
 t
 .
 d
 a
 t
  
 -
 -
 g
 m
 -
 p
 r
 o
 j
 -
 f
 r
 a
 c
  
 0
 .
 5
  
 -
 -
 n
 s
 u
 b
  
 1
  
 -
 -
 g
 m
 -
 g
 t
 -
 w
 m
  
 0
 .
 5
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 .
 0
 0
 0
 0
 0
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
  
 0
 .
 0
 7
 1
 1
 0
  
  
 -
 0
 .
 0
 7
 9
 7
 5
  
  
  
 0
 .
 9
 9
 4
 2
 8
  
  
 -
 1
 9
 .
 9
 2
 0
 1
 9
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
  
 0
 .
 0
 9
 4
 1
 7
  
  
 -
 0
 .
 9
 9
 1
 8
 1
  
  
 -
 0
 .
 0
 8
 6
 2
 9
  
  
 -
 0
 .
 8
 0
 7
 2
 0
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
  
 0
 .
 9
 9
 3
 0
 1
  
  
  
 0
 .
 0
 9
 9
 7
 7
  
  
 -
 0
 .
 0
 6
 3
 0
 1
  
  
 -
 1
 0
 .
 3
 1
 7
 5
 5
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 $
 I
 d
 :
  
 m
 r
 i
 _
 s
 e
 g
 r
 e
 g
 .
 c
 ,
 v
  
 1
 .
 1
 1
 3
  
 2
 0
 1
 6
 /
 0
 5
 /
 1
 0
  
 0
 3
 :
 2
 3
 :
 2
 0
  
 g
 r
 e
 v
 e
  
 E
 x
 p
  
 $
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 A
 d
 d
 N
 o
 i
 s
 e
  
  
 0
  
 (
 0
 )
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 G
 M
 P
 r
 o
 j
 F
 r
 a
 c
  
 0
 .
 5
 0
 0
 0
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 G
 d
 i
 a
 g
 _
 n
 o
  
  
 -
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 I
 n
 p
 u
 t
  
 r
 e
 g
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 P
 e
 n
 a
 l
 t
 y
 C
 e
 n
 t
 e
 r
  
 0
 .
 0
 0
 0
 0
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 P
 e
 n
 a
 l
 t
 y
 S
 i
 g
 n
  
  
 -
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 P
 e
 n
 a
 l
 t
 y
 S
 l
 o
 p
 e
  
 0
 .
 5
 0
 0
 0
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 P
 r
 o
 f
 i
 l
 e
  
  
  
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 R
 o
 t
 R
 a
 n
 d
 M
 a
 x
  
 0
 .
 0
 0
 0
 0
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 R
 o
 t
 a
 t
 i
 o
 n
 s
  
  
  
 0
 .
 0
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 S
 y
 n
 t
 h
 S
 e
 e
 d
  
 1
 5
 4
 4
 6
 2
 8
 1
 1
 5
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 T
 o
 l
 P
 o
 w
 e
 l
 l
  
 0
 .
 0
 0
 0
 0
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 T
 r
 a
 n
 s
 R
 a
 n
 d
 M
 a
 x
  
 0
 .
 0
 0
 0
 0
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 T
 r
 a
 n
 s
 l
 a
 t
 i
 o
 n
 s
  
 0
 .
 0
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 U
 s
 e
 L
 H
  
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 U
 s
 e
 M
 a
 s
 k
  
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 U
 s
 e
 R
 H
  
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 W
 M
 P
 r
 o
 j
 A
 b
 s
  
 2
 .
 0
 0
 0
 0
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 c
 d
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 d
 o
 f
  
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 f
 r
 a
 m
 e
  
  
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 h
 o
 s
 t
 n
 a
 m
 e
  
 9
 9
 5
 8
 f
 5
 f
 d
 3
 b
 a
 7
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 i
 n
 t
 e
 r
 p
  
  
 t
 r
 i
 l
 i
 n
 e
 a
 r
  
 (
 1
 )
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 l
 h
 c
 o
 s
 t
 f
 i
 l
 e
  
 (
 n
 u
 l
 l
 )
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 m
 a
 c
 h
 i
 n
 e
  
  
 x
 8
 6
 _
 6
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 m
 o
 v
 v
 o
 l
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 t
 e
 m
 p
 l
 a
 t
 e
 .
 n
 i
 i
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 m
 r
 i
 _
 s
 e
 g
 r
 e
 g
  
 -
 -
 m
 o
 v
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 t
 e
 m
 p
 l
 a
 t
 e
 .
 n
 i
 i
  
 -
 -
 i
 n
 i
 t
 -
 r
 e
 g
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 b
 b
 r
 .
 p
 a
 s
 s
 1
 .
 d
 a
 t
  
 -
 -
 o
 u
 t
 -
 r
 e
 g
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 _
 b
 b
 r
 e
 g
 _
 s
 u
 b
 -
 b
 m
 .
 d
 a
 t
  
 -
 -
 i
 n
 t
 e
 r
 p
  
 t
 r
 i
 l
 i
 n
 e
 a
 r
  
 -
 -
 w
 m
 -
 p
 r
 o
 j
 -
 a
 b
 s
  
 2
  
 -
 -
 t
 o
 l
  
 1
 e
 -
 8
  
 -
 -
 t
 o
 l
 1
 d
  
 1
 e
 -
 3
  
 -
 -
 c
 0
  
 0
  
 -
 -
 m
 i
 n
 c
 o
 s
 t
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 _
 b
 b
 r
 e
 g
 _
 s
 u
 b
 -
 b
 m
 .
 d
 a
 t
 .
 m
 i
 n
 c
 o
 s
 t
  
 -
 -
 d
 o
 f
  
 6
  
 -
 -
 n
 m
 a
 x
  
 3
 6
  
 -
 -
 p
 a
 r
 a
 m
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 _
 b
 b
 r
 e
 g
 _
 s
 u
 b
 -
 b
 m
 .
 d
 a
 t
 .
 p
 a
 r
 a
 m
  
 -
 -
 s
 u
 r
 f
  
 w
 h
 i
 t
 e
  
 -
 -
 b
 r
 u
 t
 e
  
 -
 0
 .
 1
  
 0
 .
 1
  
 0
 .
 1
  
 -
 -
 c
 u
 r
 -
 r
 e
 g
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 r
 e
 g
 .
 c
 u
 r
 o
 p
 t
 .
 d
 a
 t
  
 -
 -
 g
 m
 -
 p
 r
 o
 j
 -
 f
 r
 a
 c
  
 0
 .
 5
  
 -
 -
 n
 s
 u
 b
  
 1
  
 -
 -
 g
 m
 -
 g
 t
 -
 w
 m
  
 0
 .
 5
  
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 n
 1
 d
 m
 i
 n
  
  
 3
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 n
 M
 a
 x
 I
 t
 e
 r
 s
 P
 o
 w
 e
 l
 l
  
 3
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 n
 s
 u
 b
 s
 a
 m
 p
  
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 o
 u
 t
 r
 e
 g
 f
 i
 l
 e
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 _
 b
 b
 r
 e
 g
 _
 s
 u
 b
 -
 b
 m
 .
 d
 a
 t
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 r
 e
 g
 f
 i
 l
 e
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 b
 b
 r
 .
 p
 a
 s
 s
 1
 .
 d
 a
 t
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 r
 h
 c
 o
 s
 t
 f
 i
 l
 e
  
 (
 n
 u
 l
 l
 )
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 s
 e
 t
 e
 n
 v
  
 S
 U
 B
 J
 E
 C
 T
 S
 _
 D
 I
 R
  
 /
 d
 e
 r
 i
 v
 a
 t
 i
 v
 e
 s
 /
 f
 r
 e
 e
 s
 u
 r
 f
 e
 r
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 s
 u
 b
 j
 e
 c
 t
  
 s
 u
 b
 -
 b
 m
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 s
 u
 r
 f
 n
 a
 m
 e
  
 w
 h
 i
 t
 e
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 s
 y
 s
 n
 a
 m
 e
  
  
 L
 i
 n
 u
 x
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 8
 6
 0
 0
 1
 :
 u
 s
 e
 r
  
  
  
  
  
 r
 o
 o
 t
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 3
 8
 .
 0
 9
 5
 6
 8
 1
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 4
 4
 .
 1
 7
 8
 1
 6
 8
 :
 L
 o
 a
 d
 i
 n
 g
  
 l
 h
 .
 t
 h
 i
 c
 k
 n
 e
 s
 s
  
 f
 o
 r
  
 G
 M
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 4
 4
 .
 1
 7
 8
 1
 6
 8
 :
 L
 o
 a
 d
 i
 n
 g
  
 l
 h
 .
 w
 h
 i
 t
 e
  
 s
 u
 r
 f
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 4
 4
 .
 1
 7
 8
 1
 6
 8
 :
 L
 o
 a
 d
 i
 n
 g
  
 m
 o
 v
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 4
 4
 .
 1
 7
 8
 1
 6
 8
 :
 P
 r
 o
 j
 e
 c
 t
 i
 n
 g
  
 L
 H
  
 S
 u
 r
 f
 s
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 4
 9
 .
 1
 8
 8
 1
 8
 2
 :
 G
 M
  
 P
 r
 o
 j
 :
  
 1
  
 0
 .
 5
 0
 0
 0
 0
 0
  
 2
 .
 0
 0
 0
 0
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 4
 9
 .
 1
 8
 8
 1
 8
 2
 :
 L
 o
 a
 d
 i
 n
 g
  
 r
 h
 .
 t
 h
 i
 c
 k
 n
 e
 s
 s
  
 f
 o
 r
  
 G
 M
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 4
 9
 .
 1
 8
 8
 1
 8
 2
 :
 L
 o
 a
 d
 i
 n
 g
  
 r
 h
 .
 w
 h
 i
 t
 e
  
 s
 u
 r
 f
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 4
 9
 .
 1
 8
 8
 1
 8
 2
 :
 P
 r
 o
 j
 e
 c
 t
 i
 n
 g
  
 R
 H
  
 S
 u
 r
 f
 s
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 4
 9
 .
 1
 8
 8
 1
 8
 2
 :
 W
 M
  
 P
 r
 o
 j
 :
  
 0
  
 0
 .
 5
 0
 0
 0
 0
 0
  
 2
 .
 0
 0
 0
 0
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 0
 .
 8
 1
 5
 1
 0
 2
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 0
 .
 8
 1
 5
 1
 0
 2
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 0
 .
 8
 1
 5
 1
 0
 2
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 0
 .
 8
 1
 5
 1
 0
 2
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 0
 .
 8
 1
 5
 1
 0
 2
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 0
 .
 8
 1
 5
 1
 0
 2
 :
  
 0
  
  
 -
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
  
 1
 .
 0
 4
 2
 7
 4
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 0
 .
 8
 1
 5
 1
 0
 2
 :
  
 1
  
  
 -
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
  
 1
 .
 0
 2
 0
 5
 3
 3
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 0
 .
 8
 1
 5
 1
 0
 2
 :
  
 2
  
  
 -
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
  
 1
 .
 0
 4
 1
 1
 1
 7
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 0
 .
 8
 1
 5
 1
 0
 2
 :
  
 3
  
  
 -
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
  
 1
 .
 0
 2
 8
 0
 5
 3
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 0
 .
 8
 1
 5
 1
 0
 2
 :
  
 4
  
  
  
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
  
 1
 .
 0
 3
 8
 2
 0
 3
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 0
 .
 8
 1
 5
 1
 0
 2
 :
  
 5
  
  
  
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
  
 1
 .
 0
 3
 1
 5
 7
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 0
 .
 8
 1
 5
 1
 0
 2
 :
  
 6
  
  
  
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
  
 1
 .
 0
 3
 7
 5
 4
 9
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 0
 .
 8
 1
 5
 1
 0
 2
 :
  
 7
  
  
  
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
  
 1
 .
 0
 4
 0
 4
 1
 3
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 0
 .
 8
 1
 5
 1
 0
 2
 :
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 0
 .
 8
 1
 5
 1
 0
 2
 :
 B
 r
 u
 t
 e
  
 f
 o
 r
 c
 e
  
 p
 r
 e
 o
 p
 t
  
 -
 0
 .
 1
  
 0
 .
 1
  
 0
 .
 1
 ,
  
 n
  
 =
  
 7
 2
 9
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 0
 .
 8
 1
 5
 1
 0
 2
 :
 C
 o
 m
 p
 u
 t
 i
 n
 g
  
 r
 e
 l
 a
 t
 i
 v
 e
  
 c
 o
 s
 t
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 0
 .
 8
 1
 5
 1
 0
 2
 :
 C
 o
 s
 t
  
  
  
 1
 .
 0
 2
 6
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 0
 .
 8
 1
 5
 1
 0
 2
 :
 C
 t
 x
  
 I
 n
 t
 e
 n
 s
 i
 t
 y
  
  
  
 1
 3
 7
 .
 2
 3
 3
 9
  
 +
 /
 -
  
 2
 1
 7
 .
 5
 2
 0
 3
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 0
 .
 8
 1
 5
 1
 0
 2
 :
 I
 f
  
 t
 h
 e
  
 m
 o
 v
  
 d
 a
 t
 a
  
 h
 a
 s
  
 a
  
 T
 1
  
 c
 o
 n
 t
 r
 a
 s
 t
 ,
  
 r
 e
 -
 r
 u
 n
  
 w
 i
 t
 h
  
 -
 -
 T
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 0
 .
 8
 1
 5
 1
 0
 2
 :
 I
 n
 i
 t
 i
 a
 l
  
 c
 o
 s
 t
 s
  
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 0
 .
 8
 1
 5
 1
 0
 2
 :
 N
 u
 m
 b
 e
 r
  
 o
 f
  
 s
 u
 r
 f
 a
 c
 e
  
 h
 i
 t
 s
  
 9
 0
 4
 6
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 0
 .
 8
 1
 5
 1
 0
 2
 :
 P
 c
 t
  
 C
 o
 n
 t
 r
 a
 s
 t
  
  
  
  
  
 -
 0
 .
 5
 6
 3
 7
  
 +
 /
 -
  
  
 7
 6
 .
 8
 1
 4
 5
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 0
 .
 8
 1
 5
 1
 0
 2
 :
 P
 r
 o
 j
 e
 c
 t
 i
 n
 g
  
 R
 H
  
 S
 u
 r
 f
 s
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 0
 .
 8
 1
 5
 1
 0
 2
 :
 R
 E
 L
 :
  
  
 8
  
  
 1
 .
 0
 2
 6
 8
 4
 8
  
  
  
  
 8
 .
 2
 8
 0
 1
 8
 6
  
  
 1
 .
 0
 3
 5
 0
 2
 3
  
 r
 e
 l
  
 =
  
 0
 .
 9
 9
 2
 1
 0
 1
  
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 0
 .
 8
 1
 5
 1
 0
 2
 :
 R
 e
 l
 C
 o
 s
 t
  
  
  
 0
 .
 9
 9
 2
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 0
 .
 8
 1
 5
 1
 0
 2
 :
 U
 s
 i
 n
 g
  
 l
 h
 .
 c
 o
 r
 t
 e
 x
 .
 l
 a
 b
 e
 l
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 0
 .
 8
 1
 5
 1
 0
 2
 :
 U
 s
 i
 n
 g
  
 r
 h
 .
 c
 o
 r
 t
 e
 x
 .
 l
 a
 b
 e
 l
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 0
 .
 8
 1
 5
 1
 0
 2
 :
 W
 A
 R
 N
 I
 N
 G
 :
  
 i
 n
 i
 t
 i
 a
 l
  
 G
 -
 W
  
 c
 o
 n
 t
 r
 a
 s
 t
  
 i
 s
  
 n
 e
 g
 a
 t
 i
 v
 e
 ,
  
 b
 u
 t
  
 e
 x
 p
 e
 c
 t
 i
 n
 g
  
 p
 o
 s
 i
 t
 i
 v
 e
 .
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 0
 .
 8
 1
 5
 1
 0
 2
 :
 W
 M
  
  
 I
 n
 t
 e
 n
 s
 i
 t
 y
  
  
  
 1
 3
 9
 .
 1
 7
 3
 8
  
 +
 /
 -
  
 2
 2
 1
 .
 8
 4
 5
 2
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 0
 .
 8
 1
 8
 7
 9
 7
 :
  
  
  
  
  
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
  
  
  
  
 0
 .
 9
 4
 8
 8
  
  
  
 0
 .
 9
 4
 8
 8
  
  
 0
 .
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 0
 .
 8
 2
 5
 5
 8
 4
 :
  
  
  
  
  
 3
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
  
  
  
  
 0
 .
 9
 4
 2
 0
  
  
  
 0
 .
 9
 4
 2
 0
  
  
 0
 .
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 0
 .
 9
 3
 3
 2
 9
 6
 :
  
  
  
  
 5
 4
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
  
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
  
  
  
  
 0
 .
 9
 4
 0
 7
  
  
  
 0
 .
 9
 4
 0
 7
  
  
 0
 .
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 0
 .
 9
 5
 2
 7
 9
 7
 :
  
  
  
  
 6
 3
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
  
 0
 .
 1
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
  
  
  
  
 0
 .
 9
 2
 8
 8
  
  
  
 0
 .
 9
 2
 8
 8
  
  
 0
 .
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 1
 .
 6
 8
 0
 0
 7
 5
 :
  
  
  
 4
 0
 8
  
  
  
 0
 .
 0
 0
 0
 0
  
  
  
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
  
  
  
  
 0
 .
 9
 2
 6
 4
  
  
  
 0
 .
 9
 2
 6
 4
  
  
 0
 .
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 2
 .
 0
 2
 8
 9
 8
 0
 :
  
  
  
 5
 7
 4
  
  
  
 0
 .
 1
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
  
 0
 .
 1
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
  
  
  
  
 0
 .
 9
 2
 5
 5
  
  
  
 0
 .
 9
 2
 5
 5
  
  
 0
 .
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 2
 .
 0
 5
 2
 2
 9
 8
 :
  
  
  
 5
 8
 5
  
  
  
 0
 .
 1
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
  
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
  
  
  
  
 0
 .
 9
 2
 4
 2
  
  
  
 0
 .
 9
 2
 4
 2
  
  
 0
 .
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 2
 .
 0
 7
 7
 8
 0
 5
 :
  
  
  
 5
 9
 7
  
  
  
 0
 .
 1
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
  
  
  
  
 0
 .
 9
 2
 2
 6
  
  
  
 0
 .
 9
 2
 2
 6
  
  
 0
 .
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 2
 .
 0
 8
 4
 2
 2
 4
 :
  
  
  
 6
 0
 0
  
  
  
 0
 .
 1
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
  
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
  
  
  
  
 0
 .
 9
 2
 2
 2
  
  
  
 0
 .
 9
 2
 2
 2
  
  
 0
 .
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 3
 .
 0
 9
 0
 1
 1
 2
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 3
 .
 0
 9
 0
 1
 1
 2
 :
  
  
  
 7
  
  
 0
 .
 1
 8
 6
  
  
 0
 .
 0
 0
 0
  
  
 0
 .
 0
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
 0
 .
 1
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
  
 1
 .
 0
 2
 5
 9
 7
 0
 1
 5
 3
 9
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 3
 .
 0
 9
 0
 1
 1
 2
 :
  
  
 0
 .
 1
 0
 0
  
  
  
 0
 .
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
 0
 .
 1
 0
 0
  
 -
 0
 .
 1
 0
 0
  
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 3
 .
 0
 9
 0
 1
 1
 2
 :
  
  
 f
 t
 o
 l
  
  
  
 0
 .
 0
 0
 0
 0
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 3
 .
 0
 9
 0
 1
 1
 2
 :
  
  
 l
 i
 n
 m
 i
 n
 _
 x
 t
 o
 l
 _
  
  
  
 0
 .
 0
 0
 1
 0
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 3
 .
 0
 9
 0
 1
 1
 2
 :
  
  
 m
 a
 x
 f
 e
 v
  
 3
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 3
 .
 0
 9
 0
 1
 1
 2
 :
  
  
 n
 p
 a
 r
 a
 m
 s
  
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 3
 .
 0
 9
 0
 1
 1
 2
 :
  
  
 p
 o
 w
 e
 l
 l
  
 n
 t
 h
 i
 t
 e
 r
  
 0
 :
  
 f
 r
 e
 t
  
 =
  
 1
 .
 0
 2
 6
 8
 4
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 3
 .
 0
 9
 0
 1
 1
 2
 :
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 3
 .
 0
 9
 0
 1
 1
 2
 :
 0
  
 0
 .
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 3
 .
 0
 9
 0
 1
 1
 2
 :
 1
  
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 3
 .
 0
 9
 0
 1
 1
 2
 :
 2
  
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 3
 .
 0
 9
 0
 1
 1
 2
 :
 3
  
 -
 0
 .
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 3
 .
 0
 9
 0
 1
 1
 2
 :
 4
  
 0
 .
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 3
 .
 0
 9
 0
 1
 1
 2
 :
 5
  
 -
 0
 .
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 3
 .
 0
 9
 0
 1
 1
 2
 :
 B
 r
 u
 t
 e
  
 F
 o
 r
 c
 e
  
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 3
 .
 0
 9
 0
 1
 1
 2
 :
 I
 n
 i
 t
  
 P
 o
 w
 e
 l
  
 P
 a
 r
 a
 m
 s
  
 d
 o
 f
  
 =
  
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 3
 .
 0
 9
 0
 1
 1
 2
 :
 M
 i
 n
  
 c
 o
 s
 t
  
 w
 a
 s
  
 0
 .
 9
 2
 2
 2
 1
 9
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 3
 .
 0
 9
 0
 1
 1
 2
 :
 N
 u
 m
 b
 e
 r
  
 o
 f
  
 i
 t
 e
 r
 a
 t
 i
 o
 n
 s
  
  
  
 7
 2
 9
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 3
 .
 0
 9
 0
 1
 1
 2
 :
 P
 a
 r
 a
 m
 e
 t
 e
 r
 s
  
 a
 t
  
 b
 e
 s
 t
  
 (
 t
 r
 a
 n
 s
 m
 m
 ,
  
 r
 o
 t
 d
 e
 g
 )
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 3
 .
 0
 9
 0
 1
 1
 2
 :
 S
 e
 a
 r
 c
 h
  
 t
 i
 m
 e
  
 1
 .
 5
 4
 2
 0
 0
 0
  
 s
 e
 c
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 3
 .
 0
 9
 0
 1
 1
 2
 :
 S
 t
 a
 r
 t
 i
 n
 g
  
 P
 o
 w
 e
 l
 l
  
 M
 i
 n
 i
 m
 i
 z
 a
 t
 i
 o
 n
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 3
 .
 0
 9
 0
 1
 1
 2
 :
 f
 s
 _
 p
 o
 w
 e
 l
 l
 :
 :
 m
 i
 n
 i
 m
 i
 z
 e
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 3
 .
 3
 6
 5
 4
 3
 2
 :
  
  
 1
 0
  
  
 0
 .
 1
 5
 3
  
  
 0
 .
 0
 0
 0
  
  
 0
 .
 0
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
 0
 .
 1
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
  
 1
 .
 0
 2
 5
 7
 1
 5
 1
 1
 4
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 3
 .
 4
 5
 7
 0
 4
 0
 :
  
  
 1
 1
  
  
 0
 .
 1
 4
 0
  
  
 0
 .
 0
 0
 0
  
  
 0
 .
 0
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
 0
 .
 1
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
  
 1
 .
 0
 2
 5
 6
 7
 1
 2
 6
 4
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 3
 .
 6
 3
 9
 8
 2
 1
 :
  
  
 1
 3
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 0
 0
 0
  
  
 0
 .
 0
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
 0
 .
 1
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
  
 1
 .
 0
 2
 5
 6
 1
 4
 9
 5
 5
 3
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 4
 .
 0
 0
 5
 4
 3
 9
 :
  
  
 1
 7
  
  
 0
 .
 1
 4
 5
  
  
 1
 .
 0
 0
 0
  
  
 0
 .
 0
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
 0
 .
 1
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
  
 1
 .
 0
 2
 3
 0
 6
 7
 0
 5
 7
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 4
 .
 3
 7
 1
 5
 3
 4
 :
  
  
 2
 1
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 6
 1
 8
  
  
 0
 .
 0
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
 0
 .
 1
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
  
 1
 .
 0
 2
 2
 5
 2
 6
 2
 7
 7
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 4
 .
 4
 6
 3
 2
 6
 5
 :
  
  
 2
 2
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 6
 5
 0
  
  
 0
 .
 0
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
 0
 .
 1
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
  
 1
 .
 0
 2
 2
 1
 4
 1
 0
 3
 0
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 4
 .
 6
 4
 6
 2
 5
 9
 :
  
  
 2
 4
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 7
 0
 4
  
  
 0
 .
 0
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
 0
 .
 1
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
  
 1
 .
 0
 2
 1
 8
 7
 9
 9
 1
 8
 3
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 4
 .
 7
 3
 8
 3
 3
 0
 :
  
  
 2
 5
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 7
 0
 6
  
  
 0
 .
 0
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
 0
 .
 1
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
  
 1
 .
 0
 2
 1
 8
 0
 6
 2
 8
 8
 2
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 4
 .
 8
 3
 0
 0
 8
 6
 :
  
  
 2
 6
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 7
 3
 8
  
  
 0
 .
 0
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
 0
 .
 1
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
  
 1
 .
 0
 2
 1
 5
 8
 9
 7
 5
 5
 5
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 4
 .
 9
 2
 1
 5
 3
 9
 :
  
  
 2
 7
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 7
 2
 6
  
  
 0
 .
 0
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
 0
 .
 1
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
  
 1
 .
 0
 2
 1
 5
 6
 6
 9
 0
 1
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 5
 .
 0
 1
 3
 3
 3
 4
 :
  
  
 2
 8
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 7
 3
 0
  
  
 0
 .
 0
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
 0
 .
 1
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
  
 1
 .
 0
 2
 1
 5
 6
 6
 6
 1
 7
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 5
 .
 1
 9
 6
 4
 9
 7
 :
  
  
 3
 0
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 7
 3
 3
  
  
 0
 .
 0
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
 0
 .
 1
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
  
 1
 .
 0
 2
 1
 5
 6
 1
 1
 2
 7
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 5
 .
 9
 2
 8
 3
 9
 4
 :
  
  
 3
 8
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 7
 3
 3
  
  
 0
 .
 3
 8
 2
  
 -
 0
 .
 1
 0
 0
  
  
 0
 .
 1
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
  
 1
 .
 0
 1
 9
 2
 5
 2
 0
 4
 0
 7
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 6
 .
 1
 1
 1
 3
 9
 1
 :
  
  
 4
 0
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 7
 3
 3
  
  
 0
 .
 2
 4
 0
  
 -
 0
 .
 1
 0
 0
  
  
 0
 .
 1
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
  
 1
 .
 0
 1
 7
 7
 5
 1
 7
 4
 8
 5
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 8
 .
 3
 0
 4
 9
 8
 5
 :
  
  
 6
 4
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 7
 3
 3
  
  
 0
 .
 2
 4
 0
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
  
 1
 .
 0
 1
 7
 7
 3
 2
 2
 4
 8
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 9
 .
 6
 7
 8
 6
 5
 6
 :
  
  
 7
 9
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 7
 3
 3
  
  
 0
 .
 2
 4
 0
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 0
 0
  
  
 0
 .
 9
 0
 0
  
  
  
 1
 .
 0
 1
 6
 1
 5
 6
 0
 2
 7
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 5
 :
 5
 9
 .
 9
 5
 4
 5
 3
 7
 :
  
  
 8
 2
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 7
 3
 3
  
  
 0
 .
 2
 4
 0
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 0
 0
  
  
 1
 .
 5
 1
 8
  
  
  
 1
 .
 0
 1
 5
 4
 7
 5
 5
 4
 1
 3
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 0
 0
 .
 3
 2
 0
 9
 9
 1
 :
  
  
 8
 6
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 7
 3
 3
  
  
 0
 .
 2
 4
 0
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 0
 0
  
  
 1
 .
 4
 1
 8
  
  
  
 1
 .
 0
 1
 5
 0
 4
 0
 2
 9
 2
 9
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 0
 0
 .
 5
 0
 4
 0
 4
 4
 :
  
  
 8
 8
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 7
 3
 3
  
  
 0
 .
 2
 4
 0
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 0
 0
  
  
 1
 .
 4
 5
 6
  
  
  
 1
 .
 0
 1
 4
 5
 8
 0
 3
 5
 5
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 0
 0
 .
 6
 8
 7
 4
 1
 1
 :
  
  
 9
 0
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 7
 3
 3
  
  
 0
 .
 2
 4
 0
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 0
 0
  
  
 1
 .
 4
 4
 3
  
  
  
 1
 .
 0
 1
 4
 5
 5
 2
 5
 8
 3
 3
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 0
 0
 .
 8
 7
 0
 4
 4
 8
 :
  
  
 9
 2
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 7
 3
 3
  
  
 0
 .
 2
 4
 0
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 0
 0
  
  
 1
 .
 4
 4
 8
  
  
  
 1
 .
 0
 1
 4
 5
 2
 6
 0
 2
 0
 3
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 0
 0
 .
 9
 6
 2
 0
 8
 4
 :
  
  
 9
 3
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 7
 3
 3
  
  
 0
 .
 2
 4
 0
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 0
 0
  
  
 1
 .
 4
 4
 9
  
  
  
 1
 .
 0
 1
 4
 5
 2
 3
 1
 4
 6
 2
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 0
 1
 .
 1
 7
 2
 6
 9
 0
 :
  
  
 9
 5
  
  
 0
 .
 1
 9
 0
  
  
 1
 .
 4
 6
 6
  
  
 0
 .
 4
 8
 1
  
 -
 0
 .
 0
 9
 8
  
  
 0
 .
 1
 0
 0
  
  
 2
 .
 9
 9
 7
  
  
  
 1
 .
 0
 1
 3
 7
 6
 1
 1
 9
 3
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 0
 3
 .
 2
 1
 8
 1
 0
 7
 :
  
  
 p
 o
 w
 e
 l
 l
  
 n
 t
 h
 i
 t
 e
 r
  
 1
 :
  
 f
 r
 e
 t
  
 =
  
 1
 .
 0
 1
 4
 5
 2
 3
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 0
 3
 .
 2
 1
 8
 1
 0
 7
 :
  
 1
 1
 7
  
 -
 0
 .
 3
 5
 5
  
  
 1
 .
 7
 3
 3
  
  
 0
 .
 2
 4
 0
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 0
 0
  
  
 1
 .
 4
 4
 9
  
  
  
 1
 .
 0
 1
 3
 4
 3
 7
 9
 5
 1
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 0
 3
 .
 9
 4
 8
 6
 7
 8
 :
  
 1
 2
 5
  
 -
 0
 .
 3
 5
 5
  
  
 1
 .
 7
 7
 4
  
  
 0
 .
 2
 4
 0
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 0
 0
  
  
 1
 .
 4
 4
 9
  
  
  
 1
 .
 0
 1
 3
 1
 0
 3
 1
 6
 1
 7
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 0
 4
 .
 0
 4
 0
 3
 4
 9
 :
  
 1
 2
 6
  
 -
 0
 .
 3
 5
 5
  
  
 1
 .
 7
 7
 3
  
  
 0
 .
 2
 4
 0
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 0
 0
  
  
 1
 .
 4
 4
 9
  
  
  
 1
 .
 0
 1
 3
 1
 0
 0
 3
 7
 7
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 0
 4
 .
 8
 9
 3
 9
 2
 5
 :
  
 1
 3
 5
  
 -
 0
 .
 3
 5
 5
  
  
 1
 .
 7
 7
 3
  
  
 0
 .
 1
 4
 1
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 0
 0
  
  
 1
 .
 4
 4
 9
  
  
  
 1
 .
 0
 1
 1
 8
 0
 4
 1
 8
 5
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 0
 5
 .
 0
 7
 7
 3
 3
 1
 :
  
 1
 3
 7
  
 -
 0
 .
 3
 5
 5
  
  
 1
 .
 7
 7
 3
  
  
 0
 .
 1
 2
 5
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 0
 0
  
  
 1
 .
 4
 4
 9
  
  
  
 1
 .
 0
 1
 1
 3
 8
 3
 6
 2
 3
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 0
 7
 .
 7
 7
 0
 0
 0
 8
 :
  
 1
 6
 6
  
 -
 0
 .
 3
 5
 5
  
  
 1
 .
 7
 7
 3
  
  
 0
 .
 1
 2
 5
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 1
 3
  
  
 1
 .
 4
 4
 9
  
  
  
 1
 .
 0
 1
 1
 2
 9
 5
 1
 8
 4
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 0
 8
 .
 0
 4
 5
 2
 1
 8
 :
  
 1
 6
 9
  
 -
 0
 .
 3
 5
 5
  
  
 1
 .
 7
 7
 3
  
  
 0
 .
 1
 2
 5
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 1
 0
  
  
 1
 .
 4
 4
 9
  
  
  
 1
 .
 0
 1
 1
 2
 7
 0
 9
 5
 5
 2
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 0
 8
 .
 9
 6
 2
 3
 6
 2
 :
  
 1
 7
 9
  
 -
 0
 .
 3
 5
 5
  
  
 1
 .
 7
 7
 3
  
  
 0
 .
 1
 2
 5
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 1
 0
  
  
 1
 .
 4
 6
 1
  
  
  
 1
 .
 0
 1
 1
 0
 9
 1
 7
 2
 5
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 0
 9
 .
 0
 5
 5
 7
 0
 3
 :
  
 1
 8
 0
  
 -
 0
 .
 3
 5
 5
  
  
 1
 .
 7
 7
 3
  
  
 0
 .
 1
 2
 5
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 1
 0
  
  
 1
 .
 4
 6
 3
  
  
  
 1
 .
 0
 1
 1
 0
 9
 1
 0
 1
 3
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 1
 0
 .
 2
 4
 6
 5
 9
 9
 :
  
  
 p
 o
 w
 e
 l
 l
  
 n
 t
 h
 i
 t
 e
 r
  
 2
 :
  
 f
 r
 e
 t
  
 =
  
 1
 .
 0
 1
 1
 0
 9
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 1
 0
 .
 2
 4
 6
 5
 9
 9
 :
  
 1
 9
 3
  
 -
 0
 .
 3
 5
 3
  
  
 1
 .
 7
 7
 3
  
  
 0
 .
 1
 2
 5
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 1
 0
  
  
 1
 .
 4
 6
 3
  
  
  
 1
 .
 0
 1
 1
 0
 4
 8
 6
 7
 5
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 1
 0
 .
 3
 3
 8
 4
 2
 7
 :
  
 1
 9
 4
  
 -
 0
 .
 3
 4
 7
  
  
 1
 .
 7
 7
 3
  
  
 0
 .
 1
 2
 5
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 1
 0
  
  
 1
 .
 4
 6
 3
  
  
  
 1
 .
 0
 1
 1
 0
 3
 7
 9
 5
 9
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 1
 0
 .
 5
 2
 2
 2
 3
 1
 :
  
 1
 9
 6
  
 -
 0
 .
 3
 5
 0
  
  
 1
 .
 7
 7
 3
  
  
 0
 .
 1
 2
 5
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 1
 0
  
  
 1
 .
 4
 6
 3
  
  
  
 1
 .
 0
 1
 1
 0
 1
 7
 3
 6
 6
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 1
 0
 .
 7
 3
 2
 2
 8
 2
 :
  
 1
 9
 8
  
 -
 0
 .
 3
 4
 9
  
  
 1
 .
 7
 7
 3
  
  
 0
 .
 1
 2
 5
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 1
 0
  
  
 1
 .
 4
 6
 3
  
  
  
 1
 .
 0
 1
 1
 0
 1
 1
 2
 7
 6
 2
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 1
 1
 .
 7
 4
 0
 2
 5
 3
 :
  
 2
 0
 9
  
 -
 0
 .
 3
 4
 9
  
  
 1
 .
 7
 7
 2
  
  
 0
 .
 1
 2
 5
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 1
 0
  
  
 1
 .
 4
 6
 3
  
  
  
 1
 .
 0
 1
 1
 0
 0
 9
 9
 7
 6
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 1
 2
 .
 9
 3
 2
 1
 2
 5
 :
  
 2
 2
 2
  
 -
 0
 .
 3
 4
 9
  
  
 1
 .
 7
 7
 2
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 1
 0
  
  
 1
 .
 4
 6
 3
  
  
  
 1
 .
 0
 1
 1
 0
 0
 2
 2
 2
 7
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 1
 4
 .
 0
 3
 3
 1
 8
 7
 :
  
 2
 3
 4
  
 -
 0
 .
 3
 4
 9
  
  
 1
 .
 7
 7
 2
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 1
 0
  
  
 1
 .
 4
 6
 3
  
  
  
 1
 .
 0
 1
 0
 9
 8
 7
 2
 2
 4
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 1
 5
 .
 4
 0
 7
 1
 4
 7
 :
  
 2
 4
 9
  
 -
 0
 .
 3
 4
 9
  
  
 1
 .
 7
 7
 2
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 1
 5
  
  
 1
 .
 4
 6
 3
  
  
  
 1
 .
 0
 1
 0
 9
 7
 3
 0
 5
 7
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 1
 5
 .
 5
 9
 1
 2
 8
 6
 :
  
 2
 5
 1
  
 -
 0
 .
 3
 4
 9
  
  
 1
 .
 7
 7
 2
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 1
 4
  
  
 1
 .
 4
 6
 3
  
  
  
 1
 .
 0
 1
 0
 9
 4
 7
 0
 8
 0
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 1
 5
 .
 6
 8
 3
 0
 1
 3
 :
  
 2
 5
 2
  
 -
 0
 .
 3
 4
 9
  
  
 1
 .
 7
 7
 2
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 1
 2
  
  
 1
 .
 4
 6
 3
  
  
  
 1
 .
 0
 1
 0
 9
 2
 7
 3
 9
 3
 3
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 1
 6
 .
 8
 7
 4
 5
 5
 6
 :
  
 2
 6
 5
  
 -
 0
 .
 3
 4
 9
  
  
 1
 .
 7
 7
 2
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 1
 2
  
  
 1
 .
 4
 6
 6
  
  
  
 1
 .
 0
 1
 0
 9
 1
 3
 9
 9
 1
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 1
 9
 .
 2
 6
 0
 6
 6
 0
 :
  
  
 p
 o
 w
 e
 l
 l
  
 n
 t
 h
 i
 t
 e
 r
  
 3
 :
  
 f
 r
 e
 t
  
 =
  
 1
 .
 0
 1
 0
 9
 1
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 1
 9
 .
 2
 6
 0
 6
 6
 0
 :
  
 2
 9
 1
  
 -
 0
 .
 3
 4
 9
  
  
 1
 .
 7
 7
 4
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 1
 2
  
  
 1
 .
 4
 6
 6
  
  
  
 1
 .
 0
 1
 0
 9
 0
 5
 6
 6
 0
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 2
 4
 .
 4
 8
 6
 8
 9
 7
 :
  
 3
 4
 8
  
 -
 0
 .
 3
 4
 9
  
  
 1
 .
 7
 7
 4
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 1
 2
  
  
 1
 .
 4
 6
 8
  
  
  
 1
 .
 0
 1
 0
 9
 0
 5
 0
 6
 0
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 2
 5
 .
 2
 3
 6
 8
 8
 8
 :
  
 3
 5
 6
  
 -
 0
 .
 3
 4
 9
  
  
 1
 .
 7
 7
 5
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 1
 2
  
  
 1
 .
 4
 6
 8
  
  
  
 1
 .
 0
 1
 0
 9
 0
 4
 9
 5
 9
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 2
 5
 .
 3
 2
 8
 7
 4
 2
 :
  
 3
 5
 7
  
 -
 0
 .
 3
 4
 9
  
  
 1
 .
 7
 7
 4
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 1
 2
  
  
 1
 .
 4
 6
 8
  
  
  
 1
 .
 0
 1
 0
 9
 0
 4
 8
 0
 4
 2
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 2
 5
 .
 4
 2
 0
 4
 9
 9
 :
  
 3
 5
 8
  
 -
 0
 .
 3
 4
 9
  
  
 1
 .
 7
 7
 4
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 1
 2
  
  
 1
 .
 4
 6
 8
  
  
  
 1
 .
 0
 1
 0
 9
 0
 4
 7
 5
 6
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 2
 5
 .
 5
 1
 2
 9
 9
 1
 :
  
 3
 5
 9
  
 -
 0
 .
 3
 4
 9
  
  
 1
 .
 7
 7
 4
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 1
 2
  
  
 1
 .
 4
 6
 8
  
  
  
 1
 .
 0
 1
 0
 9
 0
 4
 7
 3
 8
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 2
 6
 .
 7
 9
 5
 5
 0
 1
 :
  
  
 p
 o
 w
 e
 l
 l
  
 n
 t
 h
 i
 t
 e
 r
  
 4
 :
  
 f
 r
 e
 t
  
 =
  
 1
 .
 0
 1
 0
 9
 0
 5
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 2
 6
 .
 7
 9
 5
 5
 0
 1
 :
  
 3
 7
 3
  
 -
 0
 .
 3
 4
 7
  
  
 1
 .
 7
 7
 4
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 1
 2
  
  
 1
 .
 4
 6
 8
  
  
  
 1
 .
 0
 1
 0
 9
 0
 4
 3
 9
 7
 9
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 3
 1
 .
 7
 4
 9
 0
 1
 4
 :
  
 4
 2
 7
  
 -
 0
 .
 3
 4
 7
  
  
 1
 .
 7
 7
 4
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 2
 7
  
  
 1
 .
 4
 6
 8
  
  
  
 1
 .
 0
 1
 0
 8
 9
 4
 4
 4
 0
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 3
 2
 .
 5
 1
 7
 9
 4
 2
 :
  
 4
 3
 5
  
 -
 0
 .
 3
 4
 7
  
  
 1
 .
 7
 7
 6
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 2
 7
  
  
 1
 .
 4
 7
 0
  
  
  
 1
 .
 0
 1
 0
 8
 8
 1
 4
 3
 7
 7
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 3
 2
 .
 7
 9
 3
 1
 5
 4
 :
  
 4
 3
 8
  
 -
 0
 .
 3
 4
 7
  
  
 1
 .
 7
 7
 8
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 2
 7
  
  
 1
 .
 4
 7
 1
  
  
  
 1
 .
 0
 1
 0
 8
 7
 7
 9
 2
 9
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 3
 2
 .
 9
 7
 6
 5
 6
 8
 :
  
 4
 4
 0
  
 -
 0
 .
 3
 4
 7
  
  
 1
 .
 7
 7
 7
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 2
 7
  
  
 1
 .
 4
 7
 0
  
  
  
 1
 .
 0
 1
 0
 8
 7
 7
 8
 5
 1
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 3
 3
 .
 2
 5
 2
 0
 6
 5
 :
  
 4
 4
 3
  
 -
 0
 .
 3
 4
 7
  
  
 1
 .
 7
 7
 7
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 2
 7
  
  
 1
 .
 4
 7
 0
  
  
  
 1
 .
 0
 1
 0
 8
 7
 7
 5
 8
 6
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 3
 3
 .
 4
 3
 5
 3
 0
 5
 :
  
 4
 4
 5
  
 -
 0
 .
 3
 4
 7
  
  
 1
 .
 7
 7
 7
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 2
 7
  
  
 1
 .
 4
 7
 0
  
  
  
 1
 .
 0
 1
 0
 8
 7
 7
 5
 7
 8
 5
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 3
 3
 .
 7
 1
 2
 7
 5
 2
 :
  
 4
 4
 8
  
 -
 0
 .
 3
 4
 7
  
  
 1
 .
 7
 7
 7
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 2
 7
  
  
 1
 .
 4
 7
 0
  
  
  
 1
 .
 0
 1
 0
 8
 7
 7
 5
 6
 8
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 3
 3
 .
 8
 0
 4
 7
 1
 1
 :
  
 4
 4
 9
  
 -
 0
 .
 3
 4
 7
  
  
 1
 .
 7
 7
 7
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 2
 7
  
  
 1
 .
 4
 7
 0
  
  
  
 1
 .
 0
 1
 0
 8
 7
 7
 5
 5
 5
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 3
 5
 .
 5
 4
 6
 0
 4
 5
 :
  
  
 p
 o
 w
 e
 l
 l
  
 n
 t
 h
 i
 t
 e
 r
  
 5
 :
  
 f
 r
 e
 t
  
 =
  
 1
 .
 0
 1
 0
 8
 7
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 3
 5
 .
 5
 4
 6
 0
 4
 5
 :
  
 4
 6
 8
  
 -
 0
 .
 3
 4
 6
  
  
 1
 .
 7
 7
 7
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 2
 7
  
  
 1
 .
 4
 7
 0
  
  
  
 1
 .
 0
 1
 0
 8
 6
 2
 9
 3
 6
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 3
 6
 .
 2
 7
 9
 1
 2
 9
 :
  
 4
 7
 6
  
 -
 0
 .
 3
 4
 6
  
  
 1
 .
 7
 7
 7
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 2
 7
  
  
 1
 .
 4
 8
 5
  
  
  
 1
 .
 0
 1
 0
 8
 2
 0
 5
 1
 2
 7
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 3
 6
 .
 4
 6
 2
 2
 6
 3
 :
  
 4
 7
 8
  
 -
 0
 .
 3
 4
 6
  
  
 1
 .
 7
 7
 7
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 2
 7
  
  
 1
 .
 4
 8
 0
  
  
  
 1
 .
 0
 1
 0
 7
 8
 8
 7
 7
 8
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 3
 9
 .
 0
 6
 5
 2
 0
 9
 :
  
 5
 0
 6
  
 -
 0
 .
 3
 4
 6
  
  
 1
 .
 7
 7
 7
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 6
  
  
 0
 .
 1
 2
 7
  
  
 1
 .
 4
 8
 0
  
  
  
 1
 .
 0
 1
 0
 7
 8
 7
 9
 0
 8
 7
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 4
 0
 .
 5
 3
 4
 6
 9
 7
 :
  
 5
 2
 2
  
 -
 0
 .
 3
 4
 6
  
  
 1
 .
 7
 7
 7
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 6
  
  
 0
 .
 1
 2
 9
  
  
 1
 .
 4
 8
 0
  
  
  
 1
 .
 0
 1
 0
 7
 6
 3
 0
 8
 6
 9
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 4
 1
 .
 0
 8
 4
 6
 9
 4
 :
  
 5
 2
 8
  
 -
 0
 .
 3
 4
 6
  
  
 1
 .
 7
 7
 6
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 6
  
  
 0
 .
 1
 2
 9
  
  
 1
 .
 4
 7
 9
  
  
  
 1
 .
 0
 1
 0
 7
 5
 6
 2
 4
 0
 2
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 4
 1
 .
 5
 8
 5
 3
 0
 8
 :
  
 5
 3
 3
  
 -
 0
 .
 3
 4
 6
  
  
 1
 .
 7
 7
 6
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 6
  
  
 0
 .
 1
 2
 9
  
  
 1
 .
 4
 7
 9
  
  
  
 1
 .
 0
 1
 0
 7
 5
 5
 9
 6
 6
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 4
 1
 .
 6
 7
 7
 1
 0
 9
 :
  
 5
 3
 4
  
 -
 0
 .
 3
 4
 6
  
  
 1
 .
 7
 7
 6
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 6
  
  
 0
 .
 1
 2
 9
  
  
 1
 .
 4
 7
 9
  
  
  
 1
 .
 0
 1
 0
 7
 5
 5
 7
 6
 9
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 4
 1
 .
 7
 6
 9
 0
 3
 1
 :
  
 5
 3
 5
  
 -
 0
 .
 3
 4
 6
  
  
 1
 .
 7
 7
 6
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 6
  
  
 0
 .
 1
 2
 9
  
  
 1
 .
 4
 7
 9
  
  
  
 1
 .
 0
 1
 0
 7
 5
 5
 7
 3
 8
 7
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 4
 1
 .
 8
 6
 0
 9
 6
 0
 :
  
 5
 3
 6
  
 -
 0
 .
 3
 4
 6
  
  
 1
 .
 7
 7
 6
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 6
  
  
 0
 .
 1
 2
 9
  
  
 1
 .
 4
 7
 9
  
  
  
 1
 .
 0
 1
 0
 7
 5
 5
 5
 8
 6
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 4
 1
 .
 9
 5
 3
 0
 2
 5
 :
  
 5
 3
 7
  
 -
 0
 .
 3
 4
 6
  
  
 1
 .
 7
 7
 6
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 6
  
  
 0
 .
 1
 2
 9
  
  
 1
 .
 4
 7
 9
  
  
  
 1
 .
 0
 1
 0
 7
 5
 5
 5
 4
 2
 9
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 4
 3
 .
 1
 6
 2
 3
 3
 9
 :
  
  
 p
 o
 w
 e
 l
 l
  
 n
 t
 h
 i
 t
 e
 r
  
 6
 :
  
 f
 r
 e
 t
  
 =
  
 1
 .
 0
 1
 0
 7
 5
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 4
 3
 .
 1
 6
 2
 3
 3
 9
 :
  
 5
 5
 0
  
 -
 0
 .
 3
 3
 9
  
  
 1
 .
 7
 7
 6
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 6
  
  
 0
 .
 1
 2
 9
  
  
 1
 .
 4
 7
 9
  
  
  
 1
 .
 0
 1
 0
 7
 5
 1
 4
 8
 8
 3
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 4
 3
 .
 3
 5
 3
 5
 0
 5
 :
  
 5
 5
 2
  
 -
 0
 .
 3
 4
 0
  
  
 1
 .
 7
 7
 6
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 6
  
  
 0
 .
 1
 2
 9
  
  
 1
 .
 4
 7
 9
  
  
  
 1
 .
 0
 1
 0
 7
 3
 9
 8
 5
 8
 2
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 4
 3
 .
 4
 4
 9
 5
 0
 3
 :
  
 5
 5
 3
  
 -
 0
 .
 3
 4
 2
  
  
 1
 .
 7
 7
 6
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 6
  
  
 0
 .
 1
 2
 9
  
  
 1
 .
 4
 7
 9
  
  
  
 1
 .
 0
 1
 0
 7
 3
 9
 5
 0
 0
 5
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 4
 4
 .
 5
 8
 7
 4
 1
 2
 :
  
 5
 6
 5
  
 -
 0
 .
 3
 4
 2
  
  
 1
 .
 7
 7
 6
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 6
  
  
 0
 .
 1
 2
 9
  
  
 1
 .
 4
 8
 1
  
  
  
 1
 .
 0
 1
 0
 7
 3
 0
 2
 0
 2
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 4
 9
 .
 2
 9
 2
 4
 8
 1
 :
  
 6
 1
 6
  
 -
 0
 .
 3
 4
 2
  
  
 1
 .
 7
 7
 6
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 6
  
  
 0
 .
 1
 2
 9
  
  
 1
 .
 4
 8
 1
  
  
  
 1
 .
 0
 1
 0
 7
 3
 0
 1
 3
 5
 3
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 4
 9
 .
 3
 8
 4
 2
 9
 3
 :
  
 6
 1
 7
  
 -
 0
 .
 3
 4
 2
  
  
 1
 .
 7
 7
 6
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 6
  
  
 0
 .
 1
 2
 9
  
  
 1
 .
 4
 8
 1
  
  
  
 1
 .
 0
 1
 0
 7
 3
 0
 0
 8
 7
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 4
 9
 .
 4
 7
 6
 7
 8
 8
 :
  
 6
 1
 8
  
 -
 0
 .
 3
 4
 2
  
  
 1
 .
 7
 7
 6
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 6
  
  
 0
 .
 1
 2
 9
  
  
 1
 .
 4
 8
 1
  
  
  
 1
 .
 0
 1
 0
 7
 2
 9
 9
 6
 9
 2
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 5
 7
 .
 2
 6
 9
 6
 1
 1
 :
  
  
 p
 o
 w
 e
 l
 l
  
 n
 t
 h
 i
 t
 e
 r
  
 7
 :
  
 f
 r
 e
 t
  
 =
  
 1
 .
 0
 1
 0
 7
 3
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 6
 :
 5
 7
 .
 2
 6
 9
 6
 1
 1
 :
  
 7
 0
 3
  
 -
 0
 .
 3
 4
 2
  
  
 1
 .
 7
 7
 6
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 6
  
  
 0
 .
 1
 2
 9
  
  
 1
 .
 4
 8
 1
  
  
  
 1
 .
 0
 1
 0
 7
 2
 9
 8
 5
 6
 3
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 2
 7
 7
 3
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 2
 7
 7
 3
 :
  
  
 p
 o
 w
 e
 l
 l
  
 n
 t
 h
 i
 t
 e
 r
  
 8
 :
  
 f
 r
 e
 t
  
 =
  
 1
 .
 0
 1
 0
 7
 3
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 2
 7
 7
 3
 :
  
 0
  
  
 -
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
  
 1
 .
 0
 1
 3
 2
 4
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 2
 7
 7
 3
 :
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 .
 0
 0
 0
 0
 0
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 2
 7
 7
 3
 :
  
 0
 .
 0
 9
 1
 8
 1
  
  
 -
 0
 .
 9
 9
 1
 8
 8
  
  
 -
 0
 .
 0
 8
 7
 9
 8
  
  
 -
 0
 .
 6
 2
 2
 8
 6
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 2
 7
 7
 3
 :
  
 0
 .
 0
 9
 6
 9
 2
  
  
 -
 0
 .
 0
 7
 9
 0
 3
  
  
  
 0
 .
 9
 9
 2
 1
 5
  
  
 -
 1
 8
 .
 4
 0
 5
 9
 3
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 2
 7
 7
 3
 :
  
 0
 .
 9
 9
 1
 0
 5
  
  
  
 0
 .
 0
 9
 9
 6
 2
  
  
 -
 0
 .
 0
 8
 8
 8
 8
  
  
 -
 1
 0
 .
 1
 4
 3
 2
 6
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 2
 7
 7
 3
 :
  
 1
  
  
 -
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
  
 0
 .
 9
 8
 8
 2
 0
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 2
 7
 7
 3
 :
  
 2
  
  
 -
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
  
 1
 .
 0
 5
 3
 3
 5
 5
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 2
 7
 7
 3
 :
  
 3
  
  
 -
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
  
 1
 .
 0
 3
 0
 5
 7
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 2
 7
 7
 3
 :
  
 4
  
  
  
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
  
 1
 .
 0
 4
 9
 1
 4
 2
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 2
 7
 7
 3
 :
  
 5
  
  
  
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
  
 1
 .
 0
 3
 1
 5
 1
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 2
 7
 7
 3
 :
  
 6
  
  
  
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
  
 1
 .
 0
 3
 6
 7
 3
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 2
 7
 7
 3
 :
  
 7
  
  
  
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
  
 1
 .
 0
 4
 4
 8
 0
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 2
 7
 7
 3
 :
 C
 o
 m
 p
 u
 t
 i
 n
 g
  
 r
 e
 l
 a
 t
 i
 v
 e
  
 c
 o
 s
 t
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 2
 7
 7
 3
 :
 C
 o
 s
 t
  
  
  
 1
 .
 0
 1
 0
 7
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 2
 7
 7
 3
 :
 C
 t
 x
  
 I
 n
 t
 e
 n
 s
 i
 t
 y
  
  
  
 1
 3
 6
 .
 7
 3
 5
 2
  
 +
 /
 -
  
 2
 2
 3
 .
 3
 3
 7
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 2
 7
 7
 3
 :
 F
 i
 n
 a
 l
  
 c
 o
 s
 t
 s
  
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 2
 7
 7
 3
 :
 M
 i
 n
  
 c
 o
 s
 t
  
 w
 a
 s
  
 1
 .
 0
 1
 0
 7
 3
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 2
 7
 7
 3
 :
 N
 u
 m
 b
 e
 r
  
 o
 f
  
 F
 u
 n
 c
 t
 i
 o
 n
 C
 a
 l
 l
 s
  
  
  
 7
 9
 9
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 2
 7
 7
 3
 :
 N
 u
 m
 b
 e
 r
  
 o
 f
  
 i
 t
 e
 r
 a
 t
 i
 o
 n
 s
  
  
  
  
  
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 2
 7
 7
 3
 :
 N
 u
 m
 b
 e
 r
  
 o
 f
  
 s
 u
 r
 f
 a
 c
 e
  
 h
 i
 t
 s
  
 9
 0
 3
 5
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 2
 7
 7
 3
 :
 O
 p
 t
 i
 m
 i
 z
 a
 t
 i
 o
 n
 T
 i
 m
 e
  
 7
 3
 .
 7
 2
 1
 0
 0
 0
  
 s
 e
 c
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 2
 7
 7
 3
 :
 P
 a
 r
 a
 m
 e
 t
 e
 r
 s
  
 a
 t
  
 o
 p
 t
 i
 m
 u
 m
  
 (
 r
 o
 t
 d
 e
 g
 )
  
 -
 0
 .
 1
 0
 5
 6
 0
  
  
 0
 .
 1
 2
 8
 6
 7
  
  
 1
 .
 4
 8
 1
 1
 9
  
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 2
 7
 7
 3
 :
 P
 a
 r
 a
 m
 e
 t
 e
 r
 s
  
 a
 t
  
 o
 p
 t
 i
 m
 u
 m
  
 (
 t
 r
 a
 n
 s
 m
 m
 )
  
 -
 0
 .
 3
 4
 2
 4
 1
  
  
 1
 .
 7
 7
 5
 8
 0
  
  
 0
 .
 1
 2
 4
 4
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 2
 7
 7
 3
 :
 P
 c
 t
  
 C
 o
 n
 t
 r
 a
 s
 t
  
  
  
  
  
 -
 0
 .
 7
 3
 8
 6
  
 +
 /
 -
  
  
 8
 1
 .
 5
 4
 0
 5
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 2
 7
 7
 3
 :
 P
 o
 w
 e
 l
 l
  
 d
 o
 n
 e
  
 n
 i
 t
 e
 r
 s
  
 =
  
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 2
 7
 7
 3
 :
 R
 E
 L
 :
  
  
 8
  
  
 1
 .
 0
 1
 0
 7
 3
 0
  
  
  
  
 8
 .
 2
 4
 7
 5
 5
 8
  
  
 1
 .
 0
 3
 0
 9
 4
 5
  
 r
 e
 l
  
 =
  
 0
 .
 9
 8
 0
 3
 9
 2
  
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 2
 7
 7
 3
 :
 R
 e
 g
  
 a
 t
  
 m
 i
 n
  
 c
 o
 s
 t
  
 w
 a
 s
  
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 2
 7
 7
 3
 :
 R
 e
 l
 C
 o
 s
 t
  
  
  
 0
 .
 9
 9
 2
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 2
 7
 7
 3
 :
 T
 o
 l
 P
 o
 w
 e
 l
 l
  
 0
 .
 0
 0
 0
 0
 0
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 2
 7
 7
 3
 :
 W
 M
  
  
 I
 n
 t
 e
 n
 s
 i
 t
 y
  
  
  
 1
 3
 8
 .
 2
 8
 9
 0
  
 +
 /
 -
  
 2
 2
 1
 .
 1
 8
 5
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 2
 7
 7
 3
 :
 W
 r
 i
 t
 i
 n
 g
  
 o
 p
 t
 i
 m
 a
 l
  
 r
 e
 g
  
 t
 o
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 _
 b
 b
 r
 e
 g
 _
 s
 u
 b
 -
 b
 m
 .
 d
 a
 t
 ,
  
 t
 y
 p
 e
  
 =
  
 1
 4
  
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 2
 7
 7
 3
 :
 n
 M
 a
 x
 I
 t
 e
 r
 s
 P
 o
 w
 e
 l
 l
  
 3
 6
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 9
 2
 5
 5
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 9
 2
 5
 5
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 9
 2
 5
 5
 :
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 9
 2
 5
 5
 :
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 .
 0
 0
 0
 0
 0
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 9
 2
 5
 5
 :
  
 0
 .
 0
 0
 1
 9
 7
  
  
  
 0
 .
 0
 0
 0
 1
 5
  
  
  
 0
 .
 0
 2
 5
 8
 7
  
  
 -
 0
 .
 1
 7
 4
 2
 8
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 9
 2
 5
 5
 :
  
 0
 .
 0
 0
 2
 3
 6
  
  
  
 0
 .
 0
 0
 0
 0
 7
  
  
  
 0
 .
 0
 0
 1
 6
 9
  
  
 -
 0
 .
 1
 8
 4
 3
 4
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 9
 2
 5
 5
 :
  
 0
 .
 0
 7
 1
 1
 0
  
  
 -
 0
 .
 0
 7
 9
 7
 5
  
  
  
 0
 .
 9
 9
 4
 2
 8
  
  
 -
 1
 9
 .
 9
 2
 0
 1
 9
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 9
 2
 5
 5
 :
  
 0
 .
 0
 9
 4
 1
 7
  
  
 -
 0
 .
 9
 9
 1
 8
 1
  
  
 -
 0
 .
 0
 8
 6
 2
 9
  
  
 -
 0
 .
 8
 0
 7
 2
 0
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 9
 2
 5
 5
 :
  
 0
 .
 9
 9
 3
 0
 1
  
  
  
 0
 .
 0
 9
 9
 7
 7
  
  
 -
 0
 .
 0
 6
 3
 0
 1
  
  
 -
 1
 0
 .
 3
 1
 7
 5
 5
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 9
 2
 5
 5
 :
 -
 0
 .
 0
 2
 5
 8
 2
  
  
 -
 0
 .
 0
 0
 0
 7
 2
  
  
  
 0
 .
 0
 0
 2
 1
 3
  
  
 -
 1
 .
 5
 1
 4
 2
 7
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 9
 2
 5
 5
 :
 O
 r
 i
 g
 i
 n
 a
 l
  
 R
 e
 g
  
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 1
 0
 9
 2
 5
 5
 :
 O
 r
 i
 g
 i
 n
 a
 l
  
 R
 e
 g
  
 -
  
 O
 p
 t
 i
 m
 a
 l
  
 R
 e
 g
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 2
 8
 4
 1
 2
 4
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 2
 8
 4
 1
 2
 4
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 2
 8
 4
 1
 2
 4
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 2
 8
 4
 1
 2
 4
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 2
 8
 4
 1
 2
 4
 :
 C
 o
 m
 p
 u
 t
 i
 n
 g
  
 c
 h
 a
 n
 g
 e
  
 i
 n
  
 l
 h
  
 p
 o
 s
 i
 t
 i
 o
 n
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 2
 8
 4
 1
 2
 4
 :
 C
 o
 m
 p
 u
 t
 i
 n
 g
  
 c
 h
 a
 n
 g
 e
  
 i
 n
  
 r
 h
  
 p
 o
 s
 i
 t
 i
 o
 n
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 2
 8
 4
 1
 2
 4
 :
 I
 f
  
 t
 h
 e
  
 m
 o
 v
  
 d
 a
 t
 a
  
 h
 a
 s
  
 a
  
 T
 1
  
 c
 o
 n
 t
 r
 a
 s
 t
 ,
  
 r
 e
 -
 r
 u
 n
  
 w
 i
 t
 h
  
 -
 -
 T
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 2
 8
 4
 1
 2
 4
 :
 L
 H
  
 r
 m
 s
 D
 i
 f
 f
 M
 e
 a
 n
  
 1
 .
 0
 5
 0
 2
 9
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 2
 8
 4
 1
 2
 4
 :
 S
 u
 r
 f
 a
 c
 e
 -
 R
 M
 S
 -
 D
 i
 f
 f
 -
 m
 m
  
 1
 .
 6
 4
 0
 5
 2
 8
  
 0
 .
 7
 0
 4
 0
 3
 9
  
 3
 .
 0
 6
 3
 6
 9
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 2
 8
 4
 1
 2
 4
 :
 W
 A
 R
 N
 I
 N
 G
 :
  
 i
 n
 i
 t
 i
 a
 l
  
 G
 -
 W
  
 c
 o
 n
 t
 r
 a
 s
 t
  
 w
 a
 s
  
 n
 e
 g
 a
 t
 i
 v
 e
 ,
  
 b
 u
 t
  
 e
 x
 p
 e
 c
 t
 e
 d
  
 p
 o
 s
 i
 t
 i
 v
 e
 .
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 2
 8
 4
 1
 2
 4
 :
 m
 r
 i
 _
 s
 e
 g
 r
 e
 g
  
 d
 o
 n
 e
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 4
 5
 5
 3
 9
 1
 :
 M
 i
 n
 C
 o
 s
 t
 :
  
 1
 .
 0
 1
 0
 7
 3
 0
  
 1
 3
 8
 .
 2
 8
 9
 0
 4
 7
  
 1
 3
 6
 .
 7
 3
 5
 2
 0
 1
  
 -
 0
 .
 7
 3
 8
 5
 9
 4
  
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 4
 5
 8
 5
 2
 4
 :
 t
 k
 r
 e
 g
 i
 s
 t
 e
 r
 2
 _
 c
 m
 d
 l
  
 -
 -
 m
 o
 v
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 .
 n
 i
 i
 .
 g
 z
  
 -
 -
 r
 e
 g
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 _
 b
 b
 r
 e
 g
 _
 s
 u
 b
 -
 b
 m
 .
 d
 a
 t
  
 -
 -
 n
 o
 e
 d
 i
 t
  
 -
 -
 f
 s
 l
 r
 e
 g
 o
 u
 t
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 _
 b
 b
 r
 e
 g
 _
 s
 u
 b
 -
 b
 m
 .
 m
 a
 t
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 4
 8
 5
 5
 0
 1
 :
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 .
 0
 0
 0
 0
 0
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 4
 8
 5
 5
 0
 1
 :
  
 0
 .
 0
 9
 1
 8
 1
  
  
 -
 0
 .
 9
 9
 1
 8
 8
  
  
 -
 0
 .
 0
 8
 7
 9
 8
  
  
 -
 0
 .
 6
 2
 2
 8
 6
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 4
 8
 5
 5
 0
 1
 :
  
 0
 .
 0
 9
 6
 9
 2
  
  
 -
 0
 .
 0
 7
 9
 0
 3
  
  
  
 0
 .
 9
 9
 2
 1
 5
  
  
 -
 1
 8
 .
 4
 0
 5
 9
 3
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 4
 8
 5
 5
 0
 1
 :
  
 0
 .
 9
 9
 1
 0
 5
  
  
  
 0
 .
 0
 9
 9
 6
 2
  
  
 -
 0
 .
 0
 8
 8
 8
 8
  
  
 -
 1
 0
 .
 1
 4
 3
 2
 6
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 4
 8
 5
 5
 0
 1
 :
 $
 I
 d
 :
  
 t
 k
 r
 e
 g
 i
 s
 t
 e
 r
 2
 .
 c
 ,
 v
  
 1
 .
 1
 3
 2
 .
 2
 .
 1
  
 2
 0
 1
 6
 /
 0
 8
 /
 0
 2
  
 2
 1
 :
 1
 7
 :
 2
 9
  
 g
 r
 e
 v
 e
  
 E
 x
 p
  
 $
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 4
 8
 5
 5
 0
 1
 :
 -
 -
 -
 -
  
 I
 n
 p
 u
 t
  
 r
 e
 g
 i
 s
 t
 r
 a
 t
 i
 o
 n
  
 m
 a
 t
 r
 i
 x
  
 -
 -
 -
 -
 -
 -
 -
 -
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 4
 8
 5
 5
 0
 1
 :
 D
 i
 a
 g
 n
 o
 s
 t
 i
 c
  
 L
 e
 v
 e
 l
  
 -
 1
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 4
 8
 5
 5
 0
 1
 :
 I
 N
 F
 O
 :
  
 n
 o
  
 t
 a
 r
 g
 e
 t
  
 v
 o
 l
 u
 m
 e
  
 s
 p
 e
 c
 i
 f
 i
 e
 d
 ,
  
 a
 s
 s
 u
 m
 i
 n
 g
  
 F
 r
 e
 e
 S
 u
 r
 f
 e
 r
  
 o
 r
 i
 g
  
 v
 o
 l
 u
 m
 e
 .
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 4
 8
 5
 5
 0
 1
 :
 L
 o
 a
 d
 V
 o
 l
  
  
  
  
  
  
  
  
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 4
 8
 5
 5
 0
 1
 :
 Z
 e
 r
 o
 C
 R
 A
 S
  
  
  
  
  
  
  
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 4
 8
 5
 5
 0
 1
 :
 m
 o
 v
 a
 b
 l
 e
  
 v
 o
 l
 u
 m
 e
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 .
 n
 i
 i
 .
 g
 z
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 4
 8
 5
 5
 0
 1
 :
 r
 e
 g
  
 f
 i
 l
 e
  
  
  
  
  
  
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 _
 b
 b
 r
 e
 g
 _
 s
 u
 b
 -
 b
 m
 .
 d
 a
 t
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 4
 8
 5
 5
 0
 1
 :
 t
 a
 r
 g
 e
 t
  
  
 v
 o
 l
 u
 m
 e
  
 o
 r
 i
 g
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 7
 .
 4
 8
 5
 5
 0
 1
 :
 t
 k
 r
 e
 g
 i
 s
 t
 e
 r
 _
 t
 c
 l
  
 /
 o
 p
 t
 /
 f
 r
 e
 e
 s
 u
 r
 f
 e
 r
 -
 6
 .
 0
 .
 1
 /
 t
 k
 t
 o
 o
 l
 s
 /
 t
 k
 r
 e
 g
 i
 s
 t
 e
 r
 2
 .
 t
 c
 l
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 2
 1
 5
 9
 0
 :
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 .
 0
 0
 0
 0
 0
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 2
 1
 5
 9
 0
 :
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 .
 0
 0
 0
 0
 0
  
  
 -
 1
 2
 8
 .
 0
 0
 0
 0
 0
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 2
 1
 5
 9
 0
 :
  
 0
 .
 0
 0
 0
 0
 0
  
  
 -
 1
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 2
 8
 .
 0
 0
 0
 0
 0
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 2
 1
 5
 9
 0
 :
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 2
 1
 5
 9
 0
 :
 -
 1
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 2
 8
 .
 0
 0
 0
 0
 0
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 2
 1
 5
 9
 0
 :
 I
 N
 F
 O
 :
  
 l
 o
 a
 d
 i
 n
 g
  
 t
 a
 r
 g
 e
 t
  
 /
 d
 e
 r
 i
 v
 a
 t
 i
 v
 e
 s
 /
 f
 r
 e
 e
 s
 u
 r
 f
 e
 r
 /
 s
 u
 b
 -
 b
 m
 /
 m
 r
 i
 /
 o
 r
 i
 g
 .
 m
 g
 z
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 2
 1
 5
 9
 0
 :
 I
 N
 F
 O
 :
  
 t
 a
 r
 g
 e
 t
  
 d
 o
 e
 s
  
 n
 o
 t
  
 c
 o
 n
 f
 o
 r
 m
  
 t
 o
  
 C
 O
 R
  
 f
 o
 r
 m
 a
 t
 ,
  
 s
 o
  
 I
 '
 m
  
 g
 o
 i
 n
 g
  
 t
 o
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 2
 1
 5
 9
 0
 :
 T
 t
 a
 r
 g
 :
  
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 2
 1
 5
 9
 0
 :
 f
 l
 o
 a
 t
 2
 i
 n
 t
  
 =
  
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 2
 1
 5
 9
 0
 :
 r
 e
 s
 l
 i
 c
 e
  
 t
 o
  
 C
 O
 R
 .
  
 T
 h
 i
 s
  
 w
 i
 l
 l
  
 n
 o
 t
  
 a
 f
 f
 e
 c
 t
  
 t
 h
 e
  
 f
 i
 n
 a
 l
  
 r
 e
 g
 i
 s
 t
 r
 a
 t
 i
 o
 n
 .
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 2
 3
 0
 3
 8
 :
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 .
 0
 0
 0
 0
 0
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 2
 3
 0
 3
 8
 :
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 .
 0
 0
 0
 0
 0
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 2
 3
 0
 3
 8
 :
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 .
 0
 0
 0
 0
 0
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 2
 3
 0
 3
 8
 :
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 6
 8
 2
 0
 0
  
  
 -
 6
 5
 .
 4
 7
 2
 0
 0
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 2
 3
 0
 3
 8
 :
  
 0
 .
 0
 0
 0
 0
 0
  
  
 -
 0
 .
 7
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 1
 .
 9
 0
 0
 0
 0
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 2
 3
 0
 3
 8
 :
  
 0
 .
 0
 9
 1
 8
 1
  
  
 -
 0
 .
 9
 9
 1
 8
 8
  
  
 -
 0
 .
 0
 8
 7
 9
 8
  
  
 -
 0
 .
 6
 2
 2
 8
 6
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 2
 3
 0
 3
 8
 :
  
 0
 .
 0
 9
 1
 8
 1
  
  
 -
 0
 .
 9
 9
 1
 8
 8
  
  
 -
 0
 .
 0
 8
 7
 9
 8
  
  
 -
 0
 .
 6
 2
 2
 8
 8
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 2
 3
 0
 3
 8
 :
  
 0
 .
 0
 9
 6
 9
 2
  
  
 -
 0
 .
 0
 7
 9
 0
 3
  
  
  
 0
 .
 9
 9
 2
 1
 5
  
  
 -
 1
 8
 .
 4
 0
 5
 9
 3
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 2
 3
 0
 3
 8
 :
  
 0
 .
 0
 9
 6
 9
 2
  
  
 -
 0
 .
 0
 7
 9
 0
 3
  
  
  
 0
 .
 9
 9
 2
 1
 5
  
  
 -
 1
 8
 .
 4
 0
 5
 9
 4
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 2
 3
 0
 3
 8
 :
  
 0
 .
 9
 9
 1
 0
 5
  
  
  
 0
 .
 0
 9
 9
 6
 2
  
  
 -
 0
 .
 0
 8
 8
 8
 8
  
  
 -
 1
 0
 .
 1
 4
 3
 2
 6
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 2
 3
 0
 3
 8
 :
  
 0
 .
 9
 9
 1
 0
 5
  
  
  
 0
 .
 0
 9
 9
 6
 2
  
  
 -
 0
 .
 0
 8
 8
 8
 8
  
  
 -
 1
 0
 .
 1
 4
 3
 2
 8
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 2
 3
 0
 3
 8
 :
 -
 -
 -
 -
  
 I
 n
 p
 u
 t
  
 r
 e
 g
 i
 s
 t
 r
 a
 t
 i
 o
 n
  
 m
 a
 t
 r
 i
 x
  
 -
 -
 -
 -
 -
 -
 -
 -
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 2
 3
 0
 3
 8
 :
 -
 0
 .
 6
 8
 2
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 6
 5
 .
 4
 7
 2
 0
 0
 ;
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 2
 3
 0
 3
 8
 :
 D
 e
 t
 e
 r
 m
 i
 n
 a
 n
 t
  
 0
 .
 9
 9
 9
 9
 9
 9
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 2
 3
 0
 3
 8
 :
 I
 N
 F
 O
 :
  
 l
 o
 a
 d
 i
 n
 g
  
 m
 o
 v
 a
 b
 l
 e
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 .
 n
 i
 i
 .
 g
 z
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 2
 3
 0
 3
 8
 :
 R
 e
 g
 M
 a
 t
  
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 2
 3
 0
 3
 8
 :
 T
 m
 o
 v
 :
  
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 2
 3
 0
 3
 8
 :
 m
 k
 h
 e
 a
 d
 e
 r
 r
 e
 g
  
 =
  
 0
 ,
  
 f
 l
 o
 a
 t
 2
 i
 n
 t
  
 =
  
 0
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 2
 3
 0
 3
 8
 :
 s
 u
 b
 j
 e
 c
 t
  
 =
  
 s
 u
 b
 -
 b
 m
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 2
 8
 5
 5
 4
 :
 F
 S
 L
 O
 U
 T
 P
 U
 T
 T
 Y
 P
 E
  
 N
 I
 F
 T
 I
 _
 G
 Z
  
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 2
 8
 5
 5
 4
 :
 t
 k
 r
 e
 g
 2
 F
 S
 L
 :
  
 m
 o
 v
  
 d
 e
 t
  
 =
  
 -
 0
 .
 3
 2
 5
 5
 8
 7
 ,
  
 r
 e
 f
  
 d
 e
 t
  
 =
  
 -
 0
 .
 2
 6
 2
 1
 4
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 3
 2
 3
 3
 8
 :
 C
 l
 e
 a
 n
 i
 n
 g
  
 u
 p
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 4
 3
 3
 9
 8
 :
  
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 4
 5
 5
 2
 2
 :
 S
 t
 a
 r
 t
 e
 d
  
 a
 t
  
 T
 u
 e
  
 D
 e
 c
  
 1
 1
  
 1
 5
 :
 3
 3
 :
 3
 4
  
 U
 T
 C
  
 2
 0
 1
 8
  
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 4
 8
 1
 8
 9
 :
 E
 n
 d
 e
 d
  
  
  
 a
 t
  
 T
 u
 e
  
 D
 e
 c
  
 1
 1
  
 1
 5
 :
 3
 7
 :
 0
 8
  
 U
 T
 C
  
 2
 0
 1
 8
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 5
 0
 3
 4
 3
 :
 B
 B
 R
 -
 R
 u
 n
 -
 T
 i
 m
 e
 -
 S
 e
 c
  
 2
 1
 4
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 5
 2
 4
 2
 0
 :
  
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 5
 4
 4
 1
 1
 :
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
  
 D
 o
 n
 e
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 5
 6
 4
 2
 5
 :
 T
 o
  
 c
 h
 e
 c
 k
  
 r
 e
 s
 u
 l
 t
 s
 ,
  
 r
 u
 n
 :
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 5
 8
 7
 1
 5
 :
 t
 k
 r
 e
 g
 i
 s
 t
 e
 r
 f
 v
  
 -
 -
 m
 o
 v
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 .
 n
 i
 i
 .
 g
 z
  
 -
 -
 r
 e
 g
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 _
 b
 b
 r
 e
 g
 _
 s
 u
 b
 -
 b
 m
 .
 d
 a
 t
  
 -
 -
 s
 u
 r
 f
 s
  
 

 s
 t
 d
 o
 u
 t
  
 2
 0
 1
 8
 -
 1
 2
 -
 1
 1
 T
 1
 5
 :
 3
 7
 :
 0
 8
 .
 1
 5
 8
 9
 8
 1
 :
  


Terminal - standard output
~~~~~~~~~~~~~~~~~~~~~~~~~~


 t
 m
 p
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 

 L
 o
 g
  
 f
 i
 l
 e
  
 i
 s
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 _
 b
 b
 r
 e
 g
 _
 s
 u
 b
 -
 b
 m
 .
 d
 a
 t
 .
 l
 o
 g
 

 T
 u
 e
  
 D
 e
 c
  
 1
 1
  
 1
 5
 :
 3
 3
 :
 3
 4
  
 U
 T
 C
  
 2
 0
 1
 8
 

 

 s
 e
 t
 e
 n
 v
  
 S
 U
 B
 J
 E
 C
 T
 S
 _
 D
 I
 R
  
 /
 d
 e
 r
 i
 v
 a
 t
 i
 v
 e
 s
 /
 f
 r
 e
 e
 s
 u
 r
 f
 e
 r
 

 c
 d
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 

 /
 o
 p
 t
 /
 f
 r
 e
 e
 s
 u
 r
 f
 e
 r
 -
 6
 .
 0
 .
 1
 /
 b
 i
 n
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
  
 -
 -
 b
 o
 l
 d
  
 -
 -
 f
 s
 l
 m
 a
 t
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 _
 b
 b
 r
 e
 g
 _
 s
 u
 b
 -
 b
 m
 .
 m
 a
 t
  
 -
 -
 r
 e
 g
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 _
 b
 b
 r
 e
 g
 _
 s
 u
 b
 -
 b
 m
 .
 d
 a
 t
  
 -
 -
 m
 o
 v
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 .
 n
 i
 i
 .
 g
 z
  
 -
 -
 s
  
 s
 u
 b
 -
 b
 m
 

 

 $
 I
 d
 :
  
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 ,
 v
  
 1
 .
 7
 5
  
 2
 0
 1
 6
 /
 0
 5
 /
 1
 0
  
 2
 0
 :
 0
 2
 :
 2
 8
  
 g
 r
 e
 v
 e
  
 E
 x
 p
  
 $
 

 L
 i
 n
 u
 x
  
 9
 9
 5
 8
 f
 5
 f
 d
 3
 b
 a
 7
  
 3
 .
 1
 0
 .
 0
 -
 6
 9
 3
 .
 1
 7
 .
 1
 .
 e
 l
 7
 .
 x
 8
 6
 _
 6
 4
  
 #
 1
  
 S
 M
 P
  
 T
 h
 u
  
 J
 a
 n
  
 2
 5
  
 2
 0
 :
 1
 3
 :
 5
 8
  
 U
 T
 C
  
 2
 0
 1
 8
  
 x
 8
 6
 _
 6
 4
  
 G
 N
 U
 /
 L
 i
 n
 u
 x
 

 F
 R
 E
 E
 S
 U
 R
 F
 E
 R
 _
 H
 O
 M
 E
  
 /
 o
 p
 t
 /
 f
 r
 e
 e
 s
 u
 r
 f
 e
 r
 -
 6
 .
 0
 .
 1
 

 m
 r
 i
 _
 c
 o
 n
 v
 e
 r
 t
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 .
 n
 i
 i
 .
 g
 z
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 t
 e
 m
 p
 l
 a
 t
 e
 .
 n
 i
 i
 

 m
 r
 i
 _
 c
 o
 n
 v
 e
 r
 t
 .
 b
 i
 n
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 .
 n
 i
 i
 .
 g
 z
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 t
 e
 m
 p
 l
 a
 t
 e
 .
 n
 i
 i
  
 

 $
 I
 d
 :
  
 m
 r
 i
 _
 c
 o
 n
 v
 e
 r
 t
 .
 c
 ,
 v
  
 1
 .
 2
 2
 6
  
 2
 0
 1
 6
 /
 0
 2
 /
 2
 6
  
 1
 6
 :
 1
 5
 :
 2
 4
  
 m
 r
 e
 u
 t
 e
 r
  
 E
 x
 p
  
 $
 

 r
 e
 a
 d
 i
 n
 g
  
 f
 r
 o
 m
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 .
 n
 i
 i
 .
 g
 z
 .
 .
 .
 

 T
 R
 =
 4
 0
 0
 0
 .
 0
 0
 ,
  
 T
 E
 =
 0
 .
 0
 0
 ,
  
 T
 I
 =
 0
 .
 0
 0
 ,
  
 f
 l
 i
 p
  
 a
 n
 g
 l
 e
 =
 0
 .
 0
 0
 

 i
 _
 r
 a
 s
  
 =
  
 (
 -
 1
 ,
  
 0
 ,
  
 0
 )
 

 j
 _
 r
 a
 s
  
 =
  
 (
 0
 ,
  
 0
 .
 9
 9
 9
 9
 8
 6
 ,
  
 0
 .
 0
 0
 5
 3
 4
 0
 6
 8
 )
 

 k
 _
 r
 a
 s
  
 =
  
 (
 0
 ,
  
 -
 0
 .
 0
 0
 5
 3
 4
 0
 6
 8
 ,
  
 0
 .
 9
 9
 9
 9
 8
 6
 )
 

 w
 r
 i
 t
 i
 n
 g
  
 t
 o
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 t
 e
 m
 p
 l
 a
 t
 e
 .
 n
 i
 i
 .
 .
 .
 

 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 -
 -
 s
  
 s
 u
 b
 -
 b
 m
  
 -
 -
 m
 o
 v
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 t
 e
 m
 p
 l
 a
 t
 e
 .
 n
 i
 i
  
 -
 -
 r
 e
 g
 d
 a
 t
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 r
 e
 g
 .
 i
 n
 i
 t
 .
 d
 a
 t
  
 -
 -
 r
 e
 g
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 m
 r
 i
 _
 c
 o
 r
 e
 g
 .
 l
 t
 a
  
 -
 -
 n
 t
 h
 r
 e
 a
 d
 s
  
 1
  
 -
 -
 d
 o
 f
  
 6
  
 -
 -
 s
 e
 p
  
 4
  
 -
 -
 f
 t
 o
 l
  
 .
 0
 0
 0
 1
  
 -
 -
 l
 i
 n
 m
 i
 n
 t
 o
 l
  
 .
 0
 1
 

 

 $
 I
 d
 :
  
 m
 r
 i
 _
 c
 o
 r
 e
 g
 .
 c
 ,
 v
  
 1
 .
 2
 7
  
 2
 0
 1
 6
 /
 0
 4
 /
 3
 0
  
 1
 5
 :
 1
 1
 :
 4
 9
  
 g
 r
 e
 v
 e
  
 E
 x
 p
  
 $
 

 c
 w
 d
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 

 c
 m
 d
 l
 i
 n
 e
  
 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 -
 -
 s
  
 s
 u
 b
 -
 b
 m
  
 -
 -
 m
 o
 v
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 t
 e
 m
 p
 l
 a
 t
 e
 .
 n
 i
 i
  
 -
 -
 r
 e
 g
 d
 a
 t
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 r
 e
 g
 .
 i
 n
 i
 t
 .
 d
 a
 t
  
 -
 -
 r
 e
 g
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 m
 r
 i
 _
 c
 o
 r
 e
 g
 .
 l
 t
 a
  
 -
 -
 n
 t
 h
 r
 e
 a
 d
 s
  
 1
  
 -
 -
 d
 o
 f
  
 6
  
 -
 -
 s
 e
 p
  
 4
  
 -
 -
 f
 t
 o
 l
  
 .
 0
 0
 0
 1
  
 -
 -
 l
 i
 n
 m
 i
 n
 t
 o
 l
  
 .
 0
 1
  
 

 s
 y
 s
 n
 a
 m
 e
  
  
 L
 i
 n
 u
 x
 

 h
 o
 s
 t
 n
 a
 m
 e
  
 9
 9
 5
 8
 f
 5
 f
 d
 3
 b
 a
 7
 

 m
 a
 c
 h
 i
 n
 e
  
  
 x
 8
 6
 _
 6
 4
 

 u
 s
 e
 r
  
  
  
  
  
 r
 o
 o
 t
 

 d
 o
 f
  
  
  
  
 6
 

 n
 s
 e
 p
  
  
  
  
 1
 

 c
 r
 a
 s
 0
  
  
  
  
 1
 

 f
 t
 o
 l
  
  
  
  
 0
 .
 0
 0
 0
 1
 0
 0
 

 l
 i
 n
 m
 i
 n
 t
 o
 l
  
  
  
  
 0
 .
 0
 1
 0
 0
 0
 0
 

 b
 f
  
  
  
  
  
  
  
 1
 

 b
 f
 l
 i
 m
  
  
  
  
 3
 0
 .
 0
 0
 0
 0
 0
 0
 

 b
 f
 n
 s
 a
 m
 p
  
  
  
  
 3
 0
 

 S
 m
 o
 o
 t
 h
 R
 e
 f
  
 0
 

 S
 a
 t
 P
 c
 t
  
  
  
  
 9
 9
 .
 9
 9
 0
 0
 0
 0
 

 M
 o
 v
 O
 O
 B
  
 0
 

 o
 p
 t
 s
 c
 h
 e
 m
 a
  
 1
 

 R
 e
 a
 d
 i
 n
 g
  
 i
 n
  
 m
 o
 v
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 t
 e
 m
 p
 l
 a
 t
 e
 .
 n
 i
 i
 

 R
 e
 a
 d
 i
 n
 g
  
 i
 n
  
 r
 e
 f
  
 /
 d
 e
 r
 i
 v
 a
 t
 i
 v
 e
 s
 /
 f
 r
 e
 e
 s
 u
 r
 f
 e
 r
 /
 s
 u
 b
 -
 b
 m
 /
 m
 r
 i
 /
 b
 r
 a
 i
 n
 m
 a
 s
 k
 .
 m
 g
 z
 

 R
 e
 a
 d
 i
 n
 g
  
 i
 n
  
 a
 n
 d
  
 a
 p
 p
 l
 y
 i
 n
 g
  
 r
 e
 f
 m
 a
 s
 k
  
 /
 d
 e
 r
 i
 v
 a
 t
 i
 v
 e
 s
 /
 f
 r
 e
 e
 s
 u
 r
 f
 e
 r
 /
 s
 u
 b
 -
 b
 m
 /
 m
 r
 i
 /
 a
 p
 a
 r
 c
 +
 a
 s
 e
 g
 .
 m
 g
 z
 

 S
 e
 t
 t
 i
 n
 g
  
 c
 r
 a
 s
  
 t
 r
 a
 n
 s
 l
 a
 t
 i
 o
 n
  
 p
 a
 r
 a
 m
 e
 t
 e
 r
 s
  
 t
 o
  
 a
 l
 i
 g
 n
  
 c
 e
 n
 t
 e
 r
 s
 

 C
 r
 e
 a
 t
 i
 n
 g
  
 r
 a
 n
 d
 o
 m
  
 n
 u
 m
 b
 e
 r
 s
  
 f
 o
 r
  
 c
 o
 o
 r
 d
 i
 n
 a
 t
 e
  
 d
 i
 t
 h
 e
 r
 i
 n
 g
 

 P
 e
 r
 f
 o
 r
 m
 i
 n
 g
  
 i
 n
 t
 e
 n
 s
 i
 t
 y
  
 d
 i
 t
 h
 e
 r
 i
 n
 g
 

 I
 n
 i
 t
 i
 a
 l
  
 p
 a
 r
 a
 m
 e
 t
 e
 r
 s
  
  
 6
 .
 0
 0
 5
 9
  
 -
 1
 0
 5
 .
 7
 5
 8
 5
  
 -
 9
 .
 6
 4
 2
 9
  
  
 0
 .
 0
 0
 0
 0
  
  
 0
 .
 0
 0
 0
 0
  
  
 0
 .
 0
 0
 0
 0
  
  
 1
 .
 0
 0
 0
 0
  
  
 1
 .
 0
 0
 0
 0
  
  
 1
 .
 0
 0
 0
 0
  
  
 0
 .
 0
 0
 0
 0
  
  
 0
 .
 0
 0
 0
 0
  
  
 0
 .
 0
 0
 0
 0
  
 

 S
 e
 p
 a
 r
 a
 t
 i
 o
 n
  
 l
 i
 s
 t
  
 (
 1
 )
 :
  
  
 4
  
  
  
 m
 i
 n
  
 =
  
 4
 

 D
 o
 S
 m
 o
 o
 t
 h
 i
 n
 g
  
 1
 

 D
 o
 C
 o
 o
 r
 d
 D
 i
 t
 h
 e
 r
  
 1
 

 D
 o
 I
 n
 t
 e
 n
 s
 i
 t
 y
 D
 i
 t
 h
 e
 r
  
 1
 

 n
 i
 t
 e
 r
 s
 m
 a
 x
  
 4
 

 f
 t
 o
 l
  
 1
 .
 0
 0
 0
 e
 -
 0
 4
 

 l
 i
 n
 m
 i
 n
 t
 o
 l
  
 1
 .
 0
 0
 0
 e
 -
 0
 2
 

 S
 a
 t
 P
 c
 t
  
 9
 9
 .
 9
 9
 0
 0
 0
 0
 

 H
 i
 s
 t
  
 F
 W
 H
 M
  
 7
 .
 0
 0
 0
 0
 0
 0
  
 7
 .
 0
 0
 0
 0
 0
 0
 

 n
 t
 h
 r
 e
 a
 d
 s
  
 1
 

 m
 o
 v
 s
 a
 t
  
 =
  
 2
 3
 0
 5
 .
 5
 0
 9
 0
 

 m
 o
 v
  
 g
 s
 t
 d
  
 1
 .
 9
 2
 4
 8
  
 1
 .
 9
 2
 3
 3
  
 1
 .
 9
 2
 4
 8
 

 S
 m
 o
 o
 t
 h
 i
 n
 g
  
 m
 o
 v
 

 r
 e
 f
 s
 a
 t
  
 =
  
 1
 1
 6
 .
 0
 0
 0
 0
 

 r
 e
 f
  
 g
 s
 t
 d
  
 1
 .
 9
 2
 8
 3
  
 1
 .
 9
 2
 8
 3
  
 1
 .
 9
 2
 8
 3
 

 S
 m
 o
 o
 t
 h
 i
 n
 g
  
 r
 e
 f
 

 C
 O
 R
 E
 G
 p
 r
 e
 p
 r
 o
 c
 (
 )
  
 d
 o
 n
 e
 

 T
 e
 s
 t
 i
 n
 g
  
 i
 f
  
 m
 o
 v
  
 a
 n
 d
  
 t
 a
 r
 g
 e
 t
  
 o
 v
 e
 r
 l
 a
 p
 

 I
 n
 i
 t
  
 c
 o
 s
 t
  
  
  
 -
 1
 .
 0
 2
 0
 0
 6
 3
 2
 4
 1
 8
 

 n
 h
 i
 t
 s
  
 =
  
 2
 3
 3
 5
 4
  
 o
 u
 t
  
 o
 f
  
 3
 2
 7
 6
 8
 0
 0
 0
 ,
  
 P
 e
 r
 c
 e
 n
 t
  
 O
 v
 e
 r
 l
 a
 p
 :
  
  
  
 4
 .
 6
 

 I
 n
 i
 t
 i
 a
 l
  
  
 R
 e
 f
 R
 A
 S
 -
 t
 o
 -
 M
 o
 v
 R
 A
 S
 

  
 1
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 6
 .
 0
 0
 5
 9
 0
 ;
 

  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
 -
 1
 0
 5
 .
 7
 5
 8
 5
 4
 ;
 

  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 .
 0
 0
 0
 0
 0
  
  
 -
 9
 .
 6
 4
 2
 8
 7
 ;
 

  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 .
 0
 0
 0
 0
 0
 ;
 

 I
 n
 i
 t
 i
 a
 l
  
  
 R
 e
 f
 V
 o
 x
 -
 t
 o
 -
 M
 o
 v
 V
 o
 x
 

  
 0
 .
 9
 3
 8
 4
 2
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
 -
 5
 4
 .
 1
 7
 7
 4
 5
 ;
 

  
 0
 .
 0
 0
 0
 0
 0
  
  
 -
 0
 .
 0
 0
 4
 8
 8
  
  
  
 0
 .
 9
 1
 4
 2
 7
  
  
 -
 1
 2
 8
 .
 5
 4
 7
 6
 7
 ;
 

  
 0
 .
 0
 0
 0
 0
 0
  
  
 -
 0
 .
 9
 3
 8
 4
 0
  
  
 -
 0
 .
 0
 0
 5
 0
 1
  
  
  
 2
 4
 5
 .
 9
 7
 4
 6
 6
 ;
 

  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 .
 0
 0
 0
 0
 0
 ;
 

 s
 e
 p
  
 =
  
 4
  
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 

 C
 O
 R
 E
 G
 o
 p
 t
 B
 r
 u
 t
 e
 F
 o
 r
 c
 e
 (
 )
  
 3
 0
  
 1
  
 3
 0
 

 T
 u
 r
 n
 i
 n
 g
  
 o
 n
  
 M
 o
 v
 O
 O
 B
  
 f
 o
 r
  
 B
 r
 u
 t
 e
 F
 o
 r
 c
 e
  
 S
 e
 a
 r
 c
 h
 

 #
 B
 F
 #
  
 s
 e
 p
 =
  
 4
  
 i
 t
 e
 r
 =
 0
  
 l
 i
 m
 =
 3
 0
 .
 0
  
 d
 e
 l
 t
 a
 =
 2
 .
 0
 0
  
  
 -
 7
 .
 9
 9
 4
 1
 0
  
 -
 9
 7
 .
 7
 5
 8
 5
 4
  
 -
 2
 1
 .
 6
 4
 2
 8
 7
  
  
 -
 4
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 0
 5
 6
 0
 7
 9
 

 T
 u
 r
 n
 i
 n
 g
  
  
 M
 o
 v
 O
 O
 B
  
 b
 a
 c
 k
  
 o
 f
 f
  
 a
 f
 t
 e
 r
  
 b
 r
 u
 t
 e
  
 f
 o
 r
 c
 e
  
 s
 e
 a
 r
 c
 h
 

 

 

 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 

 I
 n
 i
 t
  
 P
 o
 w
 e
 l
  
 P
 a
 r
 a
 m
 s
  
 d
 o
 f
  
 =
  
 6
 

 S
 t
 a
 r
 t
 i
 n
 g
  
 O
 p
 e
 n
 P
 o
 w
 e
 l
 2
 (
 )
 ,
  
 s
 e
 p
  
 =
  
 4
 

 I
 n
 i
 t
 i
 a
 l
 C
 o
 s
 t
  
  
  
  
  
  
  
  
 -
 1
 .
 0
 3
 5
 0
 5
 6
 9
 4
 8
 7
  
 

 #
 @
 #
  
  
 4
  
  
 1
 8
 8
  
  
 -
 7
 .
 9
 9
 4
 1
 0
  
 -
 9
 7
 .
 7
 5
 8
 5
 4
  
 -
 2
 1
 .
 6
 4
 2
 8
 7
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 5
 0
 5
 6
 9
 

 f
 s
 _
 p
 o
 w
 e
 l
 l
 :
 :
 m
 i
 n
 i
 m
 i
 z
 e
 

  
  
 n
 p
 a
 r
 a
 m
 s
  
 6
 

  
  
 m
 a
 x
 f
 e
 v
  
 4
 

  
  
 f
 t
 o
 l
  
  
  
 0
 .
 0
 0
 0
 1
 0
 0
 

  
  
 l
 i
 n
 m
 i
 n
 _
 x
 t
 o
 l
 _
  
  
  
 0
 .
 0
 1
 0
 0
 0
 0
 

  
  
 p
 o
 w
 e
 l
 l
  
 n
 t
 h
 i
 t
 e
 r
  
 0
 :
  
 f
 r
 e
 t
  
 =
  
 -
 1
 .
 0
 3
 5
 0
 5
 7
 

 #
 @
 #
  
  
 4
  
  
 1
 9
 1
  
  
 -
 9
 .
 6
 1
 2
 1
 4
  
 -
 9
 7
 .
 7
 5
 8
 5
 4
  
 -
 2
 1
 .
 6
 4
 2
 8
 7
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 5
 3
 4
 4
 6
 

 #
 @
 #
  
  
 4
  
  
 1
 9
 2
  
  
 -
 9
 .
 9
 7
 3
 7
 0
  
 -
 9
 7
 .
 7
 5
 8
 5
 4
  
 -
 2
 1
 .
 6
 4
 2
 8
 7
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 5
 3
 6
 2
 1
 

 #
 @
 #
  
  
 4
  
  
 1
 9
 6
  
  
 -
 1
 0
 .
 0
 4
 6
 3
 5
  
 -
 9
 7
 .
 7
 5
 8
 5
 4
  
 -
 2
 1
 .
 6
 4
 2
 8
 7
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 5
 3
 6
 8
 0
 

 #
 @
 #
  
  
 4
  
  
 1
 9
 7
  
  
 -
 1
 0
 .
 0
 9
 1
 2
 5
  
 -
 9
 7
 .
 7
 5
 8
 5
 4
  
 -
 2
 1
 .
 6
 4
 2
 8
 7
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 5
 3
 7
 3
 0
 

 #
 @
 #
  
  
 4
  
  
 1
 9
 9
  
  
 -
 1
 0
 .
 0
 8
 1
 2
 1
  
 -
 9
 7
 .
 7
 5
 8
 5
 4
  
 -
 2
 1
 .
 6
 4
 2
 8
 7
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 5
 3
 7
 4
 4
 

 #
 @
 #
  
  
 4
  
  
 2
 0
 0
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 9
 7
 .
 7
 5
 8
 5
 4
  
 -
 2
 1
 .
 6
 4
 2
 8
 7
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 5
 3
 7
 6
 0
 

 #
 @
 #
  
  
 4
  
  
 2
 0
 4
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 9
 9
 .
 3
 7
 6
 5
 7
  
 -
 2
 1
 .
 6
 4
 2
 8
 7
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 6
 5
 1
 1
 9
 

 #
 @
 #
  
  
 4
  
  
 2
 0
 5
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 1
 .
 9
 9
 4
 6
 1
  
 -
 2
 1
 .
 6
 4
 2
 8
 7
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 8
 1
 0
 1
 1
 

 #
 @
 #
  
  
 4
  
  
 2
 0
 6
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 1
 4
 .
 2
 1
 3
 2
 3
  
 -
 2
 1
 .
 6
 4
 2
 8
 7
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 9
 0
 2
 1
 0
 

 #
 @
 #
  
  
 4
  
  
 2
 0
 7
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 1
 5
 4
 3
 2
  
 -
 2
 1
 .
 6
 4
 2
 8
 7
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 9
 6
 0
 7
 2
 

 #
 @
 #
  
  
 4
  
  
 2
 1
 2
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 9
 2
 4
 1
  
 -
 2
 1
 .
 6
 4
 2
 8
 7
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 9
 7
 0
 6
 2
 

 #
 @
 #
  
  
 4
  
  
 2
 1
 4
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 7
 9
 8
 5
 1
  
 -
 2
 1
 .
 6
 4
 2
 8
 7
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 9
 7
 2
 7
 6
 

 #
 @
 #
  
  
 4
  
  
 2
 1
 8
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 1
 .
 6
 4
 2
 8
 7
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 9
 7
 2
 8
 2
 

 #
 @
 #
  
  
 4
  
  
 2
 2
 1
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 3
 .
 2
 6
 0
 9
 0
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 9
 7
 9
 2
 4
 

 #
 @
 #
  
  
 4
  
  
 2
 2
 7
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 3
 .
 1
 2
 0
 7
 1
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 9
 7
 9
 6
 5
 

 #
 @
 #
  
  
 4
  
  
 2
 2
 8
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 3
 .
 0
 1
 9
 3
 7
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 9
 7
 9
 8
 3
 

 #
 @
 #
  
  
 4
  
  
 2
 3
 1
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 6
 4
 4
 4
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 9
 8
 0
 1
 0
 

 #
 @
 #
  
  
 4
  
  
 2
 3
 5
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 7
 4
 4
 4
  
 -
 4
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 3
 9
 8
 0
 1
 2
 

 #
 @
 #
  
  
 4
  
  
 2
 3
 7
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 7
 4
 4
 4
  
 -
 3
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 4
 0
 0
 4
 0
 0
 

 #
 @
 #
  
  
 4
  
  
 2
 3
 8
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 7
 4
 4
 4
  
 -
 1
 .
 3
 8
 1
 9
 7
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 4
 0
 1
 2
 5
 6
 

 #
 @
 #
  
  
 4
  
  
 2
 4
 0
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 7
 4
 4
 4
  
 1
 .
 2
 3
 6
 0
 7
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 4
 0
 4
 6
 0
 3
 

 #
 @
 #
  
  
 4
  
  
 2
 4
 1
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 7
 4
 4
 4
  
 5
 .
 4
 7
 2
 1
 4
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 4
 0
 6
 9
 3
 4
 

 #
 @
 #
  
  
 4
  
  
 2
 4
 5
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 7
 4
 4
 4
  
 4
 .
 8
 5
 4
 1
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 4
 0
 7
 2
 9
 9
 

 #
 @
 #
  
  
 4
  
  
 2
 4
 8
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 7
 4
 4
 4
  
 4
 .
 7
 0
 8
 2
 0
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 4
 0
 7
 3
 5
 1
 

 #
 @
 #
  
  
 4
  
  
 2
 5
 2
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 7
 4
 4
 4
  
 4
 .
 7
 3
 1
 3
 4
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 4
 0
 7
 3
 7
 6
 

 #
 @
 #
  
  
 4
  
  
 2
 5
 4
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 7
 4
 4
 4
  
 4
 .
 7
 2
 1
 3
 4
  
 0
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 4
 0
 7
 4
 3
 9
 

 #
 @
 #
  
  
 4
  
  
 2
 5
 6
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 7
 4
 4
 4
  
 4
 .
 7
 2
 1
 3
 4
  
 1
 .
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 4
 0
 7
 5
 5
 6
 

 #
 @
 #
  
  
 4
  
  
 2
 6
 0
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 7
 4
 4
 4
  
 4
 .
 7
 2
 1
 3
 4
  
 0
 .
 6
 1
 8
 0
 3
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 4
 0
 7
 7
 5
 9
 

 #
 @
 #
  
  
 4
  
  
 2
 6
 5
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 7
 4
 4
 4
  
 4
 .
 7
 2
 1
 3
 4
  
 0
 .
 6
 0
 7
 4
 5
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 -
 1
 .
 0
 4
 0
 7
 7
 8
 3
 

 #
 @
 #
  
  
 4
  
  
 2
 7
 3
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 7
 4
 4
 4
  
 4
 .
 7
 2
 1
 3
 4
  
 0
 .
 6
 0
 7
 4
 5
  
 0
 .
 3
 8
 1
 9
 7
  
  
  
 -
 1
 .
 0
 4
 0
 7
 8
 1
 0
 

 #
 @
 #
  
  
 4
  
  
 2
 7
 5
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 7
 4
 4
 4
  
 4
 .
 7
 2
 1
 3
 4
  
 0
 .
 6
 0
 7
 4
 5
  
 0
 .
 6
 1
 8
 0
 3
  
  
  
 -
 1
 .
 0
 4
 0
 8
 0
 1
 0
 

 #
 @
 #
  
  
 4
  
  
 2
 7
 6
  
  
 -
 1
 0
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 7
 4
 4
 4
  
 4
 .
 7
 2
 1
 3
 4
  
 0
 .
 6
 0
 7
 4
 5
  
 0
 .
 7
 6
 3
 9
 3
  
  
  
 -
 1
 .
 0
 4
 0
 8
 1
 5
 8
 

  
  
 p
 o
 w
 e
 l
 l
  
 n
 t
 h
 i
 t
 e
 r
  
 1
 :
  
 f
 r
 e
 t
  
 =
  
 -
 1
 .
 0
 4
 0
 8
 1
 6
 

 #
 @
 #
  
  
 4
  
  
 2
 8
 4
  
  
 -
 9
 .
 0
 7
 1
 2
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 7
 4
 4
 4
  
 4
 .
 7
 2
 1
 3
 4
  
 0
 .
 6
 0
 7
 4
 5
  
 0
 .
 7
 6
 3
 9
 3
  
  
  
 -
 1
 .
 0
 4
 0
 9
 0
 9
 2
 

 #
 @
 #
  
  
 4
  
  
 2
 8
 8
  
  
 -
 9
 .
 4
 5
 3
 1
 8
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 7
 4
 4
 4
  
 4
 .
 7
 2
 1
 3
 4
  
 0
 .
 6
 0
 7
 4
 5
  
 0
 .
 7
 6
 3
 9
 3
  
  
  
 -
 1
 .
 0
 4
 0
 9
 1
 3
 0
 

 #
 @
 #
  
  
 4
  
  
 2
 8
 9
  
  
 -
 9
 .
 3
 1
 6
 2
 2
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 2
 .
 9
 7
 4
 4
 4
  
 4
 .
 7
 2
 1
 3
 4
  
 0
 .
 6
 0
 7
 4
 5
  
 0
 .
 7
 6
 3
 9
 3
  
  
  
 -
 1
 .
 0
 4
 0
 9
 2
 1
 8
 

 #
 @
 #
  
  
 4
  
  
 3
 0
 6
  
  
 -
 9
 .
 3
 1
 6
 2
 2
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 4
 .
 5
 9
 2
 4
 7
  
 4
 .
 7
 2
 1
 3
 4
  
 0
 .
 6
 0
 7
 4
 5
  
 0
 .
 7
 6
 3
 9
 3
  
  
  
 -
 1
 .
 0
 4
 1
 2
 5
 1
 4
 

 #
 @
 #
  
  
 4
  
  
 3
 2
 3
  
  
 -
 9
 .
 3
 1
 6
 2
 2
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 4
 .
 5
 9
 2
 4
 7
  
 4
 .
 6
 6
 0
 4
 4
  
 0
 .
 6
 0
 7
 4
 5
  
 0
 .
 7
 6
 3
 9
 3
  
  
  
 -
 1
 .
 0
 4
 1
 2
 6
 0
 0
 

 #
 @
 #
  
  
 4
  
  
 3
 2
 4
  
  
 -
 9
 .
 3
 1
 6
 2
 2
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 4
 .
 5
 9
 2
 4
 7
  
 4
 .
 6
 8
 0
 4
 1
  
 0
 .
 6
 0
 7
 4
 5
  
 0
 .
 7
 6
 3
 9
 3
  
  
  
 -
 1
 .
 0
 4
 1
 2
 7
 2
 6
 

 #
 @
 #
  
  
 4
  
  
 3
 3
 0
  
  
 -
 9
 .
 3
 1
 6
 2
 2
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 4
 .
 5
 9
 2
 4
 7
  
 4
 .
 6
 8
 0
 4
 1
  
 -
 0
 .
 0
 1
 0
 5
 8
  
 0
 .
 7
 6
 3
 9
 3
  
  
  
 -
 1
 .
 0
 4
 1
 3
 0
 7
 4
 

 #
 @
 #
  
  
 4
  
  
 3
 4
 6
  
  
 -
 9
 .
 3
 1
 6
 2
 2
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 4
 .
 5
 9
 2
 4
 7
  
 4
 .
 6
 8
 0
 4
 1
  
 -
 0
 .
 0
 1
 0
 5
 8
  
 0
 .
 8
 0
 9
 6
 7
  
  
  
 -
 1
 .
 0
 4
 1
 3
 2
 5
 1
 

 #
 @
 #
  
  
 4
  
  
 3
 6
 3
  
  
 -
 9
 .
 3
 0
 8
 6
 7
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 4
 .
 6
 0
 8
 6
 5
  
 4
 .
 6
 8
 0
 0
 0
  
 -
 0
 .
 0
 1
 6
 7
 7
  
 0
 .
 8
 1
 0
 1
 2
  
  
  
 -
 1
 .
 0
 4
 1
 3
 3
 3
 9
 

  
  
 p
 o
 w
 e
 l
 l
  
 n
 t
 h
 i
 t
 e
 r
  
 2
 :
  
 f
 r
 e
 t
  
 =
  
 -
 1
 .
 0
 4
 1
 3
 3
 4
 

 #
 @
 #
  
  
 4
  
  
 3
 6
 9
  
  
 -
 8
 .
 9
 2
 6
 7
 0
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 4
 .
 6
 0
 8
 6
 5
  
 4
 .
 6
 8
 0
 0
 0
  
 -
 0
 .
 0
 1
 6
 7
 7
  
 0
 .
 8
 1
 0
 1
 2
  
  
  
 -
 1
 .
 0
 4
 1
 3
 4
 3
 9
 

 #
 @
 #
  
  
 4
  
  
 3
 7
 0
  
  
 -
 9
 .
 0
 4
 6
 2
 3
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 4
 .
 6
 0
 8
 6
 5
  
 4
 .
 6
 8
 0
 0
 0
  
 -
 0
 .
 0
 1
 6
 7
 7
  
 0
 .
 8
 1
 0
 1
 2
  
  
  
 -
 1
 .
 0
 4
 1
 3
 5
 1
 7
 

 #
 @
 #
  
  
 4
  
  
 3
 7
 2
  
  
 -
 9
 .
 0
 0
 4
 6
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 4
 .
 6
 0
 8
 6
 5
  
 4
 .
 6
 8
 0
 0
 0
  
 -
 0
 .
 0
 1
 6
 7
 7
  
 0
 .
 8
 1
 0
 1
 2
  
  
  
 -
 1
 .
 0
 4
 1
 3
 5
 9
 8
 

 #
 @
 #
  
  
 4
  
  
 4
 3
 5
  
  
 -
 8
 .
 9
 9
 7
 0
 6
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
  
 -
 2
 4
 .
 6
 2
 4
 8
 3
  
 4
 .
 6
 7
 9
 5
 9
  
 -
 0
 .
 0
 2
 2
 9
 5
  
 0
 .
 8
 1
 0
 5
 8
  
  
  
 -
 1
 .
 0
 4
 1
 3
 6
 1
 9
 

 P
 o
 w
 e
 l
 l
  
 d
 o
 n
 e
  
 n
 i
 t
 e
 r
 s
  
 t
 o
 t
 a
 l
  
 =
  
 2
 

 O
 p
 t
 T
 i
 m
 e
 S
 e
 c
  
 1
 4
 .
 9
  
 s
 e
 c
 

 O
 p
 t
 T
 i
 m
 e
 M
 i
 n
  
  
 0
 .
 2
 5
  
 m
 i
 n
 

 n
 E
 v
 a
 l
 s
  
 4
 3
 6
 

 F
 i
 n
 a
 l
  
 p
 a
 r
 a
 m
 e
 t
 e
 r
 s
  
  
 -
 8
 .
 9
 9
 7
 0
 5
 6
 9
 6
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 0
 9
 8
 3
  
 -
 2
 4
 .
 6
 2
 4
 8
 3
 2
 1
 5
  
  
  
 4
 .
 6
 7
 9
 5
 9
 3
 0
 9
  
  
 -
 0
 .
 0
 2
 2
 9
 4
 5
 4
 8
  
  
  
 0
 .
 8
 1
 0
 5
 8
 0
 7
 3
  
 

 F
 i
 n
 a
 l
  
 c
 o
 s
 t
  
  
  
 -
 1
 .
 0
 4
 1
 3
 6
 1
 9
 3
 9
 8
 3
 0
 2
 5
 4
 

  
 

 

 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 

 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 u
 t
 i
 m
 e
 s
 e
 c
  
  
  
  
 1
 0
 6
 .
 6
 7
 4
 4
 2
 4
 

 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 s
 t
 i
 m
 e
 s
 e
 c
  
  
  
  
 0
 .
 7
 7
 3
 9
 9
 5
 

 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 r
 u
 _
 m
 a
 x
 r
 s
 s
  
  
  
 8
 5
 5
 4
 9
 2
 

 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 r
 u
 _
 i
 x
 r
 s
 s
  
  
  
  
 0
 

 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 r
 u
 _
 i
 d
 r
 s
 s
  
  
  
  
 0
 

 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 r
 u
 _
 i
 s
 r
 s
 s
  
  
  
  
 0
 

 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 r
 u
 _
 m
 i
 n
 f
 l
 t
  
  
  
 6
 4
 6
 7
 8
 4
 

 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 r
 u
 _
 m
 a
 j
 f
 l
 t
  
  
  
 3
 1
 

 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 r
 u
 _
 n
 s
 w
 a
 p
  
  
  
  
 0
 

 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 r
 u
 _
 i
 n
 b
 l
 o
 c
 k
  
  
 1
 9
 5
 6
 0
 

 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 r
 u
 _
 o
 u
 b
 l
 o
 c
 k
  
  
 1
 6
 

 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 r
 u
 _
 m
 s
 g
 s
 n
 d
  
  
  
 0
 

 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 r
 u
 _
 m
 s
 g
 r
 c
 v
  
  
  
 0
 

 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 r
 u
 _
 n
 s
 i
 g
 n
 a
 l
 s
  
 0
 

 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 r
 u
 _
 n
 v
 c
 s
 w
  
  
  
  
 4
 2
 

 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 r
 u
 _
 n
 i
 v
 c
 s
 w
  
  
  
 7
 1
 

 F
 i
 n
 a
 l
  
  
 R
 e
 f
 R
 A
 S
 -
 t
 o
 -
 M
 o
 v
 R
 A
 S
 

  
 0
 .
 9
 9
 9
 9
 0
  
  
  
 0
 .
 0
 1
 4
 1
 5
  
  
 -
 0
 .
 0
 0
 0
 4
 0
  
  
 -
 8
 .
 9
 9
 7
 0
 6
 ;
 

 -
 0
 .
 0
 1
 4
 0
 7
  
  
  
 0
 .
 9
 9
 6
 5
 7
  
  
  
 0
 .
 0
 8
 1
 5
 8
  
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
 1
 ;
 

  
 0
 .
 0
 0
 1
 5
 5
  
  
 -
 0
 .
 0
 8
 1
 5
 7
  
  
  
 0
 .
 9
 9
 6
 6
 7
  
  
 -
 2
 4
 .
 6
 2
 4
 8
 3
 ;
 

  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 .
 0
 0
 0
 0
 0
 ;
 

 F
 i
 n
 a
 l
  
  
 R
 e
 f
 V
 o
 x
 -
 t
 o
 -
 M
 o
 v
 V
 o
 x
 

  
 0
 .
 9
 3
 8
 3
 2
  
  
 -
 0
 .
 0
 0
 0
 3
 8
  
  
 -
 0
 .
 0
 1
 3
 2
 8
  
  
 -
 2
 9
 .
 8
 0
 9
 5
 2
 ;
 

  
 0
 .
 0
 1
 2
 8
 5
  
  
 -
 0
 .
 0
 7
 9
 4
 6
  
  
  
 0
 .
 9
 1
 0
 7
 4
  
  
 -
 1
 2
 4
 .
 3
 7
 7
 1
 1
 ;
 

 -
 0
 .
 0
 0
 1
 5
 3
  
  
 -
 0
 .
 9
 3
 4
 8
 7
  
  
 -
 0
 .
 0
 8
 1
 5
 4
  
  
  
 2
 3
 6
 .
 9
 7
 4
 9
 6
 ;
 

  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 .
 0
 0
 0
 0
 0
 ;
 

 F
 i
 n
 a
 l
  
 p
 a
 r
 a
 m
 e
 t
 e
 r
 s
  
 -
 8
 .
 9
 9
 7
 1
  
 -
 1
 0
 9
 .
 8
 0
 8
 5
  
 -
 2
 4
 .
 6
 2
 4
 8
  
  
 4
 .
 6
 7
 9
 6
  
 -
 0
 .
 0
 2
 2
 9
  
  
 0
 .
 8
 1
 0
 6
  
 

 n
 h
 i
 t
 s
  
 =
  
 2
 3
 2
 9
 1
  
 o
 u
 t
  
 o
 f
  
 3
 2
 7
 6
 8
 0
 0
 0
 ,
  
 P
 e
 r
 c
 e
 n
 t
  
 O
 v
 e
 r
 l
 a
 p
 :
  
  
  
 4
 .
 5
 

 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 R
 u
 n
 T
 i
 m
 e
 S
 e
 c
  
 1
 0
 7
 .
 5
  
 s
 e
 c
 

 T
 o
  
 c
 h
 e
 c
 k
  
 r
 u
 n
 :
 

  
  
  
 t
 k
 r
 e
 g
 i
 s
 t
 e
 r
 f
 v
  
 -
 -
 m
 o
 v
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 t
 e
 m
 p
 l
 a
 t
 e
 .
 n
 i
 i
  
 -
 -
 t
 a
 r
 g
  
 /
 d
 e
 r
 i
 v
 a
 t
 i
 v
 e
 s
 /
 f
 r
 e
 e
 s
 u
 r
 f
 e
 r
 /
 s
 u
 b
 -
 b
 m
 /
 m
 r
 i
 /
 b
 r
 a
 i
 n
 m
 a
 s
 k
 .
 m
 g
 z
  
 -
 -
 r
 e
 g
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 m
 r
 i
 _
 c
 o
 r
 e
 g
 .
 l
 t
 a
  
 -
 -
 s
  
 s
 u
 b
 -
 b
 m
  
 -
 -
 s
 u
 r
 f
 s
  
 

 

 m
 r
 i
 _
 c
 o
 r
 e
 g
  
 d
 o
 n
 e
 

 

 m
 r
 i
 _
 s
 e
 g
 r
 e
 g
  
 -
 -
 m
 o
 v
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 t
 e
 m
 p
 l
 a
 t
 e
 .
 n
 i
 i
  
 -
 -
 i
 n
 i
 t
 -
 r
 e
 g
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 r
 e
 g
 .
 i
 n
 i
 t
 .
 d
 a
 t
  
 -
 -
 o
 u
 t
 -
 r
 e
 g
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 b
 b
 r
 .
 p
 a
 s
 s
 1
 .
 d
 a
 t
  
 -
 -
 s
 u
 b
 s
 a
 m
 p
 -
 b
 r
 u
 t
 e
  
 1
 0
 0
  
 -
 -
 s
 u
 b
 s
 a
 m
 p
  
 1
 0
 0
  
 -
 -
 t
 o
 l
  
 1
 e
 -
 4
  
 -
 -
 t
 o
 l
 1
 d
  
 1
 e
 -
 3
  
 -
 -
 b
 r
 u
 t
 e
  
 -
 4
  
 4
  
 4
  
 -
 -
 s
 u
 r
 f
  
 w
 h
 i
 t
 e
  
 -
 -
 g
 m
 -
 p
 r
 o
 j
 -
 f
 r
 a
 c
  
 0
 .
 5
  
 -
 -
 g
 m
 -
 g
 t
 -
 w
 m
  
 0
 .
 5
 

 $
 I
 d
 :
  
 m
 r
 i
 _
 s
 e
 g
 r
 e
 g
 .
 c
 ,
 v
  
 1
 .
 1
 1
 3
  
 2
 0
 1
 6
 /
 0
 5
 /
 1
 0
  
 0
 3
 :
 2
 3
 :
 2
 0
  
 g
 r
 e
 v
 e
  
 E
 x
 p
  
 $
 

 s
 e
 t
 e
 n
 v
  
 S
 U
 B
 J
 E
 C
 T
 S
 _
 D
 I
 R
  
 /
 d
 e
 r
 i
 v
 a
 t
 i
 v
 e
 s
 /
 f
 r
 e
 e
 s
 u
 r
 f
 e
 r
 

 c
 d
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 

 m
 r
 i
 _
 s
 e
 g
 r
 e
 g
  
 -
 -
 m
 o
 v
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 t
 e
 m
 p
 l
 a
 t
 e
 .
 n
 i
 i
  
 -
 -
 i
 n
 i
 t
 -
 r
 e
 g
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 r
 e
 g
 .
 i
 n
 i
 t
 .
 d
 a
 t
  
 -
 -
 o
 u
 t
 -
 r
 e
 g
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 b
 b
 r
 .
 p
 a
 s
 s
 1
 .
 d
 a
 t
  
 -
 -
 s
 u
 b
 s
 a
 m
 p
 -
 b
 r
 u
 t
 e
  
 1
 0
 0
  
 -
 -
 s
 u
 b
 s
 a
 m
 p
  
 1
 0
 0
  
 -
 -
 t
 o
 l
  
 1
 e
 -
 4
  
 -
 -
 t
 o
 l
 1
 d
  
 1
 e
 -
 3
  
 -
 -
 b
 r
 u
 t
 e
  
 -
 4
  
 4
  
 4
  
 -
 -
 s
 u
 r
 f
  
 w
 h
 i
 t
 e
  
 -
 -
 g
 m
 -
 p
 r
 o
 j
 -
 f
 r
 a
 c
  
 0
 .
 5
  
 -
 -
 g
 m
 -
 g
 t
 -
 w
 m
  
 0
 .
 5
  
 

 s
 y
 s
 n
 a
 m
 e
  
  
 L
 i
 n
 u
 x
 

 h
 o
 s
 t
 n
 a
 m
 e
  
 9
 9
 5
 8
 f
 5
 f
 d
 3
 b
 a
 7
 

 m
 a
 c
 h
 i
 n
 e
  
  
 x
 8
 6
 _
 6
 4
 

 u
 s
 e
 r
  
  
  
  
  
 r
 o
 o
 t
 

 m
 o
 v
 v
 o
 l
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 t
 e
 m
 p
 l
 a
 t
 e
 .
 n
 i
 i
 

 r
 e
 g
 f
 i
 l
 e
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 r
 e
 g
 .
 i
 n
 i
 t
 .
 d
 a
 t
 

 s
 u
 b
 j
 e
 c
 t
  
 s
 u
 b
 -
 b
 m
 

 d
 o
 f
  
 6
 

 o
 u
 t
 r
 e
 g
 f
 i
 l
 e
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 b
 b
 r
 .
 p
 a
 s
 s
 1
 .
 d
 a
 t
 

 U
 s
 e
 M
 a
 s
 k
  
 0
 

 U
 s
 e
 L
 H
  
 1
 

 U
 s
 e
 R
 H
  
 1
 

 n
 s
 u
 b
 s
 a
 m
 p
  
 1
 0
 0
 

 P
 e
 n
 a
 l
 t
 y
 S
 i
 g
 n
  
  
 -
 1
 

 P
 e
 n
 a
 l
 t
 y
 S
 l
 o
 p
 e
  
 0
 .
 5
 0
 0
 0
 0
 0
 

 P
 e
 n
 a
 l
 t
 y
 C
 e
 n
 t
 e
 r
  
 0
 .
 0
 0
 0
 0
 0
 0
 

 s
 u
 r
 f
 n
 a
 m
 e
  
 w
 h
 i
 t
 e
 

 G
 M
 P
 r
 o
 j
 F
 r
 a
 c
  
 0
 .
 5
 0
 0
 0
 0
 0
 

 W
 M
 P
 r
 o
 j
 A
 b
 s
  
 2
 .
 0
 0
 0
 0
 0
 0
 

 l
 h
 c
 o
 s
 t
 f
 i
 l
 e
  
 (
 n
 u
 l
 l
 )
 

 r
 h
 c
 o
 s
 t
 f
 i
 l
 e
  
 (
 n
 u
 l
 l
 )
 

 i
 n
 t
 e
 r
 p
  
  
 t
 r
 i
 l
 i
 n
 e
 a
 r
  
 (
 1
 )
 

 f
 r
 a
 m
 e
  
  
 0
 

 T
 o
 l
 P
 o
 w
 e
 l
 l
  
 0
 .
 0
 0
 0
 1
 0
 0
 

 n
 M
 a
 x
 I
 t
 e
 r
 s
 P
 o
 w
 e
 l
 l
  
 3
 6
 

 n
 1
 d
 m
 i
 n
  
  
 3
 

 P
 r
 o
 f
 i
 l
 e
  
  
  
 0
 

 G
 d
 i
 a
 g
 _
 n
 o
  
  
 -
 1
 

 A
 d
 d
 N
 o
 i
 s
 e
  
  
 0
  
 (
 0
 )
 

 S
 y
 n
 t
 h
 S
 e
 e
 d
  
 1
 5
 4
 4
 9
 8
 3
 2
 0
 5
 

 T
 r
 a
 n
 s
 R
 a
 n
 d
 M
 a
 x
  
 0
 .
 0
 0
 0
 0
 0
 0
 

 R
 o
 t
 R
 a
 n
 d
 M
 a
 x
  
 0
 .
 0
 0
 0
 0
 0
 0
 

 T
 r
 a
 n
 s
 l
 a
 t
 i
 o
 n
 s
  
 0
 .
 0
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
 0
 

 R
 o
 t
 a
 t
 i
 o
 n
 s
  
  
  
 0
 .
 0
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
 0
 

 I
 n
 p
 u
 t
  
 r
 e
 g
 

  
 0
 .
 9
 9
 9
 9
 0
  
  
  
 0
 .
 0
 1
 4
 1
 5
  
  
 -
 0
 .
 0
 0
 0
 4
 0
  
  
 -
 1
 5
 .
 0
 9
 8
 0
 3
 ;
 

  
 0
 .
 0
 0
 1
 6
 3
  
  
 -
 0
 .
 0
 8
 6
 8
 9
  
  
  
 0
 .
 9
 9
 6
 2
 2
  
  
 -
 1
 4
 .
 9
 3
 1
 9
 6
 ;
 

  
 0
 .
 0
 1
 4
 0
 6
  
  
 -
 0
 .
 9
 9
 6
 1
 2
  
  
 -
 0
 .
 0
 8
 6
 9
 1
  
  
  
 4
 .
 4
 2
 1
 0
 7
 ;
 

  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 .
 0
 0
 0
 0
 0
 ;
 

 

 L
 o
 a
 d
 i
 n
 g
  
 m
 o
 v
 

 P
 r
 o
 j
 e
 c
 t
 i
 n
 g
  
 L
 H
  
 S
 u
 r
 f
 s
 

 L
 o
 a
 d
 i
 n
 g
  
 l
 h
 .
 w
 h
 i
 t
 e
  
 s
 u
 r
 f
 

 L
 o
 a
 d
 i
 n
 g
  
 l
 h
 .
 t
 h
 i
 c
 k
 n
 e
 s
 s
  
 f
 o
 r
  
 G
 M
 

 G
 M
  
 P
 r
 o
 j
 :
  
 1
  
 0
 .
 5
 0
 0
 0
 0
 0
  
 2
 .
 0
 0
 0
 0
 0
 0
 

 W
 M
  
 P
 r
 o
 j
 :
  
 0
  
 0
 .
 5
 0
 0
 0
 0
 0
  
 2
 .
 0
 0
 0
 0
 0
 0
 

 P
 r
 o
 j
 e
 c
 t
 i
 n
 g
  
 R
 H
  
 S
 u
 r
 f
 s
 

 L
 o
 a
 d
 i
 n
 g
  
 r
 h
 .
 w
 h
 i
 t
 e
  
 s
 u
 r
 f
 

 L
 o
 a
 d
 i
 n
 g
  
 r
 h
 .
 t
 h
 i
 c
 k
 n
 e
 s
 s
  
 f
 o
 r
  
 G
 M
 

 P
 r
 o
 j
 e
 c
 t
 i
 n
 g
  
 R
 H
  
 S
 u
 r
 f
 s
 

 U
 s
 i
 n
 g
  
 l
 h
 .
 c
 o
 r
 t
 e
 x
 .
 l
 a
 b
 e
 l
 

 U
 s
 i
 n
 g
  
 r
 h
 .
 c
 o
 r
 t
 e
 x
 .
 l
 a
 b
 e
 l
 

 C
 o
 m
 p
 u
 t
 i
 n
 g
  
 r
 e
 l
 a
 t
 i
 v
 e
  
 c
 o
 s
 t
 

  
 0
  
  
 -
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
  
 1
 .
 1
 2
 3
 3
 9
 7
 

  
 1
  
  
 -
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
  
 1
 .
 1
 1
 9
 1
 7
 4
 

  
 2
  
  
 -
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
  
 1
 .
 0
 4
 2
 8
 4
 4
 

  
 3
  
  
 -
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
  
 1
 .
 0
 1
 5
 8
 8
 7
 

  
 4
  
  
  
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
  
 0
 .
 9
 9
 8
 6
 8
 0
 

  
 5
  
  
  
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
  
 1
 .
 0
 5
 0
 3
 5
 6
 

  
 6
  
  
  
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
  
 1
 .
 0
 1
 7
 1
 4
 6
 

  
 7
  
  
  
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
  
 1
 .
 0
 5
 6
 2
 3
 8
 

 R
 E
 L
 :
  
  
 8
  
  
 1
 .
 1
 0
 9
 0
 3
 2
  
  
  
  
 8
 .
 4
 2
 3
 7
 2
 3
  
  
 1
 .
 0
 5
 2
 9
 6
 5
  
 r
 e
 l
  
 =
  
 1
 .
 0
 5
 3
 2
 5
  
 

 I
 n
 i
 t
 i
 a
 l
  
 c
 o
 s
 t
 s
  
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 

 N
 u
 m
 b
 e
 r
  
 o
 f
  
 s
 u
 r
 f
 a
 c
 e
  
 h
 i
 t
 s
  
 8
 7
 9
 

 W
 M
  
  
 I
 n
 t
 e
 n
 s
 i
 t
 y
  
  
  
 1
 4
 5
 .
 3
 8
 3
 4
  
 +
 /
 -
  
 2
 3
 2
 .
 7
 4
 9
 6
 

 C
 t
 x
  
 I
 n
 t
 e
 n
 s
 i
 t
 y
  
  
  
 1
 3
 8
 .
 4
 9
 6
 3
  
 +
 /
 -
  
 2
 1
 7
 .
 2
 5
 7
 8
 

 P
 c
 t
  
 C
 o
 n
 t
 r
 a
 s
 t
  
  
  
  
  
 -
 7
 .
 7
 7
 2
 1
  
 +
 /
 -
  
  
 7
 3
 .
 1
 1
 7
 5
 

 C
 o
 s
 t
  
  
  
 1
 .
 1
 0
 9
 0
 

 R
 e
 l
 C
 o
 s
 t
  
  
  
 1
 .
 0
 5
 3
 2
 

 

 

 W
 A
 R
 N
 I
 N
 G
 :
  
 i
 n
 i
 t
 i
 a
 l
  
 G
 -
 W
  
 c
 o
 n
 t
 r
 a
 s
 t
  
 i
 s
  
 n
 e
 g
 a
 t
 i
 v
 e
 ,
  
 b
 u
 t
  
 e
 x
 p
 e
 c
 t
 i
 n
 g
  
 p
 o
 s
 i
 t
 i
 v
 e
 .
 

 I
 f
  
 t
 h
 e
  
 m
 o
 v
  
 d
 a
 t
 a
  
 h
 a
 s
  
 a
  
 T
 1
  
 c
 o
 n
 t
 r
 a
 s
 t
 ,
  
 r
 e
 -
 r
 u
 n
  
 w
 i
 t
 h
  
 -
 -
 T
 1
 

 

 

 

 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 

 B
 r
 u
 t
 e
  
 f
 o
 r
 c
 e
  
 p
 r
 e
 o
 p
 t
  
 -
 4
  
 4
  
 4
 ,
  
 n
  
 =
  
 7
 2
 9
 

  
  
  
  
  
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
  
  
  
  
 1
 .
 0
 6
 2
 9
  
  
  
 1
 .
 0
 6
 2
 9
  
  
 0
 .
 0
 

  
  
  
  
  
 2
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
  
 4
 .
 0
 0
 0
 0
  
  
  
  
  
  
 1
 .
 0
 4
 6
 3
  
  
  
 1
 .
 0
 4
 6
 3
  
  
 0
 .
 0
 

  
  
  
  
  
 9
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
  
  
  
  
 1
 .
 0
 2
 0
 3
  
  
  
 1
 .
 0
 2
 0
 3
  
  
 0
 .
 0
 

  
  
  
  
 1
 1
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
  
 4
 .
 0
 0
 0
 0
  
  
  
  
  
  
 1
 .
 0
 1
 0
 0
  
  
  
 1
 .
 0
 1
 0
 0
  
  
 0
 .
 0
 

  
  
  
  
 5
 2
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
  
 4
 .
 0
 0
 0
 0
  
  
  
 4
 .
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
  
  
  
  
 1
 .
 0
 0
 2
 9
  
  
  
 1
 .
 0
 0
 2
 9
  
  
 0
 .
 0
 

  
  
  
  
 6
 1
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
  
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
  
 4
 .
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
  
  
  
  
 0
 .
 9
 9
 4
 3
  
  
  
 0
 .
 9
 9
 4
 3
  
  
 0
 .
 0
 

  
  
  
 1
 1
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
  
 4
 .
 0
 0
 0
 0
  
  
  
  
  
  
 0
 .
 9
 8
 9
 4
  
  
  
 0
 .
 9
 8
 9
 4
  
  
 0
 .
 0
 

  
  
  
 2
 0
 6
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
  
 4
 .
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
  
 4
 .
 0
 0
 0
 0
  
  
  
 4
 .
 0
 0
 0
 0
  
  
  
  
  
  
 0
 .
 9
 6
 8
 2
  
  
  
 0
 .
 9
 6
 8
 2
  
  
 0
 .
 0
 

  
  
  
 2
 2
 1
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
  
 4
 .
 0
 0
 0
 0
  
  
  
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
  
 4
 .
 0
 0
 0
 0
  
  
  
  
  
  
 0
 .
 9
 6
 6
 3
  
  
  
 0
 .
 9
 6
 6
 3
  
  
 0
 .
 0
 

  
  
  
 2
 5
 9
  
  
  
 0
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
  
 4
 .
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
  
  
  
  
 0
 .
 9
 6
 4
 3
  
  
  
 0
 .
 9
 6
 4
 3
  
  
 0
 .
 0
 

  
  
  
 4
 8
 6
  
  
  
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
  
  
  
  
 0
 .
 9
 5
 7
 0
  
  
  
 0
 .
 9
 5
 7
 0
  
  
 0
 .
 0
 

  
  
  
 4
 9
 7
  
  
  
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
 0
  
  
  
 4
 .
 0
 0
 0
 0
  
  
  
  
  
  
 0
 .
 9
 4
 8
 5
  
  
  
 0
 .
 9
 4
 8
 5
  
  
 0
 .
 0
 

 B
 r
 u
 t
 e
  
 F
 o
 r
 c
 e
  
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 

 M
 i
 n
  
 c
 o
 s
 t
  
 w
 a
 s
  
 0
 .
 9
 4
 8
 5
 3
 4
 

 N
 u
 m
 b
 e
 r
  
 o
 f
  
 i
 t
 e
 r
 a
 t
 i
 o
 n
 s
  
  
  
 7
 2
 9
 

 S
 e
 a
 r
 c
 h
  
 t
 i
 m
 e
  
 1
 .
 5
 4
 7
 0
 0
 0
  
 s
 e
 c
 

 P
 a
 r
 a
 m
 e
 t
 e
 r
 s
  
 a
 t
  
 b
 e
 s
 t
  
 (
 t
 r
 a
 n
 s
 m
 m
 ,
  
 r
 o
 t
 d
 e
 g
 )
 

  
  
 4
 .
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
  
  
 -
 4
 .
 0
 0
 0
  
  
 0
 .
 0
 0
 0
  
 -
 4
 .
 0
 0
 0
  
  
 4
 .
 0
 0
 0
  
 

 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 

 

 S
 t
 a
 r
 t
 i
 n
 g
  
 P
 o
 w
 e
 l
 l
  
 M
 i
 n
 i
 m
 i
 z
 a
 t
 i
 o
 n
 

 I
 n
 i
 t
  
 P
 o
 w
 e
 l
  
 P
 a
 r
 a
 m
 s
  
 d
 o
 f
  
 =
  
 6
 

 0
  
 4
 

 1
  
 -
 4
 

 2
  
 -
 4
 

 3
  
 0
 

 4
  
 -
 4
 

 5
  
 4
 

 f
 s
 _
 p
 o
 w
 e
 l
 l
 :
 :
 m
 i
 n
 i
 m
 i
 z
 e
 

  
  
 n
 p
 a
 r
 a
 m
 s
  
 6
 

  
  
 m
 a
 x
 f
 e
 v
  
 3
 6
 

  
  
 f
 t
 o
 l
  
  
  
 0
 .
 0
 0
 0
 1
 0
 0
 

  
  
 l
 i
 n
 m
 i
 n
 _
 x
 t
 o
 l
 _
  
  
  
 0
 .
 0
 0
 1
 0
 0
 0
 

  
  
 p
 o
 w
 e
 l
 l
  
 n
 t
 h
 i
 t
 e
 r
  
 0
 :
  
 f
 r
 e
 t
  
 =
  
 0
 .
 9
 4
 8
 5
 3
 4
 

  
  
  
 8
  
  
 3
 .
 9
 8
 7
  
 -
 4
 .
 0
 0
 0
  
 -
 4
 .
 0
 0
 0
  
  
 0
 .
 0
 0
 0
  
 -
 4
 .
 0
 0
 0
  
  
 4
 .
 0
 0
 0
  
  
  
 0
 .
 9
 4
 8
 0
 3
 2
 1
 3
 1
 8
 

  
  
 1
 2
  
  
 3
 .
 9
 8
 9
  
 -
 4
 .
 0
 0
 0
  
 -
 4
 .
 0
 0
 0
  
  
 0
 .
 0
 0
 0
  
 -
 4
 .
 0
 0
 0
  
  
 4
 .
 0
 0
 0
  
  
  
 0
 .
 9
 4
 8
 0
 2
 5
 0
 7
 1
 4
 

  
  
 2
 1
  
  
 3
 .
 9
 8
 9
  
 -
 3
 .
 9
 8
 6
  
 -
 4
 .
 0
 0
 0
  
  
 0
 .
 0
 0
 0
  
 -
 4
 .
 0
 0
 0
  
  
 4
 .
 0
 0
 0
  
  
  
 0
 .
 9
 4
 7
 2
 3
 9
 5
 6
 8
 4
 

  
  
 2
 3
  
  
 3
 .
 9
 8
 9
  
 -
 3
 .
 9
 3
 2
  
 -
 4
 .
 0
 0
 0
  
  
 0
 .
 0
 0
 0
  
 -
 4
 .
 0
 0
 0
  
  
 4
 .
 0
 0
 0
  
  
  
 0
 .
 9
 4
 7
 0
 9
 7
 6
 2
 1
 2
 

  
  
 5
 7
  
  
 3
 .
 9
 8
 9
  
 -
 3
 .
 9
 3
 2
  
 -
 4
 .
 0
 0
 0
  
 -
 0
 .
 0
 0
 5
  
 -
 4
 .
 0
 0
 0
  
  
 4
 .
 0
 0
 0
  
  
  
 0
 .
 9
 4
 7
 0
 3
 5
 6
 1
 0
 2
 

  
  
 6
 4
  
  
 3
 .
 9
 8
 9
  
 -
 3
 .
 9
 3
 2
  
 -
 4
 .
 0
 0
 0
  
 -
 0
 .
 0
 0
 5
  
 -
 4
 .
 6
 1
 8
  
  
 4
 .
 0
 0
 0
  
  
  
 0
 .
 9
 4
 2
 0
 1
 1
 4
 7
 1
 6
 

  
  
 7
 0
  
  
 3
 .
 9
 8
 9
  
 -
 3
 .
 9
 3
 2
  
 -
 4
 .
 0
 0
 0
  
 -
 0
 .
 0
 0
 5
  
 -
 4
 .
 5
 8
 5
  
  
 4
 .
 0
 0
 0
  
  
  
 0
 .
 9
 3
 7
 3
 0
 9
 7
 8
 4
 7
 

  
  
 7
 2
  
  
 3
 .
 9
 8
 9
  
 -
 3
 .
 9
 3
 2
  
 -
 4
 .
 0
 0
 0
  
 -
 0
 .
 0
 0
 5
  
 -
 4
 .
 5
 8
 7
  
  
 4
 .
 0
 0
 0
  
  
  
 0
 .
 9
 3
 7
 2
 6
 0
 3
 3
 1
 0
 

  
  
 7
 3
  
  
 3
 .
 9
 8
 9
  
 -
 3
 .
 9
 3
 2
  
 -
 4
 .
 0
 0
 0
  
 -
 0
 .
 0
 0
 5
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 0
 0
  
  
  
 0
 .
 9
 3
 7
 2
 5
 2
 4
 0
 7
 2
 

  
  
 8
 4
  
  
 3
 .
 9
 8
 9
  
 -
 3
 .
 9
 3
 2
  
 -
 4
 .
 0
 0
 0
  
 -
 0
 .
 0
 0
 5
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 1
 6
  
  
  
 0
 .
 9
 3
 7
 2
 4
 1
 8
 7
 1
 7
 

  
  
 8
 5
  
  
 3
 .
 9
 8
 9
  
 -
 3
 .
 9
 3
 2
  
 -
 4
 .
 0
 0
 0
  
 -
 0
 .
 0
 0
 5
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 0
 8
  
  
  
 0
 .
 9
 3
 7
 0
 8
 1
 2
 7
 8
 8
 

  
  
 8
 7
  
  
 3
 .
 9
 8
 9
  
 -
 3
 .
 9
 3
 2
  
 -
 4
 .
 0
 0
 0
  
 -
 0
 .
 0
 0
 5
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 1
 0
  
  
  
 0
 .
 9
 3
 7
 0
 6
 9
 9
 7
 5
 2
 

  
  
 p
 o
 w
 e
 l
 l
  
 n
 t
 h
 i
 t
 e
 r
  
 1
 :
  
 f
 r
 e
 t
  
 =
  
 0
 .
 9
 3
 7
 0
 7
 0
 

  
 1
 0
 1
  
  
 4
 .
 0
 0
 0
  
 -
 3
 .
 9
 3
 2
  
 -
 4
 .
 0
 0
 0
  
 -
 0
 .
 0
 0
 5
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 1
 0
  
  
  
 0
 .
 9
 3
 6
 2
 3
 8
 2
 0
 4
 1
 

  
 1
 0
 3
  
  
 3
 .
 9
 9
 8
  
 -
 3
 .
 9
 3
 2
  
 -
 4
 .
 0
 0
 0
  
 -
 0
 .
 0
 0
 5
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 1
 0
  
  
  
 0
 .
 9
 3
 6
 2
 1
 3
 7
 8
 0
 0
 

  
 1
 0
 4
  
  
 3
 .
 9
 9
 7
  
 -
 3
 .
 9
 3
 2
  
 -
 4
 .
 0
 0
 0
  
 -
 0
 .
 0
 0
 5
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 1
 0
  
  
  
 0
 .
 9
 3
 6
 2
 1
 2
 4
 6
 2
 5
 

  
 1
 1
 6
  
  
 3
 .
 9
 9
 7
  
 -
 3
 .
 9
 3
 8
  
 -
 4
 .
 0
 0
 0
  
 -
 0
 .
 0
 0
 5
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 1
 0
  
  
  
 0
 .
 9
 3
 5
 9
 1
 0
 9
 0
 7
 2
 

  
 1
 1
 7
  
  
 3
 .
 9
 9
 7
  
 -
 3
 .
 9
 3
 9
  
 -
 4
 .
 0
 0
 0
  
 -
 0
 .
 0
 0
 5
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 1
 0
  
  
  
 0
 .
 9
 3
 5
 9
 1
 0
 3
 1
 4
 4
 

  
 1
 3
 2
  
  
 3
 .
 9
 9
 7
  
 -
 3
 .
 9
 3
 9
  
 -
 3
 .
 9
 9
 7
  
 -
 0
 .
 0
 0
 5
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 1
 0
  
  
  
 0
 .
 9
 3
 5
 8
 7
 0
 9
 8
 4
 6
 

  
 1
 4
 3
  
  
 3
 .
 9
 9
 7
  
 -
 3
 .
 9
 3
 9
  
 -
 3
 .
 9
 9
 7
  
 -
 0
 .
 0
 0
 1
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 1
 0
  
  
  
 0
 .
 9
 3
 5
 7
 2
 3
 2
 1
 8
 0
 

  
 1
 4
 6
  
  
 3
 .
 9
 9
 7
  
 -
 3
 .
 9
 3
 9
  
 -
 3
 .
 9
 9
 7
  
  
 0
 .
 0
 0
 3
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 1
 0
  
  
  
 0
 .
 9
 3
 5
 5
 4
 4
 4
 7
 0
 7
 

  
 1
 4
 7
  
  
 3
 .
 9
 9
 7
  
 -
 3
 .
 9
 3
 9
  
 -
 3
 .
 9
 9
 7
  
  
 0
 .
 0
 0
 7
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 1
 0
  
  
  
 0
 .
 9
 3
 5
 3
 7
 0
 0
 0
 3
 4
 

  
 1
 4
 8
  
  
 3
 .
 9
 9
 7
  
 -
 3
 .
 9
 3
 9
  
 -
 3
 .
 9
 9
 7
  
  
 0
 .
 0
 1
 0
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 1
 0
  
  
  
 0
 .
 9
 3
 5
 2
 8
 9
 3
 9
 7
 7
 

  
 1
 7
 5
  
  
 3
 .
 9
 9
 7
  
 -
 3
 .
 9
 3
 9
  
 -
 3
 .
 9
 9
 7
  
  
 0
 .
 0
 1
 0
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 0
 7
  
  
  
 0
 .
 9
 3
 5
 2
 7
 5
 3
 2
 6
 4
 

  
 1
 7
 6
  
  
 3
 .
 9
 9
 7
  
 -
 3
 .
 9
 3
 9
  
 -
 3
 .
 9
 9
 7
  
  
 0
 .
 0
 1
 0
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 0
 8
  
  
  
 0
 .
 9
 3
 5
 2
 7
 2
 0
 1
 0
 3
 

  
 1
 7
 7
  
  
 4
 .
 0
 0
 6
  
 -
 3
 .
 9
 4
 5
  
 -
 3
 .
 9
 9
 3
  
  
 0
 .
 0
 2
 5
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 0
 6
  
  
  
 0
 .
 9
 3
 4
 7
 2
 9
 7
 3
 3
 0
 

  
 1
 8
 4
  
  
 4
 .
 0
 0
 6
  
 -
 3
 .
 9
 4
 5
  
 -
 3
 .
 9
 9
 3
  
  
 0
 .
 0
 2
 4
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 0
 6
  
  
  
 0
 .
 9
 3
 4
 7
 1
 5
 1
 3
 1
 8
 

  
 1
 8
 5
  
  
 4
 .
 0
 0
 6
  
 -
 3
 .
 9
 4
 5
  
 -
 3
 .
 9
 9
 3
  
  
 0
 .
 0
 2
 4
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 0
 6
  
  
  
 0
 .
 9
 3
 4
 7
 1
 2
 7
 3
 8
 8
 

  
 1
 8
 6
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 4
 4
  
 -
 3
 .
 9
 9
 4
  
  
 0
 .
 0
 2
 2
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 0
 6
  
  
  
 0
 .
 9
 3
 4
 7
 1
 0
 1
 7
 3
 0
 

  
 1
 8
 7
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 4
 4
  
 -
 3
 .
 9
 9
 3
  
  
 0
 .
 0
 2
 3
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 0
 6
  
  
  
 0
 .
 9
 3
 4
 7
 0
 4
 5
 3
 5
 7
 

  
 1
 8
 8
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 4
 4
  
 -
 3
 .
 9
 9
 4
  
  
 0
 .
 0
 2
 3
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 0
 6
  
  
  
 0
 .
 9
 3
 4
 7
 0
 3
 6
 0
 1
 4
 

  
  
 p
 o
 w
 e
 l
 l
  
 n
 t
 h
 i
 t
 e
 r
  
 2
 :
  
 f
 r
 e
 t
  
 =
  
 0
 .
 9
 3
 4
 7
 0
 4
 

  
 2
 0
 5
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 4
 4
  
 -
 3
 .
 9
 9
 4
  
  
 0
 .
 0
 2
 3
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 0
 5
  
  
  
 0
 .
 9
 3
 4
 6
 9
 8
 5
 2
 2
 1
 

  
 2
 1
 6
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 5
 3
  
 -
 3
 .
 9
 9
 4
  
  
 0
 .
 0
 2
 3
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 0
 5
  
  
  
 0
 .
 9
 3
 4
 4
 6
 1
 1
 9
 4
 8
 

  
 2
 1
 7
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 4
 9
  
 -
 3
 .
 9
 9
 4
  
  
 0
 .
 0
 2
 3
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 0
 5
  
  
  
 0
 .
 9
 3
 4
 4
 0
 6
 9
 4
 3
 7
 

  
 2
 1
 9
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 4
 7
  
 -
 3
 .
 9
 9
 4
  
  
 0
 .
 0
 2
 3
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 0
 5
  
  
  
 0
 .
 9
 3
 4
 3
 5
 3
 4
 8
 2
 2
 

  
 2
 3
 5
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 4
 7
  
 -
 3
 .
 9
 9
 5
  
  
 0
 .
 0
 2
 3
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 0
 5
  
  
  
 0
 .
 9
 3
 3
 9
 3
 4
 5
 4
 4
 0
 

  
 2
 5
 0
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 4
 7
  
 -
 3
 .
 9
 9
 5
  
  
 0
 .
 0
 2
 0
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 0
 5
  
  
  
 0
 .
 9
 3
 3
 8
 7
 6
 2
 7
 9
 0
 

  
 2
 5
 3
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 4
 7
  
 -
 3
 .
 9
 9
 5
  
  
 0
 .
 0
 1
 9
  
 -
 4
 .
 5
 8
 9
  
  
 4
 .
 0
 0
 5
  
  
  
 0
 .
 9
 3
 3
 8
 7
 2
 8
 8
 4
 2
 

  
 2
 6
 8
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 4
 7
  
 -
 3
 .
 9
 9
 5
  
  
 0
 .
 0
 1
 9
  
 -
 4
 .
 5
 9
 0
  
  
 4
 .
 0
 0
 5
  
  
  
 0
 .
 9
 3
 3
 7
 5
 6
 6
 5
 0
 8
 

  
 2
 7
 6
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 4
 7
  
 -
 3
 .
 9
 9
 5
  
  
 0
 .
 0
 1
 9
  
 -
 4
 .
 5
 9
 0
  
  
 4
 .
 0
 0
 5
  
  
  
 0
 .
 9
 3
 3
 7
 5
 4
 5
 4
 8
 6
 

  
  
 p
 o
 w
 e
 l
 l
  
 n
 t
 h
 i
 t
 e
 r
  
 3
 :
  
 f
 r
 e
 t
  
 =
  
 0
 .
 9
 3
 3
 7
 5
 5
 

  
 2
 9
 4
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 4
 7
  
 -
 3
 .
 9
 9
 5
  
  
 0
 .
 0
 1
 9
  
 -
 4
 .
 5
 9
 0
  
  
 4
 .
 0
 0
 1
  
  
  
 0
 .
 9
 3
 3
 7
 0
 7
 1
 3
 6
 5
 

  
 2
 9
 5
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 4
 7
  
 -
 3
 .
 9
 9
 5
  
  
 0
 .
 0
 1
 9
  
 -
 4
 .
 5
 9
 0
  
  
 4
 .
 0
 0
 2
  
  
  
 0
 .
 9
 3
 3
 6
 9
 4
 6
 9
 8
 5
 

  
 3
 2
 2
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 4
 7
  
 -
 3
 .
 9
 9
 7
  
  
 0
 .
 0
 1
 9
  
 -
 4
 .
 5
 9
 0
  
  
 4
 .
 0
 0
 2
  
  
  
 0
 .
 9
 3
 3
 4
 2
 0
 9
 1
 4
 5
 

  
 3
 3
 6
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 4
 7
  
 -
 3
 .
 9
 9
 7
  
  
 0
 .
 0
 2
 0
  
 -
 4
 .
 5
 9
 0
  
  
 4
 .
 0
 0
 2
  
  
  
 0
 .
 9
 3
 3
 4
 0
 7
 7
 7
 7
 6
 

  
 3
 4
 6
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 4
 7
  
 -
 3
 .
 9
 9
 7
  
  
 0
 .
 0
 2
 0
  
 -
 4
 .
 5
 9
 3
  
  
 4
 .
 0
 0
 2
  
  
  
 0
 .
 9
 3
 3
 1
 8
 0
 9
 7
 6
 8
 

  
 3
 4
 9
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 4
 7
  
 -
 3
 .
 9
 9
 7
  
  
 0
 .
 0
 2
 0
  
 -
 4
 .
 5
 9
 4
  
  
 4
 .
 0
 0
 2
  
  
  
 0
 .
 9
 3
 3
 1
 2
 0
 4
 2
 1
 9
 

  
 3
 5
 0
  
  
 4
 .
 0
 0
 5
  
 -
 3
 .
 9
 4
 7
  
 -
 3
 .
 9
 9
 7
  
  
 0
 .
 0
 2
 0
  
 -
 4
 .
 5
 9
 6
  
  
 4
 .
 0
 0
 2
  
  
  
 0
 .
 9
 3
 3
 0
 2
 9
 6
 0
 0
 4
 

  
 3
 6
 0
  
  
 4
 .
 0
 0
 6
  
 -
 3
 .
 9
 4
 8
  
 -
 3
 .
 9
 9
 7
  
  
 0
 .
 0
 2
 1
  
 -
 4
 .
 5
 9
 6
  
  
 4
 .
 0
 0
 2
  
  
  
 0
 .
 9
 3
 3
 0
 1
 2
 2
 9
 8
 2
 

  
 3
 6
 1
  
  
 4
 .
 0
 0
 6
  
 -
 3
 .
 9
 4
 8
  
 -
 3
 .
 9
 9
 7
  
  
 0
 .
 0
 2
 1
  
 -
 4
 .
 5
 9
 6
  
  
 4
 .
 0
 0
 2
  
  
  
 0
 .
 9
 3
 2
 9
 9
 8
 0
 1
 7
 4
 

  
  
 p
 o
 w
 e
 l
 l
  
 n
 t
 h
 i
 t
 e
 r
  
 4
 :
  
 f
 r
 e
 t
  
 =
  
 0
 .
 9
 3
 2
 9
 9
 8
 

  
 4
 0
 8
  
  
 4
 .
 0
 0
 6
  
 -
 3
 .
 9
 4
 8
  
 -
 3
 .
 9
 9
 8
  
  
 0
 .
 0
 2
 1
  
 -
 4
 .
 5
 9
 6
  
  
 4
 .
 0
 0
 2
  
  
  
 0
 .
 9
 3
 2
 8
 5
 5
 8
 6
 9
 2
 

  
 4
 3
 7
  
  
 4
 .
 0
 0
 6
  
 -
 3
 .
 9
 4
 8
  
 -
 3
 .
 9
 9
 8
  
  
 0
 .
 0
 2
 1
  
 -
 4
 .
 5
 9
 7
  
  
 4
 .
 0
 0
 2
  
  
  
 0
 .
 9
 3
 2
 8
 2
 6
 3
 2
 7
 5
 

  
 4
 4
 5
  
  
 4
 .
 0
 0
 6
  
 -
 3
 .
 9
 4
 8
  
 -
 3
 .
 9
 9
 8
  
  
 0
 .
 0
 2
 2
  
 -
 4
 .
 5
 9
 7
  
  
 4
 .
 0
 0
 2
  
  
  
 0
 .
 9
 3
 2
 8
 2
 5
 0
 1
 6
 9
 

  
 4
 4
 6
  
  
 4
 .
 0
 0
 6
  
 -
 3
 .
 9
 4
 8
  
 -
 3
 .
 9
 9
 8
  
  
 0
 .
 0
 2
 1
  
 -
 4
 .
 5
 9
 7
  
  
 4
 .
 0
 0
 2
  
  
  
 0
 .
 9
 3
 2
 8
 2
 0
 9
 8
 6
 6
 

  
 4
 4
 7
  
  
 4
 .
 0
 0
 6
  
 -
 3
 .
 9
 4
 8
  
 -
 3
 .
 9
 9
 8
  
  
 0
 .
 0
 2
 1
  
 -
 4
 .
 5
 9
 7
  
  
 4
 .
 0
 0
 2
  
  
  
 0
 .
 9
 3
 2
 8
 1
 8
 9
 2
 0
 2
 

  
  
 p
 o
 w
 e
 l
 l
  
 n
 t
 h
 i
 t
 e
 r
  
 5
 :
  
 f
 r
 e
 t
  
 =
  
 0
 .
 9
 3
 2
 8
 1
 9
 

  
 5
 2
 1
  
  
 4
 .
 0
 0
 6
  
 -
 3
 .
 9
 4
 8
  
 -
 3
 .
 9
 9
 8
  
  
 0
 .
 0
 2
 1
  
 -
 4
 .
 5
 9
 8
  
  
 4
 .
 0
 0
 2
  
  
  
 0
 .
 9
 3
 2
 7
 9
 7
 8
 0
 8
 6
 

  
 5
 3
 0
  
  
 4
 .
 0
 0
 6
  
 -
 3
 .
 9
 4
 8
  
 -
 3
 .
 9
 9
 8
  
  
 0
 .
 0
 2
 1
  
 -
 4
 .
 5
 9
 8
  
  
 4
 .
 0
 0
 2
  
  
  
 0
 .
 9
 3
 2
 7
 9
 6
 2
 6
 9
 4
 

 P
 o
 w
 e
 l
 l
  
 d
 o
 n
 e
  
 n
 i
 t
 e
 r
 s
  
 =
  
 5
 

 C
 o
 m
 p
 u
 t
 i
 n
 g
  
 r
 e
 l
 a
 t
 i
 v
 e
  
 c
 o
 s
 t
 

  
 0
  
  
 -
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
  
 1
 .
 1
 0
 6
 6
 4
 7
 

  
 1
  
  
 -
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
  
 1
 .
 0
 3
 9
 0
 6
 4
 

  
 2
  
  
 -
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
  
 1
 .
 0
 3
 0
 7
 1
 7
 

  
 3
  
  
 -
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
  
 0
 .
 9
 9
 9
 4
 8
 0
 

  
 4
  
  
  
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
  
 1
 .
 0
 2
 5
 5
 2
 7
 

  
 5
  
  
  
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
  
 1
 .
 0
 1
 4
 6
 9
 7
 

  
 6
  
  
  
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
  
 1
 .
 0
 2
 6
 6
 2
 1
 

  
 7
  
  
  
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
  
 1
 .
 0
 2
 1
 2
 6
 8
 

 R
 E
 L
 :
  
  
 8
  
  
 0
 .
 9
 3
 2
 7
 9
 6
  
  
  
  
 8
 .
 2
 6
 4
 0
 2
 1
  
  
 1
 .
 0
 3
 3
 0
 0
 3
  
 r
 e
 l
  
 =
  
 0
 .
 9
 0
 2
 9
 9
 5
  
 

 N
 u
 m
 b
 e
 r
  
 o
 f
  
 i
 t
 e
 r
 a
 t
 i
 o
 n
 s
  
  
  
  
  
 5
 

 M
 i
 n
  
 c
 o
 s
 t
  
 w
 a
 s
  
 0
 .
 9
 3
 2
 7
 9
 6
 

 N
 u
 m
 b
 e
 r
  
 o
 f
  
 F
 u
 n
 c
 t
 i
 o
 n
 C
 a
 l
 l
 s
  
  
  
 5
 3
 3
 

 T
 o
 l
 P
 o
 w
 e
 l
 l
  
 0
 .
 0
 0
 0
 1
 0
 0
 

 n
 M
 a
 x
 I
 t
 e
 r
 s
 P
 o
 w
 e
 l
 l
  
 3
 6
 

 O
 p
 t
 i
 m
 i
 z
 a
 t
 i
 o
 n
 T
 i
 m
 e
  
 1
 .
 1
 4
 4
 0
 0
 0
  
 s
 e
 c
 

 P
 a
 r
 a
 m
 e
 t
 e
 r
 s
  
 a
 t
  
 o
 p
 t
 i
 m
 u
 m
  
 (
 t
 r
 a
 n
 s
 m
 m
 )
  
  
 4
 .
 0
 0
 6
 0
 8
  
 -
 3
 .
 9
 4
 7
 9
 7
  
 -
 3
 .
 9
 9
 8
 0
 9
 

 P
 a
 r
 a
 m
 e
 t
 e
 r
 s
  
 a
 t
  
 o
 p
 t
 i
 m
 u
 m
  
 (
 r
 o
 t
 d
 e
 g
 )
  
  
 0
 .
 0
 2
 1
 4
 0
  
 -
 4
 .
 5
 9
 8
 2
 7
  
  
 4
 .
 0
 0
 2
 0
 0
  
 

 F
 i
 n
 a
 l
  
 c
 o
 s
 t
 s
  
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 

 N
 u
 m
 b
 e
 r
  
 o
 f
  
 s
 u
 r
 f
 a
 c
 e
  
 h
 i
 t
 s
  
 9
 1
 7
 

 W
 M
  
  
 I
 n
 t
 e
 n
 s
 i
 t
 y
  
  
  
 1
 3
 4
 .
 2
 1
 8
 8
  
 +
 /
 -
  
 2
 2
 9
 .
 0
 9
 5
 4
 

 C
 t
 x
  
 I
 n
 t
 e
 n
 s
 i
 t
 y
  
  
  
 1
 3
 5
 .
 5
 8
 7
 7
  
 +
 /
 -
  
 2
 0
 4
 .
 5
 2
 5
 2
 

 P
 c
 t
  
 C
 o
 n
 t
 r
 a
 s
 t
  
  
  
  
  
  
 3
 .
 6
 2
 1
 7
  
 +
 /
 -
  
  
 7
 4
 .
 4
 1
 4
 9
 

 C
 o
 s
 t
  
  
  
 0
 .
 9
 3
 2
 8
 

 R
 e
 l
 C
 o
 s
 t
  
  
  
 1
 .
 0
 5
 3
 2
 

 R
 e
 g
  
 a
 t
  
 m
 i
 n
  
 c
 o
 s
 t
  
 w
 a
 s
  
 

  
 0
 .
 9
 9
 3
 0
 1
  
  
  
 0
 .
 0
 9
 9
 7
 7
  
  
 -
 0
 .
 0
 6
 3
 0
 1
  
  
 -
 1
 0
 .
 3
 1
 7
 5
 5
 ;
 

  
 0
 .
 0
 7
 1
 1
 0
  
  
 -
 0
 .
 0
 7
 9
 7
 5
  
  
  
 0
 .
 9
 9
 4
 2
 8
  
  
 -
 1
 9
 .
 9
 2
 0
 1
 9
 ;
 

  
 0
 .
 0
 9
 4
 1
 7
  
  
 -
 0
 .
 9
 9
 1
 8
 1
  
  
 -
 0
 .
 0
 8
 6
 2
 9
  
  
 -
 0
 .
 8
 0
 7
 2
 0
 ;
 

  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 .
 0
 0
 0
 0
 0
 ;
 

 

 W
 r
 i
 t
 i
 n
 g
  
 o
 p
 t
 i
 m
 a
 l
  
 r
 e
 g
  
 t
 o
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 b
 b
 r
 .
 p
 a
 s
 s
 1
 .
 d
 a
 t
 ,
  
 t
 y
 p
 e
  
 =
  
 1
 4
  
 

 O
 r
 i
 g
 i
 n
 a
 l
  
 R
 e
 g
  
 

  
 0
 .
 9
 9
 9
 9
 0
  
  
  
 0
 .
 0
 1
 4
 1
 5
  
  
 -
 0
 .
 0
 0
 0
 4
 0
  
  
 -
 1
 5
 .
 0
 9
 8
 0
 3
 ;
 

  
 0
 .
 0
 0
 1
 6
 3
  
  
 -
 0
 .
 0
 8
 6
 8
 9
  
  
  
 0
 .
 9
 9
 6
 2
 2
  
  
 -
 1
 4
 .
 9
 3
 1
 9
 6
 ;
 

  
 0
 .
 0
 1
 4
 0
 6
  
  
 -
 0
 .
 9
 9
 6
 1
 2
  
  
 -
 0
 .
 0
 8
 6
 9
 1
  
  
  
 4
 .
 4
 2
 1
 0
 7
 ;
 

  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 .
 0
 0
 0
 0
 0
 ;
 

 

 O
 r
 i
 g
 i
 n
 a
 l
  
 R
 e
 g
  
 -
  
 O
 p
 t
 i
 m
 a
 l
  
 R
 e
 g
 

  
 0
 .
 0
 0
 6
 8
 9
  
  
 -
 0
 .
 0
 8
 5
 6
 2
  
  
  
 0
 .
 0
 6
 2
 6
 1
  
  
 -
 4
 .
 7
 8
 0
 4
 8
 ;
 

 -
 0
 .
 0
 6
 9
 4
 7
  
  
 -
 0
 .
 0
 0
 7
 1
 4
  
  
  
 0
 .
 0
 0
 1
 9
 4
  
  
  
 4
 .
 9
 8
 8
 2
 3
 ;
 

 -
 0
 .
 0
 8
 0
 1
 2
  
  
 -
 0
 .
 0
 0
 4
 3
 1
  
  
 -
 0
 .
 0
 0
 0
 6
 2
  
  
  
 5
 .
 2
 2
 8
 2
 7
 ;
 

  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
 ;
 

 

 C
 o
 m
 p
 u
 t
 i
 n
 g
  
 c
 h
 a
 n
 g
 e
  
 i
 n
  
 l
 h
  
 p
 o
 s
 i
 t
 i
 o
 n
 

 L
 H
  
 r
 m
 s
 D
 i
 f
 f
 M
 e
 a
 n
  
 1
 0
 .
 9
 7
 8
 6
 0
 8
 

 C
 o
 m
 p
 u
 t
 i
 n
 g
  
 c
 h
 a
 n
 g
 e
  
 i
 n
  
 r
 h
  
 p
 o
 s
 i
 t
 i
 o
 n
 

 S
 u
 r
 f
 a
 c
 e
 -
 R
 M
 S
 -
 D
 i
 f
 f
 -
 m
 m
  
 8
 .
 5
 8
 7
 8
 3
 2
  
 3
 .
 0
 7
 6
 6
 2
 2
  
 1
 4
 .
 6
 4
 3
 2
 3
 8
 

 

 

 W
 A
 R
 N
 I
 N
 G
 :
  
 i
 n
 i
 t
 i
 a
 l
  
 G
 -
 W
  
 c
 o
 n
 t
 r
 a
 s
 t
  
 w
 a
 s
  
 n
 e
 g
 a
 t
 i
 v
 e
 ,
  
 b
 u
 t
  
 e
 x
 p
 e
 c
 t
 e
 d
  
 p
 o
 s
 i
 t
 i
 v
 e
 .
 

 I
 f
  
 t
 h
 e
  
 m
 o
 v
  
 d
 a
 t
 a
  
 h
 a
 s
  
 a
  
 T
 1
  
 c
 o
 n
 t
 r
 a
 s
 t
 ,
  
 r
 e
 -
 r
 u
 n
  
 w
 i
 t
 h
  
 -
 -
 T
 1
 

 

 

 m
 r
 i
 _
 s
 e
 g
 r
 e
 g
  
 d
 o
 n
 e
 

 m
 r
 i
 _
 s
 e
 g
 r
 e
 g
  
 -
 -
 m
 o
 v
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 t
 e
 m
 p
 l
 a
 t
 e
 .
 n
 i
 i
  
 -
 -
 i
 n
 i
 t
 -
 r
 e
 g
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 b
 b
 r
 .
 p
 a
 s
 s
 1
 .
 d
 a
 t
  
 -
 -
 o
 u
 t
 -
 r
 e
 g
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 _
 b
 b
 r
 e
 g
 _
 s
 u
 b
 -
 b
 m
 .
 d
 a
 t
  
 -
 -
 i
 n
 t
 e
 r
 p
  
 t
 r
 i
 l
 i
 n
 e
 a
 r
  
 -
 -
 w
 m
 -
 p
 r
 o
 j
 -
 a
 b
 s
  
 2
  
 -
 -
 t
 o
 l
  
 1
 e
 -
 8
  
 -
 -
 t
 o
 l
 1
 d
  
 1
 e
 -
 3
  
 -
 -
 c
 0
  
 0
  
 -
 -
 m
 i
 n
 c
 o
 s
 t
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 _
 b
 b
 r
 e
 g
 _
 s
 u
 b
 -
 b
 m
 .
 d
 a
 t
 .
 m
 i
 n
 c
 o
 s
 t
  
 -
 -
 d
 o
 f
  
 6
  
 -
 -
 n
 m
 a
 x
  
 3
 6
  
 -
 -
 p
 a
 r
 a
 m
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 _
 b
 b
 r
 e
 g
 _
 s
 u
 b
 -
 b
 m
 .
 d
 a
 t
 .
 p
 a
 r
 a
 m
  
 -
 -
 s
 u
 r
 f
  
 w
 h
 i
 t
 e
  
 -
 -
 b
 r
 u
 t
 e
  
 -
 0
 .
 1
  
 0
 .
 1
  
 0
 .
 1
  
 -
 -
 c
 u
 r
 -
 r
 e
 g
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 r
 e
 g
 .
 c
 u
 r
 o
 p
 t
 .
 d
 a
 t
  
 -
 -
 g
 m
 -
 p
 r
 o
 j
 -
 f
 r
 a
 c
  
 0
 .
 5
  
 -
 -
 n
 s
 u
 b
  
 1
  
 -
 -
 g
 m
 -
 g
 t
 -
 w
 m
  
 0
 .
 5
 

 $
 I
 d
 :
  
 m
 r
 i
 _
 s
 e
 g
 r
 e
 g
 .
 c
 ,
 v
  
 1
 .
 1
 1
 3
  
 2
 0
 1
 6
 /
 0
 5
 /
 1
 0
  
 0
 3
 :
 2
 3
 :
 2
 0
  
 g
 r
 e
 v
 e
  
 E
 x
 p
  
 $
 

 s
 e
 t
 e
 n
 v
  
 S
 U
 B
 J
 E
 C
 T
 S
 _
 D
 I
 R
  
 /
 d
 e
 r
 i
 v
 a
 t
 i
 v
 e
 s
 /
 f
 r
 e
 e
 s
 u
 r
 f
 e
 r
 

 c
 d
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 

 m
 r
 i
 _
 s
 e
 g
 r
 e
 g
  
 -
 -
 m
 o
 v
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 t
 e
 m
 p
 l
 a
 t
 e
 .
 n
 i
 i
  
 -
 -
 i
 n
 i
 t
 -
 r
 e
 g
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 b
 b
 r
 .
 p
 a
 s
 s
 1
 .
 d
 a
 t
  
 -
 -
 o
 u
 t
 -
 r
 e
 g
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 _
 b
 b
 r
 e
 g
 _
 s
 u
 b
 -
 b
 m
 .
 d
 a
 t
  
 -
 -
 i
 n
 t
 e
 r
 p
  
 t
 r
 i
 l
 i
 n
 e
 a
 r
  
 -
 -
 w
 m
 -
 p
 r
 o
 j
 -
 a
 b
 s
  
 2
  
 -
 -
 t
 o
 l
  
 1
 e
 -
 8
  
 -
 -
 t
 o
 l
 1
 d
  
 1
 e
 -
 3
  
 -
 -
 c
 0
  
 0
  
 -
 -
 m
 i
 n
 c
 o
 s
 t
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 _
 b
 b
 r
 e
 g
 _
 s
 u
 b
 -
 b
 m
 .
 d
 a
 t
 .
 m
 i
 n
 c
 o
 s
 t
  
 -
 -
 d
 o
 f
  
 6
  
 -
 -
 n
 m
 a
 x
  
 3
 6
  
 -
 -
 p
 a
 r
 a
 m
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 _
 b
 b
 r
 e
 g
 _
 s
 u
 b
 -
 b
 m
 .
 d
 a
 t
 .
 p
 a
 r
 a
 m
  
 -
 -
 s
 u
 r
 f
  
 w
 h
 i
 t
 e
  
 -
 -
 b
 r
 u
 t
 e
  
 -
 0
 .
 1
  
 0
 .
 1
  
 0
 .
 1
  
 -
 -
 c
 u
 r
 -
 r
 e
 g
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 r
 e
 g
 .
 c
 u
 r
 o
 p
 t
 .
 d
 a
 t
  
 -
 -
 g
 m
 -
 p
 r
 o
 j
 -
 f
 r
 a
 c
  
 0
 .
 5
  
 -
 -
 n
 s
 u
 b
  
 1
  
 -
 -
 g
 m
 -
 g
 t
 -
 w
 m
  
 0
 .
 5
  
 

 s
 y
 s
 n
 a
 m
 e
  
  
 L
 i
 n
 u
 x
 

 h
 o
 s
 t
 n
 a
 m
 e
  
 9
 9
 5
 8
 f
 5
 f
 d
 3
 b
 a
 7
 

 m
 a
 c
 h
 i
 n
 e
  
  
 x
 8
 6
 _
 6
 4
 

 u
 s
 e
 r
  
  
  
  
  
 r
 o
 o
 t
 

 m
 o
 v
 v
 o
 l
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 t
 e
 m
 p
 l
 a
 t
 e
 .
 n
 i
 i
 

 r
 e
 g
 f
 i
 l
 e
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 t
 m
 p
 .
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 .
 4
 4
 2
 5
 /
 b
 b
 r
 .
 p
 a
 s
 s
 1
 .
 d
 a
 t
 

 s
 u
 b
 j
 e
 c
 t
  
 s
 u
 b
 -
 b
 m
 

 d
 o
 f
  
 6
 

 o
 u
 t
 r
 e
 g
 f
 i
 l
 e
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 _
 b
 b
 r
 e
 g
 _
 s
 u
 b
 -
 b
 m
 .
 d
 a
 t
 

 U
 s
 e
 M
 a
 s
 k
  
 0
 

 U
 s
 e
 L
 H
  
 1
 

 U
 s
 e
 R
 H
  
 1
 

 n
 s
 u
 b
 s
 a
 m
 p
  
 1
 

 P
 e
 n
 a
 l
 t
 y
 S
 i
 g
 n
  
  
 -
 1
 

 P
 e
 n
 a
 l
 t
 y
 S
 l
 o
 p
 e
  
 0
 .
 5
 0
 0
 0
 0
 0
 

 P
 e
 n
 a
 l
 t
 y
 C
 e
 n
 t
 e
 r
  
 0
 .
 0
 0
 0
 0
 0
 0
 

 s
 u
 r
 f
 n
 a
 m
 e
  
 w
 h
 i
 t
 e
 

 G
 M
 P
 r
 o
 j
 F
 r
 a
 c
  
 0
 .
 5
 0
 0
 0
 0
 0
 

 W
 M
 P
 r
 o
 j
 A
 b
 s
  
 2
 .
 0
 0
 0
 0
 0
 0
 

 l
 h
 c
 o
 s
 t
 f
 i
 l
 e
  
 (
 n
 u
 l
 l
 )
 

 r
 h
 c
 o
 s
 t
 f
 i
 l
 e
  
 (
 n
 u
 l
 l
 )
 

 i
 n
 t
 e
 r
 p
  
  
 t
 r
 i
 l
 i
 n
 e
 a
 r
  
 (
 1
 )
 

 f
 r
 a
 m
 e
  
  
 0
 

 T
 o
 l
 P
 o
 w
 e
 l
 l
  
 0
 .
 0
 0
 0
 0
 0
 0
 

 n
 M
 a
 x
 I
 t
 e
 r
 s
 P
 o
 w
 e
 l
 l
  
 3
 6
 

 n
 1
 d
 m
 i
 n
  
  
 3
 

 P
 r
 o
 f
 i
 l
 e
  
  
  
 0
 

 G
 d
 i
 a
 g
 _
 n
 o
  
  
 -
 1
 

 A
 d
 d
 N
 o
 i
 s
 e
  
  
 0
  
 (
 0
 )
 

 S
 y
 n
 t
 h
 S
 e
 e
 d
  
 1
 5
 4
 4
 6
 2
 8
 1
 1
 5
 

 T
 r
 a
 n
 s
 R
 a
 n
 d
 M
 a
 x
  
 0
 .
 0
 0
 0
 0
 0
 0
 

 R
 o
 t
 R
 a
 n
 d
 M
 a
 x
  
 0
 .
 0
 0
 0
 0
 0
 0
 

 T
 r
 a
 n
 s
 l
 a
 t
 i
 o
 n
 s
  
 0
 .
 0
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
 0
 

 R
 o
 t
 a
 t
 i
 o
 n
 s
  
  
  
 0
 .
 0
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
 0
  
 0
 .
 0
 0
 0
 0
 0
 0
 

 I
 n
 p
 u
 t
  
 r
 e
 g
 

  
 0
 .
 9
 9
 3
 0
 1
  
  
  
 0
 .
 0
 9
 9
 7
 7
  
  
 -
 0
 .
 0
 6
 3
 0
 1
  
  
 -
 1
 0
 .
 3
 1
 7
 5
 5
 ;
 

  
 0
 .
 0
 7
 1
 1
 0
  
  
 -
 0
 .
 0
 7
 9
 7
 5
  
  
  
 0
 .
 9
 9
 4
 2
 8
  
  
 -
 1
 9
 .
 9
 2
 0
 1
 9
 ;
 

  
 0
 .
 0
 9
 4
 1
 7
  
  
 -
 0
 .
 9
 9
 1
 8
 1
  
  
 -
 0
 .
 0
 8
 6
 2
 9
  
  
 -
 0
 .
 8
 0
 7
 2
 0
 ;
 

  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 .
 0
 0
 0
 0
 0
 ;
 

 

 L
 o
 a
 d
 i
 n
 g
  
 m
 o
 v
 

 P
 r
 o
 j
 e
 c
 t
 i
 n
 g
  
 L
 H
  
 S
 u
 r
 f
 s
 

 L
 o
 a
 d
 i
 n
 g
  
 l
 h
 .
 w
 h
 i
 t
 e
  
 s
 u
 r
 f
 

 L
 o
 a
 d
 i
 n
 g
  
 l
 h
 .
 t
 h
 i
 c
 k
 n
 e
 s
 s
  
 f
 o
 r
  
 G
 M
 

 G
 M
  
 P
 r
 o
 j
 :
  
 1
  
 0
 .
 5
 0
 0
 0
 0
 0
  
 2
 .
 0
 0
 0
 0
 0
 0
 

 W
 M
  
 P
 r
 o
 j
 :
  
 0
  
 0
 .
 5
 0
 0
 0
 0
 0
  
 2
 .
 0
 0
 0
 0
 0
 0
 

 P
 r
 o
 j
 e
 c
 t
 i
 n
 g
  
 R
 H
  
 S
 u
 r
 f
 s
 

 L
 o
 a
 d
 i
 n
 g
  
 r
 h
 .
 w
 h
 i
 t
 e
  
 s
 u
 r
 f
 

 L
 o
 a
 d
 i
 n
 g
  
 r
 h
 .
 t
 h
 i
 c
 k
 n
 e
 s
 s
  
 f
 o
 r
  
 G
 M
 

 P
 r
 o
 j
 e
 c
 t
 i
 n
 g
  
 R
 H
  
 S
 u
 r
 f
 s
 

 U
 s
 i
 n
 g
  
 l
 h
 .
 c
 o
 r
 t
 e
 x
 .
 l
 a
 b
 e
 l
 

 U
 s
 i
 n
 g
  
 r
 h
 .
 c
 o
 r
 t
 e
 x
 .
 l
 a
 b
 e
 l
 

 C
 o
 m
 p
 u
 t
 i
 n
 g
  
 r
 e
 l
 a
 t
 i
 v
 e
  
 c
 o
 s
 t
 

  
 0
  
  
 -
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
  
 1
 .
 0
 4
 2
 7
 4
 0
 

  
 1
  
  
 -
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
  
 1
 .
 0
 2
 0
 5
 3
 3
 

  
 2
  
  
 -
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
  
 1
 .
 0
 4
 1
 1
 1
 7
 

  
 3
  
  
 -
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
  
 1
 .
 0
 2
 8
 0
 5
 3
 

  
 4
  
  
  
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
  
 1
 .
 0
 3
 8
 2
 0
 3
 

  
 5
  
  
  
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
  
 1
 .
 0
 3
 1
 5
 7
 8
 

  
 6
  
  
  
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
  
 1
 .
 0
 3
 7
 5
 4
 9
 

  
 7
  
  
  
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
  
 1
 .
 0
 4
 0
 4
 1
 3
 

 R
 E
 L
 :
  
  
 8
  
  
 1
 .
 0
 2
 6
 8
 4
 8
  
  
  
  
 8
 .
 2
 8
 0
 1
 8
 6
  
  
 1
 .
 0
 3
 5
 0
 2
 3
  
 r
 e
 l
  
 =
  
 0
 .
 9
 9
 2
 1
 0
 1
  
 

 I
 n
 i
 t
 i
 a
 l
  
 c
 o
 s
 t
 s
  
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 

 N
 u
 m
 b
 e
 r
  
 o
 f
  
 s
 u
 r
 f
 a
 c
 e
  
 h
 i
 t
 s
  
 9
 0
 4
 6
 8
 

 W
 M
  
  
 I
 n
 t
 e
 n
 s
 i
 t
 y
  
  
  
 1
 3
 9
 .
 1
 7
 3
 8
  
 +
 /
 -
  
 2
 2
 1
 .
 8
 4
 5
 2
 

 C
 t
 x
  
 I
 n
 t
 e
 n
 s
 i
 t
 y
  
  
  
 1
 3
 7
 .
 2
 3
 3
 9
  
 +
 /
 -
  
 2
 1
 7
 .
 5
 2
 0
 3
 

 P
 c
 t
  
 C
 o
 n
 t
 r
 a
 s
 t
  
  
  
  
  
 -
 0
 .
 5
 6
 3
 7
  
 +
 /
 -
  
  
 7
 6
 .
 8
 1
 4
 5
 

 C
 o
 s
 t
  
  
  
 1
 .
 0
 2
 6
 8
 

 R
 e
 l
 C
 o
 s
 t
  
  
  
 0
 .
 9
 9
 2
 1
 

 

 

 W
 A
 R
 N
 I
 N
 G
 :
  
 i
 n
 i
 t
 i
 a
 l
  
 G
 -
 W
  
 c
 o
 n
 t
 r
 a
 s
 t
  
 i
 s
  
 n
 e
 g
 a
 t
 i
 v
 e
 ,
  
 b
 u
 t
  
 e
 x
 p
 e
 c
 t
 i
 n
 g
  
 p
 o
 s
 i
 t
 i
 v
 e
 .
 

 I
 f
  
 t
 h
 e
  
 m
 o
 v
  
 d
 a
 t
 a
  
 h
 a
 s
  
 a
  
 T
 1
  
 c
 o
 n
 t
 r
 a
 s
 t
 ,
  
 r
 e
 -
 r
 u
 n
  
 w
 i
 t
 h
  
 -
 -
 T
 1
 

 

 

 

 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 

 B
 r
 u
 t
 e
  
 f
 o
 r
 c
 e
  
 p
 r
 e
 o
 p
 t
  
 -
 0
 .
 1
  
 0
 .
 1
  
 0
 .
 1
 ,
  
 n
  
 =
  
 7
 2
 9
 

  
  
  
  
  
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
  
  
  
  
 0
 .
 9
 4
 8
 8
  
  
  
 0
 .
 9
 4
 8
 8
  
  
 0
 .
 0
 

  
  
  
  
  
 3
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
  
  
  
  
 0
 .
 9
 4
 2
 0
  
  
  
 0
 .
 9
 4
 2
 0
  
  
 0
 .
 0
 

  
  
  
  
 5
 4
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
  
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
  
  
  
  
 0
 .
 9
 4
 0
 7
  
  
  
 0
 .
 9
 4
 0
 7
  
  
 0
 .
 0
 

  
  
  
  
 6
 3
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
  
 0
 .
 1
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
  
  
  
  
 0
 .
 9
 2
 8
 8
  
  
  
 0
 .
 9
 2
 8
 8
  
  
 0
 .
 0
 

  
  
  
 4
 0
 8
  
  
  
 0
 .
 0
 0
 0
 0
  
  
  
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
  
  
  
  
 0
 .
 9
 2
 6
 4
  
  
  
 0
 .
 9
 2
 6
 4
  
  
 0
 .
 0
 

  
  
  
 5
 7
 4
  
  
  
 0
 .
 1
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
  
 0
 .
 1
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
  
  
  
  
 0
 .
 9
 2
 5
 5
  
  
  
 0
 .
 9
 2
 5
 5
  
  
 0
 .
 0
 

  
  
  
 5
 8
 5
  
  
  
 0
 .
 1
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
  
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
  
  
  
  
 0
 .
 9
 2
 4
 2
  
  
  
 0
 .
 9
 2
 4
 2
  
  
 0
 .
 0
 

  
  
  
 5
 9
 7
  
  
  
 0
 .
 1
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
  
  
  
  
 0
 .
 9
 2
 2
 6
  
  
  
 0
 .
 9
 2
 2
 6
  
  
 0
 .
 0
 

  
  
  
 6
 0
 0
  
  
  
 0
 .
 1
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
  
 0
 .
 1
 0
 0
 0
  
  
 -
 0
 .
 1
 0
 0
 0
  
  
  
  
  
  
 0
 .
 9
 2
 2
 2
  
  
  
 0
 .
 9
 2
 2
 2
  
  
 0
 .
 0
 

 B
 r
 u
 t
 e
  
 F
 o
 r
 c
 e
  
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 

 M
 i
 n
  
 c
 o
 s
 t
  
 w
 a
 s
  
 0
 .
 9
 2
 2
 2
 1
 9
 

 N
 u
 m
 b
 e
 r
  
 o
 f
  
 i
 t
 e
 r
 a
 t
 i
 o
 n
 s
  
  
  
 7
 2
 9
 

 S
 e
 a
 r
 c
 h
  
 t
 i
 m
 e
  
 1
 .
 5
 4
 2
 0
 0
 0
  
 s
 e
 c
 

 P
 a
 r
 a
 m
 e
 t
 e
 r
 s
  
 a
 t
  
 b
 e
 s
 t
  
 (
 t
 r
 a
 n
 s
 m
 m
 ,
  
 r
 o
 t
 d
 e
 g
 )
 

  
  
 0
 .
 1
 0
 0
  
  
  
 0
 .
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
 0
 .
 1
 0
 0
  
 -
 0
 .
 1
 0
 0
  
 

 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 

 

 S
 t
 a
 r
 t
 i
 n
 g
  
 P
 o
 w
 e
 l
 l
  
 M
 i
 n
 i
 m
 i
 z
 a
 t
 i
 o
 n
 

 I
 n
 i
 t
  
 P
 o
 w
 e
 l
  
 P
 a
 r
 a
 m
 s
  
 d
 o
 f
  
 =
  
 6
 

 0
  
 0
 .
 1
 

 1
  
 0
 

 2
  
 0
 

 3
  
 -
 0
 .
 1
 

 4
  
 0
 .
 1
 

 5
  
 -
 0
 .
 1
 

 f
 s
 _
 p
 o
 w
 e
 l
 l
 :
 :
 m
 i
 n
 i
 m
 i
 z
 e
 

  
  
 n
 p
 a
 r
 a
 m
 s
  
 6
 

  
  
 m
 a
 x
 f
 e
 v
  
 3
 6
 

  
  
 f
 t
 o
 l
  
  
  
 0
 .
 0
 0
 0
 0
 0
 0
 

  
  
 l
 i
 n
 m
 i
 n
 _
 x
 t
 o
 l
 _
  
  
  
 0
 .
 0
 0
 1
 0
 0
 0
 

  
  
 p
 o
 w
 e
 l
 l
  
 n
 t
 h
 i
 t
 e
 r
  
 0
 :
  
 f
 r
 e
 t
  
 =
  
 1
 .
 0
 2
 6
 8
 4
 0
 

  
  
  
 7
  
  
 0
 .
 1
 8
 6
  
  
 0
 .
 0
 0
 0
  
  
 0
 .
 0
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
 0
 .
 1
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
  
 1
 .
 0
 2
 5
 9
 7
 0
 1
 5
 3
 9
 

  
  
 1
 0
  
  
 0
 .
 1
 5
 3
  
  
 0
 .
 0
 0
 0
  
  
 0
 .
 0
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
 0
 .
 1
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
  
 1
 .
 0
 2
 5
 7
 1
 5
 1
 1
 4
 8
 

  
  
 1
 1
  
  
 0
 .
 1
 4
 0
  
  
 0
 .
 0
 0
 0
  
  
 0
 .
 0
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
 0
 .
 1
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
  
 1
 .
 0
 2
 5
 6
 7
 1
 2
 6
 4
 6
 

  
  
 1
 3
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 0
 0
 0
  
  
 0
 .
 0
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
 0
 .
 1
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
  
 1
 .
 0
 2
 5
 6
 1
 4
 9
 5
 5
 3
 

  
  
 1
 7
  
  
 0
 .
 1
 4
 5
  
  
 1
 .
 0
 0
 0
  
  
 0
 .
 0
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
 0
 .
 1
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
  
 1
 .
 0
 2
 3
 0
 6
 7
 0
 5
 7
 1
 

  
  
 2
 1
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 6
 1
 8
  
  
 0
 .
 0
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
 0
 .
 1
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
  
 1
 .
 0
 2
 2
 5
 2
 6
 2
 7
 7
 6
 

  
  
 2
 2
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 6
 5
 0
  
  
 0
 .
 0
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
 0
 .
 1
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
  
 1
 .
 0
 2
 2
 1
 4
 1
 0
 3
 0
 1
 

  
  
 2
 4
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 7
 0
 4
  
  
 0
 .
 0
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
 0
 .
 1
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
  
 1
 .
 0
 2
 1
 8
 7
 9
 9
 1
 8
 3
 

  
  
 2
 5
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 7
 0
 6
  
  
 0
 .
 0
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
 0
 .
 1
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
  
 1
 .
 0
 2
 1
 8
 0
 6
 2
 8
 8
 2
 

  
  
 2
 6
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 7
 3
 8
  
  
 0
 .
 0
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
 0
 .
 1
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
  
 1
 .
 0
 2
 1
 5
 8
 9
 7
 5
 5
 5
 

  
  
 2
 7
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 7
 2
 6
  
  
 0
 .
 0
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
 0
 .
 1
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
  
 1
 .
 0
 2
 1
 5
 6
 6
 9
 0
 1
 8
 

  
  
 2
 8
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 7
 3
 0
  
  
 0
 .
 0
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
 0
 .
 1
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
  
 1
 .
 0
 2
 1
 5
 6
 6
 6
 1
 7
 6
 

  
  
 3
 0
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 7
 3
 3
  
  
 0
 .
 0
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
 0
 .
 1
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
  
 1
 .
 0
 2
 1
 5
 6
 1
 1
 2
 7
 8
 

  
  
 3
 8
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 7
 3
 3
  
  
 0
 .
 3
 8
 2
  
 -
 0
 .
 1
 0
 0
  
  
 0
 .
 1
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
  
 1
 .
 0
 1
 9
 2
 5
 2
 0
 4
 0
 7
 

  
  
 4
 0
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 7
 3
 3
  
  
 0
 .
 2
 4
 0
  
 -
 0
 .
 1
 0
 0
  
  
 0
 .
 1
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
  
 1
 .
 0
 1
 7
 7
 5
 1
 7
 4
 8
 5
 

  
  
 6
 4
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 7
 3
 3
  
  
 0
 .
 2
 4
 0
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 0
 0
  
 -
 0
 .
 1
 0
 0
  
  
  
 1
 .
 0
 1
 7
 7
 3
 2
 2
 4
 8
 0
 

  
  
 7
 9
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 7
 3
 3
  
  
 0
 .
 2
 4
 0
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 0
 0
  
  
 0
 .
 9
 0
 0
  
  
  
 1
 .
 0
 1
 6
 1
 5
 6
 0
 2
 7
 1
 

  
  
 8
 2
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 7
 3
 3
  
  
 0
 .
 2
 4
 0
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 0
 0
  
  
 1
 .
 5
 1
 8
  
  
  
 1
 .
 0
 1
 5
 4
 7
 5
 5
 4
 1
 3
 

  
  
 8
 6
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 7
 3
 3
  
  
 0
 .
 2
 4
 0
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 0
 0
  
  
 1
 .
 4
 1
 8
  
  
  
 1
 .
 0
 1
 5
 0
 4
 0
 2
 9
 2
 9
 

  
  
 8
 8
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 7
 3
 3
  
  
 0
 .
 2
 4
 0
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 0
 0
  
  
 1
 .
 4
 5
 6
  
  
  
 1
 .
 0
 1
 4
 5
 8
 0
 3
 5
 5
 1
 

  
  
 9
 0
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 7
 3
 3
  
  
 0
 .
 2
 4
 0
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 0
 0
  
  
 1
 .
 4
 4
 3
  
  
  
 1
 .
 0
 1
 4
 5
 5
 2
 5
 8
 3
 3
 

  
  
 9
 2
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 7
 3
 3
  
  
 0
 .
 2
 4
 0
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 0
 0
  
  
 1
 .
 4
 4
 8
  
  
  
 1
 .
 0
 1
 4
 5
 2
 6
 0
 2
 0
 3
 

  
  
 9
 3
  
  
 0
 .
 1
 4
 5
  
  
 0
 .
 7
 3
 3
  
  
 0
 .
 2
 4
 0
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 0
 0
  
  
 1
 .
 4
 4
 9
  
  
  
 1
 .
 0
 1
 4
 5
 2
 3
 1
 4
 6
 2
 

  
  
 9
 5
  
  
 0
 .
 1
 9
 0
  
  
 1
 .
 4
 6
 6
  
  
 0
 .
 4
 8
 1
  
 -
 0
 .
 0
 9
 8
  
  
 0
 .
 1
 0
 0
  
  
 2
 .
 9
 9
 7
  
  
  
 1
 .
 0
 1
 3
 7
 6
 1
 1
 9
 3
 6
 

  
  
 p
 o
 w
 e
 l
 l
  
 n
 t
 h
 i
 t
 e
 r
  
 1
 :
  
 f
 r
 e
 t
  
 =
  
 1
 .
 0
 1
 4
 5
 2
 3
 

  
 1
 1
 7
  
 -
 0
 .
 3
 5
 5
  
  
 1
 .
 7
 3
 3
  
  
 0
 .
 2
 4
 0
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 0
 0
  
  
 1
 .
 4
 4
 9
  
  
  
 1
 .
 0
 1
 3
 4
 3
 7
 9
 5
 1
 1
 

  
 1
 2
 5
  
 -
 0
 .
 3
 5
 5
  
  
 1
 .
 7
 7
 4
  
  
 0
 .
 2
 4
 0
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 0
 0
  
  
 1
 .
 4
 4
 9
  
  
  
 1
 .
 0
 1
 3
 1
 0
 3
 1
 6
 1
 7
 

  
 1
 2
 6
  
 -
 0
 .
 3
 5
 5
  
  
 1
 .
 7
 7
 3
  
  
 0
 .
 2
 4
 0
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 0
 0
  
  
 1
 .
 4
 4
 9
  
  
  
 1
 .
 0
 1
 3
 1
 0
 0
 3
 7
 7
 0
 

  
 1
 3
 5
  
 -
 0
 .
 3
 5
 5
  
  
 1
 .
 7
 7
 3
  
  
 0
 .
 1
 4
 1
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 0
 0
  
  
 1
 .
 4
 4
 9
  
  
  
 1
 .
 0
 1
 1
 8
 0
 4
 1
 8
 5
 4
 

  
 1
 3
 7
  
 -
 0
 .
 3
 5
 5
  
  
 1
 .
 7
 7
 3
  
  
 0
 .
 1
 2
 5
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 0
 0
  
  
 1
 .
 4
 4
 9
  
  
  
 1
 .
 0
 1
 1
 3
 8
 3
 6
 2
 3
 8
 

  
 1
 6
 6
  
 -
 0
 .
 3
 5
 5
  
  
 1
 .
 7
 7
 3
  
  
 0
 .
 1
 2
 5
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 1
 3
  
  
 1
 .
 4
 4
 9
  
  
  
 1
 .
 0
 1
 1
 2
 9
 5
 1
 8
 4
 8
 

  
 1
 6
 9
  
 -
 0
 .
 3
 5
 5
  
  
 1
 .
 7
 7
 3
  
  
 0
 .
 1
 2
 5
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 1
 0
  
  
 1
 .
 4
 4
 9
  
  
  
 1
 .
 0
 1
 1
 2
 7
 0
 9
 5
 5
 2
 

  
 1
 7
 9
  
 -
 0
 .
 3
 5
 5
  
  
 1
 .
 7
 7
 3
  
  
 0
 .
 1
 2
 5
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 1
 0
  
  
 1
 .
 4
 6
 1
  
  
  
 1
 .
 0
 1
 1
 0
 9
 1
 7
 2
 5
 8
 

  
 1
 8
 0
  
 -
 0
 .
 3
 5
 5
  
  
 1
 .
 7
 7
 3
  
  
 0
 .
 1
 2
 5
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 1
 0
  
  
 1
 .
 4
 6
 3
  
  
  
 1
 .
 0
 1
 1
 0
 9
 1
 0
 1
 3
 4
 

  
  
 p
 o
 w
 e
 l
 l
  
 n
 t
 h
 i
 t
 e
 r
  
 2
 :
  
 f
 r
 e
 t
  
 =
  
 1
 .
 0
 1
 1
 0
 9
 1
 

  
 1
 9
 3
  
 -
 0
 .
 3
 5
 3
  
  
 1
 .
 7
 7
 3
  
  
 0
 .
 1
 2
 5
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 1
 0
  
  
 1
 .
 4
 6
 3
  
  
  
 1
 .
 0
 1
 1
 0
 4
 8
 6
 7
 5
 6
 

  
 1
 9
 4
  
 -
 0
 .
 3
 4
 7
  
  
 1
 .
 7
 7
 3
  
  
 0
 .
 1
 2
 5
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 1
 0
  
  
 1
 .
 4
 6
 3
  
  
  
 1
 .
 0
 1
 1
 0
 3
 7
 9
 5
 9
 0
 

  
 1
 9
 6
  
 -
 0
 .
 3
 5
 0
  
  
 1
 .
 7
 7
 3
  
  
 0
 .
 1
 2
 5
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 1
 0
  
  
 1
 .
 4
 6
 3
  
  
  
 1
 .
 0
 1
 1
 0
 1
 7
 3
 6
 6
 0
 

  
 1
 9
 8
  
 -
 0
 .
 3
 4
 9
  
  
 1
 .
 7
 7
 3
  
  
 0
 .
 1
 2
 5
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 1
 0
  
  
 1
 .
 4
 6
 3
  
  
  
 1
 .
 0
 1
 1
 0
 1
 1
 2
 7
 6
 2
 

  
 2
 0
 9
  
 -
 0
 .
 3
 4
 9
  
  
 1
 .
 7
 7
 2
  
  
 0
 .
 1
 2
 5
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 1
 0
  
  
 1
 .
 4
 6
 3
  
  
  
 1
 .
 0
 1
 1
 0
 0
 9
 9
 7
 6
 1
 

  
 2
 2
 2
  
 -
 0
 .
 3
 4
 9
  
  
 1
 .
 7
 7
 2
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 0
 9
 9
  
  
 0
 .
 1
 1
 0
  
  
 1
 .
 4
 6
 3
  
  
  
 1
 .
 0
 1
 1
 0
 0
 2
 2
 2
 7
 6
 

  
 2
 3
 4
  
 -
 0
 .
 3
 4
 9
  
  
 1
 .
 7
 7
 2
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 1
 0
  
  
 1
 .
 4
 6
 3
  
  
  
 1
 .
 0
 1
 0
 9
 8
 7
 2
 2
 4
 0
 

  
 2
 4
 9
  
 -
 0
 .
 3
 4
 9
  
  
 1
 .
 7
 7
 2
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 1
 5
  
  
 1
 .
 4
 6
 3
  
  
  
 1
 .
 0
 1
 0
 9
 7
 3
 0
 5
 7
 4
 

  
 2
 5
 1
  
 -
 0
 .
 3
 4
 9
  
  
 1
 .
 7
 7
 2
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 1
 4
  
  
 1
 .
 4
 6
 3
  
  
  
 1
 .
 0
 1
 0
 9
 4
 7
 0
 8
 0
 6
 

  
 2
 5
 2
  
 -
 0
 .
 3
 4
 9
  
  
 1
 .
 7
 7
 2
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 1
 2
  
  
 1
 .
 4
 6
 3
  
  
  
 1
 .
 0
 1
 0
 9
 2
 7
 3
 9
 3
 3
 

  
 2
 6
 5
  
 -
 0
 .
 3
 4
 9
  
  
 1
 .
 7
 7
 2
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 1
 2
  
  
 1
 .
 4
 6
 6
  
  
  
 1
 .
 0
 1
 0
 9
 1
 3
 9
 9
 1
 6
 

  
  
 p
 o
 w
 e
 l
 l
  
 n
 t
 h
 i
 t
 e
 r
  
 3
 :
  
 f
 r
 e
 t
  
 =
  
 1
 .
 0
 1
 0
 9
 1
 4
 

  
 2
 9
 1
  
 -
 0
 .
 3
 4
 9
  
  
 1
 .
 7
 7
 4
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 1
 2
  
  
 1
 .
 4
 6
 6
  
  
  
 1
 .
 0
 1
 0
 9
 0
 5
 6
 6
 0
 1
 

  
 3
 4
 8
  
 -
 0
 .
 3
 4
 9
  
  
 1
 .
 7
 7
 4
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 1
 2
  
  
 1
 .
 4
 6
 8
  
  
  
 1
 .
 0
 1
 0
 9
 0
 5
 0
 6
 0
 4
 

  
 3
 5
 6
  
 -
 0
 .
 3
 4
 9
  
  
 1
 .
 7
 7
 5
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 1
 2
  
  
 1
 .
 4
 6
 8
  
  
  
 1
 .
 0
 1
 0
 9
 0
 4
 9
 5
 9
 6
 

  
 3
 5
 7
  
 -
 0
 .
 3
 4
 9
  
  
 1
 .
 7
 7
 4
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 1
 2
  
  
 1
 .
 4
 6
 8
  
  
  
 1
 .
 0
 1
 0
 9
 0
 4
 8
 0
 4
 2
 

  
 3
 5
 8
  
 -
 0
 .
 3
 4
 9
  
  
 1
 .
 7
 7
 4
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 1
 2
  
  
 1
 .
 4
 6
 8
  
  
  
 1
 .
 0
 1
 0
 9
 0
 4
 7
 5
 6
 6
 

  
 3
 5
 9
  
 -
 0
 .
 3
 4
 9
  
  
 1
 .
 7
 7
 4
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 1
 2
  
  
 1
 .
 4
 6
 8
  
  
  
 1
 .
 0
 1
 0
 9
 0
 4
 7
 3
 8
 8
 

  
  
 p
 o
 w
 e
 l
 l
  
 n
 t
 h
 i
 t
 e
 r
  
 4
 :
  
 f
 r
 e
 t
  
 =
  
 1
 .
 0
 1
 0
 9
 0
 5
 

  
 3
 7
 3
  
 -
 0
 .
 3
 4
 7
  
  
 1
 .
 7
 7
 4
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 1
 2
  
  
 1
 .
 4
 6
 8
  
  
  
 1
 .
 0
 1
 0
 9
 0
 4
 3
 9
 7
 9
 

  
 4
 2
 7
  
 -
 0
 .
 3
 4
 7
  
  
 1
 .
 7
 7
 4
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 2
 7
  
  
 1
 .
 4
 6
 8
  
  
  
 1
 .
 0
 1
 0
 8
 9
 4
 4
 4
 0
 8
 

  
 4
 3
 5
  
 -
 0
 .
 3
 4
 7
  
  
 1
 .
 7
 7
 6
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 2
 7
  
  
 1
 .
 4
 7
 0
  
  
  
 1
 .
 0
 1
 0
 8
 8
 1
 4
 3
 7
 7
 

  
 4
 3
 8
  
 -
 0
 .
 3
 4
 7
  
  
 1
 .
 7
 7
 8
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 2
 7
  
  
 1
 .
 4
 7
 1
  
  
  
 1
 .
 0
 1
 0
 8
 7
 7
 9
 2
 9
 0
 

  
 4
 4
 0
  
 -
 0
 .
 3
 4
 7
  
  
 1
 .
 7
 7
 7
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 2
 7
  
  
 1
 .
 4
 7
 0
  
  
  
 1
 .
 0
 1
 0
 8
 7
 7
 8
 5
 1
 1
 

  
 4
 4
 3
  
 -
 0
 .
 3
 4
 7
  
  
 1
 .
 7
 7
 7
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 2
 7
  
  
 1
 .
 4
 7
 0
  
  
  
 1
 .
 0
 1
 0
 8
 7
 7
 5
 8
 6
 6
 

  
 4
 4
 5
  
 -
 0
 .
 3
 4
 7
  
  
 1
 .
 7
 7
 7
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 2
 7
  
  
 1
 .
 4
 7
 0
  
  
  
 1
 .
 0
 1
 0
 8
 7
 7
 5
 7
 8
 5
 

  
 4
 4
 8
  
 -
 0
 .
 3
 4
 7
  
  
 1
 .
 7
 7
 7
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 2
 7
  
  
 1
 .
 4
 7
 0
  
  
  
 1
 .
 0
 1
 0
 8
 7
 7
 5
 6
 8
 8
 

  
 4
 4
 9
  
 -
 0
 .
 3
 4
 7
  
  
 1
 .
 7
 7
 7
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 2
 7
  
  
 1
 .
 4
 7
 0
  
  
  
 1
 .
 0
 1
 0
 8
 7
 7
 5
 5
 5
 6
 

  
  
 p
 o
 w
 e
 l
 l
  
 n
 t
 h
 i
 t
 e
 r
  
 5
 :
  
 f
 r
 e
 t
  
 =
  
 1
 .
 0
 1
 0
 8
 7
 8
 

  
 4
 6
 8
  
 -
 0
 .
 3
 4
 6
  
  
 1
 .
 7
 7
 7
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 2
 7
  
  
 1
 .
 4
 7
 0
  
  
  
 1
 .
 0
 1
 0
 8
 6
 2
 9
 3
 6
 0
 

  
 4
 7
 6
  
 -
 0
 .
 3
 4
 6
  
  
 1
 .
 7
 7
 7
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 2
 7
  
  
 1
 .
 4
 8
 5
  
  
  
 1
 .
 0
 1
 0
 8
 2
 0
 5
 1
 2
 7
 

  
 4
 7
 8
  
 -
 0
 .
 3
 4
 6
  
  
 1
 .
 7
 7
 7
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 5
  
  
 0
 .
 1
 2
 7
  
  
 1
 .
 4
 8
 0
  
  
  
 1
 .
 0
 1
 0
 7
 8
 8
 7
 7
 8
 1
 

  
 5
 0
 6
  
 -
 0
 .
 3
 4
 6
  
  
 1
 .
 7
 7
 7
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 6
  
  
 0
 .
 1
 2
 7
  
  
 1
 .
 4
 8
 0
  
  
  
 1
 .
 0
 1
 0
 7
 8
 7
 9
 0
 8
 7
 

  
 5
 2
 2
  
 -
 0
 .
 3
 4
 6
  
  
 1
 .
 7
 7
 7
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 6
  
  
 0
 .
 1
 2
 9
  
  
 1
 .
 4
 8
 0
  
  
  
 1
 .
 0
 1
 0
 7
 6
 3
 0
 8
 6
 9
 

  
 5
 2
 8
  
 -
 0
 .
 3
 4
 6
  
  
 1
 .
 7
 7
 6
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 6
  
  
 0
 .
 1
 2
 9
  
  
 1
 .
 4
 7
 9
  
  
  
 1
 .
 0
 1
 0
 7
 5
 6
 2
 4
 0
 2
 

  
 5
 3
 3
  
 -
 0
 .
 3
 4
 6
  
  
 1
 .
 7
 7
 6
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 6
  
  
 0
 .
 1
 2
 9
  
  
 1
 .
 4
 7
 9
  
  
  
 1
 .
 0
 1
 0
 7
 5
 5
 9
 6
 6
 8
 

  
 5
 3
 4
  
 -
 0
 .
 3
 4
 6
  
  
 1
 .
 7
 7
 6
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 6
  
  
 0
 .
 1
 2
 9
  
  
 1
 .
 4
 7
 9
  
  
  
 1
 .
 0
 1
 0
 7
 5
 5
 7
 6
 9
 1
 

  
 5
 3
 5
  
 -
 0
 .
 3
 4
 6
  
  
 1
 .
 7
 7
 6
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 6
  
  
 0
 .
 1
 2
 9
  
  
 1
 .
 4
 7
 9
  
  
  
 1
 .
 0
 1
 0
 7
 5
 5
 7
 3
 8
 7
 

  
 5
 3
 6
  
 -
 0
 .
 3
 4
 6
  
  
 1
 .
 7
 7
 6
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 6
  
  
 0
 .
 1
 2
 9
  
  
 1
 .
 4
 7
 9
  
  
  
 1
 .
 0
 1
 0
 7
 5
 5
 5
 8
 6
 8
 

  
 5
 3
 7
  
 -
 0
 .
 3
 4
 6
  
  
 1
 .
 7
 7
 6
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 6
  
  
 0
 .
 1
 2
 9
  
  
 1
 .
 4
 7
 9
  
  
  
 1
 .
 0
 1
 0
 7
 5
 5
 5
 4
 2
 9
 

  
  
 p
 o
 w
 e
 l
 l
  
 n
 t
 h
 i
 t
 e
 r
  
 6
 :
  
 f
 r
 e
 t
  
 =
  
 1
 .
 0
 1
 0
 7
 5
 6
 

  
 5
 5
 0
  
 -
 0
 .
 3
 3
 9
  
  
 1
 .
 7
 7
 6
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 6
  
  
 0
 .
 1
 2
 9
  
  
 1
 .
 4
 7
 9
  
  
  
 1
 .
 0
 1
 0
 7
 5
 1
 4
 8
 8
 3
 

  
 5
 5
 2
  
 -
 0
 .
 3
 4
 0
  
  
 1
 .
 7
 7
 6
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 6
  
  
 0
 .
 1
 2
 9
  
  
 1
 .
 4
 7
 9
  
  
  
 1
 .
 0
 1
 0
 7
 3
 9
 8
 5
 8
 2
 

  
 5
 5
 3
  
 -
 0
 .
 3
 4
 2
  
  
 1
 .
 7
 7
 6
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 6
  
  
 0
 .
 1
 2
 9
  
  
 1
 .
 4
 7
 9
  
  
  
 1
 .
 0
 1
 0
 7
 3
 9
 5
 0
 0
 5
 

  
 5
 6
 5
  
 -
 0
 .
 3
 4
 2
  
  
 1
 .
 7
 7
 6
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 6
  
  
 0
 .
 1
 2
 9
  
  
 1
 .
 4
 8
 1
  
  
  
 1
 .
 0
 1
 0
 7
 3
 0
 2
 0
 2
 1
 

  
 6
 1
 6
  
 -
 0
 .
 3
 4
 2
  
  
 1
 .
 7
 7
 6
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 6
  
  
 0
 .
 1
 2
 9
  
  
 1
 .
 4
 8
 1
  
  
  
 1
 .
 0
 1
 0
 7
 3
 0
 1
 3
 5
 3
 

  
 6
 1
 7
  
 -
 0
 .
 3
 4
 2
  
  
 1
 .
 7
 7
 6
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 6
  
  
 0
 .
 1
 2
 9
  
  
 1
 .
 4
 8
 1
  
  
  
 1
 .
 0
 1
 0
 7
 3
 0
 0
 8
 7
 1
 

  
 6
 1
 8
  
 -
 0
 .
 3
 4
 2
  
  
 1
 .
 7
 7
 6
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 6
  
  
 0
 .
 1
 2
 9
  
  
 1
 .
 4
 8
 1
  
  
  
 1
 .
 0
 1
 0
 7
 2
 9
 9
 6
 9
 2
 

  
  
 p
 o
 w
 e
 l
 l
  
 n
 t
 h
 i
 t
 e
 r
  
 7
 :
  
 f
 r
 e
 t
  
 =
  
 1
 .
 0
 1
 0
 7
 3
 0
 

  
 7
 0
 3
  
 -
 0
 .
 3
 4
 2
  
  
 1
 .
 7
 7
 6
  
  
 0
 .
 1
 2
 4
  
 -
 0
 .
 1
 0
 6
  
  
 0
 .
 1
 2
 9
  
  
 1
 .
 4
 8
 1
  
  
  
 1
 .
 0
 1
 0
 7
 2
 9
 8
 5
 6
 3
 

  
  
 p
 o
 w
 e
 l
 l
  
 n
 t
 h
 i
 t
 e
 r
  
 8
 :
  
 f
 r
 e
 t
  
 =
  
 1
 .
 0
 1
 0
 7
 3
 0
 

 P
 o
 w
 e
 l
 l
  
 d
 o
 n
 e
  
 n
 i
 t
 e
 r
 s
  
 =
  
 8
 

 C
 o
 m
 p
 u
 t
 i
 n
 g
  
 r
 e
 l
 a
 t
 i
 v
 e
  
 c
 o
 s
 t
 

  
 0
  
  
 -
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
  
 1
 .
 0
 1
 3
 2
 4
 1
 

  
 1
  
  
 -
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
  
 0
 .
 9
 8
 8
 2
 0
 1
 

  
 2
  
  
 -
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
  
 1
 .
 0
 5
 3
 3
 5
 5
 

  
 3
  
  
 -
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
  
 1
 .
 0
 3
 0
 5
 7
 1
 

  
 4
  
  
  
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
  
 1
 .
 0
 4
 9
 1
 4
 2
 

  
 5
  
  
  
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
  
 1
 .
 0
 3
 1
 5
 1
 6
 

  
 6
  
  
  
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
 -
 2
 5
 .
 0
  
  
  
 1
 .
 0
 3
 6
 7
 3
 0
 

  
 7
  
  
  
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
 2
 5
 .
 0
  
  
  
 1
 .
 0
 4
 4
 8
 0
 1
 

 R
 E
 L
 :
  
  
 8
  
  
 1
 .
 0
 1
 0
 7
 3
 0
  
  
  
  
 8
 .
 2
 4
 7
 5
 5
 8
  
  
 1
 .
 0
 3
 0
 9
 4
 5
  
 r
 e
 l
  
 =
  
 0
 .
 9
 8
 0
 3
 9
 2
  
 

 N
 u
 m
 b
 e
 r
  
 o
 f
  
 i
 t
 e
 r
 a
 t
 i
 o
 n
 s
  
  
  
  
  
 8
 

 M
 i
 n
  
 c
 o
 s
 t
  
 w
 a
 s
  
 1
 .
 0
 1
 0
 7
 3
 0
 

 N
 u
 m
 b
 e
 r
  
 o
 f
  
 F
 u
 n
 c
 t
 i
 o
 n
 C
 a
 l
 l
 s
  
  
  
 7
 9
 9
 

 T
 o
 l
 P
 o
 w
 e
 l
 l
  
 0
 .
 0
 0
 0
 0
 0
 0
 

 n
 M
 a
 x
 I
 t
 e
 r
 s
 P
 o
 w
 e
 l
 l
  
 3
 6
 

 O
 p
 t
 i
 m
 i
 z
 a
 t
 i
 o
 n
 T
 i
 m
 e
  
 7
 3
 .
 7
 2
 1
 0
 0
 0
  
 s
 e
 c
 

 P
 a
 r
 a
 m
 e
 t
 e
 r
 s
  
 a
 t
  
 o
 p
 t
 i
 m
 u
 m
  
 (
 t
 r
 a
 n
 s
 m
 m
 )
  
 -
 0
 .
 3
 4
 2
 4
 1
  
  
 1
 .
 7
 7
 5
 8
 0
  
  
 0
 .
 1
 2
 4
 4
 6
 

 P
 a
 r
 a
 m
 e
 t
 e
 r
 s
  
 a
 t
  
 o
 p
 t
 i
 m
 u
 m
  
 (
 r
 o
 t
 d
 e
 g
 )
  
 -
 0
 .
 1
 0
 5
 6
 0
  
  
 0
 .
 1
 2
 8
 6
 7
  
  
 1
 .
 4
 8
 1
 1
 9
  
 

 F
 i
 n
 a
 l
  
 c
 o
 s
 t
 s
  
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 

 N
 u
 m
 b
 e
 r
  
 o
 f
  
 s
 u
 r
 f
 a
 c
 e
  
 h
 i
 t
 s
  
 9
 0
 3
 5
 6
 

 W
 M
  
  
 I
 n
 t
 e
 n
 s
 i
 t
 y
  
  
  
 1
 3
 8
 .
 2
 8
 9
 0
  
 +
 /
 -
  
 2
 2
 1
 .
 1
 8
 5
 4
 

 C
 t
 x
  
 I
 n
 t
 e
 n
 s
 i
 t
 y
  
  
  
 1
 3
 6
 .
 7
 3
 5
 2
  
 +
 /
 -
  
 2
 2
 3
 .
 3
 3
 7
 4
 

 P
 c
 t
  
 C
 o
 n
 t
 r
 a
 s
 t
  
  
  
  
  
 -
 0
 .
 7
 3
 8
 6
  
 +
 /
 -
  
  
 8
 1
 .
 5
 4
 0
 5
 

 C
 o
 s
 t
  
  
  
 1
 .
 0
 1
 0
 7
 

 R
 e
 l
 C
 o
 s
 t
  
  
  
 0
 .
 9
 9
 2
 1
 

 R
 e
 g
  
 a
 t
  
 m
 i
 n
  
 c
 o
 s
 t
  
 w
 a
 s
  
 

  
 0
 .
 9
 9
 1
 0
 5
  
  
  
 0
 .
 0
 9
 9
 6
 2
  
  
 -
 0
 .
 0
 8
 8
 8
 8
  
  
 -
 1
 0
 .
 1
 4
 3
 2
 6
 ;
 

  
 0
 .
 0
 9
 6
 9
 2
  
  
 -
 0
 .
 0
 7
 9
 0
 3
  
  
  
 0
 .
 9
 9
 2
 1
 5
  
  
 -
 1
 8
 .
 4
 0
 5
 9
 3
 ;
 

  
 0
 .
 0
 9
 1
 8
 1
  
  
 -
 0
 .
 9
 9
 1
 8
 8
  
  
 -
 0
 .
 0
 8
 7
 9
 8
  
  
 -
 0
 .
 6
 2
 2
 8
 6
 ;
 

  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 .
 0
 0
 0
 0
 0
 ;
 

 

 W
 r
 i
 t
 i
 n
 g
  
 o
 p
 t
 i
 m
 a
 l
  
 r
 e
 g
  
 t
 o
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 _
 b
 b
 r
 e
 g
 _
 s
 u
 b
 -
 b
 m
 .
 d
 a
 t
 ,
  
 t
 y
 p
 e
  
 =
  
 1
 4
  
 

 O
 r
 i
 g
 i
 n
 a
 l
  
 R
 e
 g
  
 

  
 0
 .
 9
 9
 3
 0
 1
  
  
  
 0
 .
 0
 9
 9
 7
 7
  
  
 -
 0
 .
 0
 6
 3
 0
 1
  
  
 -
 1
 0
 .
 3
 1
 7
 5
 5
 ;
 

  
 0
 .
 0
 7
 1
 1
 0
  
  
 -
 0
 .
 0
 7
 9
 7
 5
  
  
  
 0
 .
 9
 9
 4
 2
 8
  
  
 -
 1
 9
 .
 9
 2
 0
 1
 9
 ;
 

  
 0
 .
 0
 9
 4
 1
 7
  
  
 -
 0
 .
 9
 9
 1
 8
 1
  
  
 -
 0
 .
 0
 8
 6
 2
 9
  
  
 -
 0
 .
 8
 0
 7
 2
 0
 ;
 

  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 .
 0
 0
 0
 0
 0
 ;
 

 

 O
 r
 i
 g
 i
 n
 a
 l
  
 R
 e
 g
  
 -
  
 O
 p
 t
 i
 m
 a
 l
  
 R
 e
 g
 

  
 0
 .
 0
 0
 1
 9
 7
  
  
  
 0
 .
 0
 0
 0
 1
 5
  
  
  
 0
 .
 0
 2
 5
 8
 7
  
  
 -
 0
 .
 1
 7
 4
 2
 8
 ;
 

 -
 0
 .
 0
 2
 5
 8
 2
  
  
 -
 0
 .
 0
 0
 0
 7
 2
  
  
  
 0
 .
 0
 0
 2
 1
 3
  
  
 -
 1
 .
 5
 1
 4
 2
 7
 ;
 

  
 0
 .
 0
 0
 2
 3
 6
  
  
  
 0
 .
 0
 0
 0
 0
 7
  
  
  
 0
 .
 0
 0
 1
 6
 9
  
  
 -
 0
 .
 1
 8
 4
 3
 4
 ;
 

  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
 ;
 

 

 C
 o
 m
 p
 u
 t
 i
 n
 g
  
 c
 h
 a
 n
 g
 e
  
 i
 n
  
 l
 h
  
 p
 o
 s
 i
 t
 i
 o
 n
 

 L
 H
  
 r
 m
 s
 D
 i
 f
 f
 M
 e
 a
 n
  
 1
 .
 0
 5
 0
 2
 9
 0
 

 C
 o
 m
 p
 u
 t
 i
 n
 g
  
 c
 h
 a
 n
 g
 e
  
 i
 n
  
 r
 h
  
 p
 o
 s
 i
 t
 i
 o
 n
 

 S
 u
 r
 f
 a
 c
 e
 -
 R
 M
 S
 -
 D
 i
 f
 f
 -
 m
 m
  
 1
 .
 6
 4
 0
 5
 2
 8
  
 0
 .
 7
 0
 4
 0
 3
 9
  
 3
 .
 0
 6
 3
 6
 9
 4
 

 

 

 W
 A
 R
 N
 I
 N
 G
 :
  
 i
 n
 i
 t
 i
 a
 l
  
 G
 -
 W
  
 c
 o
 n
 t
 r
 a
 s
 t
  
 w
 a
 s
  
 n
 e
 g
 a
 t
 i
 v
 e
 ,
  
 b
 u
 t
  
 e
 x
 p
 e
 c
 t
 e
 d
  
 p
 o
 s
 i
 t
 i
 v
 e
 .
 

 I
 f
  
 t
 h
 e
  
 m
 o
 v
  
 d
 a
 t
 a
  
 h
 a
 s
  
 a
  
 T
 1
  
 c
 o
 n
 t
 r
 a
 s
 t
 ,
  
 r
 e
 -
 r
 u
 n
  
 w
 i
 t
 h
  
 -
 -
 T
 1
 

 

 

 m
 r
 i
 _
 s
 e
 g
 r
 e
 g
  
 d
 o
 n
 e
 

 M
 i
 n
 C
 o
 s
 t
 :
  
 1
 .
 0
 1
 0
 7
 3
 0
  
 1
 3
 8
 .
 2
 8
 9
 0
 4
 7
  
 1
 3
 6
 .
 7
 3
 5
 2
 0
 1
  
 -
 0
 .
 7
 3
 8
 5
 9
 4
  
 

 t
 k
 r
 e
 g
 i
 s
 t
 e
 r
 2
 _
 c
 m
 d
 l
  
 -
 -
 m
 o
 v
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 .
 n
 i
 i
 .
 g
 z
  
 -
 -
 r
 e
 g
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 _
 b
 b
 r
 e
 g
 _
 s
 u
 b
 -
 b
 m
 .
 d
 a
 t
  
 -
 -
 n
 o
 e
 d
 i
 t
  
 -
 -
 f
 s
 l
 r
 e
 g
 o
 u
 t
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 _
 b
 b
 r
 e
 g
 _
 s
 u
 b
 -
 b
 m
 .
 m
 a
 t
 

 t
 k
 r
 e
 g
 i
 s
 t
 e
 r
 _
 t
 c
 l
  
 /
 o
 p
 t
 /
 f
 r
 e
 e
 s
 u
 r
 f
 e
 r
 -
 6
 .
 0
 .
 1
 /
 t
 k
 t
 o
 o
 l
 s
 /
 t
 k
 r
 e
 g
 i
 s
 t
 e
 r
 2
 .
 t
 c
 l
 

 I
 N
 F
 O
 :
  
 n
 o
  
 t
 a
 r
 g
 e
 t
  
 v
 o
 l
 u
 m
 e
  
 s
 p
 e
 c
 i
 f
 i
 e
 d
 ,
  
 a
 s
 s
 u
 m
 i
 n
 g
  
 F
 r
 e
 e
 S
 u
 r
 f
 e
 r
  
 o
 r
 i
 g
  
 v
 o
 l
 u
 m
 e
 .
 

 t
 a
 r
 g
 e
 t
  
  
 v
 o
 l
 u
 m
 e
  
 o
 r
 i
 g
 

 m
 o
 v
 a
 b
 l
 e
  
 v
 o
 l
 u
 m
 e
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 .
 n
 i
 i
 .
 g
 z
 

 r
 e
 g
  
 f
 i
 l
 e
  
  
  
  
  
  
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 _
 b
 b
 r
 e
 g
 _
 s
 u
 b
 -
 b
 m
 .
 d
 a
 t
 

 L
 o
 a
 d
 V
 o
 l
  
  
  
  
  
  
  
  
 0
 

 Z
 e
 r
 o
 C
 R
 A
 S
  
  
  
  
  
  
  
 0
 

 $
 I
 d
 :
  
 t
 k
 r
 e
 g
 i
 s
 t
 e
 r
 2
 .
 c
 ,
 v
  
 1
 .
 1
 3
 2
 .
 2
 .
 1
  
 2
 0
 1
 6
 /
 0
 8
 /
 0
 2
  
 2
 1
 :
 1
 7
 :
 2
 9
  
 g
 r
 e
 v
 e
  
 E
 x
 p
  
 $
 

 D
 i
 a
 g
 n
 o
 s
 t
 i
 c
  
 L
 e
 v
 e
 l
  
 -
 1
 

 -
 -
 -
 -
  
 I
 n
 p
 u
 t
  
 r
 e
 g
 i
 s
 t
 r
 a
 t
 i
 o
 n
  
 m
 a
 t
 r
 i
 x
  
 -
 -
 -
 -
 -
 -
 -
 -
 

  
 0
 .
 9
 9
 1
 0
 5
  
  
  
 0
 .
 0
 9
 9
 6
 2
  
  
 -
 0
 .
 0
 8
 8
 8
 8
  
  
 -
 1
 0
 .
 1
 4
 3
 2
 6
 ;
 

  
 0
 .
 0
 9
 6
 9
 2
  
  
 -
 0
 .
 0
 7
 9
 0
 3
  
  
  
 0
 .
 9
 9
 2
 1
 5
  
  
 -
 1
 8
 .
 4
 0
 5
 9
 3
 ;
 

  
 0
 .
 0
 9
 1
 8
 1
  
  
 -
 0
 .
 9
 9
 1
 8
 8
  
  
 -
 0
 .
 0
 8
 7
 9
 8
  
  
 -
 0
 .
 6
 2
 2
 8
 6
 ;
 

  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 .
 0
 0
 0
 0
 0
 ;
 

 f
 l
 o
 a
 t
 2
 i
 n
 t
  
 =
  
 0
 

 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 

 I
 N
 F
 O
 :
  
 l
 o
 a
 d
 i
 n
 g
  
 t
 a
 r
 g
 e
 t
  
 /
 d
 e
 r
 i
 v
 a
 t
 i
 v
 e
 s
 /
 f
 r
 e
 e
 s
 u
 r
 f
 e
 r
 /
 s
 u
 b
 -
 b
 m
 /
 m
 r
 i
 /
 o
 r
 i
 g
 .
 m
 g
 z
 

 I
 N
 F
 O
 :
  
 t
 a
 r
 g
 e
 t
  
 d
 o
 e
 s
  
 n
 o
 t
  
 c
 o
 n
 f
 o
 r
 m
  
 t
 o
  
 C
 O
 R
  
 f
 o
 r
 m
 a
 t
 ,
  
 s
 o
  
 I
 '
 m
  
 g
 o
 i
 n
 g
  
 t
 o
 

 r
 e
 s
 l
 i
 c
 e
  
 t
 o
  
 C
 O
 R
 .
  
 T
 h
 i
 s
  
 w
 i
 l
 l
  
 n
 o
 t
  
 a
 f
 f
 e
 c
 t
  
 t
 h
 e
  
 f
 i
 n
 a
 l
  
 r
 e
 g
 i
 s
 t
 r
 a
 t
 i
 o
 n
 .
 

 T
 t
 a
 r
 g
 :
  
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 

 -
 1
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 2
 8
 .
 0
 0
 0
 0
 0
 ;
 

  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 .
 0
 0
 0
 0
 0
  
  
 -
 1
 2
 8
 .
 0
 0
 0
 0
 0
 ;
 

  
 0
 .
 0
 0
 0
 0
 0
  
  
 -
 1
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 2
 8
 .
 0
 0
 0
 0
 0
 ;
 

  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 .
 0
 0
 0
 0
 0
 ;
 

 I
 N
 F
 O
 :
  
 l
 o
 a
 d
 i
 n
 g
  
 m
 o
 v
 a
 b
 l
 e
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 .
 n
 i
 i
 .
 g
 z
 

 T
 m
 o
 v
 :
  
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 

 -
 0
 .
 6
 8
 2
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 6
 5
 .
 4
 7
 2
 0
 0
 ;
 

  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 6
 8
 2
 0
 0
  
  
 -
 6
 5
 .
 4
 7
 2
 0
 0
 ;
 

  
 0
 .
 0
 0
 0
 0
 0
  
  
 -
 0
 .
 7
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 1
 .
 9
 0
 0
 0
 0
 ;
 

  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 .
 0
 0
 0
 0
 0
 ;
 

 m
 k
 h
 e
 a
 d
 e
 r
 r
 e
 g
  
 =
  
 0
 ,
  
 f
 l
 o
 a
 t
 2
 i
 n
 t
  
 =
  
 0
 

 -
 -
 -
 -
  
 I
 n
 p
 u
 t
  
 r
 e
 g
 i
 s
 t
 r
 a
 t
 i
 o
 n
  
 m
 a
 t
 r
 i
 x
  
 -
 -
 -
 -
 -
 -
 -
 -
 

  
 0
 .
 9
 9
 1
 0
 5
  
  
  
 0
 .
 0
 9
 9
 6
 2
  
  
 -
 0
 .
 0
 8
 8
 8
 8
  
  
 -
 1
 0
 .
 1
 4
 3
 2
 8
 ;
 

  
 0
 .
 0
 9
 6
 9
 2
  
  
 -
 0
 .
 0
 7
 9
 0
 3
  
  
  
 0
 .
 9
 9
 2
 1
 5
  
  
 -
 1
 8
 .
 4
 0
 5
 9
 4
 ;
 

  
 0
 .
 0
 9
 1
 8
 1
  
  
 -
 0
 .
 9
 9
 1
 8
 8
  
  
 -
 0
 .
 0
 8
 7
 9
 8
  
  
 -
 0
 .
 6
 2
 2
 8
 8
 ;
 

  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 .
 0
 0
 0
 0
 0
 ;
 

 D
 e
 t
 e
 r
 m
 i
 n
 a
 n
 t
  
 0
 .
 9
 9
 9
 9
 9
 9
 

 s
 u
 b
 j
 e
 c
 t
  
 =
  
 s
 u
 b
 -
 b
 m
 

 R
 e
 g
 M
 a
 t
  
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 

  
 0
 .
 9
 9
 1
 0
 5
  
  
  
 0
 .
 0
 9
 9
 6
 2
  
  
 -
 0
 .
 0
 8
 8
 8
 8
  
  
 -
 1
 0
 .
 1
 4
 3
 2
 6
 ;
 

  
 0
 .
 0
 9
 6
 9
 2
  
  
 -
 0
 .
 0
 7
 9
 0
 3
  
  
  
 0
 .
 9
 9
 2
 1
 5
  
  
 -
 1
 8
 .
 4
 0
 5
 9
 3
 ;
 

  
 0
 .
 0
 9
 1
 8
 1
  
  
 -
 0
 .
 9
 9
 1
 8
 8
  
  
 -
 0
 .
 0
 8
 7
 9
 8
  
  
 -
 0
 .
 6
 2
 2
 8
 6
 ;
 

  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 0
 .
 0
 0
 0
 0
 0
  
  
  
 1
 .
 0
 0
 0
 0
 0
 ;
 

 F
 S
 L
 O
 U
 T
 P
 U
 T
 T
 Y
 P
 E
  
 N
 I
 F
 T
 I
 _
 G
 Z
  
 

 t
 k
 r
 e
 g
 2
 F
 S
 L
 :
  
 m
 o
 v
  
 d
 e
 t
  
 =
  
 -
 0
 .
 3
 2
 5
 5
 8
 7
 ,
  
 r
 e
 f
  
 d
 e
 t
  
 =
  
 -
 0
 .
 2
 6
 2
 1
 4
 4
 

 C
 l
 e
 a
 n
 i
 n
 g
  
 u
 p
 

  
 

 S
 t
 a
 r
 t
 e
 d
  
 a
 t
  
 T
 u
 e
  
 D
 e
 c
  
 1
 1
  
 1
 5
 :
 3
 3
 :
 3
 4
  
 U
 T
 C
  
 2
 0
 1
 8
  
 

 E
 n
 d
 e
 d
  
  
  
 a
 t
  
 T
 u
 e
  
 D
 e
 c
  
 1
 1
  
 1
 5
 :
 3
 7
 :
 0
 8
  
 U
 T
 C
  
 2
 0
 1
 8
 

 B
 B
 R
 -
 R
 u
 n
 -
 T
 i
 m
 e
 -
 S
 e
 c
  
 2
 1
 4
 

  
 

 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
  
 D
 o
 n
 e
 

 T
 o
  
 c
 h
 e
 c
 k
  
 r
 e
 s
 u
 l
 t
 s
 ,
  
 r
 u
 n
 :
 

 t
 k
 r
 e
 g
 i
 s
 t
 e
 r
 f
 v
  
 -
 -
 m
 o
 v
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 .
 n
 i
 i
 .
 g
 z
  
 -
 -
 r
 e
 g
  
 /
 w
 o
 r
 k
 f
 l
 o
 w
 _
 f
 o
 l
 d
 e
 r
 s
 /
 r
 e
 g
 _
 t
 e
 s
 t
 /
 b
 b
 r
 e
 g
 i
 s
 t
 e
 r
 _
 N
 /
 s
 u
 b
 -
 b
 m
 _
 s
 e
 s
 -
 o
 d
 c
 _
 t
 a
 s
 k
 -
 c
 h
 e
 c
 k
 e
 r
 b
 o
 a
 r
 d
 _
 a
 c
 q
 -
 0
 7
 _
 r
 u
 n
 -
 0
 3
 _
 b
 o
 l
 d
 _
 m
 c
 f
 _
 r
 o
 i
 _
 m
 e
 a
 n
 _
 a
 v
 _
 b
 b
 r
 e
 g
 _
 s
 u
 b
 -
 b
 m
 .
 d
 a
 t
  
 -
 -
 s
 u
 r
 f
 s
  
 

  


Terminal - standard error
~~~~~~~~~~~~~~~~~~~~~~~~~





Environment
~~~~~~~~~~~


* AFNI_PLUGINPATH : /opt/afni-latest
* ANTSPATH : /opt/ants-master/bin
* C3DPATH : /opt/convert3d-1.0.0
* CONDA_DEFAULT_ENV : neuro
* CONDA_DIR : /opt/miniconda-latest
* CONDA_EXE : /opt/miniconda-latest/bin/conda
* CONDA_PREFIX : /opt/miniconda-latest/envs/neuro
* CONDA_PROMPT_MODIFIER : (neuro) 
* CONDA_PYTHON_EXE : /opt/miniconda-latest/bin/python
* CONDA_SHLVL : 1
* FREESURFER_HOME : /opt/freesurfer-6.0.1
* FSLDIR : /opt/fsl-5.0.11
* FSLGECUDAQ : cuda.q
* FSLLOCKDIR : 
* FSLMACHINELIST : 
* FSLMULTIFILEQUIT : TRUE
* FSLOUTPUTTYPE : NIFTI_GZ
* FSLREMOTECALL : 
* FSLTCLSH : /opt/fsl-5.0.11/bin/fsltclsh
* FSLWISH : /opt/fsl-5.0.11/bin/fslwish
* HOME : /root
* HOSTNAME : 9958f5fd3ba7
* JAVA_HOME : /docker-java-home
* JCC_JDK : /docker-java-home
* LANG : en_US.UTF-8
* LC_ALL : en_US.UTF-8
* LD_LIBRARY_PATH : /opt/ants-master/lib:
* LESS : -R
* LOGNAME : root
* LSCOLORS : Gxfxcxdxbxegedabagacad
* LS_COLORS : rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:
* ND_ENTRYPOINT : /neurodocker/startup.sh
* OLDPWD : /src
* PAGER : less
* PATH : /opt/miniconda-latest/envs/neuro/bin:/opt/ants-master/bin:/opt/miniconda-latest/bin:/opt/convert3d-1.0.0/bin:/opt/dcm2niix-latest/bin:/opt/fsl-5.0.11/bin:/opt/freesurfer-6.0.1/bin:/opt/ants-2.2.0:/opt/afni-latest:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
* PWD : /src
* SHLVL : 1
* SUBJECTS_DIR : /derivatives/freesurfer
* TERM : xterm
* ZSH : /root/.oh-my-zsh
* _ : /opt/miniconda-latest/envs/neuro/bin/ipython

