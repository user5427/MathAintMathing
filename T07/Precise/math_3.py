#THE SOLUTION WITH random() CAN BE FOUND IN T06 math1_2_multithreaded.py OR IN T07 math3...

import math
from scipy.stats import norm


n = 238
m = 4.0
alfa = 0.7

prob = m / 8


#normsinv
def normsinv(p):
    return norm.ppf(p)

y = normsinv(alfa)

y *= (n * prob * (1 - prob)) ** 0.5

y += n*prob

print(y)

# it may be one larger (rounded)

print(math.ceil(y))