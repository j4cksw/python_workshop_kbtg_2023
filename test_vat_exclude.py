from exclude_vat import exclude_vat


def test_empty_item_should_return_empty():
    result = exclude_vat([])
    assert result == []

def test_one_item_should_get_one_vat():
    result = exclude_vat([{
        "title": "Python so stress",
        "price": 100,
        "type": { "book" }
    }])
    assert result == [ 6.5420560747663545 ]