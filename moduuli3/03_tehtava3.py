
#Kysytään käyttäjän sukupuoli
sukupuoli = input("Mikä on sukupuolesi? Mies/Nainen: ")

#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l
#Kysytään käyttäjän hemoglobiiniarvo
hemglob = int(input("Mikä on hemoglobiiniarvosi? g/l: "))

if sukupuoli == "Mies":
    if hemglob>195:
        print("Arvo korkea!")
    elif hemglob<134:
        print("Arvo alhainen!")
    else:
        print("Arvo normaali")

elif sukupuoli == "Nainen":
    if hemglob>175:
        print("Arvo korkea!")
    elif hemglob<117:
        print("Arvo alhainen!")
    else:
        print("Arvo normaali")

#Ilmoitetaan onko käyttäjän arvo
#hänelle alhainen, korkea vai normaali