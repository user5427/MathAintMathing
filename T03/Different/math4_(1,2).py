from My_Probability.cyclers import Repeatable_Cycler
from My_Probability.evaluators import Evaluator


n = 6 # stops
m = 9 # passangers
k = 4 # stops where no one gets off

def OneOrMOreStopWhereNoOneGetsOff(list):
    stops = []
    for i in range(0, n):
        stops.append(0)
        
    for i in list:
        stops[i-1] += 1
        
    emptyStops = 0
    for i in stops:
        if i == 0:
            emptyStops += 1
            
    if emptyStops == 4: # change based on desired stops
        return True
    return False

repeatable = Repeatable_Cycler(n, m)
evaluated = Evaluator(repeatable, OneOrMOreStopWhereNoOneGetsOff)
evaluated.printResults()

        
        