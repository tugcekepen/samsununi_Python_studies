a=int(input("a girin: "))
b=int(input("b girin: "))
c=int(input("c girin: "))

delta = (b**2)-(4*a*c)

if (delta>0):
    x1 = (-b+(delta)**(1/2))/(2*a)
    x2 = (-b-(delta)**(1/2))/(2*a)
    print("Kökler {} ve {}".format(x1,x2))
elif (delta==0):
    x1 = -b/2*a
    x2 = x1
    print("Kökler birbirine eşittir.",x1)
else:
    print("Denklemin reel kökü yoktur.")
