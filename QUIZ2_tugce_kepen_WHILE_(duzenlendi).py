#hocaya gönderdiğimin revize edilmiş hali
import time
def fonk1():
    sayac=0
    dongu=int(input("Oluşturmak istediğiniz 1. listenin uzunluğunu giriniz: "))
    liste=[]

    while sayac<=dongu-1:
        sayi=int(input("Liste elemanınızı giriniz: "))
        liste.append(sayi)
        sayac += 1

    sayac2=0
    dongu2=int(input("Oluşturmak istediğiniz 2. listenin uzunluğunu giriniz: "))
    liste2=[]

    while sayac2<=dongu2-1:
        sayi2=int(input("Liste elemanınızı giriniz: "))
        liste2.append(sayi2)
        sayac2 += 1

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

time.sleep(2)
