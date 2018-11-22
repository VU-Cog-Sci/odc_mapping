from utils import get_derivative
from nighres_interfaces import (MP2RAGESkullStrip, MP2RAGEDuraEstimation, 
                                MGDMSegmentation, ExtractBrainRegion,
                                CRUISECortexExtraction)
import nipype.pipeline.engine as pe
import nipype.interfaces.utility as niu
import argparse
from bids import BIDSLayout
from nipype.interfaces import fsl
from fmriprep.interfaces import DerivativesDataSink

def main(sourcedata, 
         derivatives,
         tmp_dir,
         subject=None):

    layout = BIDSLayout(sourcedata)

    inv2 = get_derivative(derivatives, 'averaged_mp2rages', 'anat', subject,
                          'INV2', session='anat', space='average') 
    t1w = get_derivative(derivatives, 'averaged_mp2rages', 'anat', subject,
                          'T1w', session='anat', space='average') 
    t1map = get_derivative(derivatives, 'averaged_mp2rages', 'anat', subject,
                          'T1map', session='anat', space='average')

    manual_outside_mask = get_derivative(derivatives, 'manual_segmentation',
                                         'anat', subject, 'mask',
                                         description='outside', session='anat',
                                         check_exists=False, space='average')
    manual_gm_mask = get_derivative(derivatives, 'manual_segmentation',
                                    'anat', subject, 'mask',
                                     description='gm', session='anat',
                                     check_exists=False, space='average')
    manual_wm_mask = get_derivative(derivatives, 'manual_segmentation',
                                    'anat', subject, 'mask',
                                     description='wm', session='anat',
                                     check_exists=False, space='average')

    fmriprep_wm = get_derivative(derivatives, 'fmriprep', 'anat', subject,
                                 'probseg', label='WM', session='anat')
    fmriprep_gm = get_derivative(derivatives, 'fmriprep', 'anat', subject,
                                 'probseg', label='GM', session='anat')
    fmriprep_csf = get_derivative(derivatives, 'fmriprep', 'anat', subject,
                                 'probseg', label='CSF', session='anat')

    freesurfer_seg = get_derivative(derivatives, 'fmriprep', 'anat', subject,
                                    'dseg', description='aseg', session='anat') 

    name = 'nighres_{}'.format(subject)

    wf = init_from_fmriprep_to_nighres_wf(name)
    wf.base_dir = tmp_dir

    wf.inputs.inputnode.inv2 = inv2
    wf.inputs.inputnode.t1w = t1w
    wf.inputs.inputnode.t1map = t1map
    wf.inputs.inputnode.manual_mask_outside = manual_outside_mask
    wf.inputs.inputnode.manual_mask_gm = manual_gm_mask
    wf.inputs.inputnode.manual_mask_wm = manual_wm_mask
    wf.inputs.inputnode.fmriprep_csf = fmriprep_csf
    wf.inputs.inputnode.fmriprep_wm = fmriprep_wm
    wf.inputs.inputnode.fmriprep_gm = fmriprep_gm
    wf.inputs.inputnode.aseg = freesurfer_seg

    wf.run(plugin='MultiProc', plugin_args={'n_procs':10})


def init_from_fmriprep_to_nighres_wf(name='nighres',
                                    derivatives='/derivatives',
                                    manual_weight=5):
    
    
    wf = pe.Workflow(name=name)
    inputnode = pe.Node(niu.IdentityInterface(fields=['inv2',
                                                      't1w',
                                                      't1map',
                                                      'manual_mask_outside',
                                                      'manual_mask_gm',
                                                      'manual_mask_wm',
                                                      'fmriprep_csf',
                                                      'fmriprep_gm',
                                                      'fmriprep_wm',
                                                      'aseg']),
                        name='inputnode')

    fmriprep_segmentation_wf = init_combine_segmentations_wf(manual_weight=manual_weight)
    for key in ['fmriprep_csf', 'fmriprep_wm', 'fmriprep_gm', 'aseg', 'manual_mask_outside',
                'manual_mask_gm', 'manual_mask_wm']:
        wf.connect(inputnode, key, fmriprep_segmentation_wf, 'inputnode.{}'.format(key))

    nighres_wf = init_nighres_wf()

    wf.connect([(fmriprep_segmentation_wf, nighres_wf,
                [('outputnode.wm', 'inputnode.other_wm'),
                 ('outputnode.csf', 'inputnode.other_csf'),
                 ('outputnode.gm' ,'inputnode.other_gm')]),
               ])

    wf.connect([(inputnode, nighres_wf,
                [('inv2', 'inputnode.inv2'),
                 ('t1w' ,'inputnode.t1w'),
                 ('t1map' ,'inputnode.t1map'),
                 ('manual_mask_outside' ,'inputnode.manual_mask_outside')]),
               ])


    return wf

def get_freesurfer_seg(aseg):
    from nilearn import image
    import os
    from nipype.utils.filemanip import split_filename
    _, fn, ext = split_filename(aseg)

    aseg = image.load_img(aseg)
    
    wm_l = image.math_img('aseg == 2.0', aseg=aseg)
    wm_r = image.math_img('aseg == 41.0', aseg=aseg)
    gm_l = image.math_img('aseg == 3.0', aseg=aseg)
    gm_r = image.math_img('aseg == 42.0', aseg=aseg)
    csf = image.math_img('aseg == 0', aseg=aseg)

    wm_l.to_filename(os.path.abspath('{fn}_wm_l{ext}'.format(**locals())))
    wm_r.to_filename(os.path.abspath('{fn}_wm_r{ext}'.format(**locals())))
    gm_l.to_filename(os.path.abspath('{fn}_gm_l{ext}'.format(**locals())))
    gm_r.to_filename(os.path.abspath('{fn}_gm_r{ext}'.format(**locals())))
    csf.to_filename(os.path.abspath('{fn}_csf{ext}'.format(**locals())))

    return (wm_l.get_filename(),
            wm_r.get_filename(),
            gm_l.get_filename(),
            gm_r.get_filename(),
            csf.get_filename())

def weighted_sum(images, weights):
    from nilearn import image
    import os
    from nipype.utils.filemanip import split_filename
    import numpy as np
    
    _, fn, ext = split_filename(images[0])

    weights = [weight for weight, image in zip(weights, images) if image]
    images = [image for image in images if image]
    

    images = image.concat_imgs(images)
    weights = np.array(weights) / np.sum(weights)

    weighted_sum = image.new_img_like(images, (images.get_data() * weights).sum(-1))
    weighted_sum.to_filename(os.path.abspath('{fn}_sum{ext}'.format(fn=fn, ext=ext)))

    return weighted_sum.get_filename()


    
def init_combine_segmentations_wf(name='combine_segmenetations_wf',
                                 manual_weight=5):

    wf = pe.Workflow(name=name)

    inputnode = pe.Node(niu.IdentityInterface(fields=['manual_mask_outside',
                                                      'manual_mask_gm',
                                                      'manual_mask_wm',
                                                      'fmriprep_csf',
                                                      'fmriprep_gm',
                                                      'fmriprep_wm',
                                                      'aseg']),
                        name='inputnode')


    freesurfer_seg = pe.Node(niu.Function(function=get_freesurfer_seg,
                                          input_names=['aseg'],
                                          output_names=['wm_l','wm_r', 'gm_l', 'gm_r', 'csf']),
                            name='freesurfer_seg')

    wf.connect(inputnode, 'aseg', freesurfer_seg, 'aseg')

    # White matter
    merge_wm_fs = pe.Node(niu.Merge(2), name='merge_wm_fs')
    wf.connect(freesurfer_seg, 'wm_l', merge_wm_fs, 'in1')
    wf.connect(freesurfer_seg, 'wm_r', merge_wm_fs, 'in2')
    merge_wm = pe.MapNode(niu.Merge(3), iterfield=['in1'],
                          name='merge_wm') 
    wf.connect(merge_wm_fs, 'out', merge_wm, 'in1')
    wf.connect(inputnode, 'fmriprep_wm', merge_wm, 'in2')
    wf.connect(inputnode, 'manual_mask_wm', merge_wm, 'in3')
    
    weight_wm = pe.MapNode(niu.Function(function=weighted_sum,
                                     input_names=['images', 'weights'],
                                     output_names=['weighted_sum']),
                       iterfield=['images'],
                       name='weight_wm')
    weight_wm.inputs.weights = [1., 1., manual_weight]
    wf.connect(merge_wm, 'out', weight_wm, 'images')

    # White matter
    merge_gm_fs = pe.Node(niu.Merge(2), name='merge_gm_fs')
    wf.connect(freesurfer_seg, 'gm_l', merge_gm_fs, 'in1')
    wf.connect(freesurfer_seg, 'gm_r', merge_gm_fs, 'in2')
    merge_gm = pe.MapNode(niu.Merge(3), iterfield=['in1'],
                          name='merge_gm') 
    wf.connect(merge_gm_fs, 'out', merge_gm, 'in1')
    wf.connect(inputnode, 'fmriprep_gm', merge_gm, 'in2')
    wf.connect(inputnode, 'manual_mask_gm', merge_gm, 'in3')
    
    weight_gm = pe.MapNode(niu.Function(function=weighted_sum,
                                     input_names=['images', 'weights'],
                                     output_names=['weighted_sum']),
                       iterfield=['images'],
                       name='weight_gm')
    weight_gm.inputs.weights = [1., 1., manual_weight]
    wf.connect(merge_gm, 'out', weight_gm, 'images')

    # CSF
    merge_csf_fs = pe.Node(niu.Merge(2), name='merge_csf_fs')
    wf.connect(freesurfer_seg, 'csf', merge_csf_fs, 'in1')
    wf.connect(freesurfer_seg, 'csf', merge_csf_fs, 'in2')
    merge_csf = pe.MapNode(niu.Merge(3), iterfield=['in1'],
                          name='merge_csf') 
    wf.connect(merge_csf_fs, 'out', merge_csf, 'in1')
    wf.connect(inputnode, 'fmriprep_csf', merge_csf, 'in2')
    wf.connect(inputnode, 'manual_mask_outside', merge_csf, 'in3')
    
    weight_csf = pe.MapNode(niu.Function(function=weighted_sum,
                                     input_names=['images', 'weights'],
                                     output_names=['weighted_sum']),
                       iterfield=['images'],
                       name='weight_csf')
    weight_csf.inputs.weights = [1., 1., manual_weight]
    wf.connect(merge_csf, 'out', weight_csf, 'images')
     
    outputnode = pe.Node(niu.IdentityInterface(fields=['wm', 'gm', 'csf']),
                         name='outputnode')

    wf.connect(weight_wm, 'weighted_sum', outputnode, 'wm')
    wf.connect(weight_gm, 'weighted_sum', outputnode, 'gm')
    wf.connect(weight_csf, 'weighted_sum', outputnode, 'csf')

    return wf

def init_nighres_wf(name='nighres',
                    derivatives='/derivatives',
                    weight_other_segmentations=2):


    wf = pe.Workflow(name=name)

    inputnode = pe.Node(niu.IdentityInterface(fields=['inv2',
                                                      't1w',
                                                      't1map',
                                                      'manual_mask_outside',
                                                      'other_csf',
                                                      'other_gm',
                                                      'other_wm',
                                    ]),
                        name='inputnode')


    skullstrip = pe.Node(MP2RAGESkullStrip(),
                         name='skullstrip')

    wf.connect([(inputnode, skullstrip, 
                [('inv2', 'second_inversion'),
                 ('t1map', 't1_map'),
                 ('t1w', 't1_weighted')]
                 )
               ])

    dura_estimator = pe.Node(MP2RAGEDuraEstimation(),
                             name='dura_estimator')

    # combine filters
    wf.connect(inputnode, 'inv2', dura_estimator, 'second_inversion')
    wf.connect(skullstrip, 'brain_mask', dura_estimator, 'skullstrip_mask')

    merge_filters1 = pe.Node(niu.Merge(2), name='merge_filters1')
    wf.connect(dura_estimator, 'result', merge_filters1, 'in1')
    wf.connect(inputnode, 'manual_mask_outside', merge_filters1, 'in2')
    merge_filters2 = pe.Node(fsl.Merge(dimension='t'), name='merge_filters2')
    wf.connect(merge_filters1, 'out', merge_filters2, 'in_files')
    sum_filters1 = pe.Node(fsl.MeanImage(), name='sum_filters1')
    wf.connect(merge_filters2, 'merged_file', sum_filters1, 'in_file')
    sum_filters2 = pe.Node(fsl.BinaryMaths(operation='mul', 
                                           operand_value=2.0),
                           name='sum_filters2')
    wf.connect(sum_filters1, 'out_file', sum_filters2, 'in_file')

    # Segment

    mgdm = pe.Node(MGDMSegmentation(
                       contrast_type1='T1map7T',
                       contrast_type2='Mp2rage7T',
                       contrast_type3='Filters'), name='mgdm')
    wf.connect(skullstrip, 't1map_masked', mgdm, 'contrast_image1')
    wf.connect(skullstrip, 't1w_masked', mgdm, 'contrast_image2')
    wf.connect(sum_filters2, 'out_file', mgdm, 'contrast_image3')

    extract_regions = pe.MapNode(ExtractBrainRegion(), 
                                 iterfield=['extracted_region'],
                                 name='extract_regions')
    extract_regions.inputs.extracted_region = ['left_cerebrum', 'right_cerebrum']


    wf.connect([(mgdm, extract_regions, 
                 [('segmentation', 'segmentation'),
                  ('distance', 'levelset_boundary'),
                  ('labels', 'maximum_label'),
                  ('memberships', 'maximum_membership')],)
                ])


    # merge WM
    merge_wm = pe.MapNode(niu.Merge(2), iterfield=['in1', 'in2'],
                          name='merge_wm')
    weight_wm = pe.MapNode(niu.Function(function=weighted_sum,
                                     input_names=['images', 'weights'],
                                     output_names=['weighted_sum']),
                       iterfield=['images'],
                       name='weight_wm')
    weight_wm.inputs.weights = [1., weight_other_segmentations]

    wf.connect(extract_regions, 'inside_proba', merge_wm, 'in1')
    wf.connect(inputnode, 'other_wm', merge_wm, 'in2')
    wf.connect(merge_wm, 'out', weight_wm, 'images')

    # merge GM
    merge_gm = pe.MapNode(niu.Merge(2), iterfield=['in1', 'in2'],
                          name='merge_gm')
    weight_gm = pe.MapNode(niu.Function(function=weighted_sum,
                                     input_names=['images', 'weights'],
                                     output_names=['weighted_sum']),
                       iterfield=['images'],
                       name='weight_gm')
    weight_gm.inputs.weights = [1., weight_other_segmentations]
    wf.connect(extract_regions, 'region_proba', merge_gm, 'in1')
    wf.connect(inputnode, 'other_gm', merge_gm, 'in2')
    wf.connect(merge_gm, 'out', weight_gm, 'images')

    # merge CSF
    merge_csf = pe.MapNode(niu.Merge(2), iterfield=['in1', 'in2'],
                          name='merge_csf')
    weight_csf = pe.MapNode(niu.Function(function=weighted_sum,
                                     input_names=['images', 'weights'],
                                     output_names=['weighted_sum']),
                       iterfield=['images'],
                       name='weight_csf')
    weight_csf.inputs.weights = [1., weight_other_segmentations]
    wf.connect(extract_regions, 'background_proba', merge_csf, 'in1')
    wf.connect(inputnode, 'other_csf', merge_csf, 'in2')
    wf.connect(merge_csf, 'out', weight_csf, 'images')

    cruise = pe.MapNode(CRUISECortexExtraction(), 
                        iterfield=['init_image',
                                   'wm_image',
                                   'gm_image',
                                   'csf_image'],
                        name='cruise')

    wf.connect(weight_gm, 'weighted_sum', cruise, 'gm_image')
    wf.connect(weight_wm, 'weighted_sum', cruise, 'wm_image')
    wf.connect(weight_csf, 'weighted_sum', cruise, 'csf_image')
    wf.connect(extract_regions, 'inside_mask', cruise, 'init_image')
    wf.connect(sum_filters2, 'out_file', cruise, 'vd_image')
                    
    ds_segmentation = pe.Node(DerivativesDataSink(base_directory=derivatives,
                                                  out_path_base='nighres',
                                                  desc='mgdm',
                                                  suffix='dseg'),
                                                  name='ds_segmentation')


    wf.connect(mgdm, 'segmentation', ds_segmentation, 'in_file')
    wf.connect(inputnode, 't1w', ds_segmentation, 'source_file')

    return wf
                                        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("subject", 
                        type=str,
                        help="subject to process")

    args = parser.parse_args()

    main('/sourcedata/ds-odc', 
         '/derivatives',
         tmp_dir='/workflow_folders',
         subject=args.subject)
