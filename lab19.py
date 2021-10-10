import numpy as np
from scipy.optimize import minimize

def rosen(x):
    """The Rosenbrock function"""
    return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)

x0 = np.array([1, 4, 4])
res = minimize(rosen, x0, method='nelder-mead',
                options={'xatol': 1e-8, 'disp': True})

print(res.x)
