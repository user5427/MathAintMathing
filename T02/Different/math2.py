# width in cm
from My_Probability.deprecated_combinations import Checker
from My_Probability.cyclers import Repeatable_Cycler
from My_Probability.count_calculators import Repeatable

accuracy = 15

width = 100 * accuracy
turtleWidth = 11 * accuracy

choises = width - turtleWidth + 1

# we have two turtles

def turtleCollision(list):
    if (list[0] + turtleWidth) >= list[1] and list[0] <= (list[1] + turtleWidth):
        return True
    else:
        return False

r_cycle = Repeatable_Cycler(choises, 2)
total = Repeatable(choises, 2)
found = Checker(r_cycle, turtleCollision, True)
print(found)
print(found / total)
print(1 - found / total)

# with 1m and d = 11cm the accurate result is 0.7680