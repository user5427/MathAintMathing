

import math


r = 3
b = 5
n = 5

half = n // 2
if n % 2 != 0:
    half += 1
    
probs = 0
total = r + b
for i in range (n - half):
    reds = i + half
    blues = n - (i + half)
    
    if reds> r:
        break
    if blues > b:
        break
    
    # prob = (r / total) ** reds * (b / total) ** blues * math.comb(n, reds)
    # probs += prob
    
    prob = math.comb(n, reds) / math.comb(total, n)
    probs += prob
    
    print(f"reds: {reds}, blues: {blues}")
    
print(f"Probability: {probs}")