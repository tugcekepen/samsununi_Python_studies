def tamsayi_bolme(bolunen, bolen):
    
    if (bolen != 0):
        
        sonuc = bolunen/bolen
    
    else:

        sonuc = "Tanımsız"

    return sonuc

print(tamsayi_bolme(6,3))
print(tamsayi_bolme(8,0))


