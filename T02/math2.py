from math import ceil

from My_Probability.combinations import Checker
from My_Probability.multiplier import Repeatable_Cycler
from My_Probability.static_calculation import Repeatable

aSendingTime = 8
bSendingTime = 6
gSendingTime = 10

turningOnTime = 4

# bent viena zinute
def findTimes(list):
    time = list[0]

    timeToA = (time // aSendingTime + (1 if time % aSendingTime > 0 else 0)) * aSendingTime - time
    timeToB = (time // bSendingTime + (1 if time % bSendingTime > 0 else 0)) * bSendingTime - time
    timeToG = (time // gSendingTime + (1 if time % gSendingTime > 0 else 0)) * gSendingTime - time

    if (timeToA <= turningOnTime and timeToA > 0) or (timeToB <= turningOnTime and timeToB > 0) or (timeToG <= turningOnTime and timeToG > 0):
        print(time, timeToA, timeToB, timeToG)
        return True
    else:
        return False


# tik viena zinute u laikotarpyje
def certainCountOfMessages(list):
    time = list[0]

    timeToA = (time // aSendingTime + (1 if time % aSendingTime > 0 else 0)) * aSendingTime - time
    timeToB = (time // bSendingTime + (1 if time % bSendingTime > 0 else 0)) * bSendingTime - time
    timeToG = (time // gSendingTime + (1 if time % gSendingTime > 0 else 0)) * gSendingTime - time

    count = 0
    if (timeToA <= turningOnTime and timeToA > 0):
        count += 1

    if (timeToB <= turningOnTime and timeToB > 0):
        count += 1

    if (timeToG <= turningOnTime and timeToG > 0):
        count += 1

    if (count == 2):
        print(time, timeToA, timeToB, timeToG)
        return True
    else:
        return False

time = 480
repeatable = Repeatable_Cycler(time, 1)
total = Repeatable(time, 1)
found = Checker(repeatable, certainCountOfMessages, False)
print(found)
print(found / total)




