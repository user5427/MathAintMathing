
from My_Probability.iterators import Repeatable_iterator, A_iterator, C_iterator
from warnings import deprecated

from My_Probability.cyclers import ICycler



# cycle through all C n k combinations and check if the condition is met
@deprecated("Use C_iterator instead")
def C_Cycle(n, k, condition = lambda x: True, printList = False):
    totalMetConditions = 0
    for i in C_iterator(n, k):
        if printList:
            print(i)
        if condition(i):
            totalMetConditions += 1

    return totalMetConditions

# cycle through all A n k combinations and check if the condition is met
@deprecated("Use A_iterator instead")
def A_Cycle(n, k, condition = lambda x: True, printList = False):
    totalMetConditions = 0
    for i in A_iterator(n, k):
        if printList:
            print(i)
        if condition(i):
            totalMetConditions += 1

# cycle through all n k combinations and check if the condition is met
@deprecated("Use Repeatable_iterator instead")
def Repeatable_Cycle(n, k, condition = lambda x: True, printList = False):
    totalMetConditions = 0
    for i in Repeatable_iterator(n, k):
        if printList:
            print(i)
        if condition(i):
            totalMetConditions += 1

    return totalMetConditions

# iterate through the ICycler and check if the condition is met

@deprecated("Use Evaluate class instead")
def Checker(a: "ICycler", condition = lambda x: True, printList = False):
    totalMetConditions = 0
    for i in a.giveNext():
        if printList:
            print(i)
        if condition(i):
            totalMetConditions += 1

    return totalMetConditions