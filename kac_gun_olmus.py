import datetime

tarih = input("Tarih girin (Örn. 02.09.1997): ")
tarih = tarih.split(".")
tDate = datetime.datetime(int(tarih[2]), int(tarih[1]), int(tarih[0]))
dateNow = datetime.datetime.now()
kac_gun_olmus = dateNow - tDate
print(kac_gun_olmus)
