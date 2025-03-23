
# not very precise
import math


lamb = 6.8
p = 0.47


sum = 0
for i in range(0, 150):
    prob = (lamb ** i) * (math.e ** -lamb) / math.factorial(i)
    geomProb = (1-p)**(i-1)*p
    
    totalProb = prob * geomProb
    sum += totalProb
    
print(sum)