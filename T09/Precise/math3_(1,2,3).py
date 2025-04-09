import math


h = 10
m = 562
alfa = 0.84
p = 37
n = 1000

halfProb = 0.5 

prob = m / n
opProb = 1 - prob

invProb = 1 / opProb
sqrProb = invProb ** (1 / h)

b = sqrProb
a = math.e

lamb = math.log (b) / math.log (a)

# print(lamb)

invHalf = 1 / halfProb
sqrHalf = invHalf ** (1 / lamb)
h0 = math.log (sqrHalf) / math.log (a)
# print(f"(1) specifine tikimybe: {halfProb} aukstis {h0}")


safety = (1 / alfa) ** (1 / lamb)

height = math.log (safety) / math.log (a)
print(f"(2) saugus aukstis - tikimybe: {alfa} aukstis {height}")


increased = height * (1 + p / 100)
prob = math.e ** (- lamb * increased)
print(f"(3) padidintas saugus aukstis - tikimybe: {prob} aukstis {increased}")