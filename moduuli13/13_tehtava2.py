from flask import Flask, Response, request
import mysql.connector
import json

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='aleksanteri',
         password='m4ks4',
         autocommit=True
         )

app = Flask(__name__)


#Hakee nimen ja kaupungin, (nimi, kaupunki)
def haeTietokannasta(icao):
    query = 'SELECT ident, name, municipality FROM airport WHERE ident = %s;'
    cursor = yhteys.cursor()
    cursor.execute(query, (icao,))
    vastausTuple = cursor.fetchall()[0]
    return vastausTuple


#Funktio jossa käsitellään asiakkaan kysely ja heitetään virhe
@app.route('/lentokentta')
def asiakasKysely():
    try:
        args = request.args
        icao = args.get('icao')
        tiedotTuple = haeTietokannasta(icao)
        vastaus = {
            "ICAO": tiedotTuple[0],
            "Nimi": tiedotTuple[1],
            "Kaupunki": tiedotTuple[2]
        }
        return Response(response=json.dumps(vastaus), status=200, mimetype='application/json')
    except:
        vastaus = {
            "status": 400,
            "teksti": "Tietoa ei löytynyt tai tapahtui virhe"
        }
        return Response(response=json.dumps(vastaus), status=400, mimetype='application/json')


#Yleinen notfound
@app.errorhandler(404)
def notFound():
    vastaus = {
        "status": 404,
        "teksti": "Sivua ei löytynyt"
    }


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)