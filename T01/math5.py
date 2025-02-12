from random import random, randint

from My_Probability.combinations import C_Cycle
from My_Probability.static_calculation import C

# 5 task


# array of chars

k = 12
m = 14
n = 10

testArray = []

# fill array with 'k' characters
for i in range(0, k):
    testArray.append('k')

# fill array with 'm' characters
for i in range(0, m):
    testArray.append('m')

# fill array with 'n' characters
for i in range(0, n):
    testArray.append('n')

# shuffle the array
for i in range(0, len(testArray)):
    randomIndex = randint(0, len(testArray)-1)
    temp = testArray[i]
    testArray[i] = testArray[randomIndex]
    testArray[randomIndex] = temp


attempts = 1000
equal = 0

for i in range(0, attempts):
    twoChars = []
    copy = testArray.copy()
    # choose two random characters from the array
    first = randint(0, len(testArray)-1)
    twoChars.append(testArray[first])
    copy.pop(first)
    twoChars.append(copy[randint(0, len(testArray)-2)])

    # if the two characters are the same, increment the counter
    if twoChars[0] == twoChars[1]:
        equal += 1

print(equal/attempts)


# red 0 - 12
# blue 12 - 26
# green 26 - 36
def comparable(list):
    colors = [0, 0, 0]
    for i in range(0, 2):
        if list[i] <= 12:
            colors[0] += 1
        elif list[i] <= 26:
            colors[1] += 1
        else:
            colors[2] += 1

    if colors[0] == 2 or colors[1] == 2 or colors[2] == 2:
        return True
    return False

totalFound = C_Cycle(36, 2, comparable, True)
total = C(36, 2)

print(totalFound/total)
print(1 - totalFound/total)