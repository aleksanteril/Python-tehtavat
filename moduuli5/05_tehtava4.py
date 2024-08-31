
#Lista kaupunkeja varten
cities = []

#Kysytään 5 kaupunkia syötettä
for i in range(5):
    cities.append(input("Hei! Syötä kaupungin nimi: "))

#Tulostetaan lista for rakenteella allekkain
print("\n__Kaupunkilista__")
for city in cities:
    print(f"-> {city}")