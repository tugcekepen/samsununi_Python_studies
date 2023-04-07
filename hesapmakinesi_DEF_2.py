def topla(sayi1, sayi2):
    return sayi1 + sayi2

def cikar(sayi1, sayi2):
    return sayi1 - sayi2
    
def carp(sayi1, sayi2):
    return sayi1 * sayi2

def bol(sayi1, sayi2):
    return sayi1 // sayi2

def HesapMakinesi(fonk, sayi1, sayi2):
    return fonk(sayi1, sayi2)

print(HesapMakinesi(topla, 5, 46))
