
#Luodaan joukko tietotyyppi
nimet = set()

#Luodaan while loop jossa kysytään nimiä
#Lisätään joukkoon jos uusi nimi ja tulostetaan samalla palaute
nimistr = input("Hei! syötä nimi: ")
while nimistr != "":
    if nimistr in nimet:
        print("Aiemmin syötetty nimi!")
    else:
        print("Uusi nimi!")
        nimet.add(nimistr)
    nimistr = input("Hei! syötä nimi: ")

#Tulostetaan joukko
print("\n")
for nimi in nimet:
    print(nimi)