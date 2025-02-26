
from My_Probability.cyclers import C_Cycler, Repeatable_Cycler
from My_Probability.evaluators import DecisionalEvaluator


n = 12
x = 22


def SumLargerThanX(list):
    # two elements
    if list[0] + list[1] > x:
        return True
    return False

def FirstEvenSumLargerThanX(list):
    # two elements
    if list[0] % 2 == 0 and list[0] + list[1] > x:
        print(list)
        return True
    return False

cycler = Repeatable_Cycler(n, 2)
evaluated = DecisionalEvaluator(cycler, FirstEvenSumLargerThanX)
evaluated.printResults()