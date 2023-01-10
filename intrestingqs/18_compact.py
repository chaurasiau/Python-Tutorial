def compact(lst):
    """
    It takes a list, filters out the falsy values, and returns the resulting list

    :param lst: The list to compact
    :return: A list of all the non-empty elements in the list.
    """

    return list(filter(None, lst))


a = ['', None, 1, 3, 5, 0, False]

print(compact(a))
