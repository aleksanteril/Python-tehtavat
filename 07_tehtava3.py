
#Luodaan sanakirja lentoasemien nimistä ja ICAO koodista
lentoasemat = {"EFFI" : "Helsinki-Vantaan lentokenttä"}
#Funktio sanakirjaan lisäämiseen
def syotauusi():
    asema = input("Syötä lentoaseman nimi: "),
    icao = input("Syötä lentoaseman ICAO-koodi: ")
    return asema, icao

while True:
    print("\nValitse haluatko syöttää uuden, hakea tietoa tai lopettaa")
    print("Komennot: syötä, hae, lopeta")
    komento = input("Komento: ")

    if komento == "syötä":
        nimi, icao = syotauusi()
        lentoasemat[icao] = nimi
    elif komento == "hae":
        icaoinp = input("Syötä haettava ICAO-koodi: ")
        if icaoinp in lentoasemat:
            print(f"{icaoinp} tunnuksen lentoasema on: {lentoasemat[icaoinp]}")
        else:
            print("Ei vastaavuuksia")
    elif komento == "lopeta":
        print("\nNäkemiin!")
        break
    else:
        print("\nTuntematon syöte")



