import argparse
import cortex
import os.path as op
import pickle as pkl
import numpy as np
import pandas as pd

def main(derivatives,
         subject):

    coordinates = []
    for hemi in ['lh', 'rh']:
        coordinates.append(pd.read_pickle(op.join(derivatives,
                                                  'coordinate_patches',
                                                  'sub-{subject}',
                                                  'anat',
                                                  'sub-{subject}_hemi-{hemi}_coordinatepatch.pkl').format(**locals())))


    coordinates = pd.concat(coordinates, axis=0, ignore_index=True)
    print(coordinates.shape)
    print(coordinates.head())
    print(coordinates['x'].dtype)

    x = cortex.Vertex(coordinates['x'].values, 'odc.{}'.format(subject),
                      cmap='BROYG', vmin=-35, vmax=35)
    y = cortex.Vertex(coordinates['y'].values, 'odc.{}'.format(subject),
                      cmap='BROYG', vmin=-35, vmax=35)
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
