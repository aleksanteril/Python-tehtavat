
#Luodaan sanakirja lentoasemien nimistä ja ICAO koodista
lentoasemat = {}
#Funktio sanakirjaan lisäämiseen
def syotauusi(asema, icao):
    lentoasemat[icao] = asema
    return


#Funktio sanakirjasta tiedon hakemiseen
def haetiedot(icao):
    asema = lentoasemat[icao]
    return asema

while True:
    print("Valitse haluatko syöttää uuden, hakea tietoa tai lopettaa")
    print("Komennot: syötä, hae, lopeta")
    komento = input("komento: ")

    if komento == "syötä":
        syotauusi(
            input("Syötä lentoaseman nimi: "),
            input("Syötä lentoaseman ICAO-koodi: "))
    elif komento == "hae":
        nimi = haetiedot(
            input("Syötä ICAO-koodi: "))
        print(f"Lentoaseman nimi on {nimi}")
    elif komento == "lopeta":
        break
    else:
        print("\nTuntematon syöte")



