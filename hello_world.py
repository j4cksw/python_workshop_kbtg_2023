from pprint import pprint


vat = 7

def vat_exclude(price, vat):
    return price * (vat/(100 + vat))


# print(vat_exclude(100, vat))
# print(vat_exclude(200, vat))
# print(vat_exclude(500, vat))

price_list = [100, 200, 500, 1000, 1099]

# for price in price_list:
#     print(vat_exclude(price, vat))

item_list = [
    {
        "title": "Python so stress",
        "price": 100,
        "type": {"book"}
    },
    {
        "title": "Dry mango",
        "price": 599,
        "type": {"food"}
    },
    {
        "title": "Dry fish",
        "price": 999,
        "type": {"food", "otop"}
    }
]

# whitelist = [ "book", "notebook" ] # List, mutable, ordered
# whitelist = ( "book", "notebook", "otop" ) # Tuple, immutable, ordered
whitelist = { "book", "notebook", "otop" } # Set, mutable, unordered


total_vat = 0
for item in item_list:

    item_type = item.get("type", "") # { "book", "...", "..." }

    # is_whitelisted = item_type in whitelist

    # is_whitelisted = False
    # for type in item_type:
    #     if type in whitelist:
    #         is_whitelisted = True
    #         break

    is_whitelisted = whitelist.intersection(item_type)
    print(is_whitelisted)
    print(bool(is_whitelisted))
    excluded_vat = 0 if is_whitelisted  else vat_exclude(item["price"], vat)

    total_vat += excluded_vat
    print(f'{item["title"]} {item["price"]} {excluded_vat:.2f}')

print(f"Total vat: {total_vat:.2f}")

# vat_list = []
# for item in item_list:
#     vat_list.append(vat_exclude(item["price"], vat))
# # print(vat_list)
# # print(f"Total vat: {sum(vat_list):.2f}")

# # List comprehension
# total_vat = sum([vat_exclude(item["price"], vat) for item in item_list])
# print(f"Total vat: {total_vat:.2f}")



