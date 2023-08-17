vat = 7

def vat_exclude(price, vat):
    return price * (vat/(100 + vat))

def exclude_vat(item_list, whitelist = set()):
    return [ 0 if whitelist.intersection(item["type"]) else vat_exclude(item["price"], vat) for item in item_list ]