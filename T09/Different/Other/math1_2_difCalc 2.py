import numpy as np
from statsmodels.nonparametric.smoothers_lowess import lowess

a = 11.0
b = 5.0
x = 2.21 

bFor = b
aFor = -b / a

def simulate_empirical_cdf(n_samples=1_000_000):
    y_values = []
    for _ in range(n_samples):
        aRand = np.random.uniform(0, a)
        bRand = np.random.uniform(0, b)
        yNow = aFor * aRand + bFor
        if bRand <= yNow:  # Only keep points inside the triangle
            y_values.append(bRand)
    y_values = np.sort(np.array(y_values))
    x_vals = np.linspace(0, b, 1000)
    ecdf = np.searchsorted(y_values, x_vals) / len(y_values)  # Empirical CDF
    return x_vals, ecdf

x_vals, ecdf = simulate_empirical_cdf()

# Smooth the empirical CDF (LOESS is robust to noise)
smoothed = lowess(ecdf, x_vals, frac=0.1)  # frac=bandwidth
x_smooth, F_smooth = smoothed[:, 0], smoothed[:, 1]

from scipy.interpolate import UnivariateSpline

# Fit a spline to the smoothed CDF (ensures smooth derivatives)
spline = UnivariateSpline(x_smooth, F_smooth, s=0.5, k=3)  # k=3 for cubic spline
f_estimated = spline.derivative()  # Analytical derivative!

# Evaluate at x=2.21
print(f"Estimated f(2.21): {f_estimated(2.21):.6f}")
print(f"Exact f(2.21): {2*(b - 2.21)/b**2:.6f}")