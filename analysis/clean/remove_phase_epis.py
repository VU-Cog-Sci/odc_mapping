import glob
from bids.grabbids import BIDSLayout
import os, sys
from nilearn import image
import nibabel as nb
import numpy as np

LENGTH_EPI = 10
LENGTH_BOLD = 132


def main(sourcedata, subject):
    print('Fixing subject {} in {}'.format(subject, sourcedata))

    layout = BIDSLayout(sourcedata)

    epis = layout.get(subject=subject,
                      extensions='nii',
                      type='epi')

    for epi in epis:
        epi_im = nb.load(epi.filename)

        if epi_im.shape[-1] == LENGTH_EPI:
            print('Correcting {}'.format(epi.filename))
            index = np.zeros(LENGTH_EPI, dtype=bool)
            index[:LENGTH_EPI/2] = True
            new_im = image.index_img(epi_im, index)
            print(new_im.shape)
            new_im.to_filename(epi.filename)


    bolds = layout.get(subject=subject,
                       extensions='nii',
                       type='bold')

    for bold in bolds:
        bold_im = nb.load(bold.filename)

        if bold_im.shape[-1] == LENGTH_BOLD:
            print('Correcting {}'.format(bold.filename))
            index = np.zeros(LENGTH_BOLD, dtype=bool)
            index[:int(LENGTH_BOLD/2)] = True
            new_im = image.index_img(bold_im, index)
            print(new_im.shape)
            new_im.to_filename(bold.filename)

if __name__ == '__main__':

    if len(sys.argv) < 2:
        raise Exception('Please provide subject')

    main('/sourcedata',
         subject=sys.argv[1])
