from flask import Flask, Response, jsonify

app = Flask(__name__)

profile_email = {"email": "oli@example.com"}


@app.route('/email')
def read_email():
    return jsonify({"email": profile_email['email']})


@app.route('/email/<new_email>', methods=['PUT'])
def change_email(new_email):
    profile_email['email'] = new_email
    return Response(status=200)


if __name__ == '__main__':
    app.run(debug=True, port=5006)
