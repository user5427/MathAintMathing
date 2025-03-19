#THE SOLUTION WITH random() CAN BE FOUND IN T06 math1_2_multithreaded.py OR IN T07 math3...

import math
from scipy.stats import norm


p = 4/8
n = 238
a = 123

u = (a - n * p) / (n * p * (1 - p)) ** 0.5

prob =  norm.cdf(u) 

print(prob)