from My_Probability.cyclers import A_Cycler
from My_Probability.evaluators import Evaluator

# same as math2_1.py just slower

important = 3
n = 10
even = 1

importantPpl = []
for i in range(0, important):
    importantPpl.append(i + 1)

# find the important people in the list and check if their positions are correct
def Eval(list):
    # cycle through list
    pos = []
    for i in importantPpl:
        pos.append(list.index(i)+1)
            
    count = 0
    for i in pos:
        if i % 2 == 0:
            count += 1
            
    if count == even:
        return True
    else:
        return False
        
aCycler = A_Cycler(n, n)
eval = Evaluator(aCycler, Eval)
eval.printResults()