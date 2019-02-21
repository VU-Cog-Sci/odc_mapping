import numpy as np
import pandas as pd
from stim import create_visual_designmatrix_all, create_bd_designmatrix_all
from popeye.visual_stimulus import VisualStimulus
import popeye.utilities as utils
import ctypes
from scipy.signal import fftconvolve, resample

distance_screen = 15
size_cm = 6
TR = 2.7
n_pixels = 50

df = pd.read_table('/data/odc/sourcedata/sub-de/ses-prf/beh/sub-de_ses-odc1_task-prf_run-01.tsv', index_col=0).iloc[1:]
df['direction'] = df.apply(lambda row: row.bar_direction if row.stim_bool else -1,1)

total_duration = df.bar_pass_duration.sum()

dms = []

for ix, row in df.iterrows():
    dm = create_visual_designmatrix_all(bar_width=0.125, 
                                        iti_duration=0, 
                                        thetas=[row.direction], 
                                        n_pixels=n_pixels,
                                        nr_timepoints=row.bar_pass_duration) # Note that we make a design matrix at level of seconds
    
    dms.append(dm)
    
dm = np.concatenate(dms, -1)


stimulus = VisualStimulus(dm, distance_screen, size_cm, 0.50, 1.0, ctypes.c_int16)

hrf = utils.spm_hrf(0, 1.)
bold_dm = fftconvolve(stimulus.stim_arr, hrf[np.newaxis, np.newaxis, :], 'full')

bold_dm = np.moveaxis(bold_dm, -1, 0)[:total_duration]
bold_dm = resample(bold_dm, int(total_duration/TR), axis=0)

np.savetxt('/data/odc/derivatives/prf/dm.txt', dm.reshape(-1, n_pixels**2))
np.savetxt('/data/odc/derivatives/prf/bold_dm.txt', bold_dm.reshape(-1, n_pixels**2))

np.save('/data/odc/derivatives/prf/dm.npy', dm)

