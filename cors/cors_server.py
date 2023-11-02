"""
Cross-Origin Resource Sharing (CORS) ist ein Mechanismus, der es erlaubt, auf Ressourcen von einer anderen Domain
aus zuzugreifen, als von der aus die erste Ressource geladen wurde. Eine CORS-Schwachstelle entsteht, wenn eine
Anwendung zu freizügig im Umgang mit diesen Anfragen ist und Zugriffe von nicht vertrauenswürdigen oder nicht
vorgesehenen Ursprüngen (Origins) erlaubt.

Hier ist ein Beispiel für eine einfache Python-Flask-Anwendung, die unsachgemäß konfigurierte CORS-Header setzt,
wodurch eine CORS-Schwachstelle entsteht.

In diesem Code wird der Access-Control-Allow-Origin-Header auf * gesetzt, was bedeutet, dass jede Website die Daten
dieser Endpunkt-Route anfordern und lesen kann. Das ist ein Sicherheitsrisiko, insbesondere wenn die Route sensible
Informationen liefert, da bösartige Websites diese Daten bei ihren Benutzern abfragen und empfangen könnten.
"""
from flask import Flask

app = Flask(__name__)


@app.after_request
def add_cors_headers(response):
    # Unsicher: Es wird auf alle Anfragen '*' gesetzt, was bedeutet, dass jeder Ursprung (Origin) akzeptiert wird.
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:5004'

    return response


@app.route('/sensitive')
def sensitive_data():
    # Stell dir vor, dies wäre eine sensible Operation, deren Daten nicht für alle Origins freigegeben werden sollten.
    return {'secret': 'oli@example.com'}


if __name__ == '__main__':
    app.run(debug=True, port=5003)
