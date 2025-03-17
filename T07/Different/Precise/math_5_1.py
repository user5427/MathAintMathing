#THE SOLUTION WITH random() CAN BE FOUND IN T06 math1_2_multithreaded.py OR IN T07 math3...

import math
from scipy.stats import norm


n = 940
p1 = 51/100
p2 = 49/100
p3 = 46/100
m = 2
r = 17


#normsinv
def normsinv(p):
    return norm.ppf(p)

y = normsinv(1 - r / 100)

y *= (n * p3 * (1 - p3)) ** 0.5

y += n*p3

print(y)

# it may be one larger (rounded)

print(math.ceil(y))