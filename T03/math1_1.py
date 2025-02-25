


from My_Probability.deprecated_combinations import Checker
from My_Probability.cyclers import Repeatable_Cycler
from My_Probability.count_calculators import Repeatable

n = 13

def x1x2x3(list):
    if (list[0] < list[1] and list[1] < list[2]):
        print(list)
        return True
    else:
        return 

repeatable = Repeatable_Cycler(n, 3)
total = Repeatable(n, 3)
found = Checker(repeatable, x1x2x3)
print(found)
print(found/total)
print(total)