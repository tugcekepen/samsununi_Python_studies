matris = [[1,2,3],[4,5,6],[7,8,9]]

def ortalama(matris):
    toplam=0
    for i in range(len(matris)):
        for j in matris[i]:
            toplam += j
            j += 1
        i+=1
    ortalama = toplam/9
    print("Dizi ortalaması:", ortalama)

ortalama(matris)