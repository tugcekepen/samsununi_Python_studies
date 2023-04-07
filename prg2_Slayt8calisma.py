"""
liste = ["tugce", "kepen", 24, 1.52, ["başak", "yengeç"]]
var_mi = "kepen" in liste
print(var_mi)
var_mi = 18 in liste
print(var_mi)
uzunluk = len(liste)
print(uzunluk)
print(liste[4][0])
"""
"""
liste = ["tugce", "kepen", 24, 1.52, ["başak", "yengeç"]]
i=0
while i<len(liste):
    print("Listenin", str(i+1)+".", "elemanı:",liste[i])
    i += 1
"""
"""
x=0
liste = ["tugce", "kepen", 24, 1.52, ["başak", "yengeç"]]
liste2 = ["alper", "başal", 23, 1.78, ["yengeç", "yengeç"]]
for eleman in liste:
    liste[x] = liste2[x] #yani liste elemanları değiştirilebilirdir. dizgide olduğu gibi değil.
    x += 1
print(liste)
"""
"""
# for'lu döngüyü sırf for kullanmak için yaptık. aslında tek satırla da aynısı gerçekleştirilebilir.
liste = ["tugce", "kepen", 24, 1.52, ["başak", "yengeç"]]
liste2 = ["alper", "başal", 23, 1.78, ["yengeç", "yengeç"]]
liste=liste2
print(liste)
"""
"""
liste = ["tugce", "kepen", 24, 1.52, ["başak", "yengeç"]]
liste2 = ["alper", "başal", 23, 1.78, ["yengeç", "yengeç"]]
birlesim = liste + liste2
print(birlesim)
"""
"""
x = ["a"]*4
print(x)
liste = ["tugce", "kepen", 24, 1.52, ["başak", "yengeç"]]
x = liste * 3
print(x)
"""
"""
liste = ["tugce", "kepen", 24, 1.52, ["başak", "yengeç"]]
for indis, eleman in enumerate(liste): # !!!!!!!!!!!!!!!!!!!enumerate()!!!!!!!!!!!!!!!!!!!!!
    print(indis,"-",eleman)
"""
"""
lst = ["spam!", 1, ["Brie", "Roquefort", "Pol le Veq"], [1, 2, 3]]
for i in range(len(lst)):
    if type(lst[i])==int:
        boyut = len(str(lst[i]))
    else:
        boyut = len(lst[i])
    print(boyut)
"""

lst = ["spam!", 1, ["Brie", "Roquefort", "Pol le Veq"], [1, 2, 3]]
for indis, eleman in enumerate(lst):
    if type(eleman)==list:
        for index, oge in enumerate(eleman):
            print(indis, ".", index, "-", oge)
    else:
        print("%-5d - %s" %(indis,eleman))

"""
import webbrowser as web
web.open("www.google.com")
"""
