import math


h = 14
m = 456
alfa = 0.89
p = 54
n = 1000

halfProb = 0.5 

prob = m / n
opProb = 1 - prob

invProb = 1 / opProb
sqrProb = invProb ** (1 / h)

b = sqrProb
a = math.e

lamb = math.log (b) / math.log (a)

print(lamb)

invHalf = 1 / halfProb
sqrHalf = invHalf ** (1 / lamb)
h0 = math.log (sqrHalf) / math.log (a)

# NO CLUE AT ALL WHAT THIS IS DOING
