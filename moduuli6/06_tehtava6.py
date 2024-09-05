
import math
#Funktio saa parametreinä arvot pizzan halkaisija cm
#ja pizzan hinta, funktio laskee pizzan arvon
# euroa / neliömetri


#Aliohjelma arvojen kysymistä varten
def pizzatiedot(num, arvo):
    return float(input(f"Syötä pizzan {num} {arvo}: "))

#Lasketaan pizzan pinta-ala ja muutetaan returnissa vielä neliömetreiksi
def pizzavalue(halkaisija, hinta):
    area = math.pi * ((halkaisija/2)**2)
    value = hinta / (area/10000)
    return value


#Pääohjelmassa kysytään kahden pizzan halkaisijat ja hinnat
#ja ilmoitetaan kummassa on parempi arvo suhteessa pinta-alaan
pizzavaluelist = []
for i in range (1,3):
    halkaisija = pizzatiedot(i, "halkaisija cm")
    hinta = pizzatiedot(i, "hinta euroa")
    pizzavaluelist.append(pizzavalue(halkaisija, hinta))


#Vertaillaan pizzat listalla
if pizzavaluelist[0] < pizzavaluelist[1]:
    print(f"Pizza 1 on parempi hintasuhde! {pizzavaluelist[0]:.2f} e/neliö")
else:
    print(f"Pizza 2 on parempi hintasuhde! {pizzavaluelist[1]:.2f} e/neliö")