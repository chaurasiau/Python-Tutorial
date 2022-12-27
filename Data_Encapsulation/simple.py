# data access without security
# The class Stock is created with three attributes: name, shares, and price. 
# 
# The __init__ method is a special method that is called when an instance of the class is created. 
# 
# The __init__ method is passed three arguments: self, name, shares, and price. 
# 
# The self argument is a reference to the instance of the class. 
# 
# The self argument is used to access variables that belong to the class. 
# 
# The __init__ method is used to initialize the attributes of the class. 
# 
# The __init__ method is called automatically when an instance of the class is created. 
# 
# The __init__ method is used to initialize the attributes of the class. 
# 
# The __init__ method is called automatically when an instance of the class is created. 
# 
# The __init
class Stock:
    # It creates a class called Stock.
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


s = Stock('IBM', 50, 91.1)
print(s.shares)
print(s.name)
print(s.prices)
