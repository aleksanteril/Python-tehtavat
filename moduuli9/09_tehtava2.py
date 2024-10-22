
#Luodaan luokka auto, jossa on ominaisuudet olioilla
class Auto:
    def __init__(self, rekTunnus, huippuNopeus):
        self.rekTunnus = rekTunnus
        self.huippuNopeus = huippuNopeus
        self.nopeus = 0
        self.kuljettuMatka = 0

    #Metodi jolla haetaan olion tiedot
    def haeTiedot(self):
        print(f"{self.rekTunnus}, {self.huippuNopeus}, {self.kuljettuMatka}, {self.nopeus} ")

    #Metodi jolla kiihdytetään olion nopeutta, ylittämättä huippua tai alittamatta 0
    def kiihdytä(self, muutosNopeus):
        self.nopeus += muutosNopeus
        if self.nopeus > self.huippuNopeus:
            self.nopeus = self.huippuNopeus
            return
        elif self.nopeus < 0:
            self.nopeus = 0
            return

#Luodaan auto1 olio
auto1 = Auto("ABC-123", 142)

#Kiihdytetään auto1 olion nopeutta.
auto1.kiihdytä(30)
auto1.kiihdytä(70)
auto1.kiihdytä(50)
print(auto1.nopeus)

auto1.kiihdytä(-200)
print(auto1.nopeus)