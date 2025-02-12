from math import ceil

from My_Probability.combinations import Checker
from My_Probability.multiplier import Repeatable_Cycler
from My_Probability.static_calculation import Repeatable

aSendingTime = 16
bSendingTime = 19
gSendingTime = 11

turningOnTime = 7


def findTimes(list):
    time = list[0]

    timeToA = (time // aSendingTime + (1 if time % aSendingTime > 0 else 0)) * aSendingTime - time
    timeToB = (time // bSendingTime + (1 if time % bSendingTime > 0 else 0)) * bSendingTime - time
    timeToG = (time // gSendingTime + (1 if time % gSendingTime > 0 else 0)) * gSendingTime - time

    if timeToA <= turningOnTime or timeToB <= turningOnTime or timeToG <= turningOnTime:
        print(time, timeToA, timeToB, timeToG)
        return True
    else:
        return False

time = 200
repeatable = Repeatable_Cycler(time, 1)
total = Repeatable(time, 1)
found = Checker(repeatable, findTimes, False)
print(found)
print(found / total)




