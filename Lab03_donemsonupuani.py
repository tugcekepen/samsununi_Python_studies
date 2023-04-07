def hesapla(vize,final):
    dsp= vize*0.4 + final*0.6
    print("Dönem sonu notunuz: ", dsp)

vize = int(input("Vize notunuz: "))
final = int(input("Final notunuz: "))

hesapla(vize, final)
