from pprint import pprint
from flask import Flask, request
from exclude_vat import exclude_vat
from repository import ItemsRepository, SQLItemRepository, ORMItemRepository
from models import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)

@app.route("/")
def hello_world():
    return "Hello world"

#item_reposotry = ItemsRepository()
#item_reposotry = SQLItemRepository()
item_reposotry = ORMItemRepository(db)

@app.route("/items", methods=["PUT"])
def add_item():
    item_reposotry.add_item(request.json)
    pprint(item_reposotry.get_all_items())
    return "", 201


@app.route("/vat")
def get_vat_list():
    whitelist = { "book" }
    return exclude_vat(item_reposotry.get_all_items(), whitelist)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)