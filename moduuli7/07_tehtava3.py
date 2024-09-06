
#Luodaan sanakirja lentoasemien nimistä ja ICAO koodista
lentoasemat = {"EFFI" : "Helsinki-Vantaan lentokenttä"}


#Aliohjelmassa kysytään syötettävän aseman nimi ja ICAO tunnus ja palautetaan pääohjelmaan monikkona
def syotauusi():
    asema, icao = input("Syötä lentoaseman nimi: "), input("Syötä lentoaseman ICAO-koodi: ")
    return asema, icao

#Pääohjelmassa loop kunnes käyttäjä lopettaa komennolla
while True:
    print("\nValitse haluatko syöttää uuden, hakea tietoa tai lopettaa")
    print("Komennot: syötä, hae, lopeta")
    komento = input("Komento: ")

    if komento == "syötä":         #syöttö ja sanakirjaan lisäys hoidetaan aliohjelman avulla
        nimi, icao = syotauusi()   #puretaan monikko ja asetetaan sanakirjaan
        lentoasemat[icao] = nimi
    elif komento == "hae":         #Haussa tarkistetaan löytyykö vastaavuuksia ja printataan aseman nimi
        icaoQ = input("Syötä haettava ICAO-koodi: ")
        if icaoQ in lentoasemat:
            print(f"{icaoQ} tunnuksen lentoasema on: {lentoasemat[icaoQ]}")
        else:
            print("Ei vastaavuuksia")
    elif komento == "lopeta":      #Ohjelman lopetus
        print("\nNäkemiin!")
        break
    else:                           #Jos komento tuntematon  tulostetaan käyttäjälle ilmoitus
        print("\nTuntematon syöte")



