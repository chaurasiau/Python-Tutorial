from collections import defaultdict


# Function to return a default
# values for keys that is not
# present
def def_value():
    return "Key Not Present"


# Defining the dict
d = defaultdict(def_value)
# d = defaultdict(lambda: "Not Present")
d["a"] = 1
d["b"] = 2

print(d["a"])
print(d["b"])
print(d["c"])

# ---------map key to multiple values--------------

portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]

holdings = defaultdict(list)
for name, shares, price in portfolio:
    holdings[name].append((shares, price))

print(f"One Key to Many \n {holdings}")
