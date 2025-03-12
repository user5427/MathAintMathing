from My_Probability.count_calculators import C


m = 28
k = 2

whiteProb = m / 100
blackProb = 1 - whiteProb

loops = 1000

sum = 0

for i in range(loops):
    res = ((whiteProb ** k) * (blackProb ** (1 + 2*i))) * (1 + i) * 2 #* C(2+i*2, k-1)   #* (1 + i) * 2
    sum += res
    
print(sum)