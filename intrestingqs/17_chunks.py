def chunks(lst, size):
    """
    It takes a list and a size and returns a list of lists of the given size.
    
    :param lst: the list you want to split
    :param size: the number of items in each chunk
    :return: A list of lists.
    """
    return [list[i:i+size] for i in range(0, len(lst), size)]


a = [1, 1, 2, 3, 3, 4, 5, 6]

print(chunks(a, 3))