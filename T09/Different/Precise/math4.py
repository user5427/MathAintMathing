from math import log
import math


r = 79
t = 18.0
n = 7
T = 33.0
alfa = 0.47          



                               
r = r / 100

lamb = log((1 / r) ** (1 / t)) / log(math.e)

print(lamb)


