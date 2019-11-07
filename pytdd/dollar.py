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
