from My_Probability.combinations import Checker
from My_Probability.multiplier import Repeatable_Cycler
from My_Probability.static_calculation import Repeatable

multiply = 1000000

xTo = 11 * multiply
a = 6.8
b = 11.56

def equationCorrect(list):
    x = list[0] / multiply -1
    if (x ** 2 + b > x * a):
        # print("({}) > ({}) where x = {}".format(x**2+b, x*a, x))

        return True
    else:
        return False



repeat = Repeatable_Cycler(xTo, 1)
total = Repeatable(xTo, 1)
found = Checker(repeat, equationCorrect)
print(found)
print(found/total)
