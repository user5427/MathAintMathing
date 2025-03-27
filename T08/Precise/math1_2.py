from My_Probability.count_calculators import C


n = 14
r = 4
a = 7

sum = 0
for k in range(a - r + 1):
    max = C(n, r)
    available = C(a - k - 1, r-1)
    # print(available / max)
    sum += available / max
    
print(sum)