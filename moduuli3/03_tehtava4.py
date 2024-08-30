
#Kysytään vuosiluku käyttäjältä ja asetetaan se muuttujaan
in_vuosi = int(input("Syötä tarkastettava vuosiluku: "))

#Tarkistetaan logiikalla onko vuosiluku karkausvuosi
#Ilmoitetaan käyttäjälle onko vuosiluku karkausvuosi vai ei

if (in_vuosi % 4 == 0 and not in_vuosi % 100 == 0) or in_vuosi % 400 == 0:
    print("Vuosi on karkausvuosi")
else:
    print("Vuosi ei ole karkausvuosi")

#Ilmoitetaan käyttäjälle onko vuosiluku karkausvuosi vai ei