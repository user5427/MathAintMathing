a = 14
b = 18
c = 18
d = 27

b = a + b
d = c + d

prob1 = a / b
prob11 = (a - 1) / (b - 1)

prob2 = c / d
prob22 = (c - 1) / (d - 1)

totalProb = (prob1 * prob11) + (prob2 * prob22)
totalProb = totalProb / 2

print(f"Total Probability: {totalProb}")