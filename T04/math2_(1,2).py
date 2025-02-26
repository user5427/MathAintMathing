from My_Probability.cyclers import A_Cycler, C_Cycler, Repeatable_Cycler
from My_Probability.evaluators import DecisionalEvaluator, Evaluator


n = 10
m = 3
k = 2

# def WillHaveSeatsWithEvenNumeration(list):
#     # we have m people
#     AllEven = True    
#     for i in range(0, len(list)):
#         if list[i] % 2 != 0:
#             AllEven = False
#             break

#     return AllEven

def FirstKEvenOtherMEven(list):
    # if the first k are not even return - 1
    
    for i in range(0, k):
        if list[i] % 2 != 0:
            return -1
        
    # if the rest are not even return 0
    for i in range(k, len(list)):
        if list[i] % 2 != 0:
            return 0
    
    return 1

cycler = A_Cycler(n, k+m)
evaluated = DecisionalEvaluator(cycler, FirstKEvenOtherMEven)
evaluated.printResults()