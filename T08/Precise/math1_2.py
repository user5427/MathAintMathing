from My_Probability.count_calculators import C


n = 15
r = 5
a = 9

a = a - 1

sum = 0
for k in range(a - r + 1):
    max = C(n, r)
    available = C(a - k - 1, r-1)
    # print(available / max)
    sum += available / max
    
print(sum)


# gud