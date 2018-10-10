import argparse
import os
from bids.grabbids import BIDSLayout
from nilearn import image
from spynoza.utils import average_over_runs


def main(sourcedata,
         derivatives,
         subject,
         session,
         onefield,
         tmp_dir):

    if onefield:
        derivatives = os.path.join(derivatives, 'onefield')

    sourcedata_layout = BIDSLayout(sourcedata)
    sourcedata_df = sourcedata_layout.as_data_frame()
    events =  sourcedata_df[(sourcedata_df['type'] == 'events') &
                               (sourcedata_df['subject'] == subject) &
                               (sourcedata_df['session'] == session)]

    derivatives_layout = BIDSLayout(os.path.join(derivatives, 'spynoza'))
    derivatives_df = derivatives_layout.as_data_frame()
    bold =  derivatives_df[(derivatives_df['type'] == 'preproc') &
                               (derivatives_df['subject'] == subject) &
                               (derivatives_df['session'] == session)]

    mask = derivatives_layout.get(subject=subject,
                                  session=session,
                                  type='mask',
                                  return_type='file')[0]

    row = bold.iloc[0]

    results_dir = os.path.join(derivatives, 
                               'average_timeseries', 
                               'sub-{}'.format(row['subject']))
    os.makedirs(results_dir, exist_ok=True)

    av_bold_fn = os.path.join(results_dir, 'sub-{}_ses-{}_bold_psc_average.nii.gz'.format(row['subject'], row['session']))
    av_bold = average_over_runs(bold.path.tolist(), output_filename=av_bold_fn)

    av_bold = image.math_img('(av_bold / av_bold.mean(-1)[..., np.newaxis]) * 100', av_bold=av_bold)
    av_bold.to_filename(av_bold_fn)

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("subject", 
                        #nargs='?',
                        type=str,
                        help="subject to process")
    parser.add_argument("session", 
                        type=str,
                        default='*',
                        help="subject to process")
    parser.add_argument("--onefield", 
                        dest='onefield',
                        action='store_true')
    parser.set_defaults(onefield=False)
    args = parser.parse_args()

    main('/sourcedata', 
         '/derivatives',
         subject=args.subject,
         session=args.session,
         onefield=args.onefield,
         tmp_dir='/workflow_folders')

