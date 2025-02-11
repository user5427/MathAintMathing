from My_Probability.static_calculation import Repeatable


# cycle through all C n k combinations


def C_iterator(n, k):
    list = []
    for i in range(0, k):
        list.append(i + 1)

    while True:
        yield list

        if list[0] == n - k + 1:
            break

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

# cycle through all A n k combinations
# this function is not optimized and is very slow for large n and k


def A_iterator(n, k):
    numbers = list(range(1, n + 1))

    def recursiveSearcher(remaining, newlist, depth):
        if depth == 0:
            yield newlist  # Yield the completed combination
            return

        for i in range(len(remaining)):
            smaller_list = remaining[:i] + remaining[i + 1:]  # Remove the selected element
            yield from recursiveSearcher(smaller_list, newlist + [remaining[i]], depth - 1)

    yield from recursiveSearcher(numbers, [], k)  # Start recursion

# cycle through all Repeatable n k combinations


def Repeatable_iterator(n, k):
    list = []
    for i in range(0, k):
        list.append(0+1)

    total = 0
    while True:
        yield list

        # check if the last element is the last possible element
        if total == Repeatable(n, k) - 1:
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

        total += 1


