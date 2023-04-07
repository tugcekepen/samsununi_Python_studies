def harf(strHarf):
    """
    >>> harf('a')
    True
    >>> harf('b')
    False
    >>> harf('e')
    True
    >>> harf('c')
    False
    """

    if (strHarf=="a" or strHarf=="e" or strHarf=="i"or strHarf=="ı" or strHarf=="o" or strHarf=="ö" or strHarf=="u" or strHarf=="ü"):
        return True
    else:
        return False


if __name__=="__main__":
    import doctest
    doctest.testmod()

