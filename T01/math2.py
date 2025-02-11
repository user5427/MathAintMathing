from random import random, randint

# 2 task
houses = 8
phonesPerHouse = 4
phones = houses * phonesPerHouse
calls = 4

attempts = 0
equal = 0
notDemasked = 0

demaskedAtExact = 0

def shiftOccupation(phones, calls):
    if calls == []:
        return []

    lastWatcher = calls[-1]
    if lastWatcher >= phones - 1:
        backwardsShift = shiftOccupation(phones - 1, calls[:-1])
        if backwardsShift == []:
            return []
        backwardsShift.append(backwardsShift[-1] + 1)
        return backwardsShift
    else:
        calls[-1] += 1
        return calls

homNum = []
for i in range(0, houses):
    homNum.append(0)

isFinished = False
phoneCalls = []
for i in range(0, calls):
    phoneCalls.append(i)
while not isFinished:
    print(phoneCalls)

    attempts += 1
    homesCalled = []
    for j in range(0, houses):
        homesCalled.append(0)
    for j in range(0, calls):
        homesCalled[phoneCalls[j] // phonesPerHouse] += 1

    for j in range(0, houses):
        if homesCalled[j] >= 2:
            homNum[j] += 1

    notDem = False
    for j in range(0, houses):
        if homesCalled[j] >= 2:
            equal += 1
            notDem = True
            break

    # check if that house has been called exactly 2 times
    if homesCalled[phoneCalls[calls - 1] // phonesPerHouse] == 2:
        demaskedAtExact += 1

    if not notDem:
        notDemasked += 1

    phoneCalls = shiftOccupation(phones, phoneCalls)
    if phoneCalls == []:
        break

print(equal / attempts) #demaskuotas
print(1.0 - equal / attempts) # NEdemaskuotas
print(notDemasked / attempts) # nedemaskuotas

print (equal)
print (notDemasked)
print( attempts)

print(demaskedAtExact / attempts)
print(demaskedAtExact)

# print(homNum)
