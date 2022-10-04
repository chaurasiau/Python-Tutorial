# data access without security
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


s = Stock('IBM', 50, 91.1)
print(s.shares)
print(s.name)
print(s.prices)
