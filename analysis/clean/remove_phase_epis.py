import glob
from bids import BIDSLayout
import os, sys
from nilearn import image
import nibabel as nb
import numpy as np
import argparse

LENGTH_EPI = 10
LENGTH_BOLD = 132


def main(sourcedata, 
         subject,
         session,
         length_epi,
         length_bold):
    print('Fixing subject {} in {} ({}. {})'.format(subject,
                                                    sourcedata,
                                                    length_epi,
                                                    length_bold))

    layout = BIDSLayout(sourcedata)

    LENGTH_EPI = length_epi
    LENGTH_BOLD = length_bold

    epis = layout.get(subject=subject,
                      session=session,
                      extensions='nii',
                      suffix='epi')

    for epi in epis:
        epi_im = nb.load(epi.filename)

        if epi_im.shape[-1] == LENGTH_EPI:
            print('Correcting {}'.format(epi.filename))
            index = np.zeros(LENGTH_EPI, dtype=bool)
            #index[:int(LENGTH_EPI/2)] = True
            index[::2] = True
            new_im = image.index_img(epi_im, index)
            print(new_im.shape)
            new_im.to_filename(epi.filename)


    bolds = layout.get(subject=subject,
                       session=session,
                       extensions='nii',
                       suffix='bold')

    for bold in bolds:
        bold_im = nb.load(bold.filename)

        if bold_im.shape[-1] == LENGTH_BOLD:
            print('Correcting {}'.format(bold.filename))
            index = np.zeros(LENGTH_BOLD, dtype=bool)
            #index[:int(LENGTH_BOLD/2)] = True
            index[::2] = True
            new_im = image.index_img(bold_im, index)
            print(new_im.shape)
            new_im.to_filename(bold.filename)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("subject", 
                        help="subject to process")
    parser.add_argument("session", 
                        default='*',
                        help="Session to process")
    parser.add_argument("length_epi", 
                        default=10, #or 16 for prf
                        nargs='?',
                        type=int,
                        help="Length of EPIs to correct")
    parser.add_argument("length_bold", 
                        default=132, # or 236 for prf
                        nargs='?',
                        type=int,
                        help="Length of BOLDs to correct")
    args = parser.parse_args()

    main('/sourcedata/ds-odc', 
         subject=args.subject,
         session=args.session,
         length_epi=args.length_epi,
         length_bold=args.length_bold)

