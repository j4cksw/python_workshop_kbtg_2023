from pprint import pprint
from flask import Flask, request
from exclude_vat import exclude_vat

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world"

item_list = []

@app.route("/items", methods=["PUT"])
def add_item():
    item_list.append(request.json)
    pprint(item_list)
    return "", 201

@app.route("/vat")
def get_vat_list():
    whitelist = { "book" }
    return exclude_vat(item_list, whitelist)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)