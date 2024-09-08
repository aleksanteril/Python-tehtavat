import mysql.connector
from geopy import distance

#Yhteyden luonti tietokantaan
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='aleksanteri',
         password='m4ks4',
         autocommit=True
         )


#Aliohjelma käyttäjän syötettä varten
def syote(lkm):
    list = []
    for i in range(1,lkm+1):
        list.append(input(f"Syötä {i}. ICAO-koodi: "))
    return list #Palautus listana jossa koodit

#Aliohjelma koordinaatti kyselyä varten jossa 2 paikkaa saadaan paluuna
def coordinatequery(icao1, icao2):
    sql = (f"SELECT latitude_deg, longitude_deg "
           f"FROM airport "
           f"WHERE ident = '{icao1}' or ident = '{icao2}'; ")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos  #Palautus listana, jossa monikkoja

#ICAO koodi lista syötteistä aliohjelmalta
icaolist = syote(2)

#Koordinaattien kysely syötteiden mukaan
koordinaatit = coordinatequery(icaolist[0], icaolist[1])

#Lasketaan geopy kirjaston avulla etäisyys paikkojen välillä
dist = distance.distance(koordinaatit[0], koordinaatit[1]).kilometers

#Tulostetaan tulokset käyttäjälle
print(f"Lentokenttien {icaolist[0]} ja {icaolist[1]} välinen etäisyys on {dist:.2f} km.")