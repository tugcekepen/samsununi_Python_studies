n=int(input("faktöriyel hesabı için sayı gir: "))

def factorial(n):
    x = list()
    for i in range(1,n+1):
        x.append(i)
    carp=1
    for u in x:
        carp *= u
    print("{} tam sayısının faktöriyeli= {}".format(n,carp))

factorial(n)
