import random


class Kilpailu:
    def __init__(self, kilpailunNimi, pituusKm, autotLista):
        self.kilpailunNimi = kilpailunNimi
        self.pituusKm = pituusKm
        self.autotLista = autotLista
        self.tuntejaKulunut = 0

    #Käydään läpi jokaiselle autolle nopeudenmuutos
    #Ajetaan jokaisella autolla 1h
    def tuntiKuluu(self):
        for i in range(len(self.autotLista)):
            nopeudenMuutos = random.randint(-10,15)
            self.autotLista[i].kiihdytä(nopeudenMuutos)
            self.autotLista[i].kulje(1)
        self.tuntejaKulunut += 1

    def tulostaTilanne(self):
        for i in range(len(self.autotLista)):
            self.autotLista[i].haeTiedot()

    def kilpailuOhi(self):
        for i in range(len(self.autotLista)):
            if self.autotLista[i].kuljettuMatka > self.pituusKm:
                print(f"\n{self.autotLista[i].rekTunnus}, on voittaja! Kilpailu {self.kilpailunNimi.upper()} on päättynyt")
                return True
        return False

    def tenTuntiaKulunut(self):
        if self.tuntejaKulunut < 10:
            return False
        print("\nKYMMENEN TUNNIN RAPORTTI")
        return True


# Luodaan luokka auto, jossa on ominaisuudet olioilla
class Auto:
    def __init__(self, rekTunnus, huippuNopeus):
        self.rekTunnus = rekTunnus
        self.huippuNopeus = huippuNopeus
        self.nopeus = 0
        self.kuljettuMatka = 0

    # Metodi jolla haetaan olion tiedot
    def haeTiedot(self):
        print(f"{self.rekTunnus}, {self.huippuNopeus}, {self.kuljettuMatka}, {self.nopeus} ")
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




#Luodaan autoille lista ja luodaan 10 autoa
autotLista = []
for i in range(10):
    huippuNopeus = random.randint(100, 200)
    autotLista.append(Auto("ABC-" + str(i), huippuNopeus))



romuralli = Kilpailu("Suuri Romuralli", 8000, autotLista)

while not romuralli.kilpailuOhi():
    romuralli.tuntiKuluu()
    if romuralli.tenTuntiaKulunut():
        romuralli.tulostaTilanne()
