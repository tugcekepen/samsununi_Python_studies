def tekmiciftmi(x,y):
    if (x%2 == 0 and y%2 == 0):
        print("x ve y değerleri çift")
    elif (x%2 == 0 and y%2 == 1):
        print("x çift, y tek")
    elif (x%2 == 1 and y%2 == 0):
        print("x tek, y çift")
    else:
        print("x ve y tek")

x=int(input("x gir: "))
y=int(input("y gir: "))

tekmiciftmi(x,y)
