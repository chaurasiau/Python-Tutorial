# The Property decorator

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        print("I am in @property of shares!!")
        return self._shares

    @shares.setter
    def shares(self, value):
        print("I am in @shares.setter of shares!!")
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value


s = Stock('IBM', 50, 91.1)
print(s.shares)
s.shares = 300
print(s.shares)
