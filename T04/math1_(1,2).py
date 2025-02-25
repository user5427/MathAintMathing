
from My_Probability.cyclers import C_Cycler
from My_Probability.evaluators import Evaluator


n = 10
x = 14


def SumLargerThanX(list):
    # two elements
    if list[0] + list[1] > x:
        return True
    return False

def FirstEvenSumLargerThanX(list):
    # two elements
    if list[0] % 2 == 0 and list[0] + list[1] > x:
        return True
    return False

cycler = C_Cycler(n, 2)
evaluated = Evaluator(cycler, FirstEvenSumLargerThanX)
evaluated.printResults()