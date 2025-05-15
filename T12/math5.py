import numpy as np
from scipy.stats import norm

# Parameters
n_pairs = 1000
black_speed = 9.47
brown_speed_min = 0
brown_speed_max = 19
time = 321

# After time seconds, black ants travel a fixed distance
black_distance = black_speed * time

# For brown ants, we need to use Central Limit Theorem
# For a uniform distribution in [0, b], the mean is b/2 and variance is b²/12
brown_mean_speed = (brown_speed_min + brown_speed_max) / 2
brown_var_speed = (brown_speed_max - brown_speed_min)**2 / 12

# Using CLT, after n steps the sum follows normal distribution with:
brown_mean_distance = brown_mean_speed * time
brown_std_distance = np.sqrt(time * brown_var_speed)

# Probability that a black ant is ahead of its brown counterpart
z_score = (black_distance - brown_mean_distance) / brown_std_distance
prob_black_ahead = norm.cdf(z_score)

# Expected number of black ants ahead
expected_black_ahead = n_pairs * prob_black_ahead

print(f"Black ant distance: {black_distance:.2f} mm")
print(f"Brown ant mean distance: {brown_mean_distance:.2f} mm, std: {brown_std_distance:.2f} mm")
print(f"Probability of black ant being ahead: {prob_black_ahead:.4f}")
print(f"Expected number of black ants ahead (out of {n_pairs}): {expected_black_ahead:.0f}")