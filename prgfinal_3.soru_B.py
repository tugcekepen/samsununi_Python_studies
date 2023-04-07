sayi1=complex(input("İlk karmaşık sayıyı girin: "))
sayi2=complex(input("İkinci karmaşık sayıyı girin: "))
islem=input("Yapmak istediğiniz işlemi girin(+,-,*,/): ")

if (islem=="+"):
    sonuc=sayi1+sayi2
elif (islem=="-"):
    sonuc=sayi1-sayi2
elif (islem=="*"):
    sonuc=sayi1*sayi2
elif (islem=="/"):
    sonuc=sayi1/sayi2
else:
    print("İşlem bulunamadı")

print("İşlemin sonucu: ",sayi1,islem,sayi2,"=",sonuc)
