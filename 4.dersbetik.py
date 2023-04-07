"""
def esit_mi():
    x = input("Birinci sayiyi giriniz: ")
    y = input("İkinci sayiyi giriniz: ")

    if (x==y):
        print("Girilen sayilar aynidir.")
    else:
        print("Girilen sayilar farklidir.")

esit_mi()
"""


"""
def esit_mi():
    x = int(input("Birinci sayiyi giriniz: "))
    y = int(input("İkinci sayiyi giriniz: "))
    
    if (x>10 and y>5):
        print("Koşul sağlandı.")
    else:
        print("Koşul sağlanamadı.")

esit_mi()
"""


"""
def dogrula(tahmin):
    parola = "M_YAZXXX"

    if ( parola == tahmin):
        print("Parola doğrulandı!")
    else:
        print("Yanlış parola!")

tahmin = input("Parola tahmininizi giriniz: ")

dogrula(tahmin)
"""


"""
def aralik_bul():
    sayi = int(input("Sayı giriniz: "))

    if (sayi>=10):
        print("Sayı 10 veya 10'dan büyük.")
        
        if (sayi<=20):
            print("Sayı [10-20] aralığındadır.")
        else:
            print("Sayı 20'den büyüktür.")
    else:
        print("Sayı 10'dan küçük.")

        if (sayi>=5):
            print("Sayı [5,10) aralığındadır.")
        else:
            print("Sayı 5'ten küçüktür.")

aralik_bul()
"""
