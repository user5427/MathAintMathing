import math


p = 65
x = 14
y = 9
z = 15


b = (100 / p) ** (1 / x)
a = math.e

lamb = math.log (b) / math.log (a)

# print(lamb)

# test = math.e ** (- lamb * x)

# print(test)

lessThanY = 1 - math.e ** (- lamb * y)
print(lessThanY)