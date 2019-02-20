import nibabel as nb
import os
import sys
from bids import BIDSLayout
import shutil
import argparse

def main(bids_dir, subject, session):

    print(subject, bids_dir)
    layout = BIDSLayout(bids_dir)
    bolds = layout.get(subject=subject, 
                       session=session,
                       extensions='nii', suffix='bold')

    for bold in bolds:
        print(bold.filename)
        im = nb.load(bold.filename)
        zooms = list(im.header.get_zooms())
        units  = list(im.header.get_xyzt_units())

        if (zooms[-1] != layout.get_metadata(bold.filename)['RepetitionTime']) or (units[1] != 's'):
            im.header.set_xyzt_units(t=8) # 8 = seconds

            zooms[-1] = layout.get_metadata(bold.filename)['RepetitionTime']
            im.header.set_zooms(zooms)
            print(im.get_filename())
            nb.save(im, im.get_filename()+'.new.nii')
            shutil.move(bold.filename+'.new.nii', bold.filename)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("subject", 
                        help="subject to process")
    parser.add_argument("session", 
                        default='*',
                        help="Session to process")
    args = parser.parse_args()

    main('/sourcedata/ds-odc', 
         subject=args.subject,
         session=args.session)

