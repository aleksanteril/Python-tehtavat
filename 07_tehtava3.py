
#Luodaan sanakirja lentoasemien nimistä ja ICAO koodista
lentoasemat = {"EFFI" : "Helsinki-Vantaan lentokenttä"}
#Funktio sanakirjaan lisäämiseen
def syotauusi():
    asema, icao = input("Syötä lentoaseman nimi: "), input("Syötä lentoaseman ICAO-koodi: ")
    return asema, icao

while True:
    print("\nValitse haluatko syöttää uuden, hakea tietoa tai lopettaa")
    print("Komennot: syötä, hae, lopeta")
    komento = input("Komento: ")

    if komento == "syötä":
        nimi, icao = syotauusi()
        lentoasemat[icao] = nimi
    elif komento == "hae":
        icaoQ = input("Syötä haettava ICAO-koodi: ")
        if icaoinp in lentoasemat:
            print(f"{icaoQ} tunnuksen lentoasema on: {lentoasemat[icaoQ]}")
        else:
            print("Ei vastaavuuksia")
    elif komento == "lopeta":
        print("\nNäkemiin!")
        break
    else:
        print("\nTuntematon syöte")



