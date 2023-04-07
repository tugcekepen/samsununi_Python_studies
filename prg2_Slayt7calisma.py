
isim = "selamunaleyküm" #Bu bir dizgidir ve karakterleri değiştirilemez.
"""
harf = isim[2]
print(harf)
harf = isim[-1]
print(harf)
harf = isim[1:4]
print(harf)
uzunluk=len(isim)
"""
"""
# 1. yöntem
i, x = 0, -(len(isim))
while i < len(isim):
    print(isim[x])
    x += 1
    i += 1

# 2. yöntem
i = 0
while i < len(isim):
    print(isim[i])
    i += 1
"""
"""
#for döngüsü kelime üzerinde daha kolay gezinebilmeyi sağlar. # 3. yöntem
for ch in isim:
    print(ch)
"""
"""
var_mi = "u" in isim
print(var_mi)
var_mi = "t" in isim
print(var_mi)
"""
"""
sesli="aeıioöuüAEIİOÖUÜ"
word = input("Kelimeniz: ")
for ch in word:
    if ch in sesli:
        continue
    print(ch, end="")
"""
"""
sayac = 0
for letter in isim:
    if letter=="ü":
        sayac += 1
print(sayac)
"""
"""
# ASCII TABLOSU !!!!!!!!!!
for i in range(128):
    print("%s ==> %c" %(i, i))
"""