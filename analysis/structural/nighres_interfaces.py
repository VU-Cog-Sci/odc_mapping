from nipype.interfaces.base import (traits, TraitedSpec, LibraryBaseInterface,
                               SimpleInterface, BaseInterfaceInputSpec, File,
                               Directory, InputMultiPath, Str, isdefined)


class NighresBaseInterface(LibraryBaseInterface):
    _pkg = 'nighres'

    def _list_outputs(self):

        outputs = {}

        for key in self._results:
            outputs[key] = self._results[key].get_filename()

        return outputs

    def _get_inputs(self, skip=None):
        
        inputs = self.inputs.get()

        for key in inputs:
            if not isdefined(inputs[key]):
                inputs[key] = None
        
        return inputs
        

class MP2RAGESkullStripInputSpec(BaseInterfaceInputSpec):

    second_inversion = File(exists=True,
                            mandatory=True,
                            desc='Second inversion image derived from MP2RAGE sequence')
    t1_weighted = File(exists=True,
                       mandatory=True,
                       desc='T1-weighted image derived from MP2RAGE sequence'
                            ' (also referred to as “uniform” image) At least one of'
                            ' t1_weighted and t1_map is required')

    t1_map = File(exists=True,
                  mandatory=True,
                  desc='Quantitative T1 map image derived from MP2RAGE'
                        'sequence At least one of t1_weighted and t1_map is required',)

    skip_zero_values = traits.Bool(True,
                                   use_defaul=True, 
                                   desc='Ignores voxels with zero value (default is True)')
    
    topology_lut_dir = Directory(desc='Path to directory in which topology files '
                                      'are stored (default is stored in TOPOLOGY_LUT_DIR)')
    
    prefix = Str(desc='Prefix of the resulting filenames')


class MP2RAGESkullStripOutputSpec(TraitedSpec):
    brain_mask = File(
        exists=True,
        desc='Binary brain mask (_strip_mask)')

    inv2_masked = File(
        exists=True,
        desc='Masked second inversion imamge (_strip_inv2)')

    t1w_masked = File(
        exists=True,
        desc='Masked T1-weighted image (_strip_t1w)')

    t1map_masked = File(
        exists=True,
        desc='Masked T1 map (_strip_t1map)')

class MP2RAGESkullStrip(NighresBaseInterface, SimpleInterface):

    input_spec = MP2RAGESkullStripInputSpec
    output_spec = MP2RAGESkullStripOutputSpec

    def _run_interface(self, runtime):
        from nighres.brain import mp2rage_skullstripping  

        output_dir = runtime.cwd

        self._results = mp2rage_skullstripping(self.inputs.second_inversion,
                                         self.inputs.t1_weighted,
                                         self.inputs.t1_map,
                                         save_data=True,
                                         output_dir=output_dir)


        return runtime

class MGDMSegmentationInputSpec(BaseInterfaceInputSpec):

    contrast_image1 = File(
        exists=True,
        mandatory=True,
        desc='First input image to perform segmentation on')

    contrast_type1 = Str(
        mandatory=True,
        desc='Contrast type of first input image, must be listed as a prior in used'
             'atlas(specified in atlas_file)')

    contrast_image2 = File(
        exists=True,
        mandatory=False,
        desc='Second input image to perform segmentation on')
    contrast_type2 = Str(
        None,
        usedefault=True, 
        mandatory=True,
        desc='Contrast type of second input image, must be listed as a prior in used'
             'atlas(specified in atlas_file)')

    contrast_image3 = File(
        None,
        usedefault=True,
        exists=True,
        mandatory=False,
        desc='Third input image to perform segmentation on')
    contrast_type3 = Str(
        mandatory=False,
        desc='Contrast type of third input image, must be listed as a prior in used'
             'atlas(specified in atlas_file)')

    contrast_image4 = File(
        exists=True,
        mandatory=False,
        desc='Fourth input image to perform segmentation on')
    contrast_type4 = Str(
        mandatory=False,
        desc='Contrast type of fourth input image, must be listed as a prior in used'
             'atlas(specified in atlas_file)')

    n_steps = traits.Int(
        default=5,
        usedefault=True,
        desc='Number of steps for MGDM (default is 5, set to 0 for quick testing of '
             'registration of priors, which does not perform true segmentation).')

    max_iterations = traits.Int(
        default=800,
        usedefault=True,
        desc='Maximum number of iterations per step for MGDM (default is 800, set '
             'to 1 for quick testing of registration of priors, which does not '
             'perform true segmentation')

    topology = traits.Enum('wcs', 'no',
        default='wcs',
        usedefault=True,
        desc='Topology setting, choose "wcs" (well-composed surfaces) for strongest '
             'topology constraint, "no" for no topology constraint (default is "wcs")')

    atlas_file = File(
        mandatory=False,
        desc='Path to plain text atlas file (default is stored in DEFAULT_ATLAS) '
             'or atlas name to be searched in ATLAS_DIR')

class MGDMSegmentationOutputSpec(TraitedSpec):

    segmentation = File(
        exists=True,
        desc='Hard brain segmentation with topological '
             'constraints (if chosen) (_mgdm_seg)')

    labels = File(
        exists=True,
        desc='Maximum tissue probability labels (_mgdm_lbls)')

    memberships = File(
        exists=True,
        desc='Maximum tissue probability values, 4D image '
             'where the first dimension shows each voxel\'s highest probability to '
             'belong to a specific tissue, the second dimension shows the second '
             'highest probability to belong to another tissue etc. (_mgdm_mems)')
    
    distance = File(
        exists=True,
        desc='distance (niimg): Minimum distance to a segmentation boundary (_mgdm_dist)')


class MGDMSegmentation(NighresBaseInterface, SimpleInterface):

    input_spec = MGDMSegmentationInputSpec
    output_spec = MGDMSegmentationOutputSpec

    def _run_interface(self, runtime):
        from nighres.brain import mgdm_segmentation  

        output_dir = runtime.cwd

        settings = self._get_inputs()
        
        self._results = mgdm_segmentation(save_data=True,
                                          overwrite=True,
                                          output_dir=runtime.cwd,
                                          **settings)

        self._list_outputs()

        return runtime

class MP2RAGEDuraEstimationInputSpec(BaseInterfaceInputSpec):


    second_inversion = File(
        mandatory=True,
        desc='Second inversion image derived from MP2RAGE sequence')

    skullstrip_mask = File(
        mandatory=True,
        desc='Skullstripping mask defining the approximate region including the brain')

    background_distance = traits.Float(
        5,
        usedefault=True,
        desc='Maximum distance within the mask for dura (default is 5.0 mm)')

    output_type = traits.Enum(
        'dura_region',
        'boundary',
        'dura_prior',
        'bg_prior',
        'intens_prior',
        default='dura_region',
        usedefault=True,
        desc='Type of output result (default is "dura_region")')



class MP2RAGEDuraEstimationOutputSpec(TraitedSpec):

    result = File(
        exists=True,
        desc='Output of MP2RAGEDuraEstimation (dura_region, boundary, '
             'dura_prior, bg_prior or intens_prior)')





class MP2RAGEDuraEstimation(NighresBaseInterface, SimpleInterface):

    input_spec = MP2RAGEDuraEstimationInputSpec
    output_spec = MP2RAGEDuraEstimationOutputSpec

    def _run_interface(self, runtime):
        from nighres.brain import mp2rage_dura_estimation  

        self._results = mp2rage_dura_estimation(
                            self.inputs.second_inversion,
                            self.inputs.skullstrip_mask,
                            self.inputs.background_distance,
                            self.inputs.output_type,
                            save_data=True,
                            overwrite=True,
                            output_dir=runtime.cwd)

        self._list_outputs()

        return runtime

class ExtractBrainRegionInputSpec(BaseInterfaceInputSpec):

    segmentation = File(
        mandatory=True,
        desc='Segmentation result from MGDM.') 

    levelset_boundary = File(
        mandatory=True,
        desc='Levelset boundary from MGDM.') 

    maximum_membership = File(
        mandatory=True,
        desc='4D image of the maximum membership values from MGDM.')

    maximum_label = File(
        mandatory=True,
        desc='4D imageof the maximum labels from MGDM.')

    atlas_file = File(
        desc='Path to plain text atlas file (default is stored in DEFAULT_ATLAS).'
             'or atlas name to be searched in ATLAS_DIR')

    extracted_region = traits.Enum(
            'left_cerebrum',
            'right_cerebrum',
            'cerebrum',
            'cerebellum',
            'cerebellum_brainstem',
            'subcortex',
            'tissues(anat)',
            'tissues(func)',
            'brain_mask',
            desc='Region to be extracted from the MGDM segmentation.')

    normalize_probabilities = traits.Bool(
        False,
        usedefault=True,
        desc='Whether to normalize the output probabilities to sum to 1'
             '(default is False).')
    
    estimate_tissue_densities = traits.Bool(
        False,
        usedefault=True,
        desc='Wheter to recompute partial volume densities from the probabilites'
             '(slow, default is False).')

    partial_volume_distance = traits.Float(
        1.0,
        usedefault=True,
        desc='Distance in mm to use for tissues densities, if recomputed'
             '(default is 1mm).')

class ExtractBrainRegionOutputSpec(TraitedSpec):
        
    region_mask = File(
        exists=True,
        desc='Hard segmentation mask of the (GM) region '
             'of interest (_xmask_#gm)')

    inside_mask = File(
        exists=True,
        desc='Hard segmentation mask of the (WM) inside of'
             'the region of interest (_xmask_#wm)')

    background_mask  = File(
        exists=True,
        desc='Hard segmentation mask of the (CSF) region '
             'background (_xmask_#bg)')

    region_proba = File(
        exists=True,
        desc='Probability map of the (GM) region '
             'of interest (_xproba_#gm)')

    inside_proba = File(
        exists=True,
        desc='Probability map of the (WM) inside of '
             'the region of interest (_xproba_#wm)')

    background_proba = File(
        exists=True,
        desc='Probability map of the (CSF) region '
             'background (_xproba_#bg)')

    region_lvl = File(
        exists=True,
        desc='Levelset surface of the (GM) region '
             'of interest (_xlvl_#gm)')

    inside_lvl = File(
        exists=True,
        desc='Levelset surface of the (WM) inside of '
             'the region of interest (_xlvl_#wm)')

    background_lvl = File(
        exists=True,
        desc='Levelset surface of the (CSF) region'
             'background (_xlvl_#bg)')

class ExtractBrainRegion(NighresBaseInterface, SimpleInterface):

    input_spec = ExtractBrainRegionInputSpec
    output_spec = ExtractBrainRegionOutputSpec

    def _run_interface(self, runtime):
        from nighres.brain import extract_brain_region  

        settings = self._get_inputs()
        self._results = extract_brain_region(save_data=True,
                                             overwrite=True,
                                             output_dir=runtime.cwd,
                                             **settings)

        self._list_outputs()

        return runtime

class CRUISECortexExtractionInputSpec(BaseInterfaceInputSpec):

    init_image = File(
        mandatory=True,
        exists=True,
        desc='Initial white matter (WM) segmentation mask (binary mask>0 inside WM)')

    wm_image = File(
        mandatory=True,
        exists=True,
        desc='Filled WM probability map (values in [0,1], including subcortical GM '
             'and ventricles)')

    gm_image = File(
        mandatory=True,
        exists=True,
        desc='Cortical gray matter (GM) probability map (values in [0,1], highest '
             'inside the cortex)')

    csf_image = File(
        mandatory=True,
        exists=True,
        desc='Sulcal cerebro-spinal fluid (CSf) and background probability map '
             '(values in [0,1], highest in CSf and masked regions)')

    vd_image = File(
        exists=True,
        desc='Additional probability map of vessels and dura mater to be excluded')

    data_weight = traits.Float(
        0.4,
        usedefault=True,
        desc='Weighting of probability-based balloon forces in CRUISE (default 0.4, '
             'sum of {data_weight,regularization_weight} should be below or equal '
             'to 1)')

    regularization_weight = traits.Float(
        0.1,
        usedefault=True,
        desc='Weighting of curvature regularization forces in CRUISE (default 0.1, '
             'sum of {data_weight,regularization_weight} should be below or equal '
             'to 1)')

    max_iterations = traits.Int(
        500,
        usedefault=True,
        desc='Maximum number of iterations in CRUISE (default is 500)')

    normalize_probabilities = traits.Bool(
        False,
        usedefault=True,
        desc='Whether to normalize the wm, gm, and csf probabilities '
             '(default is False)')
        
    correct_wm_pv = traits.Bool(
        True,
        usedefault=True,
        desc='Whether to correct for WM partial voluming in gyral crowns '
             '(default is True)')

    wm_dropoff_dist = traits.Float(
        1.0,
        usedefault=True,
        desc='Distance parameter to lower WM probabilities away from current '
             'segmentation (default is 1.0 voxel)')

    topology = traits.Enum( 'wcs', 'no',
        default='wcs',
        usedefault=True,
        desc='Topology setting, choose "wcs" (well-composed surfaces) for strongest '
             'topology constraint, "no" for no topology constraint (default is "wcs")')

    topology_lut_dir = Directory(desc='Path to directory in which topology files '
                                      'are stored (default is stored in TOPOLOGY_LUT_DIR)')

class CRUISECortexExtractionOutputSpec(TraitedSpec):

    cortex = File(
        exists=True,
        desc='Hard segmentation of the cortex with labels '
             'background=0, gm=1, and wm=2 (_cruise_cortex)')

    gwb = File(
        exists=True,
        desc='Gray-White matter Boundary (GWB) level set function (_cruise_gwb)')

    
    cgb = File(
        exists=True,
        desc='CSF-Gray matter Boundary (CGB) level set function (_cruise_cgb)')

    avg = File(
        exists=True,
        desc='Central level set function, obtained as geometric '
             'average of GWB and CGB (*not* the middle depth of the '
             'cortex, use volumetric_layering if you want accurate '
             'depth measures) (_cruise_avg)')
    thickness = File(
        exists=True,
        desc='Simple cortical thickness estimate: distance to '
             'the GWB and CGB surfaces, in mm (_cruise_thick)')

    pwm = File(
        exists=True,
        desc='Optimized WM probability, including partial volume and '
             'distant values correction (_cruise_pwm)')

    pgm = File(
        exists=True,
        desc='Optimized GM probability, including CSF sulcal ridges '
             'correction (_cruise_pgm)')

    pcsf = File(
        exists=True,
        desc='Optimized CSF probability, including sulcal ridges and '
             'vessel/dura correction (_cruise_pwm)')

class CRUISECortexExtraction(NighresBaseInterface, SimpleInterface):

    input_spec = CRUISECortexExtractionInputSpec
    output_spec = CRUISECortexExtractionOutputSpec

    def _run_interface(self, runtime):
        from nighres.cortex import cruise_cortex_extraction  

        settings = self._get_inputs()
        self._results = cruise_cortex_extraction(save_data=True,
                                                overwrite=True,
                                                 output_dir=runtime.cwd,
                                                 **settings)

        self._list_outputs()

        return runtime


class VolumetricLayeringInputSpec(BaseInterfaceInputSpec):

    inner_levelset = File(
        mandatory=True,
        exists=True,
        desc='Levelset representation of the inner surface, typically GM/WM surface')

    outer_levelset = File(
        mandatory=True,
        exists=True,
        desc='Levelset representation of the outer surface, typically GM/CSF surface')

    n_layers = traits.Int(
        mandatory=False,
        desc='Number of layers to be created (default is 10)')

    topology_lut_dir = Directory(desc='Path to directory in which topology files '
                                      'are stored (default is stored in TOPOLOGY_LUT_DIR)')


class VolumetricLayeringOutputSpec(TraitedSpec):

    depth = File(
        exists=True,
        desc='Continuous depth from 0 (inner surface) to 1 '
             '(outer surface) (_layering_depth)')

    layers = File(
        exists=True,
        desc='Discrete layers from 1 (bordering inner surface) to '
             'n_layers (bordering outer surface) (_layering_layers)')

    boundaries = File(
        exists=True,
        desc='Levelset representations of boundaries between '
             'all layers in 4D (_layering_boundaries)')

class VolumetricLayering(NighresBaseInterface, SimpleInterface):

    input_spec = VolumetricLayeringInputSpec
    output_spec = VolumetricLayeringOutputSpec

    def _run_interface(self, runtime):
        from nighres.laminar import volumetric_layering  

        settings = self._get_inputs()
        self._results = volumetric_layering(save_data=True,
                                            overwrite=True,
                                            output_dir=runtime.cwd,
                                            **settings)

        self._list_outputs()

        return runtime
