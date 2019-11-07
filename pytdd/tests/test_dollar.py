from pytdd.dollar import Dollar


def test_dollar_add():
    assert Dollar(10) + Dollar(2) == Dollar(12)


def test_get_value():
    assert Dollar(5).value == 5


def test_equal():
    assert Dollar(1) == Dollar(1)
    assert Dollar(1) != Dollar(2)
