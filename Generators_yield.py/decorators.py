# This is tutorial for Decorators

def add(x, y):
    print('Calling add')
    return x + y


def sub(x, y):
    print('Calling sub')
    return x - y


def logged(func):
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper


@logged
def add(x, y):
    return x + y


@logged
def sub(x, y):
    return x - y


print(add(2, 3))
print(sub(5, 3))
