import time

cevap=""
while cevap!="h":
    girdi=str(input("Yapmak istediğiniz işlemi yazınız(Sadece tek işlem ve 2 sayı için): "))
    
    for i in girdi:
        if i=="+" or i=="-" or i=="*" or i=="/":
            islemListesi=girdi.split(i)            

    for j in range(0,len(islemListesi)):
        islemListesi[j]=int(islemListesi[j])

    for i in girdi:
        if i=="+":
            top=islemListesi[0]+islemListesi[1]
            print("İşlem sonucu:",top)
            while cevap!="h":
                cevap=input("Yeni işlem yapmak istiyor musunuz? (e/h) ")
                if cevap=="e":
                    break
                elif cevap=="h":
                    print("Çıkış yapılıyor...")
                    time.sleep(2)
                else:
                    print("Lütfen 'e' ya da 'h' ile cevap veriniz.")
        elif i=="-":
            cik=islemListesi[0]-islemListesi[1]
            print("İşlem sonucu:",cik)
            while cevap!="h":
                cevap=input("Yeni işlem yapmak istiyor musunuz? (e/h) ")
                if cevap=="e":
                    break
                elif cevap=="h":
                    print("Çıkış yapılıyor...")
                    time.sleep(2)
                else:
                    print("Lütfen 'e' ya da 'h' ile cevap veriniz.")
        elif i=="*":
            car=islemListesi[0]*islemListesi[1]
            print("İşlem sonucu:",car)
            while cevap!="h":
                cevap=input("Yeni işlem yapmak istiyor musunuz? (e/h) ")
                if cevap=="e":
                    break
                elif cevap=="h":
                    print("Çıkış yapılıyor...")
                    time.sleep(2)
                else:
                    print("Lütfen 'e' ya da 'h' ile cevap veriniz.")
        elif i=="/":
            bol=islemListesi[0]/islemListesi[1]
            print("İşlem sonucu:",bol)
            while cevap!="h":
                cevap=input("Yeni işlem yapmak istiyor musunuz? (e/h) ")
                if cevap=="e":
                    break
                elif cevap=="h":
                    print("Çıkış yapılıyor...")
                    time.sleep(2)
                else:
                    print("Lütfen 'e' ya da 'h' ile cevap veriniz.")
            
    


