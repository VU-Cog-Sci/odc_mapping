import argparse
import cortex
import os.path as op
import pickle as pkl
import numpy as np
import pandas as pd

def main(derivatives,
         subject):

    coordinates = []
    for hemi in ['lh', 'rh'][:1]:
        coordinates.append(pd.read_pickle(op.join(derivatives,
                                                  'coordinate_patches',
                                                  'sub-{subject}',
                                                  'anat',
                                                  'sub-{subject}_hemi-{hemi}_coordinatepatch.pkl').format(**locals())))

    coordinates = pd.concat(coordinates, axis=0, ignore_index=True)
    print(coordinates.shape)

    x = cortex.Vertex(coordinates['x'], 'odc.{}'.format(subject),
                      cmap='BROYG', vmin=10, vmax=60)
    y = cortex.Vertex(coordinates['y'], 'odc.{}'.format(subject),
                      cmap='BROYG',
                      vmin=-25, vmax=25)

    cortex.webshow(cortex.Dataset(x=x,
                                  y=y))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("subject", 
                        type=str,
                        help="subject to process")

    args = parser.parse_args()

    main('/data/odc/derivatives',
         subject=args.subject)
