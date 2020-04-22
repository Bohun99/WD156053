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
