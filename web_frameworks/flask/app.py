from flask import Flask, render_template, jsonify, request

from uuid import uuid4

app = Flask(__name__)
GET = "GET"
POST = "POST"
DELETE = "DELETE"


def _generate_id():
    return str(uuid4())[0:5]


dog_data = {
    _generate_id(): {
        "name": "Annika",
        "type": "Black Mouth Cur",
        "weight": 65,
        "playfulness": 10,
    },
    _generate_id(): {"name": "Ace", "type": "Husky", "weight": 110, "playfulness": 8},
}
type_ids = {"Black Mouth Cur": 1, "Husky": 2}
next_type_id = 3


@app.route("/", methods=[GET])
def main():
    return render_template("index.html")


@app.route("/dog", methods=[GET, POST])
def dog():
    if request.method == GET:
        return jsonify(dog_data)
    elif request.method == POST:
        dog_data[_generate_id()] = request.json
        return jsonify(request.json)
    else:
        raise ValueError


@app.route("/dog/<dog_id>", methods=[GET, DELETE])
def get_dog(dog_id):
    if request.method == GET:
        return dog_data.get(dog_id, None)
    elif request.method == DELETE:
        return dog_data.pop(dog_id)
    else:
        raise ValueError
