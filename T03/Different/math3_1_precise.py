# n = 2
# WinCombinations = 4

# winChances = []
# chanceToWin = WinCombinations / (6 ** 2)
# chanceToLoose = 1 - chanceToWin
# for i in range(0, n):
#     winChances.append(chanceToWin * (chanceToLoose ** i))
    
# print(winChances)

# sum = 0
# for i in winChances:
#     sum += i

# print(sum)

n = 5
AWinCombinations = 4
BWinCombinations = 6
winChances = []
chanceToWin = AWinCombinations / (6 ** 2)
chanceToLoose = ((6 ** 2) - AWinCombinations - BWinCombinations) / (6 ** 2)
for i in range(0, n):
    winChances.append(chanceToWin * (chanceToLoose ** i))
    
sum = 0
for i in winChances:
    sum += i
    
print(sum)