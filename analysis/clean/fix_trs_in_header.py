import nibabel as nb
import os
import sys
from bids.layout import BIDSLayout
import shutil

def main(bids_dir, subject):

    print(subject, bids_dir)
    layout = BIDSLayout(bids_dir, absolute_paths=True)
    bolds = layout.get(subject=subject, 
                       extensions='nii', type='bold')

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
    if 'DATA_DIR' in os.environ:
        data_dir = os.environ['DATA_DIR']
    else:
        data_dir = '/data'

    if len(sys.argv) > 1:
        subject = sys.argv[1]
    else:
        subject = None

    main(os.path.join(data_dir, 'sourcedata'), subject)

