p1 = 0.77
p2 = 0.73
p3 = 0.84

sum = p1 * p2 * p3 + p1 * p2 * (1 - p3) + p1 * (1 - p2) * p3 + (1 - p1) * p2 * p3

print(sum)