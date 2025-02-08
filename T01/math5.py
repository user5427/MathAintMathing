# task 1.2

# 1.2 task

students = 6
tasks = 12
sameTasks = 3

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
newWayEqual = 0

isFinished = False
watcherPozitions = []
for i in range(0, students):
    watcherPozitions.append(0)
while not isFinished:
    print(watcherPozitions)

    attempts += 1
    tempEqual = 0

    foundTasks = []
    foundTaskCount = []
    for j in range (0, students):
        if watcherPozitions[j] in foundTasks:
            foundTaskCount[foundTasks.index(watcherPozitions[j])] += 1
        else:
            foundTasks.append(watcherPozitions[j])
            foundTaskCount.append(1)


    totalCommonTasks = 0
    for j in range(0, len(foundTasks)):
        if foundTaskCount[j] >= 2:
            totalCommonTasks += foundTaskCount[j]

    print("Total common tasks: " + str(totalCommonTasks))
    # for j in range(0, len(foundTasks)):
    #     if foundTaskCount[j] >= sameTasks:
    #         # print(foundTasks)
    #         # print(foundTaskCount)
    #         equal += 1
    #         break

    if totalCommonTasks >= sameTasks:
        # print(foundTasks)
        # print(foundTaskCount)
        newWayEqual += 1

    watcherPozitions = shiftOccupation(tasks, watcherPozitions)
    if watcherPozitions == []:
        break

# print(equal/attempts)
# print(1.0 - equal/attempts)
# print(equal)

print(newWayEqual/attempts)
print(1.0 - newWayEqual/attempts)
print(newWayEqual)
print(attempts - newWayEqual)


print(attempts)