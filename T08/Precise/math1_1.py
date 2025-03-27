from My_Probability.count_calculators import C


n = 13
r = 4
a = 6

max = C(n, r)
available = C(a-1, r-1)
print(available / max)

# gud