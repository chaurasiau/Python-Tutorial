# This is tutorial for - A generator is any function that uses the yield statement
# Producer
def countdown(n):
    while n > 0:
        yield n
        n -= 1


# Consumer
for x in countdown(10):
    print(x, end=' ')


# ---------------------------
a = [1, 2, 3, 4]
b = (2*x for x in a)
print(type(b))
for i in b:
    print(i, end=' ')
