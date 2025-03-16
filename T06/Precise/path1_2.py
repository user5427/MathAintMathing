from My_Probability.count_calculators import C


p = 0.63
n = 14
r = 8

sum = 0

# find these with -r <= 2x - n <= r
for i in range(3, 12):
    sum += C(n, i) * (p ** i) * ((1 - p) ** (n - i))
    
print(sum)