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
        "type": "book"
    },
    {
        "title": "Python so stress part.2",
        "price": 1000,
        "type": "book"
    },
    {
        "title": "Data something",
        "price": 1999,
        "type": "notebook"
    },
    {
        "title": "Dry mango",
        "price": 599,
    }
]

#book_list = [???]
#not_book_list = [???]

total_vat = 0
for item in item_list:
    # try:
    #     item_type = item["type"]
    # except KeyError:
    #     item_type = ""

    item_type = item.get("type", "")
    
    if item_type == "book" :
        excluded_vat = 0
    else:
        excluded_vat = vat_exclude(item["price"], vat)

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



