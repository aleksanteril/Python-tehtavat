

#Ohjelma loppuu kun käyttäjä antaa negatiivisen tuumamäärän
tuuma = 0
while tuuma >= 0:
    # Otetaan käyttäjältä tuuma syötteet
    tuuma = float(input("Syötä muunnettavat tuumat: "))
    #Muutetaan tuumat senttimetreiksi  1 tuuma = 2,54cm
    if tuuma >=0:
        tuuma = tuuma * 2.54
        print(f"Mitat senttimetreissä ovat: {tuuma}cm")


