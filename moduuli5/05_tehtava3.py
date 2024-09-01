

#Kysytään käyttäjältä kokonaisluku
in_luku = int(input("Hei! Syötä kokonaisluku: "))
jkerta = False

#Tarkistetaan onko syötetty luku alkuluku
#for loopilla käydään läpi numerot 2 - syötetty luku
#Ja jaetaan aina joka kierroksella luku, jos tasan jakoja tapahtuu niin nostetaan lippu
#ja lopetetaan for loop ajan säästämiseksi
if in_luku == 1 or in_luku == 0:
    jkerta = True

else:
    for i in range(2,in_luku):
        if in_luku % i == 0:
            jkerta = True
            break

#Ilmoitetaan tulos jos lippu on nostettu luku ei ole alkuluku
#muuten Luku on alkuluku
if jkerta == True:
    print(f"{in_luku} ei ole alkuluku!")
else:
    print(f"{in_luku} on alkuluku!!")