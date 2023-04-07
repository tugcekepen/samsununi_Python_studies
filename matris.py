x=[1,2,3,4]
y=[5,6,7,8]
z=[9,10,11,12]
r=[x,y,z]
for n in r:
    print(n)

print("-------------------")

X=[[1,2,3,4],
   [5,6,7,8],
   [9,10,11,12]]
for x in X:
    print(x)

print("-------------------")

X=[[1,2,3,4],
   [5,6,7,8],
   [9,10,11,12]]
for i in range(len(X)):
    print(X[i])

print("-------------------")

#matris elemanlarını normal yazdırma
X=[[1,2,3],
   [4,5,6],
   [7,8,9]]
for i in range(len(X)):
    for j in range(len(X[0])):
        print(X[i][j] , end=" ")
    print()
                   
print("-------------------")

X=[[0,0,0],
   [0,0,0],
   [0,0,0]]
t=1
for i in range(len(X)):
    for j in range(len(X[0])):
        X[i][j]= t
        t += 1
        print(X[i][j] , end=" ")
    print()

print("-------------------")

#1010 2020 3030 şeklinde matris
X=[[0,0,0,0],
   [0,0,0,0],
   [0,0,0,0]]
for i in range(len(X)):
    for j in range(len(X[0])):
        if j % 2 == 0:
            X[i][j]= i+1
        print(X[i][j] , end=" ")
    print()

print("---------SON----------")







