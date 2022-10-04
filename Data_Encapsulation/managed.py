# Managed Attributes for data security
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.set_shares(shares)
        self.price = price

    # Function that layers the "get" operation
    def get_shares(self):
        return self._shares

    # Function that layers the "set" operation
    def set_shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        self._shares = value


s = Stock('IBM', 50, 91.1)
print(s.get_shares())
s.set_shares(300)
print(s.get_shares())
