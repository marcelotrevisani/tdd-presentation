class Dollar():
    def __init__(self, value):
        self._value = value

    def add(self, value):
        return Dollar(self._value + value)