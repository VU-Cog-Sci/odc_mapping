import argparse
import os.path as op
import yaml
import cortex
import pickle as pkl
import os
import numpy as np
import pandas as pd

def main(derivatives,
         subject):

    with open(op.abspath('coordinate_vertices.yml')) as f:
        db = yaml.load(f)

    if 'sub-{}'.format(subject) not in db:
        raise Exception('Subject {} not present in coordinate_vertices.yml'.format(subject))

    meta = db['sub-{}'.format(subject)]

    left, right = cortex.db.get_surf('odc.{}'.format(subject), 'fiducial')

    surfaces = {}
    surfaces['lh'] = cortex.polyutils.Surface(left[0], left[1])
    surfaces['rh'] = cortex.polyutils.Surface(right[0] , right[1])


    for hemisphere in ['lh', 'rh']:
        patch = surfaces[hemisphere].get_geodesic_strip_patch(v0=meta[hemisphere]['start'],
                                                             v1=meta[hemisphere]['end'],
                                                             m=2.5,
                                                             method='whole_surface',
                                                             radius=20)

        xy = pd.DataFrame({'x':patch['coordinates'][0, :],
                           'y':patch['coordinates'][1, :]})

        # Subsurface is non-pickable
        ss = patch.pop('subsurface', None)

        #patch_indices = xy[patch['vertex_mask']].index
        #patch['distances'] = np.array([ss.geodesic_distance(ss.subsurface_vertex_map[ix]) for ix in patch_indices])

        # rows correspond to centers of coordinate system
        #patch['vertexwise_coordinate_system'] = (xy.loc[patch_indices].values[np.newaxis, :, :] - xy.loc[patch_indices].values[:, np.newaxis, :])


        target_dir = op.join(derivatives, 'coordinate_patches', 'sub-{subject}', 'anat').format(**locals())

        if not op.exists(target_dir):
            os.makedirs(target_dir)

        with open(op.join(target_dir,
                          'sub-{subject}_hemi-{hemisphere}_coordinatepatch.pkl').format(**locals()),
                  'wb') as f:
            pkl.dump(patch, f, protocol=4)

        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("subject", 
                        type=str,
                        help="subject to process")

    args = parser.parse_args()

    main('/derivatives',
         subject=args.subject)
