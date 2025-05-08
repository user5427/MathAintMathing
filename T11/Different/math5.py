import numpy as np
from scipy import stats

def solve_probability_problem(n, a, x, epsilon):
    """
    Calculates the probability that the empirical distribution function differs 
    from the true CDF by at least epsilon.
    
    Parameters:
    n (int): Sample size
    a (float): Upper bound of uniform distribution [0, a]
    x (float): Point at which to evaluate the CDF
    epsilon (float): Threshold difference
    
    Returns:
    tuple: (Chebyshev bound, CLT probability)
    """
    # Calculate the true CDF value at x for uniform distribution on [0, a]
    if x <= 0:
        Fx = 0
    elif x >= a:
        Fx = 1
    else:
        Fx = x / a
    
    # Variance of the empirical CDF at point x
    variance = Fx * (1 - Fx) / n
    
    # Method 1: Using Chebyshev's inequality
    # P(|X - E[X]| ≥ k * sigma) ≤ 1/k^2
    chebyshev_bound = variance / (epsilon**2)
    
    # Method 2: Using Central Limit Theorem
    std_dev = np.sqrt(variance)
    z_score = epsilon / std_dev
    clt_prob = 2 * (1 - stats.norm.cdf(z_score))
    
    return Fx, chebyshev_bound, clt_prob

# Given parameters
n = 215
a = 3.9
x = 3
epsilon = 0.1

# Calculate results
Fx, chebyshev_bound, clt_prob = solve_probability_problem(n, a, x, epsilon)

# Print results
print(f"Parameters: n = {n}, a = {a}, x = {x}, epsilon = {epsilon}")
print(f"True CDF value at x = {x}: Fx = {Fx:.6f}")

print("\nMethod 1: Using Chebyshev's inequality")
print(f"P(|F(x) - Fx| ≥ {epsilon}) ≤ {chebyshev_bound:.6f}")

print("\nMethod 2: Using Central Limit Theorem")
print(f"P(|F(x) - Fx| ≥ {epsilon}) ≈ {clt_prob:.6f}")