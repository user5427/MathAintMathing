from abc import ABC, abstractmethod
from typing import List

from My_Probability.iterators import A_iterator, C_iterator, Repeatable_iterator
from My_Probability.count_calculators import A, C, Repeatable

class ICycler(ABC):

    @abstractmethod
    def giveNext(self) -> List[int]:
        pass

    @abstractmethod
    def reset(self):
        pass
    
    @abstractmethod
    def getTotal(self):
        pass
    
    @abstractmethod
    def getParameters(self):
        pass


class A_Cycler(ICycler):
    def __init__(self, n, k, startingList = None):
        self.iterator = A_iterator(n, k, startingList)  # Store generator
        self.n = n
        self.k = k
        self.startingList = startingList

    def reset(self):
        self.iterator = A_iterator(self.n, self.k, self.startingList)

    def giveNext(self):
        yield from self.iterator
        
    def getTotal(self):
        return A(self.n, self.k)
    
    def getParameters(self):
        return self.n, self.k


class C_Cycler(ICycler):
    def __init__(self, n, k, startingList = None):
        self.iterator = C_iterator(n, k, startingList)
        self.n = n
        self.k = k
        self.startingList = startingList

    def reset(self):
        self.iterator = C_iterator(self.n, self.k, self.startingList)

    def giveNext(self):
        yield from self.iterator
        
    def getTotal(self):
        return C(self.n, self.k)
    
    def getParameters(self):
        return self.n, self.k


class Repeatable_Cycler(ICycler):
    def __init__(self, n, k, startingList = None):
        self.iterator = Repeatable_iterator(n, k, startingList)
        self.n = n
        self.k = k
        self.startingList = startingList

    def reset(self):
        self.iterator = Repeatable_iterator(self.n, self.k, self.startingList)

    def giveNext(self):
        yield from self.iterator
        
    def getTotal(self):
        return Repeatable(self.n, self.k)
    
    def getParameters(self):
        return self.n, self.k


class CombinationGenerator(ICycler):
    def __init__(self, a: "ICycler", b: "ICycler" = None):
        self.a = a
        self.b = b

    def giveNext(self) -> List[int]:
        if self.b is None:
            yield from self.a.giveNext()
        else:
            for i in self.a.giveNext():
                for j in self.b.giveNext():
                    yield i + j

                self.b.reset()

    def reset(self):
        if self.b is None:
            self.a.reset()
        else:
            self.a.reset()
            self.b.reset()
            
    def getTotal(self):
        if self.b is None:
            return self.a.getTotal()
        else:
            return self.a.getTotal() * self.b.getTotal()


