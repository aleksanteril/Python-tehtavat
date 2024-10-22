import random


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


#Tarkista matka, rekursiivinen tapa harjoitus
def tarkistaMatka(i):
    if i < 0:
        return True
    elif autotLista[i].kuljettuMatka < 10000:
        return tarkistaMatka(i - 1)
    print(f"{autotLista[i].rekTunnus}, on voittaja!")
    return False


#Funktio jolla tarkistetaan matka listasta, iteratiivinen tapa
#def tarkistaMatka():
#    for i in range(len(autotLista)):
#        if autotLista[i].kuljettuMatka >= 10000:
#            print(f"{autotLista[i].rekTunnus}, on voittaja!")
#            return False
#    return True

#Luodaan autoille lista ja luodaan 10 autoa
autotLista = []
for i in range(10):
    huippuNopeus = random.randint(100, 200)
    autotLista.append(Auto("ABC-" + str(i), huippuNopeus))


#Kiihdytyskisa kunnes kuljettumatka yli 10000km
while tarkistaMatka(len(autotLista)-1):

    #Käydään läpi jokaiselle autolle nopeudenmuutos
    #Ajetaan jokaisella autolla 1h
    for i in range(len(autotLista)):
        nopeudenMuutos = random.randint(-10,15)
        autotLista[i].kiihdytä(nopeudenMuutos)
        autotLista[i].kulje(1)



#Tulostetaan kaikki ominaisuudet autoista
print('\n')
for i in range(len(autotLista)):
    autotLista[i].haeTiedot()