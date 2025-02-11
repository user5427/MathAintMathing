# width in cm
from My_Probability.combinations import Checker
from My_Probability.multiplier import Repeatable_Cycler
from My_Probability.static_calculation import Repeatable

width = 100
turtleWidth = 11

choises = width - turtleWidth

# we have two turtles

def turtleCollision(list):
    if (list[0]-1) // turtleWidth == (list[1]-1) // turtleWidth:
        return True
    else:
        return False

r_cycle = Repeatable_Cycler(choises, 2)
total = Repeatable(choises, 2)
found = Checker(r_cycle, turtleCollision, True)
print(found)
print(found / total)

