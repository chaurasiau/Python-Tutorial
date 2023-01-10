def sum(x, y):
    return x + y


def sub(x, y):
    return x - y


a, b = 4, 5
print((sub if a > b else sum)(a,b))
print((sub(a,b) if a > b else sum(a,b)))