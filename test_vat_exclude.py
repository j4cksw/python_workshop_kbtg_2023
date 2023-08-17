from exclude_vat import exclude_vat


def test_empty_item_should_return_empty():
    result = exclude_vat([])
    assert result == []


def test_one_item_should_get_one_extracted_vat():
    result = exclude_vat([
        make_item("Python so stress", 100, { "book" })
    ])
    assert result == [ 6.5420560747663545 ]


def test_two_item_should_get_two_extracted_vat():
    result = exclude_vat([
        make_item("Python so stress", 100, { "book" }),
        make_item("Python so stress", 100, { "book" })
    ])
    assert result == [ 6.5420560747663545, 6.5420560747663545 ]


def test_one_exclude_item_should_get_one_zero_vat():
    result = exclude_vat([
        make_item("Python so stress", 100, { "book" })
    ], { "book" })
    assert result == [ 0 ]


def test_two_excludes_item_should_get_two_zero_vat():
    result = exclude_vat([
        make_item("Python so stress", 100, { "book" }),
        make_item("Python so stress", 100, { "book" })
    ], { "book" })
    assert result == [ 0, 0 ]


def test_two_excludes_item_should_get_two_zero_vat():
    result = exclude_vat([
        make_item("Python so stress", 100, { "book" }),
        make_item("Python so stress", 100, { "book" })
    ], { "book" })
    assert result == [ 0, 0 ]

def test_two_items_with_one_exclude_item_should_get_one_vat_and_zero_vat():
    result = exclude_vat([
        make_item("Python so stress", 100, { "book" }),
        make_item("Dried mango", 100, { "food" })
    ], { "book" })
    assert result == [ 0, 6.5420560747663545 ]

def make_item(title, price, type):
    return {
        "title": title,
        "price": price,
        "type": type
    }
