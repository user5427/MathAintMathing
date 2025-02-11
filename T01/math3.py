# 3 task

walls = 4
colors = 4
equalColorWallCount = 4


def shiftOccupation(seats, watchers):
    if watchers == []:
        return []

    lastWatcher = watchers[-1]
    if lastWatcher >= seats-1:
        backwardsShift = shiftOccupation(seats, watchers[:-1])
        if backwardsShift == []:
            return []
        backwardsShift.append(0)
        return backwardsShift
    else:
        watchers[-1] += 1
        return watchers


attempts = 0
equal = 0
equalToColor = 0

isFinished = False
watcherPozitions = []
for i in range(0, walls*2):
    watcherPozitions.append(0)
while not isFinished:
    print(watcherPozitions)

    attempts += 1
    tempEqual = 0
    for j in range(0, walls):
        if watcherPozitions[j*2] == watcherPozitions[j*2+1]:
            if tempEqual == 0:
                equal += 1
            tempEqual += 1

    if tempEqual == equalColorWallCount:
        equalToColor += 1

    watcherPozitions = shiftOccupation(colors, watcherPozitions)
    if watcherPozitions == []:
        break

print(1.0 - equal/attempts)
print(equalToColor/attempts)

print(equal)
print(equalToColor)
print(attempts)