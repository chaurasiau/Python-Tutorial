def all_unique(lst):
    """
    If the length of the list is the same as the length of the set of the list, then all the elements in
    the list are unique

    :param lst: The list to check
    :return: True or False
    """
    return len(lst) == len(set(lst))


a = [1, 1, 2, 3, 3, 4, 5, 6]

print(all_unique(a))
