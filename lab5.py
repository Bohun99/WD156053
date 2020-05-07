#ZADNIE 1
class material:
    def __init__(self, rodzaj, dlugosc, szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc
    
    def wyswietl_nazwe(self):
        return str(self.rodzaj) + str(self.dlugosc) + str(self.szerokosc)

class ubrania(material):
    def __init__(self, rozmiar, kolor, dla_kogo):
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.dla_kogo = dla_kogo

    def wyswietl(self):
        return str(self.rozmiar) + str(self.kolor) + str(self.dla_kogo)

class swetry(ubrania):
    def __init__(self, rodzaj_swetra):
        self.rodzaj_swetra = rodzaj_swetra

    def wyswietl(self):
        return str(self.rodzaj_swetra)
    
material1 = material("jedwab ", 100 , 100)
ubranie1 = ubrania(123 , " niebieski", " Kota")
sweter1 = swetry("bez rekawa")

print(ubranie1.wyswietl())

#ZADANIE 2


class kwadrat:

    def __init__(self, x):
        self.x = x
        self.y = x

    def __add__(self):
        return self.x*2, self.y*2

kw1 = Kwadrat(5)
kw2= Kwadrat(7)
kw3= kw1 + kw2
print(kw3)

#ZADANIE 6

class Wspak:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

slowo=Wspak("mrowisko")
print(wyraz.__next__())
print(wyraz.__next__())
print(wyraz.__next__())
print(wyraz.__next__())
print(wyraz.__next__())
print(wyraz.__next__())
print(wyraz.__next__())
print(wyraz.__next__())

#ZADANIE 7


def parzyste(dane):
    for index in range(0, len(dane)):
        if index % 2 == 0:
            yield dane[index]
napis = parzyste("Moro")
print(next(napis))
print(next(napis))

#ZADANIE 12

def nazwy_miesiecy():
    for x in ["styczen", "luty", "marzec", "kwiecien", "maj", "czerwiec", "lipiec", "sierpien", "wrzesien", "pazdziernik", "listopad", "grudzien"]:
        yield x
m = nazwy_miesiecy()
print(m.__next__())
print(m.__next__())
print(m.__next__())
print(m.__next__())
print(m.__next__())
print(m.__next__())
print(m.__next__())
print(m.__next__())
print(m.__next__())
print(m.__next__())
print(m.__next__())
print(m.__next__())
