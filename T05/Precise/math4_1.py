import math

α = 0.77
r = 0.04

good = (1 - 2 * r) ** 2

x = 1 - α

res = math.log(x) / math.log(good)
print(res)
rounded = math.ceil(res)
print(rounded)