class ItemsRepository():
    item_list = []

    def get_all_items(self):
        return self.item_list
    
    def add_item(self, item):
        self.item_list.append(item)



