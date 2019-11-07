from pytdd.dollar import Dollar


def test_dollar_add():
    num = Dollar(10)
    assert num.add(2) == Dollar(12)
