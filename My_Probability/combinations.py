
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

# cycle trough all C n k combinations and check if the condition is met


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

# cycle trough all A n k combinations and check if the condition is met


def A_Cycle(n, k, condition = lambda x: True, printList = False):
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
        if total == A(n, k) - 1:
            break

        # increment the last element if possible, otherwise increment the previous element, and so on
        if list[k-1] + 1 > n:
            checkingPosition = 0
            while checkingPosition < k:
                if list[k - checkingPosition - 1] + 1 > n - checkingPosition:
                    checkingPosition += 1
                    list[k - checkingPosition - 1] = 0
                else:
                    list[k - checkingPosition - 1] += 1
                    break
        else:
            list[k - 1] += 1

        total += 1

    return totalMetConditions