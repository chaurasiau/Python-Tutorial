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
    """
    It takes a function, waits a number of seconds, then calls the function and returns the result
    
    :param seconds: the number of seconds to wait before calling the function
    :param func: a function that returns a string
    :param d: a string
    :param y: a string
    :return: "abcd"
    """
    import time
    time.sleep(seconds)
    str = func()
    str += "d" + "y"
    return str


def greeting():
    """
    The function `greeting()` prints the string `Hello Gopal` to the console
    """
    print('Hello Gopal')


after(30, greeting)


after()
