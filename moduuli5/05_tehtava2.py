
#Luodaan lista käyttäjän syöttämille numeroille
numerot = []

#Kysytään käyttäjältä lukuja kunnes
#käyttäjä syöttää tyhjän merkin
num_inp = input("Hei! Syötä lukuja, jos lopetat laita tyhjä: ")
while num_inp != "":
    if int(num_inp) not in numerot:   #Otetaan listaan vain 1 jokaista
        numerot.append(int(num_inp))
    num_inp = input("Hei! Syötä lukuja, jos lopetat laita tyhjä: ")

#Lajitellaan lista suurimmasta pienimpään
#Tulostetaan 5 ensimmäistä indeksiä eli suurinta
numerot.sort(reverse=True)
print(numerot[0:5])
