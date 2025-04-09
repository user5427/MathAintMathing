import math

from My_Probability.count_calculators import C


p = 0.34
t = 30 # no touchey
lamb = math.log((1 / p) ** (1 / t)) / math.log(math.e)

T = 34
n = 5

prob = 1 - math.exp(-lamb * T)

# print(prob)
count = 3
newProb = C(n, count) * (prob ** count) * ((1 - prob) ** (n - count))

print(newProb)