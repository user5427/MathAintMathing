from My_Probability.iterators import Repeatable_iterator, A_iterator, C_iterator



# cycle through all C n k combinations and check if the condition is met


def C_Cycle(n, k, condition = lambda x: True, printList = False):
    totalMetConditions = 0
    for i in C_iterator(n, k):
        if printList:
            print(i)
        if condition(i):
            totalMetConditions += 1

    return totalMetConditions

# cycle through all A n k combinations and check if the condition is met


def A_Cycle(n, k, condition = lambda x: True, printList = False):
    totalMetConditions = 0
    for i in A_iterator(n, k):
        if printList:
            print(i)
        if condition(i):
            totalMetConditions += 1

# cycle through all n k combinations and check if the condition is met


def Repeatable_Cycle(n, k, condition = lambda x: True, printList = False):
    totalMetConditions = 0
    for i in Repeatable_iterator(n, k):
        if printList:
            print(i)
        if condition(i):
            totalMetConditions += 1

    return totalMetConditions


