# Closure- When an inner function is returned as a result, that inner function is known as a closure.
def add(x, y):
    def do_add():
        print('Adding', x, y)
        return x + y
    return do_add


a = add(3, 4)
print(f"the sum is {a()}")


# ----------------
def after(seconds, func, d, y):
    import time
    time.sleep(seconds)

    str = func()
    str += "d" + "y"
    return str


def greeting():
    print('Hello Gopal')


after(30, greeting)
