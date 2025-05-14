x = [3.8, 5.5, 4.7, 4.8, 4.4, 4.3, 4.4, 5.3, 3.4, 4.3, 5.2, 3.5, 4.9]


a1 = sum(x) / len(x)
a2 = sum(i ** 2 for i in x) / len(x)

# For uniform distribution, method of moments gives:
# u = a1 - sqrt(3*(a2 - a1²))
# v = a1 + sqrt(3*(a2 - a1²))

import math

variance_estimate = 3 * (a2 - a1**2)
u = a1 - math.sqrt(variance_estimate)
v = a1 + math.sqrt(variance_estimate)

print(f"Sample mean (a1): {a1:.4f}")
print(f"Sample second moment (a2): {a2:.4f}")
print(f"Estimated interval [u, v]: [{u:.4f}, {v:.4f}]")