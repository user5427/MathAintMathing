from My_Probability.cyclers import C_Cycler
from My_Probability.evaluators import Evaluator


n = 20
m = 6
k = 2

def WillHaveSeatsWithEvenNumeration(list):
    # we have m people
    
    for i in range(0, len(list)):
        if list[i] % 2 == 0:
            return True
    return False


cycler = C_Cycler(n, m+k)
evaluated = Evaluator(cycler, WillHaveSeatsWithEvenNumeration)
evaluated.printResults()