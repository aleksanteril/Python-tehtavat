class Auto:
    def __init__(self, rekTunnus, huippuNopeus):
        self.rekTunnus = rekTunnus
        self.huippuNopeus = huippuNopeus
        self.nopeus = 0
        self.kuljettuMatka = 0

    # Metodi jolla haetaan olion tiedot
    def haeTiedot(self):
        print(f"REK: {self.rekTunnus}, MAX_V: {self.huippuNopeus}, TRAVELLED: {self.kuljettuMatka}, V: {self.nopeus} ")
        return

    # Metodi jolla kiihdytetään olion nopeutta, ylittämättä huippua tai alittamatta 0
    def kiihdytä(self, muutosNopeus):
        self.nopeus += muutosNopeus
        if self.nopeus > self.huippuNopeus:
            self.nopeus = self.huippuNopeus
            return
        elif self.nopeus < 0:
            self.nopeus = 0
            return
        return

    # Metodi jolla lasketaan kuljettumatka autolle
    def kulje(self, tuntiMäärä):
        self.kuljettuMatka += self.nopeus * tuntiMäärä
        return


class Sähköauto(Auto):

    def __init__(self, rekTunnus, huippuNopeus, kapasiteettiKWH):
        self.kapasiteettiKWH = kapasiteettiKWH
        super().__init__(rekTunnus, huippuNopeus)


class Polttomoottoriauto(Auto):

    def __init__(self, rekTunnus, huippuNopeus, tankinKokoLitra):
        self.tankinKokoLitra = tankinKokoLitra
        super().__init__(rekTunnus, huippuNopeus)


sähköauto = Sähköauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

#Asetetaan nopeudet autoille
sähköauto.kiihdytä(60)
polttomoottoriauto.kiihdytä(100)
#ddfd
#Ajetaan autoilla 3h
sähköauto.kulje(3)
polttomoottoriauto.kulje(3)

#Tulostetaan autojen tiedot
sähköauto.haeTiedot()
polttomoottoriauto.haeTiedot()