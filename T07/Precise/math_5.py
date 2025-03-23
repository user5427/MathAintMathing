import math

n = 766
k = 5
p = 0.009

sum = 0

for i in range(0, k+1):
    Lambda = n * p
    prob = (Lambda ** i) * (math.e ** -Lambda) / math.factorial(i)
    sum += prob
    
print(1 - sum)