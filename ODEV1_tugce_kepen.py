import time

def girdi():

    metin=str(input("Herhangi bir metin giriniz: "))

    return metin

def degisim(metin):

    sesli="aeıioöuüAEIİOÖUÜ"

    for harf in metin:
        if (harf in sesli):
            metin=metin.replace(harf,"*")

    print(metin)

degisim(girdi())

time.sleep(3)
