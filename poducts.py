from abc import ABC


class Product(ABC):
    def __init__(self, naziv, barkod, cijena):
        self.naziv = naziv
        self.barkod = barkod
        self.cijena = cijena
        self.porez = 0.2

class Chocolate(Product):
    def __init__(self, naziv, barkod, cijena,tezina):
        super().__init__(naziv,barkod,cijena)
        self.tezina = tezina
    def izracunajCijenu(self):
        osnovnaTaksa = self.cijena * self.porez
        self.novacijena = self.cijena + osnovnaTaksa
        print(f"Cijena ovog proizvoda sa porezom od 20% iznosi: {self.novacijena}")
    def __str__(self):
        return f"Naziv proizvoda: {self.naziv}\nBarkod: {self.barkod}\nOsnovna cijena proizvoda: {self.cijena}\nTezina: {self.tezina}\nTaksa: {self.porez}% "


class Wine(Product):
    def __init__(self, naziv, barkod, cijena, zapreminaBoce):
        super().__init__(naziv,barkod,cijena)
        self.zapremina = zapreminaBoce
        self.dodatniporez = 0.1
    def izracunajCijenu(self):
        self.osnovnaTaksa= self.cijena *self.porez
        cijenaBezDodatnog = self.osnovnaTaksa + self.cijena
        dodatniPorez = cijenaBezDodatnog * self.dodatniporez
        self.ukupnacijena = cijenaBezDodatnog + dodatniPorez
        print(f"Cijena ovog proizvoda sa porezod od drzave(20%) i dodatnim porezom(10%) iznosi: {self.ukupnacijena}")
    def __str__(self):
        return f"Naziv proizvoda: {self.naziv}\nBarkod: {self.barkod}\nOsnovna cijena proizvoda: {self.cijena}\nZapremina Boce: {self.zapremina}\nTaksa: 20%\nDodatni Porez na alkohol iznosi: 10%"

    


milka = Chocolate("Milka",123456,10,5)
milka.izracunajCijenu()
print(milka)

pinot = Wine("Pinot",534213,150,50)
pinot.izracunajCijenu()
print(pinot)