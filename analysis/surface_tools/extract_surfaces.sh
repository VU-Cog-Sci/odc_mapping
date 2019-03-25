export SUBJECTS_DIR=/derivatives/freesurfer
SID=$1
echo sub-$SID

echo python /surface_tools/equivolumetric_surfaces/generate_equivolumetric_surfaces.py --smoothing 5 $SUBJECTS_DIR/sub-$SID/surf/lh.pial $SUBJECTS_DIR/sub-$SID/surf/lh.white 8 lh.equi --software freesurfer --subject_id sub-$SID
python /surface_tools/equivolumetric_surfaces/generate_equivolumetric_surfaces.py --smoothing 5 $SUBJECTS_DIR/sub-$SID/surf/lh.pial $SUBJECTS_DIR/sub-$SID/surf/lh.white 8 lh.equi --software freesurfer --subject_id sub-$SID
echo python /surface_tools/equivolumetric_surfaces/generate_equivolumetric_surfaces.py --smoothing 5 $SUBJECTS_DIR/sub-$SID/surf/rh.pial $SUBJECTS_DIR/sub-$SID/surf/rh.white 8 rh.equi --software freesurfer --subject_id sub-$SID
python /surface_tools/equivolumetric_surfaces/generate_equivolumetric_surfaces.py --smoothing 5 $SUBJECTS_DIR/sub-$SID/surf/rh.pial $SUBJECTS_DIR/sub-$SID/surf/rh.white 8 rh.equi --software freesurfer --subject_id sub-$SID
