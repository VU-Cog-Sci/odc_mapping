# This uses the master-branch of Gilles86 that can deal
# with T1w data that is not 1mm isotropic at 256x256x256
# 
import cortex
import cortex.fmriprep
import argparse
import os
import os.path as op
from utils import get_bids_file
import numpy as np
from nilearn import image

def main(sourcedata,
         derivatives,
         subject,
         session):
    out_dir = op.join(derivatives, 
                          'pycortex',
                          'sub-{}'.format(subject)) 

    for version in ['light', 'full']:
        d = op.join(out_dir, version)
        if not op.exists(d):
            os.makedirs(d)
    
    if subject not in cortex.db.subjects:
        cortex.fmriprep.import_subj(subject, '/derivatives', None, dataset='odc')

    pc_subject = 'odc.{}'.format(subject)

    images = {}
    t1w = get_bids_file(derivatives, 'averaged_mp2rages', 'anat',
                         subject, 'T1w', session, 'average')
    images['t1w'] = cortex.Volume(t1w, pc_subject, 'identity', vmin=0, vmax=4095)

    t1map = get_bids_file(derivatives, 'averaged_mp2rages', 'anat',
                           subject, 'T1map', session, 'average')
    images['t1map'] = cortex.Volume(t1map, pc_subject, 'identity', vmin=1000, vmax=2200)

    t2starmap = get_bids_file(derivatives, 'qmri_memp2rages', 'anat',
                            subject, 't2starmap', session, 'average')
    images['t2starmap'] = cortex.Volume(t2starmap, pc_subject, 'identity', vmin=10, vmax=60)

    s0 = get_bids_file(derivatives, 'qmri_memp2rages', 'anat',
                            subject, 'S0', session, 'average')
    images['s0'] = cortex.Volume(s0, pc_subject, 'identity')


    for echo_ix in range(1,5):
        echo = get_bids_file(sourcedata, '', 'anat', subject, 'MPRAGE',
                              session='anat', acquisition='memp2rage', echo=echo_ix,
                              inversion=2, part='mag')
        if echo_ix == 1:
            transform = cortex.xfm.Transform(np.identity(4), echo)
            transform.save(subject, 'memp2rage')
            max_first_echo = np.percentile(image.load_img(echo).get_data(), 95)
        images['echo{}'.format(echo_ix)] = cortex.Volume(echo, 
                                                         pc_subject, 
                                                         'memp2rage',
                                                         vmin=0,
                                                         vmax=max_first_echo)
    ds = cortex.Dataset(t1map=images['t1map'],
                        s0=images['s0'],
                        t2starmap=images['t2starmap'])
                                     
    cortex.webgl.make_static(op.join(out_dir, 'light'), ds)
    cortex.webshow(ds)

    ds = cortex.Dataset(**images)
    cortex.webgl.make_static(op.join(out_dir, 'full'), ds)
    cortex.webshow(ds)

 




if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("subject", 
                        #nargs='?',
                        type=str,
                        help="subject to process")
    args = parser.parse_args()

    main('/data/odc/sourcedata', 
         '/data/odc/derivatives',
         subject=args.subject,
         session='anat')

