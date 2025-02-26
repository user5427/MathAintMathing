from My_Probability.cyclers import A_Cycler
from My_Probability.evaluators import DecisionalEvaluator

# same as math2_1_different.py

important = 3
n = 10
even = 3

# find the important people in the list and check if their positions are correct
def Eval(list):
    count = 0
    for i in list:
        if i % 2 == 0:
            count += 1
            
    if count == even:
        print(list)
        return True
    else:
        return False
        
aCycler = A_Cycler(n, important)
eval = DecisionalEvaluator(aCycler, Eval)
eval.printResults()