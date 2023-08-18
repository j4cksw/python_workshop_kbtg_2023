from pprint import pprint
import sqlite3


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
        self.connection.commit()
        


