import math

N = 582
n = 386
k = 3

prob = k / N

Lambda = n * prob

required = 3

res = (Lambda ** required) * (2.71828 ** -Lambda) / math.factorial(required)

print(res)