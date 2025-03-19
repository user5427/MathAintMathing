import math

n = 776
k = 5
p = 0.009

sum = 0

for i in range(0, k+1):
    Lambda = n * p
    prob = (Lambda ** i) * (2.71828 ** -Lambda) / math.factorial(i)
    sum += prob
    
print(1 - sum)