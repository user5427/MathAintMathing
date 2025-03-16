import math


p = 0.3
n = 100
a = 30
b = 35

u = (a - n * p) / (n * p * (1 - p)) ** 0.5
v = (b - n * p) / (n * p * (1 - p)) ** 0.5

prob =  math.erf(v / 2 ** 0.5) - math.erf(u / 2 ** 0.5)

prob *= 0.5

print(prob)