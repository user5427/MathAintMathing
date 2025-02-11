from abc import ABC, abstractmethod
from typing import List

from My_Probability.iterators import A_iterator, C_iterator, Repeatable_iterator

class ICycler(ABC):

    @abstractmethod
    def giveNext(self) -> List[int]:
        pass

    @abstractmethod
    def reset(self):
        pass


class A_Cycler(ICycler):
    def __init__(self, n, k):
        self.iterator = A_iterator(n, k)  # Store generator
        self.n = n
        self.k = k

    def reset(self):
        self.iterator = A_iterator(self.n, self.k)

    def giveNext(self):
        yield from self.iterator


class C_Cycler(ICycler):
    def __init__(self, n, k):
        self.iterator = C_iterator(n, k)
        self.n = n
        self.k = k

    def reset(self):
        self.iterator = C_iterator(self.n, self.k)

    def giveNext(self):
        yield from self.iterator


class Repeatable_Cycler(ICycler):
    def __init__(self, n, k):
        self.iterator = Repeatable_iterator(n, k)
        self.n = n
        self.k = k

    def reset(self):
        self.iterator = Repeatable_iterator(self.n, self.k)

    def giveNext(self):
        yield from self.iterator


class Multiplier(ICycler):
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


