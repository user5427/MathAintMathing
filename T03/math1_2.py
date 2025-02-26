from My_Probability.cyclers import Repeatable_Cycler
from My_Probability.evaluators import Evaluator


n = 13

def Equal(list):
    if (list[0] == list[1] or list[1] == list[2] or list[0] == list[2]):
        return True
    else:
        return False
    
repeatabl = Repeatable_Cycler(n, 3)
evaluated = Evaluator(repeatabl, Equal)
evaluated.printResults()

