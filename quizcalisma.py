x="çok sıkılıyorum"
yenix=""
sesli="aeıioöuü"

for i in x:
    if i in sesli:
        yenix += "*"
    else:
        yenix += i
        
print(yenix)

print("----------------------------------")

print(x[0:3])
print(x[-11:-7])
print(x[8:])

print("----------------------------------")

for i in x:
    print(i)
    
print("----------------------------------")

ters=""
for i in range(len(x)-1,-1,-1):
    ters += x[i]
print(ters)

print("----------------------------------")

print(x[::-1])

print("----------------------------------")

for i in range(len(x)-1,-1,-1):
    print(x[i])
