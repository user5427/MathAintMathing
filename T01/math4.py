from random import random, randint
# 4 task
seats = 40
watchers = 5

attempts = 0
equal = 0

# occupation = []
# for i in range(0, seats):
#     occupation.append(0)
#
# for i in range(0, watchers):
#     occupation[i] = watchers - i
#
# print(occupation)


def shiftOccupation(seats, watchers):
    if watchers == []:
        return []

    lastWatcher = watchers[-1]
    if lastWatcher >= seats-1:
        backwardsShift = shiftOccupation(seats-1, watchers[:-1])
        if backwardsShift == []:
            return []
        backwardsShift.append(backwardsShift[-1] + 1)
        return backwardsShift
    else:
        watchers[-1] += 1
        return watchers




isFinished = False
watcherPozitions = []
for i in range(0, watchers):
    watcherPozitions.append(i)
while not isFinished:
    # print(watcherPozitions)

    attempts += 1
    for j in range(0, watchers - 1):
        if watcherPozitions[j] == watcherPozitions[j+1]-1 or watcherPozitions[j] == watcherPozitions[j+1]+1:
            equal += 1
            break

    watcherPozitions = shiftOccupation(seats, watcherPozitions)
    if watcherPozitions == []:
        break



#
# for i in range(0, attempts):
#     # occupy the seats randomly with watchers
#     occupiedSeats = []
#     for j in range(0, watchers):
#         seat = randint(0, seats-1)
#         while seat in occupiedSeats:
#             seat = randint(0, seats-1)
#
#         occupiedSeats.append(seat)
#
#     # print(occupiedSeats)
#
#     # if two watchers are sitting in the same seat, increment the counter
#     for j in range(0, watchers-1):
#         if occupiedSeats[j] == occupiedSeats[j+1]-1 or occupiedSeats[j] == occupiedSeats[j+1]+1:
#             equal += 1
#             break
#
print(equal/attempts)
print(1.0 - equal/attempts)
