#THE SOLUTION WITH random() CAN BE FOUND IN T06 math1_2_multithreaded.py OR IN T07 math2...

import math


p = 0.7
n = 1280
r = 525
a = (-r + n) / 2
b = (r + n) / 2

u = (a - n * p) / (n * p * (1 - p)) ** 0.5
v = (b - n * p) / (n * p * (1 - p)) ** 0.5

prob =  math.erf(v / 2 ** 0.5) - math.erf(u / 2 ** 0.5)

prob *= 0.5

print(prob)