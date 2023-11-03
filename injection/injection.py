from flask import Flask, request, render_template_string
from sqlalchemy import text, create_engine
from dotenv import load_dotenv
import os


app = Flask(__name__)

load_dotenv()

db_db = os.environ['POSTGRES_DB']
db_password = os.environ['POSTGRES_PASSWORD']
db_user = os.environ['POSTGRES_USER']
db_url = \
    (f'postgresql://'
     f'{db_user}:{db_password}@localhost:5432/{db_db}')
engine = create_engine(db_url, echo=True)


@app.route('/')
def index():
    # Eine einfache HTML-Form ohne CSRF-Token
    return render_template_string('''
    <form action="/login" method="POST">
        <label for="username">Username</label>
        <input type="text" name="username" />
        <label for="password">Password</label>
        <input type="password" name="password" />
        <input type="submit" value="Login" />
    </form>
    ''')


@app.route('/login', methods=['POST'])
def search():
    username = request.form.get("username")
    password = request.form.get("password")
    with engine.connect() as con:
        sql = "SELECT * FROM public.user as u WHERE u.username = '"
        sql += username + "' AND u.password = '" + password + "'"

        sql = text(sql)
        result_set = con.execute(sql)
        if len(result_set.fetchall()) == 0:
            reply: str = "Login fehlgeschlagen!"
        else:
            reply: str = "Login erfolgreich!"

    # Unsicher: Der Query-Parameter wird direkt ohne Bereinigung oder Escaping in die Antwort eingefügt.
    return render_template_string(reply)


if __name__ == '__main__':
    app.run(debug=True, port=5007)
