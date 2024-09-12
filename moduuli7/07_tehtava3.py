

#Aliohjelma valintaa varten
def valinta():
    print("\nValitse haluatko syöttää uuden, hakea tietoa tai lopettaa")
    print("Komennot: syötä, hae, lopeta")
    komento = input("Komento: ")
    return komento

#Aliohjelma sanakirjaan syöttämistä varten
def syotauusi(lentoasemat):
    asema = input("Syötä lentoaseman nimi: ")
    icao = input("Syötä lentoaseman ICAO-koodi: ")
    lentoasemat[icao] = asema
    return lentoasemat

#Aliohjelma hakua varten
def haku(lentoasemat):
    icao = input("Syötä haettava ICAO-koodi: ")
    if icao in lentoasemat:
        print(f"{icao} tunnuksen lentoasema on: {lentoasemat[icao]}")
    else:
        print("Ei vastaavuuksia")
    return


#Luodaan sanakirja lentoasemien nimistä ja ICAO koodista
komento = None
lentoasemat = {"EFHK" : "Helsinki-Vantaan lentokenttä"}

#Pääohjelma jossa pyöritään kunnes lopeta komento
while komento != "lopeta":
    komento = valinta()
    if komento == "syötä":         #syöttö ja sanakirjaan lisäys hoidetaan aliohjelman avulla
        lentoasemat = syotauusi(lentoasemat)
    elif komento == "hae":         #Haussa tarkistetaan löytyykö vastaavuuksia ja printataan aseman nimi
        haku(lentoasemat)
    elif komento != "lopeta":                           #Jos komento tuntematon  tulostetaan käyttäjälle ilmoitus
        print("\nTuntematon syöte")

print("Näkemiin!")