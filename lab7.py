#ZADANIE 1

import numpy as np
a = np.arange(3)
b = np.arange(3,6)
print(a)
print(b)
print(a.dot(b))

#ZADANIE 2

import numpy as np

a= np.arange(9).reshape(3,3)
b= np.arange(16).reshape(4,4)
print(a)
print("\n")
print(b)
print("\n")
print(a.min(axis=0))
print("\n")
print(b.min(axis=0))
print("\n")
print(a.min(axis=1))
print("\n")
print(b.min(axis=1))

#ZADANIE 3

import numpy as np
a = np.arange(3)
b = np.arange(3,6)
print(a)
print(b)
print(np.dot(a,b))

#ZADANIE 4



#ZADANIE 5

import numpy as np
a1= np.arange(6).reshape(2,3)
print(a1)
a=np.sin(a1)
print(a)

#ZADANIE 6

import numpy as np
b1= np.arange(6).reshape(2,3)
print(b1)
b=np.cos(b1)
print(b)

#ZADANIE 7

import numpy as np

a1= np.arange(6).reshape(2,3)
print(a1)
print("\n")
a=np.sin(a1)
print(a)
print("\n")

b1= np.arange(6).reshape(2,3)
print(b1)
print("\n")
b=np.cos(b1)
print(b)
print("\n")

print(np.add(a, b))




#ZADANIE 10





#ZADANIE 11
#Są identyczne

import numpy as np

a = np.arange(12)
print(a, "\n")
b = a.reshape(3,4)
print(b, "\n")
c = a.reshape(4,3)
print(c, "\n")
d = a.reshape(2,6)
print(d, "\n")
print(b.ravel(), "\n")
print(c.ravel(), "\n")
print(d.ravel(), "\n")
