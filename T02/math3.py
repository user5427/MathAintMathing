from My_Probability.deprecated_combinations import Checker
from My_Probability.cyclers import Repeatable_Cycler
from My_Probability.count_calculators import Repeatable

accuracy = 40
totalLength = 100 * accuracy
smallerThan = 22 * accuracy
largerThan = 69 * accuracy

def atLeastOneSmaller(list):
    # in the list we have two dividing points
    # the first dividing point is the first element of the list
    # the second dividing point is the second element of the list
    if list[0] < list[1]:
        smallerX1 = list[0]
        largerX2 = list[1]
    else:
        smallerX1 = list[1]
        largerX2 = list[0]


    if smallerX1 < smallerThan or totalLength - largerX2 < smallerThan or largerX2 - smallerX1 < smallerThan:
        return True
    else:
        return False

def atLeastOneLarger(list):
    if list[0] < list[1]:
        smallerX1 = list[0]
        largerX2 = list[1]
    else:
        smallerX1 = list[1]
        largerX2 = list[0]

    if smallerX1 > largerThan or totalLength - largerX2 > largerThan or largerX2 - smallerX1 > largerThan:
        return True
    else:
        return False


r_cycle = Repeatable_Cycler(totalLength, 2)
total = Repeatable(totalLength, 2)
found = Checker(r_cycle, atLeastOneLarger, False)
print(found)
print(found / total)

