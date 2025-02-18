from My_Probability.cyclers import ICycler

class Evaluator():
    def __init__(self, a: "ICycler", condition = lambda x: True):
        self.a = a
        self.condition = condition
        self.totalMetConditions = 0
        self.evaluated = False
        self.total = 0
        self.totalMetConditions = 0
        
    def Evaluate(self, printList = False):
        visualization = ['\\', '|', '/', '-']
        visualizationTime = 40000
        visualizationCurrent = 0
        vizIndex = 0
        statusTime = 0
        self.total = self.a.getTotal()
            
        totalMetConditions = 0
        for i in self.a.giveNext():
            if printList:
                print(i)
            else:
                visualizationCurrent += 1
                if visualizationCurrent == visualizationTime:
                    visualizationCurrent = 0
                    
                    print(visualization[vizIndex], statusTime * visualizationTime / self.total, end = '\r')
                    
                    statusTime += 1
                    vizIndex += 1
                    if vizIndex == 4:
                        vizIndex = 0
            if self.condition(i):
                totalMetConditions += 1

        self.totalMetConditions = totalMetConditions
        self.evaluated = True
        return totalMetConditions

    def getResults(self):
        return self.totalMetConditions, self.total
    
    def printResults(self):
        if not self.evaluated:
            print("Evaluator has not been evaluated yet.")
            print("Evaluating automatically...")
            self.Evaluate()
            
        print("Total Met Conditions: ", self.totalMetConditions)
        print("Total: ", self.total)
        print("Probability: ", self.totalMetConditions / self.total)
        print("Opposite Probability: ", 1 - self.totalMetConditions / self.total)