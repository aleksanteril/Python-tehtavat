
#Monikossa säilytetään vuodenajat
vuodenaika = ("Talvi", "Kevät", "Kesä", "Syksy")

#Kysytään käyttäjältä vuodenaika
kknumero = int(input("Hei! Syötä kuukauden numero 1-12: "))


#Verrataan kknumeroa ja mikä vuodenaika se on
if kknumero != 0:
    if kknumero <= 3:
        print(vuodenaika[0])
    elif kknumero <= 6:
        print(vuodenaika[1])
    elif kknumero <= 9:
        print(vuodenaika[2])
    elif kknumero <= 12:
        print(vuodenaika[3])
else:
    print("Tuntematon")