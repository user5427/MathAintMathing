from My_Probability.cyclers import Repeatable_Cycler
from My_Probability.evaluators import Evaluator

# NOTICE. THE CODE BELOW MAY NOT ACCURATELY REPRESENT REQUIREMENTS.

n = 4


AWinNum = 12
BWinNum = 3

def Eval(list):
    sums = []
    for i in range(0, n):
        sums.append(list[i*2] + list[i*2 + 1])
        
    # for i in sums:
    #     if i == AWinNum:
    #         return True
    #     elif i == BWinNum:
    #         return False
    # return False
    
    # if last sum is AWinNum
    if sums[-1] == AWinNum:
        return True
    else:
        return False
    
# def OnlyAWins(list):
#     sums = []
#     for i in range(0, n):
#         sums.append(list[i*2] + list[i*2 + 1])
        
#     for i in sums:
#         if i == AWinNum:
#             return True
#         if i == BWinNum:
#             return False
#     return False
    
repeatable = Repeatable_Cycler(6, n*2)
evaluated = Evaluator(repeatable, Eval)
evaluated.printResults()
     