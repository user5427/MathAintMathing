from My_Probability.cyclers import Repeatable_Cycler
from My_Probability.evaluators import Evaluator


m = 17
n = 4

def CWillGetLessBadMessagesThanA(list):
    cGood = m
    cBad = n
    
    if (list[0] <= m):
        cGood -= 1
    else:
        cBad -= 1
        
    cGood += 1
    
    if (list[1] <= m):
        cGood -= 1
    else:
        cBad -= 1
        
    cGood += 1
    
    if (cBad < n):
        return True
    return False

repeatable = Repeatable_Cycler(n+m, 2)
evaluated = Evaluator(repeatable, CWillGetLessBadMessagesThanA)
evaluated.printResults()