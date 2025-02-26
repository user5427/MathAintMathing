from My_Probability.cyclers import Repeatable_Cycler
from My_Probability.evaluators import DecisionalEvaluator


n = 14
m = 12

# list contains only 0 and 1
def Shorten(list):
    copyList = list.copy()
    # remove all 0s from the end and the beginning
    while copyList and copyList[0] == 1:
        copyList.pop(0)
    while copyList and copyList[-1] == 1:
        copyList.pop(-1)
        
    # check if the list length is equal to m
    if len(copyList) > m:
        return True
    return False

repeatable = Repeatable_Cycler(2, n)
evaluated = DecisionalEvaluator(repeatable, Shorten)
evaluated.printResults()