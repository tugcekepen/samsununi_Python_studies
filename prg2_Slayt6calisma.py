# id() : nesnelerin bellekte tutulduğu yeri söyler
#print(id(5)) veya x=5 tanımlamasından sonra print(id(x)) -> aynı sonucu vereceklerdir.
"""
#while kullanımı -> True False -> şart True döndüğü sürece çalıştır, False döndüğünde döngüyü sonlandır.
def countdown(n):
    while n>0:
        print(n)
        n -= 1
    print("Yok ol!")
countdown(5)
"""
"""
def sequence(n):
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n/2
        else:
            n = n*3 + 1
sequence(5)
"""
"""
def kac_basamak(n):
    sayac = 0
    while n>=1:
        sayac = sayac + 1
        n = n / 10
    return sayac
print(kac_basamak(710))
print(kac_basamak(25))
print(kac_basamak(45893))
"""
"""
    #doctest'i hatırlayalım
def kac_basamak(n):
    '''
    >>> kac_basamak(710)
    3
    >>> kac_basamak(25)
    2
    >>> kac_basamak(45893)
    5
    '''
    sayac = 0
    while n>=1:
        sayac = sayac + 1
        n = n / 10
    return sayac
if __name__=="__main__":
    import doctest
    doctest.testmod()
"""
"""
def sadece_istedigim_basamaktan_kactanevar(n):
    sayac = 0
    while n>=1:
        digit = int(n % 10)
        if digit == 0 or digit == 5:
            sayac = sayac + 1
        n = int(n / 10)
    return sayac
print(sadece_istedigim_basamaktan_kactanevar(1530))
print(sadece_istedigim_basamaktan_kactanevar(14566783300345))
print(sadece_istedigim_basamaktan_kactanevar(235))
"""
"""
def carpimtablosu():
    for n in range(1,11):
        i = 1
        while i!=11:
            x = n*i
            i += 1
            print(x, end="\t")
        print("\n")
carpimtablosu()
"""
"""
def fibonacci():
    a,b = 0,1
    while b<1000:
        print(b, end=" ")
        a , b = b , a+b
fibonacci()
"""
"""
def ucgensel(high):
    # 1 3 6 10 15 21...
    i = 0
    a = 1
    fark = 2
    while i<high:
        print(a)
        a = a + fark
        fark += 1
        i += 1
ucgensel(7)
"""
"""
n = int(input("Sınır? :  "))
aralik=range(1, n+1)
toplam=0
while aralik:
    toplam += aralik[n-1]
    n -= 1
    if n==0:
        break
print(toplam)
"""
"""
x = sayi = int(input("Sayı? "))
logaritma = -1
while x > 0 :
    x //= 2
    logaritma += 1
print("log2(%f) yaklaşık %f" %(sayi, logaritma))
"""
"""
a = int(input("ilk sayı: "))
b = int(input("ikinci sayı: "))
def ebob(a,b):
    sayac = 1
    ebobu = 1
    while sayac <= max(a,b):
        if a%sayac==0 and b%sayac==0:
            ebobu = sayac
        sayac += 1
    print(ebobu)
ebob(a,b)
"""


