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
a = float(przeciw())
print("Przeciwprostokątna wynosi : " + str(a) )


#Zadanie 8
def suma(a1=1, r=1, ile=10):
    ostatni = a1+(ile-1)*r
    return ((a1 + ostatni)/2)*ile
a = float(suma())
print("Suma podanego ciągu to: " + str(a) )

#Zadanie 9
def ciag(* liczby):
    if len(liczby) == 0:
        return 0
    else:
        ilo = 1
        for x in liczby:
            ilo = ilo*x
    return ilo
print(ciag(12,2,5,1))

#Zadanie 10
def ilosc(** produkt):
    ilosc=0
    for x in produkt:
        ilosc = ilosc + produkt[x]
    print(ilosc)
    
ilosc(chleb = 1, ketchup = 3, tosty = 9)

#Zadanie 12
from ciagi import aryt
from ciagi import geo
#arytmetyczne
a1=3
r=1
n1=8
print(aryt.anaryt(a1, r, n1))
#geometryczne
a2=5
q=1
n2=3
print(geo.angeo(a2, q, n2))

#ciągi aryt
def anaryt(a1, r, n):
    an = a1 + (n-1)*r
    return an

#ciągi geo
def angeo(a1, q, n):
    an = a1*q**(n-1)
    return an

