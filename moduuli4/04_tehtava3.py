pienin = suurin = None
#Ohjelma aloitetaan kysymällä käyttäjältä syöte ja tämä luku
#Asetetaan pienin ja suurin muuttujien alkuluvuksi mistä verrataan
syotto = input("Syötä luku, jos haluat lopettaa syötä tyhjä: ")
if syotto != "":
    pienin = suurin = int(syotto)

#Ohjelma kysyy käyttäjältä lukuja kunnes käyttäjä syöttää tyhjän
while (syotto != ""):

    #Verrataan käyttäjän syöttämiä lukuja
    #Ja lisätään aina pienin ja suurin vertailun avulla muistiin
    if int(syotto) < pienin:
        pienin = int(syotto)
    elif int(syotto) > suurin:
        suurin = int(syotto)

    syotto = input("Syötä luku, jos haluat lopettaa syötä tyhjä: ")

#Kun ohjelma loppuu, tulostetaan pienin ja suurin näytölle
print(f"\nPienin luku: {pienin}\nSuurin luku: {suurin}")


