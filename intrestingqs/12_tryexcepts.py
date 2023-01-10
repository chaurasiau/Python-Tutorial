a, b = 1, 0
try:
    print(a/b)
except ZeroDivisionError:
    print('Division by zero')
else:
    print("No Error")
finally:
    print("Run this always")
