import numpy as np
from scipy.signal import savgol_filter, fftconvolve, resample
from sklearn.model_selection import LeaveOneOut
from sklearn import linear_model
from popeye.visual_stimulus import VisualStimulus
import popeye.og as OGModel
import popeye.utilities as utils
from scipy import signal
from scipy import interpolate
from scipy import optimize
from popeye.utilities import gradient_descent_search, error_function, coeff_of_determination
import pandas as pd
from joblib import Parallel, delayed

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


class PRFGridSearch(object):
    
    
    def __init__(self, dm, viewing_distance, screen_width, tr_dm):
        
        self.stimulus = VisualStimulus(stim_arr=dm,
                            viewing_distance=viewing_distance, 
                            screen_width=screen_width,
                            scale_factor=1,
                            tr_length=tr_dm,
                            dtype = np.short)
        
        self.model_func = OGModel.GaussianModel(stimulus=self.stimulus, hrf_model=utils.spm_hrf)
        self.model_func.hrf_delay = 0
        self.predictions = None
        
        
    def make_predictions(self, angles, eccentricities, sizes):
        self.angles, self.eccentricities, self.sizes, = np.meshgrid(angles, eccentricities, sizes)        
        self.predictions = np.zeros(list(self.angles.shape) + [self.stimulus.run_length])
        self.predictions = self.predictions.reshape(-1, self.predictions.shape[-1]).T

        self.xs = np.cos(self.angles) * self.eccentricities
        self.ys = np.sin(self.angles) * self.eccentricities
        
        for i, (x, y, s) in enumerate(zip(self.xs.ravel(), self.ys.ravel(), self.sizes.ravel())):
            self.predictions[:, i] = self.model_func.generate_prediction(x, y, s, 1, 0)        
        
    def fit(self, data,
            include_intercept_slope=False,
            include_predictions=False):
        if self.predictions is None:
            raise Exception('First use self.make_predictions!')
        
        self.predictions_ = self.predictions - self.predictions.mean(0)[np.newaxis, :]
        self.data = data
        self.data_ = data - data.mean(0)[np.newaxis, :]
        
        # Calculate R^2
        print('Calculate R2')
        self.num = (np.dot(self.predictions_.T, self.data_) / self.data_.shape[0])
        self.denom = self.predictions_.std(0)[:, np.newaxis] * self.data_.std(0)[np.newaxis, :]
        self.r2 = (self.num / self.denom)**2
        self.r2[np.isnan(self.r2)] = 0
        
        print('Find best R2')
        self.best_pars_ix = np.argmax(self.r2, 0)
        
        print('Find best parameters')
        self.best_x, self.best_y, self.best_s = self.xs.ravel()[self.best_pars_ix], self.ys.ravel()[self.best_pars_ix], self.sizes.ravel()[self.best_pars_ix]
        self.best_angle = self.angles.ravel()[self.best_pars_ix]
        self.best_ecc = self.eccentricities.ravel()[self.best_pars_ix]

        print('Store results')
        results =  {'x':self.best_x,
                    'y':self.best_y,
                    'size':self.best_s,
                    'r2':self.r2.max(0),
                    'angle':self.best_angle,
                    'ecc':self.best_ecc}

        if include_intercept_slope or include_predictions:
            print('Find intercept and slope')
            results['intercept'] = self.data.mean(0)
            results['slope'] = self.data.std(0) / self.predictions[:, self.best_pars_ix].std(0)


        if include_predictions:
            print('Make best fitting predictions')
            self.predictions = results['intercept'] + results['slope'] * self.predictions_[:, self.best_pars_ix]

        return pd.DataFrame(results)

    def refine_parameters(self,
                          results,
                          correlation_method=True,
                          verbose=1,
                          n_jobs=1):

        results = results.copy()
        if correlation_method:
            def make_zscored_prediction(x, y, size):
           
                pred = self.model_func.generate_prediction(x, y, size, 1, 0)
                pred -= pred.mean()
                pred /= pred.std()
           
                return pred

            bounds = ((self.xs.min(), self.xs.max()),
                      (self.ys.min(), self.ys.max()),
                      (self.sizes.min(), self.sizes.max()))

            generate_prediction_func = make_zscored_prediction

            ballparks = results[['x', 'y', 'size']].values
            #ballparks = [(row.x, row.y, row.size ) for _, row in results.iterrows()

                         #b

            #def optimize_prf(ix, row, data, bounds, generate_prediction_func):
                #print('Correlation method')

                #ballpark = row.x, row.y, row.size

                #data_ =  data - data.mean()
                #data_ /= data_.std()

                #r = gradient_descent_search(data_,
                                        #error_function,
                                        #generate_prediction_func,
                                        #ballpark,
                                        #bounds,
                                        #4)

                #row['x_opt'] = r[0][0]
                #row['y_opt'] = r[0][1]
                #row['s_opt'] = r[0][2]

                #X = np.ones((len(data_), 2))
                #X[:, 1] = make_zscored_prediction(*r[0])

                #beta, residuals, _, _ = np.linalg.lstsq(X, data)

                #row['baseline_opt'] = beta[0]
                #row['amplitude_opt'] = beta[1]

                #row['r2_opt'] = 1 - residuals / (len(data) * data.var())
                #row['estimation method'] = 'correlation method'
                #print("Used {} function evaluations".format(r[4]))
                #return ix, row

        else:
            bounds = ((self.xs.min(), self.xs.max()),
                              (self.ys.min(), self.ys.max()),
                              (self.sizes.min(), self.sizes.max()),
                              (0, self.data.max() * 3),
                              (self.data.min(), self.data.max()))

            generate_prediction_func = self.model_func.generate_prediction

            ballparks = results[['x', 'y', 'size', 'slope', 'intercept']].values

            #def optimize_prf(ix, row, data, bounds, generate_prediction_func):
                #print('Classic method')
                #ballpark = row.x, row.y, row.size, row.slope, row.intercept

                #r = gradient_descent_search(data,
                                        #error_function,
                                        #generate_prediction_func,
                                        #ballpark,
                                        #bounds,
                                        #4)
                #row['x_opt'] = r[0][0]
                #row['y_opt'] = r[0][1]
                #row['s_opt'] = r[0][2]
                #row['baseline_opt'] = r[0][3]
                #row['amplitude_opt'] = r[0][4]


                #pred = self.model_func.generate_prediction(*r[0])

                #row['r2_opt'] = coeff_of_determination(data, pred) / 100

                #row['estimation method'] = 'Classic method'

                #print("Used {} function evaluations".format(r[4]))

                #return ix, row

        #if n_jobs == 1:
            #r = []
            #for ix, row in results.iterrows():
                #d = self.data[:, ix]
                #r.append(optimize_prf(ix, row, d, bounds, generate_prediction_func))
        #else:
            #r = Parallel(n_jobs=n_jobs, verbose=9)(delayed(optimize_prf)(ix, row.copy(), self.data[:, ix].copy(), bounds, generate_prediction_func) for ix, row in results.iterrows())

            #r = parallel(n_jobs=n_jobs, verbose=9)(delayed(gradient_descent_search)(self.data[:, ix], error_function, generate_prediction_func, ballpark, bounds) for ix, ballpark in zip(results.index, ballparks))

        r = Parallel(n_jobs=n_jobs,
                     verbose=9,
                     backend='threads')(delayed(gradient_descent_search)(self.data[:, ix], error_function, generate_prediction_func, ballpark, bounds, 1) for ix, ballpark in zip(results.index, ballparks))


        return r
        #return pd.DataFrame(data=[_[1] for _ in r], index=[_[0] for _ in r])
