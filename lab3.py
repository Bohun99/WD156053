#Zadanie 1
A = [1/x for x in range(1,10)]
B = [2**i for i in range(11)] 
C = [x for x in B if x % 4 == 0]
print(A)
print(B)
print(C)

#Zadanie 2
import random
A = [[random.randint(0,10) for x in range(4)],
[random.randint(0,10) for x in range(4)],
[random.randint(0,10) for x in range(4)],
[random.randint(0,10) for x in range(4)]]
B  = [A[x][x] for x in range(4) ]
print(A)
print(B)
