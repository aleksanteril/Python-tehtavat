
#Kysytään käyttäjän sukupuoli
sukupuoli = input("Mikä on sukupuolesi? Mies/Nainen: ")

#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l
#Kysytään käyttäjän hemoglobiiniarvo
hemglob = int(input("Mikä on hemoglobiiniarvosi? g/l: "))

if sukupuoli == "Mies":
    if 134 <= hemglob <= 195:
        print("Arvo normaali")
    elif hemglob>195:
        print("Arvo korkea!")
    elif hemglob<134:
        print("Arvo alhainen!")

if sukupuoli == "Nainen":
    if 117 <= hemglob <= 175:
        print("Arvo normaali")
    elif hemglob>175:
        print("Arvo korkea!")
    elif hemglob<117:
        print("Arvo alhainen!")

#Ilmoitetaan onko käyttäjän arvo
#hänelle alhainen, korkea vai normaali