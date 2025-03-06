m = 28
k = 2

whiteProb = m / 100
blackProb = 1 - whiteProb

loops = 1000000

sum = 0

for i in range(loops):
    res = ((whiteProb ** k) * (blackProb ** (1 + 2*i))) * (1 + i) * 2
    sum += res
    
print(sum)