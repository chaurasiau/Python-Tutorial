def list_to_dict(lst1, lst2):
    return dict(zip(lst1,lst2))


l1 = ['a', 'b', 'c']
l2 = [1,2,3]

print(list_to_dict(l1, l2))