
#Kirjasto pi tarkkaa arvoa varten
import math

#Kysytään käyttäjältä syöte
radius = float(input("Syötä ympyrän säde: "))

#Lasketaan ympyrän pinta-ala kaavalla
area = math.pi * radius ** 2

#Tulostetaan tulos käyttäjälle
print("Ympyrän pinta-ala on: " + str(area))
#print(f"Ympyrän pinta-ala on: {math.pi * pow(radius, 2)}")
#print("Ympyrän pinta-ala on: ",area,"!")