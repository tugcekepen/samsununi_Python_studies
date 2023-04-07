def sayi_en_kucuk_sayi(sayi):
    """
    >>> sayi_en_kucuk_sayi(5768)
    [8, 7, 6, 5]
    >>> sayi_en_kucuk_sayi(13256)
    [6, 5, 3, 2, 1]
    """
    x=str(sayi)
    liste=[]
    for i in x:
        liste.append(int(i))
    liste.sort(reverse=True)
    return liste

print(sayi_en_kucuk_sayi(5678))
print(sayi_en_kucuk_sayi(555423579021))

if __name__=='__main__':
    import doctest
    doctest.testmod()

