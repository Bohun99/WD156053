#ZADANIE 1 

import random

A = [random.randint(0, 50) for i in range(20) ]
B = [x for x in A if x % 4 == 0]
plik = open("zadanie1.txt", "w")
plik.writelines(str(B))
plik.close()

#ZADANIE 2

plik = open("zadanie1.txt", "r")
dane = plik.readlines()
plik.close()
print(dane)

#ZADANIE 3

with open("zadanie3.txt", "w") as plik:
    plik.writelines("jakis tekst")

with open("zadanie3.txt", "r") as plik1:
    for linia in plik1:
        print(linia, end="")
