import math


λ = 3.07
k = 6

# gud x values
xVals = []

for i in range (0, 100_000_0):
    if (k / (i + 1)) % 1 == 0:
        xVals.append(i)
        
sum = 0
for x in xVals:
    # find the puaoson probability
    prob = (λ ** x) * (math.e ** -λ) / math.factorial(x)
    sum += prob
    
print(sum) # gud