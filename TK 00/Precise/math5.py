a = 14
b = 18
c = 18
d = 27

# port1 = (a+b) / (a+b+c+d)
# port2 = (c+d) / (a+b+c+d)

# print(f"Port1: {port1}")
# print(f"Port2: {port2}")



b = a + b
d = c + d

prob1 = a / b
prob11 = (a - 1) / (b - 1)

prob2 = c / d
prob22 = (c - 1) / (d - 1)


totalProb1 = (prob1 * prob11) / prob1
totalProb2 = (prob2 * prob22) / prob2
totalProb = totalProb1 * 0.501 + totalProb2 * 0.501 # 0.501 because why not

print(f"Total Probability: {totalProb}")