"""
Dies ist ein sehr einfaches Beispiel einer Webanwendung in Python mit Flask,
die eine Reflected Cross-Site Scripting (XSS) Schwachstelle enthält.

Bitte beachte, dass dies nur zu Bildungszwecken dient und du diesen Code
niemals in einer echten Anwendung verwenden solltest, da er unsicher ist.

In diesem Codebeispiel wird die search-Route die Benutzereingabe query aus dem GET-Request
direkt in die Antwort eingefügt. Dies bedeutet, dass wenn ein Angreifer eine URL
mit schädlichem JavaScript-Code als Teil des query-Parameters erstellt, dieser Code
im Browser des Benutzers ausgeführt werden könnte.

Zum Beispiel, wenn jemand den folgenden Link besucht:
http://localhost:5000/search?query=<script>alert('XSS')</script>

Dann würde ein JavaScript-Alert mit der Nachricht 'XSS' im Browser angezeigt werden.

Um diesen Code sicherzumachen, müsste man die Benutzereingabe bereinigen oder besser,
die Benutzereingabe mit einer Template-Engine rendern, die automatisch XSS-Schutz bietet,
indem sie spezielle Zeichen escaped. In Flask kann das z.B. mit der escape-Funktion
von Jinja oder durch die sichere Verwendung von render_template_string erreicht werden.
"""
from flask import Flask, request, render_template_string

app = Flask(__name__)


@app.route('/')
def home():
    return '''
        <h1>Willkommen auf der Suche</h1>
        <form action="/search" method="get">
            <input type="text" name="query" />
            <input type="submit" value="Suchen" />
        </form>
    '''


@app.route('/search')
def search():
    query = request.args.get('query')
    # Unsicher: Der Query-Parameter wird direkt ohne Bereinigung oder Escaping in die Antwort eingefügt.
    return render_template_string('<h2>Suchergebnisse für: ' + query + '</h2><p>Keine Ergebnisse gefunden!</p>')


if __name__ == '__main__':
    app.run(debug=True)
