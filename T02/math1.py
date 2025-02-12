from My_Probability.combinations import Checker
from My_Probability.multiplier import Repeatable_Cycler
from My_Probability.static_calculation import Repeatable

accuracyImprovment = 0.1
accuracyMultiplier = 1 / accuracyImprovment

distance = 61 * accuracyMultiplier
distanceToCafe = 18 * accuracyMultiplier
distanceToService = 37 * accuracyMultiplier



inRangeOfService = (distanceToCafe + distanceToService) / 2

# 1 question

def isServiceCloser(list):
    # this list will only contain one element
    stopDistance = list[0]
    if stopDistance > inRangeOfService:
        return True
    else:
        return False


# r_cycle = Repeatable_Cycler(distance, 1)
# total = Repeatable(distance, 1)
# found = Checker(r_cycle, isServiceCloser, True)
# print(found)
# print(found / total)

# 2 question

def areAnyCloser(list):
    for i in list:
        if i > inRangeOfService:
            return True
    return False

def bothFurther(list):
    if list[0] > inRangeOfService and list[1] > inRangeOfService:
        return True
    else:
        return False

r_cycle = Repeatable_Cycler(distance, 2)
total = Repeatable(distance, 2)
found = Checker(r_cycle, areAnyCloser, True)
print(found)
print(found / total)






