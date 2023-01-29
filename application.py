from flask import Flask
from flask import jsonify
from flask import request

application = Flask(__name__)
response = list()


@application.route("/")
def say_hello():
    return jsonify("Welcome to Home Page")


@application.route("/name")
def say_hello_from_request():
    name = request.json.get("name")
    return jsonify("my name is " + name)


@application.route("/adddata", methods=["POST"])
def add_data():
    data = dict()
    name = request.json.get("name")
    age = request.json.get("age")
    data["name"] = name
    data["age"] = age
    response.append(data)
    return jsonify(response)


if __name__ == "__main__":
    application.run()
