x=int(input("sayı girin: "))
y=int(input("sayı girin: "))
fonk=input("fonk. girin: ")

def f(x, y):
    return x+y

def g(x, y):
    return x-y

def h(x, y):
    return x*y

def t(x, y):
    return x//y

def hm(fonk, x, y):
    return fonk(x, y)

if (fonk=="+" or fonk=="topla"):
    fonk = f
elif (fonk=="-" or fonk=="çıkar"):
    fonk = g
elif (fonk=="*" or fonk=="çarp"):
    fonk = h
elif (fonk=="/" or fonk=="böl"):
    fonk = t
else:
    print("geçersiz işlem!")

print(hm(fonk, x, y))

