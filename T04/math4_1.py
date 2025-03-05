from My_Probability.cyclers import Repeatable_Cycler
from My_Probability.evaluators import Evaluator


p = 12
p1 = 96
p2 = 9

resolution = 20
# calculates A - the sum of all positivities
def possitiveTest(list):
    if list[0] / resolution > p and list[1] / resolution <= p2:
        return True
    if list[0] / resolution <= p and list[1] / resolution <= p1:
        return True
    
    return False

cycler = Repeatable_Cycler(100 * resolution, 2)
evaluated = Evaluator(cycler, possitiveTest)
evaluated.printResults()