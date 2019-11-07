import requests

URL_API = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
API_KEY = "FJOSXYTTSW4VUT7H"


class Dollar:
    def __init__(self, value):
        self._value = value

    def __add__(self, dollar_add):
        return Dollar(self._value + dollar_add.value)

    @property
    def value(self):
        return self._value

    def __eq__(self, compare):
        return self._value == compare.value

    def convert_to_pound(self):
        url_request = (
            f"{URL_API}" f"&from_currency=USD&to_currency=GBP&apikey={API_KEY}"
        )

        response = requests.get(url_request)
        data_exchange = response.json()
        exchange_rate = data_exchange["Realtime Currency Exchange Rate"]
        exchange_rate = float(exchange_rate["5. Exchange Rate"])
        return Dollar(self.value * exchange_rate)
