import time

def tcuretme():
    import random

    tc_ilk10hane=random.randint(1000000000,10000000000)

    toplam=0
    for rakam in str(tc_ilk10hane):
        toplam+=int(rakam)

    sonhane=toplam%10

    print("\nTC no: ",tc_ilk10hane,sonhane,sep="")

tcuretme()

while(True):
    onay=input("""\nYeniden TC no üretilsin mi?
-Evet için; E
-Hayır için; H\n\n""")

    if (onay=="E" or onay=="e"):
        tcuretme()
    elif  (onay=="H" or onay=="h"):
        print("\nİsteğiniz üzerine rastgele TC no üretme işlemi sonlandırıldı.")
        break
    else:
        print('\nLütfen "Evet(E)" veya "Hayır(H) şeklinde cevap veriniz.')
        continue

time.sleep(3)

        
