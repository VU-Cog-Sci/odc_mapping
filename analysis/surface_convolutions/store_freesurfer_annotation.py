import argparse
import cortex
import numpy as np
import nibabel as nb
import seaborn as sns
import os.path as op

def main(derivatives,
         subject):

    masks = cortex.utils.get_roi_verts('odc.{}'.format(subject), mask=True)

    left, right = cortex.db.get_surf('odc.{}'.format(subject), 'pia')

    colors = np.array(sns.color_palette()[:len(masks)]) * 255
    colors = np.vstack((np.array([[0, 0, 0]]), colors))
    colors = np.hstack((colors, np.zeros((colors.shape[0], 1))))


    names = []
    labels = np.zeros(len(left[0]) + len(right[0]), dtype=int)

    for ix, key in enumerate(masks):
        names.append(key)
        labels[masks[key]] = ix

    for hemi in ['lh', 'rh']:
        target_path = op.join(derivatives,
                              'freesurfer',
                              'sub-{}'.format(subject),
                              'label',
                              '{}.pycortex.annot'.format(hemi))

        
        if hemi == 'lh':
            nb.freesurfer.write_annot(target_path,
                                      labels[:len(left[0])],
                                      colors,
                                      names)
        else:
            nb.freesurfer.write_annot(target_path,
                                      labels[len(left[0]):],
                                      colors,
                                      names)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("subject", 
                        type=str,
                        help="subject to process")
    args = parser.parse_args()

    main('/data/odc/derivatives',
         subject=args.subject)
         



