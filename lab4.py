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

        
#ZADANIE 4

class NaZakupy:
    nazwa_produktu = ""
    ilosc = 0
    jednostka_miary = ""
    cena_jed = 0
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed ):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed
    
    def wyswietl_produkt(self):
        print(f"{self.nazwa_produktu} {self.ilosc} {self.jednostka_miary} {self.cena_jed}")
    
    def ile_produktu(self):
        print(f"{self.ilosc} {self.jednostka_miary}")
    
    def ile_kosztuje(self):
        return self.ilosc*self.cena_jed
produkt = NaZakupy("woda", 2, "sztuki", 1.50)
produkt.wyswietl_produkt()
produkt.ile_produktu()
print(produkt.ile_kosztuje())
