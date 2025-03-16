from My_Probability.count_calculators import C


m = 28
k = 2

# even offset
offset = 0
if k % 2 == 0:
    offset = 1

whiteProb = m / 100
blackProb = 1 - whiteProb

loops = 2000

sum = 0

for i in range(loops):
    res = ((whiteProb ** k) * (blackProb ** (offset + 2*i))) * C((offset + k-1)+i*2, k-1)   #* (1 + i) * 2
    sum += res
    
print(sum)