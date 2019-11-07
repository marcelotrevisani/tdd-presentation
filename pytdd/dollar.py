class Dollar():
    def __init__(self, value):
        self._value = value

    def add(self, value):
        return Dollar(self._value + value)

    @property
    def value(self):
        return self._value

    def __eq__(self, compare):
        return self._value == compare.value
