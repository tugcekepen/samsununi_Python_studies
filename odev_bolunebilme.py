print("Çift sayı sorgulamasına hoş geldiniz!\n")

def is_divisible(x,y):
        return x%y==0

while True:
    x=int(input("Bölünecek tam sayıyı girin: "))

    def is_even(x):
        return is_divisible(x,2) #çift mi? sorgulaması için y=2'dir.

    print(is_even(x))

    end_or_go=input("""Başka sorgulama yapmak ister misiniz?
    Evet?
    Hayır?\n""")

    end_or_go=end_or_go.lower()

    if (end_or_go=="evet"):
        continue
    else:
        print("Çıkılıyor...")
        break
