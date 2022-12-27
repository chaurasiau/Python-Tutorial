class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price


c = Computer()
c.sell()

# change the price
print(f"Setting the Price using c.__maxprice")
c.__maxprice = 1000
c.sell()
print(f"After Setting the Price using c.__maxprice")

# using setter function
c.setMaxPrice(1000)
c.sell()
