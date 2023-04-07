def en_kucuk(dizi):
    x=[]
    for i in dizi:
        if (i//10 >= 1 and i//10 <= 9):
            x.append(i)
    print(x)
    print(min(x))

en_kucuk([1, 10, 20, 100])
            
