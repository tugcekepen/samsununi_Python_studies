def gectikaldi():
    vize=int(input("Vize: "))
    final=int(input("Final: "))

    if (final>=50):
        dsp = vize*0.4 + final*0.6
        if (dsp>=60):
            print(dsp,"ile geçtiniz.")
        else:
            print("Kaldınız.")
    else:
        print("Kaldınız.")

gectikaldi()
