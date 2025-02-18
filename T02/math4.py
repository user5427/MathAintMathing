from My_Probability.deprecated_combinations import Checker
from My_Probability.cyclers import Repeatable_Cycler
from My_Probability.static_calculators import Repeatable

multiply = 1

x = 6 * multiply
y = 22 * multiply

timeBetween = 60 * multiply

def willMeetUp(list):
    if (list[0] > list[1] and list[0] - list[1] <= y) or (list[1] > list[0] and list[1] - list[0] <= x) or list[0] == list[1]:
        # print(list)
        return True
    else:
        return False

repeat = Repeatable_Cycler(timeBetween, 2)
total = Repeatable(timeBetween, 2)
found = Checker(repeat, willMeetUp)
print(found)
print(found/total)
