from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)


@app.route('/')
def index():
    # Eine einfache HTML-Form ohne CSRF-Token
    return render_template_string('''
    <form action="/change_email" method="POST">
      <input type="email" name="email" value="" placeholder="Enter new email" />
      <input type="submit" value="Change Email" />
    </form>
    ''')


@app.route('/change_email', methods=['POST'])
def change_email():
    email = request.form['email']
    # Hier würden Sie die E-Mail im Benutzerprofil aktualisieren
    # Aber da es keinen CSRF-Schutz gibt, könnte jede Seite diese Aktion ausführen

    token_response = requests.post('http://localhost:5006/token', json={'user_id': 'user1'})
    user_token = token_response.json()['user_token']

    email_response = requests.put('http://localhost:5006/email/' + email, json={'user_token': user_token})
    if email_response.status_code == 401:
        return 'Nicht autorisiert'
    else:
        return 'E-Mail wurde geändert zu: ' + email


if __name__ == '__main__':
    app.run(debug=True, port=5005)
