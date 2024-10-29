
import requests

#Api-key, poistettu githubista
key = ###

#Kysytään käyttäjältä paikkakunta joka haetaan
paikka = input("Syötä paikkakunta: ")

#Muodostetaan kysely url ja haetaan tiedot
url = "https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s" % (paikka, key)
#try except request kirjaston juttuja varten
try:
    vastaus = requests.get(url)
    #Jos status_code eri kuin 200, virheilmoitus
    if vastaus.status_code != 200:
        print("Säätietoja ei saatavilla")
    else:
        vastaus = vastaus.json()
        tempCels = vastaus["main"]["temp"] - 273.15
        weather = vastaus["weather"][0]["main"]
        print(f"Today is {weather} with temp of {tempCels:.0f} Celsius")
except requests.exceptions.RequestException:
    print("Hakua ei voitu suorittaa")
