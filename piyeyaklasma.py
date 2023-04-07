import numpy as np

terim = int(input("Pi sayısına kaç hamlede yaklaşmak istediğinizi tam sayı olarak yazın: "))

#pay=np.ones(terim)
#payda=np.linspace(1, terim*2, terim)

pay = []
for a in range(0,terim):
    if (a % 2 == 0):
        pay.append(1)
    else:
        pay.append(-1)

print(pay)

payda = []
for b in range(1,terim+1):
    payda.append((2*b)-1)

print(payda)

"""for i in range(1,terim):
    pay[i]=pow(-1,i)"""

sayac=0
toplam_deger=0

while sayac<terim:
    toplam_deger = toplam_deger + (pay[sayac]/payda[sayac])
    sayac += 1

pi_sayisi=4*toplam_deger
print(pi_sayisi)