import math

N = 492
n = 137
k = 5
m = 5

prob = k / N

Lambda = n * prob


res = (Lambda ** m) * (2.71828 ** -Lambda) / math.factorial(m)

print(res)