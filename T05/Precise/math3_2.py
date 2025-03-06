p1 = 0.6
p2 = 0.58
p3 = 0.85

sum = p1 * p2 * p3 + p1 * p2 * (1 - p3) + p1 * (1 - p2) * p3

sum1 = p1 * p2 * p3 + p1 * p2 * (1 - p3) + p1 * (1 - p2) * p3 + (1 - p1) * p2 * p3

res = sum / sum1
print(res)