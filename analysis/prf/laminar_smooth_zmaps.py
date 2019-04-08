from nighres.laminar import laminar_iterative_smoothing, profile_sampling
from nilearn import image
import os.path as op

derivatives = '/derivatives'


subject = 'tk'

session = 'odc2'
fwhm = 1.0

zmap = op.join(derivatives,
               'modelfitting/sub-{subject}/ses-{session}/sub-{subject}_ses-{session}_left_over_right_zmap.nii.gz').format(**locals())

ls_l  = op.join(derivatives,
                'nighres/sub-tk/ses-anat/anat/sub-{subject}_ses-anat_space-average_desc-layerboundaries_hemi-left_levelset.nii.gz').format(**locals())
ls_r  = op.join(derivatives,
                'nighres/sub-tk/ses-anat/anat/sub-{subject}_ses-anat_space-average_desc-layerboundaries_hemi-right_levelset.nii.gz').format(**locals())

zmap_l = image.resample_to_img(zmap, ls_l)
zmap_l_smooth = laminar_iterative_smoothing(ls_l, zmap_l, 1)['result']

sample = profile_sampling(ls_l, zmap_l_smooth)

