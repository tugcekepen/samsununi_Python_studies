def is_divisible(x,y):
    return x%y==0

def is_even(x):
    """
    >>> is_even(2)
    True
    >>> is_even(5)
    False
    >>> is_even(7)
    False
    >>> is_even(100)
    True
    """

    return is_divisible(x,2)

def is_15(x):
    """
    >>> is_15(30)
    True
    >>> is_15(90)
    True
    >>> is_15(45)
    True
    >>> is_15(24)
    False
    """
    
    return is_divisible(x,5) and is_divisible(x,3)

if __name__=="__main__":
    import doctest
    doctest.testmod()
