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

#Aliohjelma lentokenttien tyypin ja määrän saamiseksi maatunnuksella
def airportcount(iso):
    sql = (f"SELECT type, count(*) "
           f"FROM airport "
           f"WHERE iso_country = '{iso}'"
           f"group by type "
           f"order by count(*) desc; ")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for tulo in tulos:
        print(f"Tyyppi: {tulo[0]} Määrä: {tulo[1]}")
    return

#Pääohjelma, kysytään maatunnus ja kutsutaan aliohjelmaa
iso = input("Syötä maatunnus: ")
airportcount(iso)


