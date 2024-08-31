
#Kysytään käyttäjältä kokonaisluku
in_luku = int(input("Hei! Syötä kokonaisluku: "))
jkerta = 0

#Tarkistetaan onko syötetty luku alkuluku
#for loopilla käydään läpi numerot 1 - syötetty luku
#Ja jaetaan aina joka kierroksella luku, jos tasan jakoja on vain 2
#lisätään kerrat tarkistukseen 1
for i in range(1,in_luku+1):
    if in_luku % i == 0:
        jkerta = jkerta + 1


#Ilmoitetaan tulos jos jakokertoja on vain 2
#Luku on alkuluku
if jkerta == 2:
    print(f"{in_luku} on alkuluku!!")
else:
    print(f"{in_luku} ei ole alkuluku!")