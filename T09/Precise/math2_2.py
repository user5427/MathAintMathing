import math


p = 56
x = 12
y = 10
z = 15


b = (100 / p) ** (1 / x)
a = math.e

lamb = math.log (b) / math.log (a)

# print(lamb)

# test = math.e ** (- lamb * x)

# print(test)

moreThanY = math.e ** (- lamb * y)
lessThanZ = 1 - math.e ** (- lamb * z)
moreThanYAndLessThanZ = moreThanY + lessThanZ - 1

print(moreThanYAndLessThanZ)

