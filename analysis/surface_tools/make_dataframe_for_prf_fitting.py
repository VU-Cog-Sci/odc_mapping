import argparse
from nilearn import surface
import glob
import os.path as op
import re
import pandas as pd

subject = 'tk'
derivatives = '/derivatives'

def main(derivatives, subject):

	fns = glob.glob(op.join(derivatives,
							'sampled_giis/sub-{subject}/ses-prf/func/sub-{subject}_ses-prf_task-prf_acq-*_run-*_desc-depth.*_hemi-*.gii').format(subject=subject))


	reg = re.compile('.*/sub-(?P<subject>.+)_ses-prf_task-prf_acq-(?P<acq>.+)_run-(?P<run>.+)_desc-depth(?P<depth>.+)_hemi-(?P<hemisphere>.+)\.gii')

	df = []
	n_vertices_left = 0
	for fn in fns:
		
		meta = reg.match(fn).groupdict()
		
		data = surface.load_surf_data(fn)
			
		if meta['hemisphere'] == 'lh':
			n_vertices_left = data.shape[0]
		
		data = pd.DataFrame(data[(data!=0).any(1)].T)
		
		for key in meta:
			data[key] = meta[key]
			
		data.index.names = ['frame']
		data.reset_index()
			
		df.append(data)

	df = pd.concat(df)

	df.index.name = 'frame'
	df = df.reset_index()

	df.columns.name = 'vertex'
	df = df.pivot_table(index=['subject', 'acq', 'run', 'frame'], columns=['hemisphere', 'depth'])
	df = df.swaplevel('hemisphere', 'vertex', axis=1).sort_index(axis=1)

	df.to_pickle(op.join(derivatives, 'sampled_giis', 'sub-{subject}', 'ses-prf', 'func', 'sub-{subject}_ses-prf_bold.pkl').format(**locals()))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("subject", 
                        type=str,
                        help="subject to process")
    parser.add_argument("session", 
                        type=str,
                        nargs='?',
                        default='prf',
                        help="subject to process")
    args = parser.parse_args()

    main('/derivatives',
         subject=args.subject)
         



