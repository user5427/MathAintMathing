from random import random, randint
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


attempts = 1000000
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

