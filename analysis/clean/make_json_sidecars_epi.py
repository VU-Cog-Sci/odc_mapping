import os
from bids.layout import BIDSLayout
import sys
import json

def main(bids_dir, subject=None):
    
    print(subject, bids_dir)
    layout = BIDSLayout(bids_dir, absolute_paths=False)
    bolds = layout.get(subject=subject, 
                       extensions='nii', 
                       type='bold')
    
    for bold in bolds:
        epi = layout.get(type='epi',
                         subject=subject,
                         extensions='nii',
                         run=bold.run)
        assert(len(epi) == 1)
        epi = epi[0]

        json_d = {'PhaseEncodingDirection':'i',
                  'TotalReadoutTime':0.04, 
                  'IntendedFor':bold.filename.replace('sub-{}/'.format(subject), '')}

        print(json_d)

        json_filename = os.path.join(layout.root,
                                     epi.filename.replace("nii", "json"))
        print(json_filename)

        with open(json_filename, 'w') as f:
            json.dump(json_d, f)


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

