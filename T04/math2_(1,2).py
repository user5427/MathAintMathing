from My_Probability.cyclers import C_Cycler
from My_Probability.evaluators import Evaluator


n = 23
m = 6
k = 3

def WillHaveSeatsWithEvenNumeration(list):
    # we have m people
    AllEven = True    
    for i in range(0, len(list)):
        if list[i] % 2 != 0:
            AllEven = False
            break

    return AllEven

cycler = C_Cycler(n, k)
evaluated = Evaluator(cycler, WillHaveSeatsWithEvenNumeration)
evaluated.printResults()