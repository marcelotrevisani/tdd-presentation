import requests

from pytdd.dollar import Dollar


def test_dollar_add():
    assert Dollar(10) + Dollar(2) == Dollar(12)


def test_get_value():
    assert Dollar(5).value == 5


def test_equal():
    assert Dollar(1) == Dollar(1)
    assert Dollar(1) != Dollar(2)


def test_convert_pound(monkeypatch):
    monkeypatch.setattr(requests, "get", mock_requests_get)
    assert Dollar(10).convert_to_pound() == Dollar(5)


def mock_requests_get(url):
    return MockResponse()


class MockResponse:
    def json(self):
        return {"Realtime Currency Exchange Rate": {"5. Exchange Rate": "0.5"}}


def test_dollar_repr():
    assert str(Dollar(10)) == "Dollar(value=10)"
