def has_duplicates(lst):
    return len(lst) != len(set(lst))


a = [1, 1, 2, 3, 4, 5]

print(has_duplicates(a))
