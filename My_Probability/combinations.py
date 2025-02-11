
# C n k calculation


def C(n, k):
    if k == 0 or k == n:
        return 1
    return C(n - 1, k - 1) + C(n - 1, k)

# A n k calculation


def A(n, k):
    if k == 0:
        return 1
    return n * A(n - 1, k - 1)

# N ^ k calculation


def Repeatable(n, k):
    return n ** k


# cycle through all C n k combinations and check if the condition is met


def C_Cycle(n, k, condition = lambda x: True, printList = False):
    list = []
    for i in range(0, k):
        list.append(i + 1)

    totalMetConditions = 0

    while True:
        if printList:
            print(list)

        # check if the condition is met
        if condition(list):
            totalMetConditions += 1

        # check if the last element is the last possible element
        if list[0] == n - k + 1:
            break

        # increment the last element if possible, otherwise increment the previous element, and so on
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

    return totalMetConditions

# cycle through all A n k combinations and check if the condition is met
# this function is not optimized and is very slow for large n and k


def A_Cycle(n, k, condition = lambda x: True, printList = False):
    list = []
    for i in range(0, n):
        list.append(i + 1)

    def recursiveSearcher(list, newlist, condition, depth):
        if depth == 0:
            if printList:
                print(newlist)
            if condition(newlist):
                return 1
            else:
                return 0
        depth -= 1

        sum = 0
        for i in range(0, len(list)):
            listSmaller = list.copy()
            listSmaller.remove(list[i])
            newerList = newlist.copy()
            newerList.append(list[i])
            sum += recursiveSearcher(listSmaller, newerList, condition, depth)
        return sum

    return recursiveSearcher(list, [], condition, k)

# cycle through all n k combinations and check if the condition is met


def Repeatable_Cycle(n, k, condition = lambda x: True, printList = False):
    list = []
    for i in range(0, k):
        list.append(0)

    totalMetConditions = 0
    total = 0
    while True:
        if printList:
            print(list)

        # check if the condition is met
        if condition(list):
            totalMetConditions += 1

        # check if the last element is the last possible element
        if total == Repeatable(n, k) - 1:
            break

        # increment the last element if possible, otherwise increment the previous element, and so on
        if list[k-1] + 1 >= n:
            checkingPosition = 0
            while checkingPosition < k:
                if list[k - checkingPosition - 1] + 1 >= n and k - checkingPosition - 1 != 0:
                    list[k - checkingPosition - 1] = 0
                    checkingPosition += 1
                else:
                    list[k - checkingPosition - 1] += 1
                    break
        else:
            list[k - 1] += 1

        total += 1

    return totalMetConditions
