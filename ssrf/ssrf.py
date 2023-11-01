# noinspection HttpUrlsUsage
"""
Server Side Request Forgery (SSRF) ist eine Sicherheitslücke, bei der ein Angreifer einen Server dazu bringt,
Anfragen zu stellen, die er normalerweise nicht machen würde, möglicherweise an Systeme hinter einer Firewall,
die für den Angreifer selbst nicht direkt zugänglich sind.

Im folgenden Beispiel wird eine einfache Python-Anwendung mit Flask erstellt, die eine SSRF-Schwachstelle aufweist.
Der Anwendungscode verwendet die requests-Bibliothek, um URL-Anfragen zu verarbeiten, die von einem Benutzer über
einen Webformular-Parameter bereitgestellt werden. Das ist ein klassisches Beispiel für eine SSRF-Schwachstelle,
da der Server externe URLs abruft, die ein Benutzer eingeben kann, ohne diese ordnungsgemäß zu validieren oder zu
beschränken.

Wenn du dieses Beispiel ausführst, bietet es ein einfaches Formular, in das Benutzer eine URL eingeben können.
Die Anwendung holt dann den Inhalt der URL ab und zeigt ihn an. Ein Angreifer könnte jedoch eine URL zu einem
internen Service innerhalb der Infrastruktur des Unternehmens eingeben (zum Beispiel http://localhost:5002/internal
oder http://internal-database:3306) und dadurch möglicherweise sensible Informationen abrufen oder interne Systeme
beeinflussen.

Um SSRF zu verhindern, musst du ausgehende Anfragen anhand einer sicheren Liste validierter Dienste beschränken
und/oder sicherstellen, dass nicht auf interne Ressourcen zugegriffen werden kann. Zudem solltest du niemals
ungeprüfte Benutzereingaben als URL für Serveranfragen verwenden.
"""
from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return '''
        <h1>URL Inhaltsprüfer</h1>
        <form action="/check" method="POST">
            URL: <input type="text" name="url" value="http://localhost:5002/internal" />
            <input type="submit" value="Inhalt prüfen" />
        </form>
    '''


@app.route('/check', methods=['POST'])
def check():
    url = request.form['url']
    # Sicherheitsproblem: Hier wird der von Benutzern bereitgestellte URL ohne Validierung verwendet.
    # Ein Angreifer könnte eine interne oder sensible URL angeben, die der Server dann abruft.
    response = requests.get(url)
    return f"Inhalt der URL: {response.text}"


if __name__ == '__main__':
    app.run(debug=True, port=5001)
