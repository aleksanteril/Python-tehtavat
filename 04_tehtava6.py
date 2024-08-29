#Random kirjasto, random float varten
import random

#Kysytään käyttäjältä pisteiden määrät
total_count = int(input("Anna pisteiden määrä: "))

#Luodaan muuttujat looppia varten, looppi loppuu kun kerrat == käyttäjän syöte
ymp_sisalla = kerrat = 0

#Arvotaan x ja y arvot väliltä -1 ja 1, lasketaan epäyhtälöllä
#Ovatko koordinaatit ympyrän sisällä ja merkataan ylös jos ovat
while kerrat != total_count:
    x_arvo = random.uniform(-1,1)
    y_arvo = random.uniform(-1,1)
    if (pow(x_arvo, 2) + pow(y_arvo, 2)) < 1:
        ymp_sisalla = ymp_sisalla + 1
    kerrat = kerrat + 1

#Kun loop on saatu ajettua lasketaan pi liki arvo kaavalla pi = 4n/N
#Eli ympyrän sisälläolevat * 4 jaettuna kaikilla pisteillä
pi_likiarvo = 4 * ymp_sisalla / total_count

#Tulostetaan tulos käyttäjälle
print(pi_likiarvo)