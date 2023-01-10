def most_frequent(lst):
    return max(lst, key=lst.count)
    # return max(set(lst), key=lst.count)


a = [1, 2, 1, 2, 3, 4, 5, 2, 1, 1, 2, 1]

print(a.count(1))
#

print(most_frequent(a))
