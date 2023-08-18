from pprint import pprint
import sqlite3

from flask_sqlalchemy import SQLAlchemy

from models import Items, Types


class ItemsRepository():
    item_list = []

    def get_all_items(self):
        return self.item_list
    
    def add_item(self, item):
        self.item_list.append(item)

class SQLItemRepository():

    # Constructor
    def __init__(self):
        self.connection = sqlite3.connect("vat_api.db", check_same_thread=False)
        self.connection.row_factory = sqlite3.Row
    
    def __del__(self):
        self.connection.close()

    def get_all_items(self):
        result = self.connection.execute("SELECT * FROM ITEMS").fetchall()
        pprint(result)

        output = []
        for item in result:
            output.append({
                "title": item["title"],
                "price": item["price"],
                "type": []
            })
        pprint(output)
        return output
    
    def add_item(self, item):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO ITEMS (title, price) VALUES (?, ?)", 
                       (item["title"], item["price"]))
        item_id = cursor.lastrowid
        
        types = cursor.execute("SELECT * FROM TYPES WHERE title IN ('book')").fetchall()
        
        for type in types:
            cursor.execute(
                "INSERT INTO ITEMS_TYPES (item_id, type_id) VALUES (?, ?)",
                (item_id, type["id"]))

        self.connection.commit()
        
class ORMItemRepository():

    def __init__(self, db: SQLAlchemy):
        self.db = db

    def get_all_items(self):
        items = Items.query.all()
        return items
    
    def add_item(self, item):
        new_item = Items(title=item["title"], price=item["price"])
        
        types = Types.query.filter(Types.title.in_(item["type"]))
        new_item.type = list(types)

        self.db.session.add(new_item)
        self.db.session.commit()