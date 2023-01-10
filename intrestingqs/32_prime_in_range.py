def prime(num):
    Flag = False
    if num == 1:
        return False
    elif num > 1:
        for i in range(2, num):
            if num % i == 0:
                Flag = True
                break
        if Flag:
            return False
        else:
            return True


lower = 900
upper = 1000

for num in range(lower, upper+1):
    if prime(num):
        print(f"{num} is a Prime Number")
