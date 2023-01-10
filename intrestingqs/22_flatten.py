def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)

    return ret


def deep_flatten(arg):
    flat_list = []
    [flat_list.extend(deep_flatten(x)) for x in arg] if isinstance(
        arg, list) else flat_list.append(arg)
