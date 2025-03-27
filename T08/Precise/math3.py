
# not very precise
import math


lamb = 3.7
p = 0.61


sum = 0
for i in range(0, 150):
    prob = (lamb ** i) * (math.e ** -lamb) / math.factorial(i)
    geomProb = (1-p)**(i-1)*p
    
    totalProb = prob * geomProb
    sum += totalProb
    
print(sum)