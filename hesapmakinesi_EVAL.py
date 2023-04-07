import time

girdi=str(input("İşleminizi girin: "))

izinliler="1234567890+-*/"

for i in girdi:
    if i in izinliler:
        x=eval(girdi)
    elif not i in izinliler:
        print("Hoooppp! Ne yapıyorsun???")
        time.sleep(2)
        quit()
print(x)
time.sleep(2)
quit()



"""
#burada postfix için stacklemeye çalıştım
stackList=list()
charList=list()

for i in girdi:
    if i=="(" or i==")" or i=="+" or i=="-" or i=="*" or i=="/":
        stackList.append(i)
    else:
        charList.append(int(i))

print(stackList)
print(charList)
"""
