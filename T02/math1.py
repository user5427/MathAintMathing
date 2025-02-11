from My_Probability.combinations import Checker
from My_Probability.multiplier import Repeatable_Cycler
from My_Probability.static_calculation import Repeatable

distance = 157
distanceToCafe = 71
distanceToService = 37

accuracyImprovment = 0.1
accuracyMultiplier = 1 / accuracyImprovment

distanceBetweenCafeAndService = distanceToCafe - distanceToService
inRangeOfService = distanceToService + distanceBetweenCafeAndService // 2
if (distanceBetweenCafeAndService % 2 == 0):
    inRangeOfService -= 1

# 1 question

def isServiceCloser(list):
    # this list will only contain one element
    stopDistance = list[0]
    if stopDistance <= inRangeOfService:
        return True
    else:
        return False


# r_cycle = Repeatable_Cycler(distance, 1)
# total = Repeatable(distance, 1)
# found = Checker(r_cycle, isServiceCloser, True)
# print(found)
# print(found / total)

# 2 question
accuracyMultiplier = 1
def areAnyCloser(list):
    for i in list:
        if i <= inRangeOfService * accuracyMultiplier:
            return True
    return False

def bothFurther(list):
    if list[0] > inRangeOfService * accuracyMultiplier and list[1] > inRangeOfService * accuracyMultiplier:
        return True
    else:
        return False

r_cycle = Repeatable_Cycler(distance * accuracyMultiplier, 2)
total = Repeatable(distance * accuracyMultiplier, 2)
found = Checker(r_cycle, bothFurther, True)
print(found)
print(found / total)






