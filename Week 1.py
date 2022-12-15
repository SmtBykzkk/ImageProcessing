import numpy as np
A = np.array([[1,2,3],[3,4,5]])
print(A)


array =np.zeros( (2,3) )
print(array)


array =np.ones( (1,5) )
print(array)


n = int(input("Girilecek sayi miktari: "))
a = []
for i in range(0,n):
    elem = int(input("Sayi girin: "))
    a.append(elem)
avg = sum(a) / n
print("Ortalama: ", round(avg,2))