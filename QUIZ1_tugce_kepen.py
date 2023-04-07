def anabilgi():
    cihaz=int(input("Cihaz sayısı giriniz: "))
    hizmet=str(input("Hizmet türü giriniz: "))

    if (hizmet=="N" or hizmet=="n"):
        stream_n(cihaz)
        
    elif (hizmet=="A" or hizmet=="a"):
        stream_a(cihaz)
        
    else:
        stream_c(cihaz)

    return cihaz

def stream_n(cihaz):
    if (cihaz<=2):
        aylik=8.99
        print("Yıllık ücretiniz",aylik*12,"$")

    else:
        aylik=13.99
        print("Yıllık ücretiniz",aylik*12,"$")

def stream_a(cihaz):
    if (cihaz>=4 and cihaz<7):
        aylik=18.99
        print("Yıllık ücretiniz",aylik*12,"$")

    else:
        aylik=29.99
        print("Yıllık ücretiniz",aylik*12,"$")

def stream_c(cihaz):
    if (cihaz<=4):
        aylik=20.99
        print("Yıllık ücretiniz",aylik*12,"$")

    elif (cihaz>=5 and cihaz<10):
        aylik=28.99
        print("Yıllık ücretiniz",aylik*12,"$")

    else:
        aylik=34.99

anabilgi()


#                                              NOTLAR
#    stream_c fonksiyonunda else bloğuna print("Yıllık ücretiniz",aylik*12,"$") yazmayı unutmuşum.
#    alternatif olarak anabilgi() bloğunda ikinci bir elif bloğu kullanarak "H" or "h" girişi ile stream_c fonksiyonuna yönlendirebilir,
# else ile de N,A,H harfleri dışındaki girişler için "platform bulunamadı" çıktısı verdirebilirdim."""
