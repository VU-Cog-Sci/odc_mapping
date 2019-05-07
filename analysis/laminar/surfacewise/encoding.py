import numpy as np
import scipy.stats as ss
from scipy import optimize
from sklearn.linear_model import Ridge

class BinocularModelFitter(object):
    
    def __init__(self):
        pass
    
    def fit(self, data, X, ridge=True, alpha=1.0):
        
        if ridge:
            clf = Ridge(alpha=alpha).fit(X, data)
            beta = clf.coef_.T
            residuals = ((clf.predict(X) - data)**2).sum(0)
        else:
            beta, residuals, _, _ = np.linalg.lstsq(X, data, rcond=None)

        self.W = beta.T
        tau_ = np.sqrt(residuals / (len(data) - 1))[:, np.newaxis]
                               
        def loglikelihood(data, X, W, rho, tau2, sigma2):    
            
#             print(rho, tau2[:5], sigma2)
            omega = rho * tau2 + \
                   (1 - rho) * np.identity(len(tau2)) * tau2 + \
                    sigma2 * self.W.dot(self.W.T)

            predicted_timecourse = X.dot(self.W.T)

            try:    
                dist = ss.multivariate_normal(mean=np.zeros(omega.shape[0]), cov=omega)
            except ValueError:
                return -1e9
            except np.linalg.LinAlgError:
                return -1e9            

            return np.sum(dist.logpdf(data - predicted_timecourse))
        
        def loglikelihood_wrapper(pars):    
    
            rho = pars[0]
            tau = pars[1:-1][:, np.newaxis]
            sigma2 = pars[-1:]

            tau2 = tau.dot(tau.T)

            ll = loglikelihood(data, X, self.W, rho, tau2, sigma2)

            return -ll        
        
        bounds = [(.01, 0.99)] + list(zip([1e-6] * data.shape[1], data.std(0)*1.1)) + [(0, 1000)]
        x0 = np.array([0.01] + list(tau_) + [1.])
        
        print(x0.shape, len(bounds))
        
        pars = optimize.minimize(loglikelihood_wrapper,
                                 x0=x0,
                                 bounds=bounds,
                                 method='L-BFGS-B',
                                 options={'disp':True,'maxfun': 15000000, 'factr': 10})

        
        self.rho_ = pars.x[0]
        self.tau_ = pars.x[1:-1][:, np.newaxis]
        self.tau2_ = self.tau_.dot(self.tau_.T)
        self.sigma2_ = pars.x[-1]
        
        
        self.omega_ = self.rho_ * self.tau2_ + \
                      (1 - self.rho_) * np.identity(len(self.tau_)) * self.tau2_ + \
                      self.sigma2_ * self.W.dot(self.W.T)        

        self.mv_norm = ss.multivariate_normal(mean=np.zeros(self.omega_.shape[0]), cov=self.omega_)
        
        
    def decode(self, data, log_p=True, stimulus_range=None):

        if stimulus_range is None:
            stimulus = np.linspace(-5, 5, 1000)
        elif type(stimulus_range) is tuple:
            stimulus = np.linspace(stimulus_range[0], stimulus_range[1], 1000)
        else:
            stimulus = stimulus_range

        # n_timepoints x n_stimuli x n_stimulus_populations x n_voxels
        hypothetical_timeseries = (self.W.T[np.newaxis, :, :] * stimulus[:, np.newaxis, np.newaxis])
        residuals = data[:, np.newaxis, np.newaxis, :] - hypothetical_timeseries[np.newaxis, ...]
        
        
        if log_p:
            logp_ds = self.mv_norm.logpdf(residuals)        
            p_ds = np.exp(logp_ds - logp_ds.max(1)[:, np.newaxis, :])
            
        else:
            # n_timepoints x n_stimuli x n_stimulus_populations
            p_ds = self.mv_norm.pdf(residuals)

        # Normalize
        p_ds /= p_ds.sum(1)[:, np.newaxis, :] * (stimulus[1] - stimulus[0])

        return stimulus, p_ds        
    
    
    def get_map_stimulus_timeseries(self, data, stimulus_range=None):
        s, p_ds = self.decode(data, stimulus_range)
        
        
        return (s[np.newaxis, :, np.newaxis] * p_ds).sum(1)
    
    
    def get_std_stimulus_timeseries(self, data, stimulus_range=None):
        s, p_ds = self.decode(data, stimulus_range)
        
        
        return (s[np.newaxis, :, np.newaxis] * p_ds).sum(1)
