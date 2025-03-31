import math


p = 75
x = 5.0
y = 7.0
z = 16.0


b = (100 / p) ** (1 / x)
a = math.e

lamb = math.log (b) / math.log (a)

# print(lamb)

# test = math.e ** (- lamb * x)

# print(test)

lessThanY = 1 - math.e ** (- lamb * y)
print(lessThanY)