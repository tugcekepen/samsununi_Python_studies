import numpy as np

n=int(input("Kare matris için boyut girin: "))
matris=np.zeros((n,n)) #matris boyutunu ayarladık.

c=1
for i in range(n):
    for j in range(n):
        matris[i,j] = c
        c += 1
print(matris)

print()

#oluşan matrisin diagonel kısmındaki sayıları ve altında kalan üçgeni 0'lama
for i in range(n):
    for j in range(n):
        if j<=i:
            matris[i,j] = 0
print(matris)

print()

#oluşan matrisin diagonel kısmındaki sayıları listeye atama
t=[]
for i in range(n):
    t.append(int(matris[i,i]))
print(t)


        
