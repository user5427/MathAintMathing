from My_Probability.cyclers import Repeatable_Cycler
from My_Probability.evaluators import Evaluator


m = 6
n = 6

def CWillGetLessBadMessagesThanA(list):
    cGood = m
    cBad = n
    
    print(list)
    
    if list[0] == 1:
        cGood -= 1
    elif list[0] == 2:
        cBad -= 1
        
    if list[1] == 1:
        cGood -= 1
    elif list[1] == 2:
        cBad -= 1
        
    cGood += 1
    cBad += 1
    
    if cBad < n:
        return True
    return False

repeatable = Repeatable_Cycler(2, 2)
evaluated = Evaluator(repeatable, CWillGetLessBadMessagesThanA)
evaluated.printResults()