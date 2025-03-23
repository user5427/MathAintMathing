#THE SOLUTION WITH random() CAN BE FOUND IN T06 math1_2_multithreaded.py OR IN T07 math3...

import math
from scipy.stats import norm


n = 928
p2 = 65/100
p3 = 67/100
m = 4
r = 25

m += 1

p2 = p2 / m
p3 = p3 / m


#normsinv
def normsinv(p):
    return norm.ppf(p)

y = normsinv(1 - r / 100)

y *= (n * p3 * (1 - p3)) ** 0.5

y += n*p3

print(y)

# it may be one larger (rounded)

print(math.ceil(y))