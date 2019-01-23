Node: invert_EPI_N (fsl)
========================


 Hierarchy : reg_test.invert_EPI_N
 Exec ID : invert_EPI_N


Original Inputs
---------------


* args : <undefined>
* concat_xfm : <undefined>
* environ : {'FSLOUTPUTTYPE': 'NIFTI_GZ'}
* fix_scale_skew : <undefined>
* in_file : /workflow_folders/reg_test/bbregister_N/sub-bm_ses-odc_task-checkerboard_acq-07_run-03_bold_mcf_roi_mean_av_bbreg_sub-bm.mat
* in_file2 : <undefined>
* invert_xfm : True
* out_file : <undefined>
* output_type : NIFTI_GZ

Execution Inputs
----------------


* args : <undefined>
* concat_xfm : <undefined>
* environ : {'FSLOUTPUTTYPE': 'NIFTI_GZ'}
* fix_scale_skew : <undefined>
* in_file : /workflow_folders/reg_test/bbregister_N/sub-bm_ses-odc_task-checkerboard_acq-07_run-03_bold_mcf_roi_mean_av_bbreg_sub-bm.mat
* in_file2 : <undefined>
* invert_xfm : True
* out_file : <undefined>
* output_type : NIFTI_GZ


Execution Outputs
-----------------


* out_file : /workflow_folders/reg_test/invert_EPI_N/sub-bm_ses-odc_task-checkerboard_acq-07_run-03_bold_mcf_roi_mean_av_bbreg_sub-bm_inv.mat


Runtime info
------------


* command : convert_xfm -omat /workflow_folders/reg_test/invert_EPI_N/sub-bm_ses-odc_task-checkerboard_acq-07_run-03_bold_mcf_roi_mean_av_bbreg_sub-bm_inv.mat -inverse /workflow_folders/reg_test/bbregister_N/sub-bm_ses-odc_task-checkerboard_acq-07_run-03_bold_mcf_roi_mean_av_bbreg_sub-bm.mat
* duration : 0.145529
* hostname : 9958f5fd3ba7
* prev_wd : /src
* working_dir : /workflow_folders/reg_test/invert_EPI_N


Terminal output
~~~~~~~~~~~~~~~





Terminal - standard output
~~~~~~~~~~~~~~~~~~~~~~~~~~





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
* SUBJECTS_DIR : /derivatives/freesurfer/
* TERM : xterm
* ZSH : /root/.oh-my-zsh
* _ : /opt/miniconda-latest/envs/neuro/bin/ipython

