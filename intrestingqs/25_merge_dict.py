def merge_two_dict(dict1, dict2):
    dict3 = dict1.copy()
    dict3.update(dict2)
    return dict3


a = {'x': 1, 'y': 2}
b = {'z': 1, 'y': 3}

print(merge_two_dict(a, b))
