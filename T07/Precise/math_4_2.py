#THE SOLUTION WITH random() CAN BE FOUND IN T06 math1_2_multithreaded.py OR IN T07 math3...

import math
from scipy.stats import norm


n = 940
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


# q 2 and 3

q2 = (y - n*p2) / (n * p2 * (1 - p2)) ** 0.5

prob2 =  1 - norm.cdf(q2)

print(prob2)