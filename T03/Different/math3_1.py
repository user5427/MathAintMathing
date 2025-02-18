from My_Probability.cyclers import Repeatable_Cycler
from My_Probability.evaluators import Evaluator


n = 5

AWins = True
BWins = False

AWinNum = 5
BWinNum = 7

def Eval(list):
    sums = []
    for i in range(0, n):
        sums.append(list[i*2] + list[i*2 + 1])
        
    for i in sums:
        if i == AWinNum:
            if not AWins:
                return False
            return True
        if i == BWinNum:
            if not BWins:
                return False
            return True
    return False
    
def OnlyAWins(list):
    sums = []
    for i in range(0, n):
        sums.append(list[i*2] + list[i*2 + 1])
        
    for i in sums:
        if i == AWinNum:
            return True
        if i == BWinNum:
            return False
    return False
    
repeatable = Repeatable_Cycler(6, n*2)
evaluated = Evaluator(repeatable, Eval)
evaluated.printResults()
     