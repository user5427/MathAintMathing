import math

N = 582
n = 386
k = 3

prob = k / N

Lambda = n * prob

requiredAbove = 3

sum = 0
for i in range(requiredAbove):
    sum += (Lambda ** i) * (2.71828 ** -Lambda) / math.factorial(i)

print(1 - sum)