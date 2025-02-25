from math import factorial



def C(n, k):
    """_summary_
    Calculate n! / (k! * (n - k)!)
    
    Args:
        n (_type_): _description_
        k (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    return factorial(n) // (factorial(k) * factorial(n - k))


def A(n, k):
    """_summary_
    Calculate n! / (n - k)!

    Args:
        n (_type_): _description_
        k (_type_): _description_

    Returns:
        _type_: _description_
    """
    if k == 0:
        return 1
    return n * A(n - 1, k - 1)


def Repeatable(n, k):
    """_summary_
    Calculate n^k
    
    Args:
        n (_type_): _description_
        k (_type_): _description_

    Returns:
        _type_: _description_
    """
    return n ** k


