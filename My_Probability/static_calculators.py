
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
