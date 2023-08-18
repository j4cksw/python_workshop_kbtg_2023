vat = 7

def vat_exclude(price, vat):
    return price * (vat/(100 + vat))

def exclude_vat(item_list, whitelist = set()):
    return [ 0 if whitelist.intersection(item["type"]) 
            else vat_exclude(item["price"], vat) 
            for item in item_list ]


if __name__ == "__main__":
    item_list = [
        {
            "title": "Python so stress",
            "price": 100,
            "type": {"book"}
        },
        {
            "title": "dried mango",
            "price": 100,
            "type": {"food"}
        }
    ]
    whitelist = { "book" }
    print(exclude_vat(item_list, whitelist))