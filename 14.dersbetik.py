"""
mList=[] #veya mList=list()
mDict={} #veya mDict=dict()
mTuple=() #veya mTuple=tuple() #DEĞİŞTİRİLEMEZ. OLUŞTURDUĞUN ŞEKLİYLE KALIR

mTuple = ("a", "b", "c", "d")

#print(mTuple[0])
#print(mTuple.count("a"))
#index metodu????

len(mTuple)

"""

"""

mTuple = ("1","2","3","4","5")

for i in mTuple:
    print(i)

"""

"""
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))
"""

"""
def factorial(n):
    carp = 1
    for i in range(1,n+1):
        carp = carp * i
    return carp


print(factorial(5))
"""

"""
def factorial(n):
    carp = n
    for i in range(1,n):
        carp = carp * i
    return carp


print(factorial(5))
"""

"""
def factorial(n):
    carp = n
    for i in range(n-1, 1, -1):
        carp = carp * i
    return carp


print(factorial(5))
"""

"""
def factorial(n):
    carp = 1
    while n>0:
        carp = carp * n
        n = n -1
    print(carp)
factorial(5)
"""

#fibonacci dizisinde n. terimi bulma
#1,1,2,3,5,8,13,21,34,55,89,144,.......
def fibo(n):
    if 0<n<=2:
        return 1
    elif n<=0:
        print("böyle bir sıra numarası yok")
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(10))



















