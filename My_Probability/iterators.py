import deprecated
from My_Probability.count_calculators import Repeatable


def C_iterator(n, k, startingList = None, cycles = None):
    """_summary_
    Cycle through all C n k combinations
    
    Args:
        n (_type_): _description_
        k (_type_): _description_
        startingList (_type_, optional): _description_. Defaults to None.
        cycles (_type_, optional): _description_. Defaults to None. Number of cycles to run

    Yields:
        _type_: _description_
    """
    if startingList is not None:
        list = startingList
    else:
        list = []
        for i in range(0, k):
            list.append(i + 1)

    cycl = 0
    while True:
        yield list

        if list[0] == n - k + 1:
            break
        
        if cycles is not None and cycl == cycles:
            break
        
        cycl += 1
        if list[k-1] + 1 > n:
            checkingPosition = 0
            while checkingPosition < k:
                if list[k - checkingPosition - 1] + 1 > n - checkingPosition:
                    checkingPosition += 1
                else:
                    selected = list[k - checkingPosition - 1] + 1
                    for i in range(k - checkingPosition - 1, k):
                        list[i] = selected
                        selected += 1
                    break
        else:
            list[k - 1] += 1
            


def A_iterator(n, k, startingList = None):
    """_summary_
    Cycle through all A n k combinations
    This function is not optimized and is very slow for large n and k
    
    Args:
        n (_type_): _description_
        k (_type_): _description_
        startingList (_type_, optional): _description_. Defaults to None. Pass a list of tuples to start from a specific point

    Yields:
        _type_: _description_
    """
    numbers = list(range(1, n + 1))

    def recursiveSearcher(remaining, newlist, depth):
        if depth == 0:
            yield newlist  # Yield the completed combination
            return

        for i in range(len(remaining)):
            smaller_list = remaining[:i] + remaining[i + 1:]  # Remove the selected element
            yield from recursiveSearcher(smaller_list, newlist + [remaining[i]], depth - 1)

    if startingList is not None:
        firstTouple = startingList[0]
        length = len(firstTouple)
        for i in startingList:
            yield from recursiveSearcher(numbers, i, k - length)
    else:
        yield from recursiveSearcher(numbers, [], k)  # Start recursion


def Repeatable_iterator(n, k, startingList = None, cycles = None):
    """_summary_
    Cycle through all Repeatable n k combinations
    
    Args:
        n (_type_): _description_
        k (_type_): _description_
        startingList (_type_, optional): _description_. Defaults to None.
        cycles (_type_, optional): _description_. Defaults to None. Number of cycles to run

    Yields:
        _type_: _description_
    """
    if startingList is not None:
        list = startingList
    else:
        list = []
        for i in range(0, k):
            list.append(1)

    cycl = 0
    while True:
        yield list

        # check if the last element is the last possible element
        if cycl == Repeatable(n, k) - 1:
            break
        
        if cycles is not None and cycl == cycles:
            break

        # increment the last element if possible, otherwise increment the previous element, and so on
        if list[k - 1] + 1 > n:
            checkingPosition = 0
            while checkingPosition < k:
                if list[k - checkingPosition - 1] + 1 > n and k - checkingPosition - 1 != 0:
                    list[k - checkingPosition - 1] = 1
                    checkingPosition += 1
                else:
                    list[k - checkingPosition - 1] += 1
                    break
        else:
            list[k - 1] += 1

        cycl += 1


