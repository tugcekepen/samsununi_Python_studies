#Hocanın istediği format
def fonk1():
    liste=[]
    for i in range(8):
        sayi=int(input("1.listenin elemanlarını giriniz: "))
        liste.append(sayi)

    print("--------------")

    liste2=[]
    for u in range(8):
        sayi2=int(input("2. listenin elemanlarını giriniz: "))
        liste2.append(sayi2)

    print("--------------")

    fonk2(liste,liste2)
    
def fonk2(liste, liste2):
    ortaklarListesi=[]
    for x in liste:
        for y in liste2:
            if (x==y):
                ortaklarListesi.append(y)
                for z in ortaklarListesi:
                    if (ortaklarListesi.count(z)>=2):
                        ortaklarListesi.remove(z)
    ortaklarListesi.sort()
    print("Ortak elemanlar listesi=",ortaklarListesi)

    toplam = 0
    for z in ortaklarListesi:
        toplam += z
    print("Ortak elemanların toplamı=",toplam)

fonk1()
