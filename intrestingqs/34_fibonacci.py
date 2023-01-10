def fibonacci(number):
    n1, n2 = 0, 1

    count = 0
    if number <= 0:
        return "Give a positive number"
    elif number == 1:
        print(n1)
    else:
        while count < number:
            print(n1)
            next = n1 + n2
            n1 = n2
            n2 = next
            count += 1

fibonacci(2)
