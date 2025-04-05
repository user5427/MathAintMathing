import math

from My_Probability.count_calculators import C


p = 0.25
t = 30 # no touchey
lamb = math.log((1 / p) ** (1 / t)) / math.log(math.e)

T = 43
n = 6

prob = 1 - math.exp(-lamb * T)

# print(prob)
count = 3
sum = 0
for i in range(count, n + 1):
    newProb = C(n, i) * (prob ** i) * ((1 - prob) ** (n - i))
    sum += newProb

print(sum)