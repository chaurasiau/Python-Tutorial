def prime(num):
    Flag = False
    if num == 1:
        return f"{num} is not a prime Number"
    elif num > 1:
        for i in range(2, num):
            if num % i == 0:
                Flag = True
                break
        if Flag:
            return f"{num} is not a prime number"
        else:
            return f"{num} is prime number"


while True:
    number = int(input("Enter a number : "))
    print(prime(number))
