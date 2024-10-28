class Julkaisu:

    def __init__(self, nimi):
        self.nimi = nimi

    def tulostaTiedot(self):
        print("\n")
        print(f"Julkaisun nimi: {self.nimi}")
        return

class Kirja(Julkaisu):

    def __init__(self, nimi, kirjoittaja, sivumäärä):
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä
        super().__init__(nimi)

    def tulostaTiedot(self):
        super().tulostaTiedot()
        print(f"Kirjoittaja: {self.kirjoittaja}, Sivumäärä: {self.sivumäärä}")
        return


class Lehti(Julkaisu):

    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)

    def tulostaTiedot(self):
        super().tulostaTiedot()
        print(f"Päätoimittaja: {self.päätoimittaja}")
        return


lehti = Lehti("Aku Ankka", "Aki Hyyppä")
kirja = Kirja("Hytti n:o 6", "Rosa Liksom", "200")

lehti.tulostaTiedot()
kirja.tulostaTiedot()