p1 = 0.87
p2 = 0.92
p3 = 0.52

sum = p1 * p2 * p3 + p1 * p2 * (1 - p3) + p1 * (1 - p2) * p3

sum1 = p1 * p2 * p3 + p1 * p2 * (1 - p3) + p1 * (1 - p2) * p3 + (1 - p1) * p2 * p3

res = sum / sum1
print(res)