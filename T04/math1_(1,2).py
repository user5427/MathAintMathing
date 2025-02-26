
from My_Probability.cyclers import C_Cycler, Repeatable_Cycler
from My_Probability.evaluators import DecisionalEvaluator, Evaluator


n = 12
x = 22


def SumLargerThanX(list):
    # two elements
    if list[0] + list[1] > x:
        return True
    return False

def FirstEvenSumLargerThanX(list):
    if list[0] % 2 == 1:
        return -1
    
    # two elements
    if list[0] % 2 == 0 and list[0] + list[1] > x:
        print(list)
        return 1
    return 0

cycler = Repeatable_Cycler(n, 2)
evaluated = DecisionalEvaluator(cycler, FirstEvenSumLargerThanX)
evaluated.printResults()