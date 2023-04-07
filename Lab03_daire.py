import math

def daire(r):
    alan = math.pi * r**2
    cevre = 2*math.pi*r
    print('''Yarıçapının değerini girdiğiniz dairenin\nAlanı: %s \nÇevresi %s''' %(alan,cevre))

r = int(input("Yarıçap giriniz: "))

daire(r)
