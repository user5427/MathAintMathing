import numpy as np
from scipy.interpolate import UnivariateSpline
from multiprocessing import Pool

# Your triangle parameters
a = 11.0
b = 5.0
x_eval = 2.21  # Point where we evaluate density

def sample_y_in_triangle(n):
    """Generates n samples of y-coordinates inside the triangle."""
    y_vals = []
    for _ in range(n):
        aRand = np.random.uniform(0, a)
        bRand = np.random.uniform(0, b)
        yNow = (-b / a) * aRand + b
        if bRand <= yNow:  # Check if point is inside the triangle
            y_vals.append(bRand)
    return np.array(y_vals)

def simulate_empirical_cdf(n_total=1_000_000, num_processes=4):
    """Parallel simulation of the empirical CDF."""
    chunk_size = n_total // num_processes
    with Pool(num_processes) as pool:
        results = pool.map(sample_y_in_triangle, [chunk_size] * num_processes)
    y_samples = np.concatenate(results)
    y_sorted = np.sort(y_samples)
    x_vals = np.linspace(0, b, 1000)  # Points to evaluate CDF
    ecdf = np.searchsorted(y_sorted, x_vals) / len(y_sorted)  # Empirical CDF
    return x_vals, ecdf

def estimate_density(x_eval, x_vals, ecdf):
    """Estimates f(x) by fitting a spline to the CDF and differentiating."""
    spline = UnivariateSpline(x_vals, ecdf, s=0.1, k=3)  # Smoothing spline
    f_estimated = spline.derivative()  # Analytical derivative
    return f_estimated(x_eval)

# Run the simulation
x_vals, ecdf = simulate_empirical_cdf()
f_x = estimate_density(x_eval, x_vals, ecdf)

# Compare with exact density
exact_density = 2 * (b - x_eval) / b**2
print(f"Simulated f({x_eval}): {f_x:.6f}")
print(f"Exact f({x_eval}): {exact_density:.6f}")