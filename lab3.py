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

#Zadanie 3
slownik = {"ziemniaki" : "kg" , "chleb" : "sztuki" , "czekolada": "sztuki" , "jabłka": "kg" , "ketchup": "sztuki"}
sztuki = [x for x in slownik if slownik[x] == "sztuki"]
print(sztuki)

#Zadanie 4

def monotonicznosc(a):
    if(a > 0):
        print("Funkcja jest rosnąca")

    elif (a < 0):
        print("Funkcja jest malejąca")

    else:
        print("Funkcja jest stała ")

a = input("Podaj a w funkcji y=ax+b")
a = int(a)
print (monotonicznosc(a))

#Zadanie 5
def spr(a1, a2):
    if(a1 == a2):
        print("Proste są równoległe")
    elif (a1*a2 == -1):
        print("Proste są prostopadłe")
    else:
        print("Nie są prostopadłe ani równoległe")

a1 = input("Podaj a w 1 funkcji y=ax+b")
a1 = int(a1)
a2 = input("Podaj a w 2 funkcji y=ax+b")
a2 = int(a2)
print (spr(a1,a2))

#Zadanie 6
def promien(a=5, b=5, x=1, y=2):
    r = ((x-a)*(x-a))+((y-b)*(y-b))
    return r**(1/2)

print(promien())

#Zadanie 7
def przeciw(a=6, b=2):
    c = a**2 + b**2
    return c**(1/2)

print(przeciw())


