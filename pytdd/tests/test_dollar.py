from pytdd.dollar import Dollar


def test_dollar_add():
    num = Dollar(10)
    assert num.add(2) == Dollar(12)


def test_get_value():
    assert Dollar(5).get_value() == 5


def test_equal():
    assert Dollar(1) == Dollar(1)
    assert Dollar(1) != Dollar(2)
