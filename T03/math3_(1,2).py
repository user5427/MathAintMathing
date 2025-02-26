import multiprocessing

n = 7 # stops
m = 7 # passangers
k = 4 # stops where no one gets off
    
def OneOrMOreStopWhereNoOneGetsOff(list):
        stops = []
        for i in range(0, n):
            stops.append(0)
            
            
        for i in list:
            stops[i-2] += 1
            
        emptyStops = 0
        for i in stops:
            if i == 0:
                emptyStops += 1
                
        if emptyStops >= 1: # change based on desired stops
            return True
        return False

if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    from My_Probability.cyclers import Repeatable_Cycler
    from My_Probability.evaluators import DecisionalEvaluator, MultiThreadedEvaluator



#     import matplotlib.pyplot as plt

    

    # repeatable = Repeatable_Cycler(n, m)
    # evaluated = Evaluator(repeatable, OneOrMOreStopWhereNoOneGetsOff)
    # evaluated.printResults()


    # results = []
    # stops_range = range(1, 9)

    # for cyc in stops_range:
    #     n = cyc
    #     repeatable = Repeatable_Cycler(n, m)
    #     evaluated = Evaluator(repeatable, OneOrMOreStopWhereNoOneGetsOff)
    #     evaluated.Evaluate()
    #     result, total = evaluated.getResults()
    #     results.append(result / total)

    # plt.plot(stops_range, results, marker='o')
    # plt.xlabel('Number of Stops')
    # plt.ylabel('Probability')
    # plt.title('Probability of One or More Stops Where No One Gets Off')
    # plt.grid(True)
    # plt.show()

# n = 4 # stops
# m = 5 # passangers
# k = 4 # stops where no one gets off
    
# def OneOrMOreStopWhereNoOneGetsOff(list):
#         stops = []
#         for i in range(0, n):
#             stops.append(0)
            
#         for i in list:
#             stops[i-1] += 1
            
#         emptyStops = 0
#         for i in stops:
#             if i == 0:
#                 emptyStops += 1
                
#         if emptyStops >= 1: # change based on desired stops
#             return True
#         return False


    repeatable = Repeatable_Cycler(n, m)
    evaluated = MultiThreadedEvaluator(repeatable, OneOrMOreStopWhereNoOneGetsOff)
    evaluated.printResults()
            
            #0.9891