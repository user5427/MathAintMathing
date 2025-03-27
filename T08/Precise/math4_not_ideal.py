



# Y = k (X + 1)^-1
# check if Y is integer. how?
# X + 1 = k / Y
# X = k / Y - 1
# we know that X is a puason distribution, alfa = 0.47, k = 3
# we dont know the m parameter, so we will loop through all the values of m and check if Y is integer

import math
from random import random

a = 3.07
k = 6

total = 0
gud = 0

for i in range(0, 160):
    prob = (a ** i) * (math.e ** -a) / math.factorial(i)
    total += prob
    if (k / (i + 1)) % 1 == 0:
        print(i)
        gud += prob
        
print(gud / total)
print(gud)
print(total)

# or in other words this will be true when X is equal to 0, 1, 2, 5 so just sum the probabilities of these values

prob1 = (a ** 0) * (math.e ** -a) / math.factorial(0)
prob2 = (a ** 1) * (math.e ** -a) / math.factorial(1)
prob3 = (a ** 2) * (math.e ** -a) / math.factorial(2)
prob4 = (a ** 5) * (math.e ** -a) / math.factorial(5)

print(prob1 + prob2 + prob3 + prob4) # yep looks gud to me