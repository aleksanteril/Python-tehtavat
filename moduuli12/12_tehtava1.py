import requests


#Virheilmoitus
def virhe():
    print("Vitsiä ei löytynyt")
    return

#Luodaan kysely url
url = "https://api.chucknorris.io/jokes/random"

#Request erroreita varten
try:
    # GET Chuck norris vitsi
    vastaus = requests.get(url)
    #Jos yhteydenotto ei ok
    if vastaus.status_code != 200:
        virhe()
    else:
        vastaus = vastaus.json()
        print(vastaus["value"])
except requests.exceptions.RequestException:
    virhe()
