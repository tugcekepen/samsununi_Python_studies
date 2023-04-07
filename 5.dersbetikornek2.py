def bolme(number):
    """
    >>> bolme(5)
    no
    >>> bolme(6)
    ok
    >>> bolme(4)
    ok
    >>> bolme(9)
    ok
    """

    if (number % 2 == 0 or number % 3 == 0):
        print("ok")
    else :
        print("no")

    return 

if __name__ == '__main__':
    import doctest
    doctest.testmod()
