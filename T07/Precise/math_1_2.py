import math

N = 492
n = 137
k = 5
requiredAboveOrEqual = 5

prob = k / N

Lambda = n * prob


sum = 0
for i in range(0, requiredAboveOrEqual):
    sum += (Lambda ** i) * (2.71828 ** -Lambda) / math.factorial(i)

print(1 - sum)