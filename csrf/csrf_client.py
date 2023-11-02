from flask import Flask, request, render_template_string

app = Flask(__name__)


@app.route('/')
def index():
    # Eine einfache HTML-Form ohne CSRF-Token
    return render_template_string('''
    <form action="/change-email" method="POST">
      <input type="email" name="email" value="" placeholder="Enter new email" />
      <input type="submit" value="Change Email" />
    </form>
    ''')


@app.route('/change-email', methods=['POST'])
def change_email():
    email = request.form['email']
    # Hier würden Sie die E-Mail im Benutzerprofil aktualisieren
    # Aber da es keinen CSRF-Schutz gibt, könnte jede Seite diese Aktion ausführen
    return 'E-Mail wurde geändert zu: ' + email


if __name__ == '__main__':
    app.run(debug=True, port=5005)
