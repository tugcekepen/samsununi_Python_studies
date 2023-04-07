import numpy as np
dizin1 = np.array([1,2,3,4,5])
print(dizin1)
dizin1_1 = dizin1 * 2 #numpyde dizini bir sayı ile çarptığımızda elemanların o sayı ile çarpılmış halini verir #normal listede ise listeyi yan yana o sayı kadar yazdırır
print(dizin1_1)
print(type(dizin1))
print("------------------")
dizin2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(dizin2)
print("------------------")
print(dizin2.ndim) #boyut öğrenme
print(dizin2.shape) #şeklini öğrenme m x n değerleri
print("------------------")
dizin2_2 = dizin2.reshape(1,9) #kendi belirlediğimiz m x n değerlerine göre dizini yeniden boyutlandırdık, şekillendirdik
print(dizin2_2)
print("------------------")
dizin3 = np.arange(4, 16, 2) #sondaki elemanı dahil etmez
print(dizin3)
print("------------------")
dizin4 = np.linspace(1,5,5) #sondaki eleman dahildir
print(dizin4)
print("------------------")
dizin5 = np.zeros((5,2)) #yanlarına noktalar koyuyor
print(dizin5)
print("------------------")
dizin6 = np.ones((2,7)) #yanlarına noktalar koyuyor
print(dizin6)
print("------------------")
dizin7 = np.full((4,2),9) #istediğin bir eleman ile belirttiğin boyutta dizin oluşturma
print(dizin7)
print("------------------")
dizin8 = np.random.random((6,3)) #0-1 aralığında belirttiğin boyutta rastgele elemanlarla dizin oluşturur
print(dizin8)
print("------------------")
dizin9 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(dizin9[:2])
print("---")
print(dizin9[1:2])
print("---")
print(dizin9[1:2,0:2])
print("---")
print(dizin9[:,:1])
print("---")
print(dizin9[:,:2])
print("---")
print(dizin9[:,2])
print("------------------")
dizin10 = np.concatenate((dizin1,dizin1)) #1 boyutlu iki dizini birleştirir. 1 BOYUTLU OLANLARI !!!!
print(dizin10)
print("------------------")
dizin_satiragore = np.concatenate((dizin2,dizin9), axis=0) #sutun sayısı aynı olmazsa ERROR !!
print(dizin_satiragore)
print("---")
dizin_sutunagore = np.concatenate((dizin2,dizin9), axis=1) #satır sayısı aynı olmazsa ERROR !!
print(dizin_sutunagore)
print("------------------")
dizin_bolunmus1 = np.array_split(dizin1, 5)
print(dizin_bolunmus1)
dizin_bolunmusten = np.array(dizin_bolunmus1)
print(dizin_bolunmusten)
print("------------------")
dizin_bolunmus2 = np.array_split(dizin2, 3) #axis belirtilmezse varsayılan sıfır alır
print(dizin_bolunmus2)
print("---")
dizin_bolunmus3 = np.array_split(dizin2, 4, axis = 0) #satıra göre bölme
print(dizin_bolunmus3)
print("---")
dizin_bolunmus4 = np.array_split(dizin2, 3, axis = 1) #sütuna göre bölme
print(dizin_bolunmus4)
dizin_bolunmusten4 = np.array(dizin_bolunmus4)
print(dizin_bolunmusten4)
print("------------------")
# toplama - çıkarma - bölme - çarpma işlemleri normal bilinen formatta yapılıyor

transpoz_dizin = dizin9.T #satırlardaki elemanları sütunlara dizer veya tam tersi.
print(transpoz_dizin)
print("------------------")
#önce ilk dizinin ilk satırı ile ikinci dizinin tüm sütunları ile işlem yapılır, bu şekilde yeni dizinin ilk satır elemanları belirlenir.
#daha sonra aynı işlemler ilk dizinin diğer satırları ile de sırasıyla yapılarak yeni dizin elde edilir.
carpim_matris = np.dot(dizin2,dizin9) #!!!
print(carpim_matris)
print("------------------")
print(dizin2.sum()) #dizinin tüm elemanlarını toplar.
print("------------------")
dizin_toplamsutun = dizin2.sum(axis=0) #sütunlardaki elemanları toplar ve o sütunun indis değerine elemanı yerleştirir.
print(dizin_toplamsutun)
dizin_toplamsatir = dizin2.sum(axis=1) #satırlardaki elemanları toplar ve o satırın indis değerine elemanı yerleştirir.
print(dizin_toplamsatir)
print("------------------")
dizin2.max()
dizin2.min()
dizin2.mean()
dizin2.var()
dizin2.std()
np.median(dizin2)
print("------------------")