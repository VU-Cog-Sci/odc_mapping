import numpy as np
from scipy.signal import savgol_filter, fftconvolve, resample
from sklearn.model_selection import LeaveOneOut
from sklearn import linear_model

class PRFRidgeModel(object):
    
    def __init__(self, 
                 bold_dm, 
                 data, 
                 window_length=51, 
                 polyorder=3):
        
        self.bold_dm = bold_dm
        self.data = np.array(data)
        self.n_runs, self.n_timepoints, self.n_vertices = self.data.shape
        self.bold_dm = self.bold_dm[:self.n_timepoints]


        self.mask = self.data.mean(0).sum(0) != 0
        
        self.loo = LeaveOneOut()
        
        
        if window_length is not None:
            if window_length % 2 == 0:
                window_length += 1
                
            self.data[..., self.mask] -= savgol_filter(self.data[..., self.mask], window_length, polyorder, axis=1)
            self.bold_dm -= savgol_filter(self.bold_dm, window_length, polyorder, axis=0)
        
        self.X_ = self.bold_dm.reshape(self.n_timepoints, -1)

    def fit(self, alpha=1.0):
        
        ridge = linear_model.Ridge(alpha=alpha)
        
        self.parameters = []
        self.predictions = []
        
        r = np.zeros((self.n_runs, self.n_vertices))
        
        for i, (train, test) in enumerate(self.loo.split(range(self.n_runs))):
            train_data = np.mean(self.data[train], 0)            
            test_data = np.mean(self.data[test], 0)

            x_ = self.X_
            
            
            ridge.fit(self.X_, train_data[:, self.mask])
            predictions = ridge.predict(self.X_)
            self.predictions.append(predictions)

            self.parameters.append(ridge.coef_)
            
            predictions_ = predictions - predictions.mean(0)
            test_data_ = test_data - test_data.mean(0)
            
            n = self.n_timepoints
            r[i, self.mask] = (np.sum(test_data_[:, self.mask]*predictions_, 0)/n) / (np.std(test_data[:, self.mask], 0)*np.std(predictions_, 0))

        r[np.isnan(r)] = 0
    
        
        self.predictions = np.array(self.predictions)
        self.parameters = np.array(self.parameters)
            
        return r**2

class PRFTikhonovModel(PRFRidgeModel):

    def __init__(self, bold_dm, data, rbf_kernel_sigma=None, window_length=51, polyorder=3):

        super(PRFTikhonovModel, self).__init__(bold_dm,
                                               data,
                                               window_length,
                                               polyorder)

        self.rbf_kernel_sigma = rbf_kernel_sigma

        resolution = bold_dm.shape[-2:]

        x, y = np.meshgrid(np.arange(0, resolution[0]), np.arange(0, resolution[0]))
        xy = np.vstack((x.ravel(), y.ravel())).T
        self.distances = rbf_kernel(xy, xy, 1./rbf_kernel_sigma)
        self.C_ = self.distances
        self.A = bold_dm.reshape(bold_dm.shape[0], -1).dot(self.C_)
        self.X_ = self.A

    def fit(self):

        r2 = super(PRFTikhonovModel, self).fit()

        self.parameters = [self.C_.dot(p.T) for p in self.parameters]

        return r2

