import time
while(True):
    while(True):

        ilk10hane=input("TC kimlik numaranızın ilk 10 rakamını giriniz: ")

        try:
            sayi = int(ilk10hane)
                
        except:
            print("\nLütfen sadece sayı girin\n")
            continue

        
        if ( len(ilk10hane)!=10):
            print("Girilen değer 10 adet rakam içermelidir.\n")
            continue
        else:
            break

    while(True):
        
        sonhane=input("TC kimlik numaranızın son rakamını giriniz: ")

        if ( len(sonhane)!=1):
            print("Girilen değer 1 adet rakam içermelidir.\n")
            continue
        else:
            break

    toplam=0

    for rakam in ilk10hane:
        toplam += int(rakam)

    tcsonhane= toplam%10

    if (int(sonhane) == tcsonhane):
        print("\nTC numarası doğrulandı! ",sayi,tcsonhane,"\n",sep="")
        break
    else:
        print("\nTC numarası geçerli değil! Lütfen yeniden deneyiniz.\n")
        continue
    
time.sleep(2)
quit()
