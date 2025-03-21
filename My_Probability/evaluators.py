from My_Probability.cyclers import ICycler
import multiprocessing
from My_Probability.cyclers import C_Cycler, Repeatable_Cycler, A_Cycler
from My_Probability.splitters import AListSplit, CListSplit, RepeatableListSplit
from abc import ABC, abstractmethod
from typing import List

def worker_C_Cycler(args):
    n, k, sublist, condition = args
    newCycler = C_Cycler(n, k, sublist)
    count = 0
    for i in newCycler.giveNext():
        if condition(i):
            count += 1
    return count

def worker_Repeatable_Cycler(args):
    n, k, sublist, condition = args
    newCycler = Repeatable_Cycler(n, k, sublist)
    count = 0
    for i in newCycler.giveNext():
        if condition(i):
            count += 1
    return count

def worker_A_Cycler(args):
    n, k, sublist, condition = args
    newCycler = A_Cycler(n, k, sublist)
    count = 0
    for i in newCycler.giveNext():
        if condition(i):
            count += 1
    return count


class IDecision(ABC):
    @abstractmethod
    def Decide(self, list: List[int], condition: "function") -> (int, int):
        pass
    
    @abstractmethod
    def Reset(self, total):
        pass
    
    @abstractmethod
    def GetResults(self):
        pass
    
class Decision(IDecision):
    def __init__(self, total):
        self.total = total
        self.good = 0
        super().__init__()
        
    def Reset(self, total):
        self.total = total
        self.good = 0
        
    def Decide(self, list: List[int], condition: "function") -> (int, int):
        if condition(list):
            self.good += 1
    
    def GetResults(self):
        return self.good, self.total
        
        
    
    

class MultiThreadedEvaluator():
    def __init__(self, a: "ICycler", condition = lambda x: True):
        self.a = a
        self.condition = condition
        self.totalMetConditions = 0
        self.total = 0
        self.Evaluated = False
        self.n, self.k = self.a.getParameters()
        
    def Evaluate(self):
        cpuCount = multiprocessing.cpu_count()
        
        
        if isinstance(self.a, C_Cycler):
            listSeparation = CListSplit(self.n, self.k, cpuCount)
            self.total = self.a.getTotal()
            # ok so the list contains seperate lists for each seperate thread where cycles are split
            # now we need to create the threads and run them
            
            with multiprocessing.Pool(cpuCount) as pool:
                results = pool.map(worker_C_Cycler, [(self.n, self.k, sublist, self.condition) for sublist in listSeparation])

            self.totalMetConditions = sum(results)
            
        elif isinstance(self.a, Repeatable_Cycler):
            listSeparation = RepeatableListSplit(self.n, self.k, cpuCount)
            self.total = self.a.getTotal()
            
            with multiprocessing.Pool(cpuCount) as pool:
                results = pool.map(worker_Repeatable_Cycler, [(self.n, self.k, sublist, self.condition) for sublist in listSeparation])
                
            self.totalMetConditions = sum(results)

        elif isinstance(self.a, A_Cycler):
            listSeparation = AListSplit(self.n, self.k, cpuCount)
            self.total = self.a.getTotal()
            
            with multiprocessing.Pool(cpuCount) as pool:
                results = pool.map(worker_A_Cycler, [(self.n, self.k, sublist, self.condition) for sublist in listSeparation])
                
            self.totalMetConditions = sum(results)
        else:
            print("ICycler is of an unknown type")
            return
        
    def getResults(self):
        return self.totalMetConditions, self.total
    
    def printResults(self):
        if not self.Evaluated:
            print("Evaluator has not been evaluated yet.")
            print("Evaluating automatically...")
            self.Evaluate()
            
        resultPrinter(self.total, self.totalMetConditions)
        

class Evaluator():
    def __init__(self, a: "ICycler", condition = lambda x: True):
        self.a = a
        self.condition = condition
        self.totalMetConditions = 0
        self.evaluated = False
        self.total = 0
        
    def Evaluate(self):
        visualization = ['\\', '|', '/', '-']
        visualizationTime = 40000
        visualizationCurrent = 0
        vizIndex = 0
        statusTime = 0
        self.total = self.a.getTotal()
            
        totalMetConditions = 0
        for i in self.a.giveNext():
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
            
        resultPrinter(self.total, self.totalMetConditions)
        



class DecisionalEvaluator():
    """
    This class is used to evaluate a given ICycler object with a given condition.
    The condition is a function that takes a list of integers and returns a boolean.
    1 -> True
    -1 -> Reduce the total by 1
    0 -> False
    """
    def __init__(self, a: "ICycler", condition = lambda x: True):
        self.a = a
        self.condition = condition
        self.totalMetConditions = 0
        self.evaluated = False
        self.total = 0
        
    def Evaluate(self):
        visualization = ['\\', '|', '/', '-']
        visualizationTime = 40000
        visualizationCurrent = 0
        vizIndex = 0
        statusTime = 0
        self.total = self.a.getTotal()
        temp = self.total
            
        totalMetConditions = 0
        for i in self.a.giveNext():
            visualizationCurrent += 1
            if visualizationCurrent == visualizationTime:
                visualizationCurrent = 0
                
                print(visualization[vizIndex], statusTime * visualizationTime / self.total, end = '\r')
                
                statusTime += 1
                vizIndex += 1
                if vizIndex == 4:
                    vizIndex = 0
            if self.condition(i) == 1:
                totalMetConditions += 1
            elif self.condition(i) == -1:
                temp -= 1

        self.totalMetConditions = totalMetConditions
        self.total = temp
        self.evaluated = True
        return totalMetConditions

    def getResults(self):
        return self.totalMetConditions, self.total
    
    def printResults(self):
        if not self.evaluated:
            print("Evaluator has not been evaluated yet.")
            print("Evaluating automatically...")
            self.Evaluate()
            
        resultPrinter(self.total, self.totalMetConditions)
        
        
        
        
        
def resultPrinter(total, totalMetConditions):
    print("Total Met Conditions: ", totalMetConditions)
    print("Total: ", total)
    print("Probability: ", totalMetConditions / total)
    print("Opposite Probability: ", 1 - totalMetConditions / total)