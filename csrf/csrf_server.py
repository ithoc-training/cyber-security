import uuid
from flask import Flask, Response, jsonify, request

app = Flask(__name__)

profile_email = {"email": "oli@example.com"}

session_store: [] = []


@app.route('/email')
def read_email():
    return jsonify({"email": profile_email['email']})


@app.route('/token', methods=['POST'])
def token():
    body = request.get_json()
    user_id: str = body['user_id']
    user_token: str = str(uuid.uuid1())
    session_store.append(user_token)
    return jsonify({"user_token": user_token})


@app.route('/email/<new_email>', methods=['PUT'])
def change_email(new_email):
    user_token = request.json['user_token']
    if user_token in session_store:
        profile_email['email'] = new_email
        return Response(status=200)
    else:
        return Response(status=401)


if __name__ == '__main__':
    app.run(debug=True, port=5006)
