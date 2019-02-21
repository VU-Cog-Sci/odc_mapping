from popeye.visual_stimulus import VisualStimulus
from popeye import og, dog
import popeye.utilities as utils
import numpy as np
import os.path as op
from scipy import signal
import ctypes
from popeye.visual_stimulus import VisualStimulus, simulate_bar_stimulus

derivatives = '/data/odc/derivatives'

v = np.load('/data/odc/zooi/tr_prf.npy')
data = np.mean(v, 0)
data = data[:, (data != 0).all(0)]

dm = np.load(op.join(derivatives, 'prf/dm.npy'))
dm = signal.resample(dm, 318, axis=-1)

viewing_distance=15
screen_width=6
TR=2.7
n_pixels=50

sweeps = np.array([-1,45,135,-1,225,315,-1]) # in degrees, -1 is blank
#stimulus = VisualStimulus(stim_arr=dm,
                    #viewing_distance=viewing_distance,
                    #screen_width=screen_width,
                    #scale_factor=1,
                    #tr_length=1.0,
                    #dtype=np.short)
bar = simulate_bar_stimulus(100, 100, 40, 40, sweeps, 30, 30, 20, 0.67)
stimulus = VisualStimulus(bar, 50, 25, 0.50, 1.0, ctypes.c_int16)

model= og.GaussianModel(stimulus, utils.double_gamma_hrf)
model.hrf_delay = 0

pars = dict(np.load('/data/odc/derivatives/voxel_prf/modelfree/sub-tr_desc-None_prf_pars.npz'))

x =  np.cos(pars['angle']) * pars['ecc']
y =  np.cos(pars['angle']) * pars['ecc']


### FIT
## define search grids
# these define min and max of the edge of the initial brute-force search. 
x_grid = (-10,10)
y_grid = (-10,10)
s_grid = (1/stimulus.ppd + 0.25,5.25)
h_grid = (-1.0,1.0)

## define search bounds
# these define the boundaries of the final gradient-descent search.
x_bound = (-12.0,12.0)
y_bound = (-12.0,12.0)
s_bound = (1/stimulus.ppd, 12.0) # smallest sigma is a pixel
b_bound = (1e-8,None)
u_bound = (None,None)
h_bound = (-3.0,3.0)

    
## package the grids and bounds
grids = (x_grid, y_grid, s_grid)
bounds = (x_bound, y_bound, s_bound, h_bound, b_bound, u_bound,)
# fit
#fit = dog.DifferenceOfGaussiansFit(model, data, grids, bounds, Ns=5,
                 #voxel_index=(1,2,3), auto_fit=True, verbose=1)        
# fit
fit = og.GaussianFit(model, data[:, 0], grids, bounds, Ns=4,
                 voxel_index=(1,2,3), auto_fit=True, verbose=0)
























import ctypes, multiprocessing
import numpy as np
import sharedmem
import popeye.og_hrf as og
import popeye.utilities as utils
from popeye.visual_stimulus import VisualStimulus, simulate_bar_stimulus

# seed random number generator so we get the same answers ...
np.random.seed(2764932)

### STIMULUS
## create sweeping bar stimulus
sweeps = np.array([-1,0,90,180,270,-1]) # in degrees, -1 is blank
bar = simulate_bar_stimulus(100, 100, 40, 20, sweeps, 30, 30, 10)

## create an instance of the Stimulus class
stimulus = VisualStimulus(bar, 50, 25, 0.50, 1.0, ctypes.c_int16)

### MODEL
## initialize the gaussian model
model = og.GaussianModel(stimulus, utils.double_gamma_hrf)

## generate a random pRF estimate
x = -5.24
y = 2.58
sigma = 1.24
hrf_delay = -0.25
beta = 0.55
baseline = -0.88

## create the time-series for the invented pRF estimate
data = model.generate_prediction(x, y, sigma, hrf_delay, beta, baseline)

## add in some noise
data += np.random.uniform(-data.max()/10,data.max()/10,len(data))

### FIT
## define search grids
# these define min and max of the edge of the initial brute-force search. 
x_grid = (-10,10)
y_grid = (-10,10)
s_grid = (1/stimulus.ppd + 0.25,5.25)
h_grid = (-1.0,1.0)

## define search bounds
# these define the boundaries of the final gradient-descent search.
x_bound = (-12.0,12.0)
y_bound = (-12.0,12.0)
s_bound = (1/stimulus.ppd, 12.0) # smallest sigma is a pixel
b_bound = (1e-8,None)
u_bound = (None,None)
h_bound = (-3.0,3.0)

## package the grids and bounds
grids = (x_grid, y_grid, s_grid, h_grid)
bounds = (x_bound, y_bound, s_bound, h_bound, b_bound, u_bound,)

## fit the response
# auto_fit = True fits the model on assignment
# verbose = 0 is silent
# verbose = 1 is a single print
# verbose = 2 is very verbose
fit = og.GaussianFit(model, data, grids, bounds, Ns=3,
                     voxel_index=(1,2,3), auto_fit=True,verbose=1)

## plot the results
import matplotlib.pyplot as plt
plt.plot(fit.prediction,c='r',lw=3,label='model',zorder=1)
plt.scatter(range(len(fit.data)),fit.data,s=30,c='k',label='data',zorder=2)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.xlabel('Time',fontsize=18)
plt.ylabel('Amplitude',fontsize=18)
plt.xlim(0,len(fit.data))
plt.legend(loc=0)

## multiprocess 3 voxels
data = [data,data,data]
indices = ([1,2,3],[4,6,5],[7,8,9])
bundle = utils.multiprocess_bundle(og.GaussianFit, model, data, 
                                   grids, bounds, indices, 
                                   auto_fit=True, verbose=1, Ns=3)
