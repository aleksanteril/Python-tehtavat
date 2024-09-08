import mysql.connector

#Yhteyden luonti tietokantaan
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='aleksanteri',
         password='m4ks4',
         autocommit=True
         )

#Aliohjelma kyselyä varten jossa tulostetaan nimi ja kunta ICAO koodin perusteella
def namequery(icao):
    sql = (f"SELECT name, municipality "
           f"FROM airport "
           f"WHERE ident = '{icao}' ")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for tulo in tulos:
        print(f"Lentoasema {tulo[0]} sijaitsee kunnassa {tulo[1]}")
    return

icao = input("Syötä haettava ICAO koodi: ")
namequery(icao)
