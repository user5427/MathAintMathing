#THE SOLUTION WITH random() CAN BE FOUND IN T06 math1_2_multithreaded.py OR IN T07 math2...

import math


p = 0.67
n = 1052
r = 388
a = (-r + n) / 2
b = (r + n) / 2

u = (a - n * p) / (n * p * (1 - p)) ** 0.5
v = (b - n * p) / (n * p * (1 - p)) ** 0.5

prob =  math.erf(v / 2 ** 0.5) - math.erf(u / 2 ** 0.5)

prob *= 0.5

print(prob)