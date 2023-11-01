from flask import Flask
import json

app = Flask(__name__)


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


@app.route('/internal')
def internal():
    users = [
        {"name": "Max", "email": "max@example.com"},
        {"name": "Otto", "email": "otto@example.com"}
    ]

    return users


if __name__ == '__main__':
    app.run(debug=True, port=5002)
