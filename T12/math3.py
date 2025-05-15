import math
from numpy import mean, std
from scipy.stats import norm, t, chi2, f

Q = 0.74
x = [17.5, 16.5, 17.8, 21.9, 13.3, 18.2, 16.3, 16.5, 22.2, 16.5, 18.2, 16.8, 20.3, 18.7, 17.2]


Xavr = sum(x) / len(x)
S = math.sqrt(sum([(i - Xavr) ** 2 for i in x]) / (len(x) - 1))
myt = t.ppf(Q, len(x) - 1)

av1 = Xavr - myt * S / math.sqrt(len(x))
av2 = Xavr + myt * S / math.sqrt(len(x))

# print(f"Pasikliautinis intervalas vidurkiui: {av1:.4f} < x < {av2:.4f}")

alpha = 1 - Q  # alpha = 0.26
lower_quantile = chi2.ppf(alpha/2, len(x) - 1)         # χ²(0.13, 14)
upper_quantile = chi2.ppf(1 - alpha/2, len(x) - 1)     # χ²(0.87, 14)

# The proper formula for variance confidence interval
var_lower = (len(x) - 1) * S**2 / upper_quantile
var_upper = (len(x) - 1) * S**2 / lower_quantile

print(f"Pasikliautinis intervalas dispersijai: {var_lower:.4f} < s^2 < {var_upper:.4f}")