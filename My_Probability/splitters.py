
import math

from My_Probability.count_calculators import C, Repeatable
from My_Probability.cyclers import A_Cycler


def RepeatableListSplit(n, k, splits):
    splitLengths = Repeatable(n, k) // splits
    if splitLengths == 0:
        list = []
        for i in range(0, splits):
            list.append(0)
        return [(list, Repeatable(n, k))]
    
    splitLists = []
    
    startingValue = 1
    for i in range(0, splits):
        # convert the starting value to the n number system
        splitList = []
        temp = startingValue
        for j in range(0, k):
            splitList.append(temp % n)
            temp = temp // n
        splitList.reverse()
        splitLists.append((splitList, splitLengths))
        startingValue += splitLengths
        
    # check if the division was not perfect
    if startingValue != Repeatable(n, k):
        splitLists[-1] = (splitLists[-1][0], splitLists[-1][1] + (Repeatable(n, k) - startingValue))
        
    return splitLists
        
def AListSplit(n, k, splits):
    toupleDepth = math.ceil(splits / n)
    if toupleDepth > k:
        toupleDepth = k
        splits = n * k
        
    a_cycler = A_Cycler(n, toupleDepth)
    combinations = []
    for i in a_cycler.giveNext():
        combinations.append(i)
        
    # now just divide the combinations into the splits
    # NOTICE : THIS USES THE SIMPLE SPLITTING METHOD
    splitLists = []
    # ONLY MOVE THE ELEMENTS IN splits count of lists
    # EXAMPLE
    # [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4]]
    # 3 splits
    # [[1, 2], [1, 3]]
    # [[2, 1], [1, 4]]
    # [[2, 4], [2, 3]]
    
    for i in range(0, splits):
        splitLists.append([])
        
    for i in range(0, len(combinations)):
        splitLists[i % splits].append(combinations[i])
        
    return splitLists


def CListSplit(n, k, splits):
    list = []
    for i in range(0, k):
        list.append(i+1)
        
    splitLengths = C(n, k) // splits
        
    splitLists = []
    copy = list.copy()
    splitLists.append((copy, 0))
    while len(splitLists) <= splits:
        weights = []
        for i in range(0, k):
            element = list[k - i - 1]
            weight = C(n - element+1, i+1)
            weights.append(weight)
            
        # weights.reverse()
        # print(weights)
        # break
        changePosition = k - 1
        weight = 0
        for i in weights:
            if i >= splitLengths:
                changePosition -= 1
                weight = i
                break
            changePosition -= 1
            
        if changePosition >= 0:
            startingElement = list[changePosition]
            increment = 1
            for i in range(changePosition, k):
                list[i] = startingElement + increment
                increment += 1
                
            copy = list.copy()
            splitLists.append((copy, weight))
        else:
            break
        
    # fix the count by moving the count from second element to the first touple. calculate the count for the last touple by using C(n, k) - sum of all other counts
    sum = 0
    for i in range(1, len(splitLists)):
        splitLists[0] = (splitLists[0][0], splitLists[i][1])
        sum += splitLists[i][1]
        
    totalForLast = C(n, k) - sum
    splitLists[-1] = (splitLists[-1][0], totalForLast)
        
        
    return splitLists
