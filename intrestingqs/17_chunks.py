def chunks(lst, size):
    return [list[i:i+size] for i in range(0, len(lst), size)]


a = [1, 1, 2, 3, 3, 4, 5, 6]

print(chunks(a, 3))