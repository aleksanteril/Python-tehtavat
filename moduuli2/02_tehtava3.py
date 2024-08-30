
#Kysytään käyttäjältä syötteet
kanta = float(input("Syötä suorakulmion kanta: "))
korkeus = float(input("Syötä suorakulmion korkeus: "))

#Lasketaan piiri ja pinta-ala syötteistä
area = kanta * korkeus
perimeter = kanta * 2 + korkeus * 2

#Tulostetaan tulokset piiri ja pinta-ala
print("Suorakulmion pinta-ala on: " + str(area) +
    "\nSuorakulmion piiri on: " + str(perimeter))
