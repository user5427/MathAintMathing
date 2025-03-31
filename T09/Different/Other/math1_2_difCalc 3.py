import numpy as np
from scipy.stats import gaussian_kde

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
    kde = gaussian_kde(y_values, bw_method=0.01)  # Bandwidth affects smoothness
    print(f"KDE f(2.21): {kde(2.21)[0]:.6f}")


simulate_empirical_cdf()