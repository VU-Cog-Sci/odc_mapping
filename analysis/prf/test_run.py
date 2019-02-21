import argparse
from utils import get_voxel_data, get_vertex_data
import numpy as np
from prf import PRFGridSearch
import os.path as op
import numpy as np
from scipy import signal

derivatives = '/data/odc/derivatives'
subject = 'ms'
session = 'prf'

distance_screen=15
size_cm=6
TR=2.7
n_pixels=50

dm = np.load(op.join(derivatives, 'prf/dm.npy'))

dm = signal.resample(dm, 118, axis=-1)

grid_searcher = PRFGridSearch(dm, distance_screen, size_cm, 1.0)

eccs = np.hstack(([0], np.geomspace(.1, 30, 10)))
angles = np.linspace(-np.pi, np.pi, 16, endpoint=False)
sizes = np.geomspace(.1, 30, 10)

print('making predictions')
grid_searcher.make_predictions(angles, eccs, sizes)


print('loading data')
#data = np.load('/data/odc/zooi/bm.npy')
#data = np.load('/data/odc/zooi/de.npy')
data = np.load('/data/odc/zooi/ms_prf.npy')
#data = get_vertex_data(derivatives,
                       #subject,
                       #session)
#np.save('/data/odc/zooi/ms_prf.npy', data)

data = np.mean(data, 0)
mask = (data != 0).all(0)

print('searching')
pars = grid_searcher.fit(data[:, mask],
                         include_predictions=True)

#return pars

r2 = np.zeros(data.shape[1])
size = np.zeros(data.shape[1])
angle = np.zeros(data.shape[1])
ecc = np.zeros(data.shape[1])

r2[mask] = pars['r2']
size[mask] = pars['size']
angle[mask] = pars['angle']
ecc[mask] = pars['ecc']

results = pars
results = results[results.r2 > .3]

r = grid_searcher.refine_parameters(results)
