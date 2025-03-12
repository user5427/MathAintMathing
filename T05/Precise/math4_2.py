import math

α = 0.77
r = 0.04
s = 0.17
a = 0.39

rSurvivalProb = (1 - 2 * r) ** 2
sSurvivalProb = (1 - 2 * s) ** 2


x = 1 - α

count = math.log(x) / math.log(rSurvivalProb)

count = math.ceil(count)


res = (a) * (rSurvivalProb ** count) + (1 - a) * (sSurvivalProb ** count)

print(res)
