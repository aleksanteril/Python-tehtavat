from flask import Flask, Response
import json


app = Flask(__name__)

#Tarkistetaan onko syötetty luku alkuluku
#Alkuluku = True jos on, muuten false
def alkulukuTarkistaja(luku):
    Alkuluku = True
    if luku == 1 or luku == 0:
        Alkuluku = True
        return Alkuluku
    for i in range(2,luku):
        if luku % i == 0:
            Alkuluku = False
            break
    return Alkuluku


@app.route('/alkuluku/<inluku>')
def alkuluku(inluku):
    try:
        luku = int(inluku)
        onkoAlkuluku = alkulukuTarkistaja(luku)
        tilakoodi = 200
        vastaus = {
            "Number":luku,
            "isPrime":onkoAlkuluku
        }
        return Response(json.dumps(vastaus),status=tilakoodi, mimetype='application/json')
    except:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen syöttö tai muu virhe"
        }
        return Response(response=json.dumps(vastaus), status=tilakoodi, mimetype='application/json')

@app.errorhandler(404)
def not_found(error):
    vastaus = {
        "status": 404,
        "teksti": "Sivua ei löytynyt"
    }
    return Response(response=json.dumps(vastaus), status=404, mimetype='application/json')



#Serveri
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)