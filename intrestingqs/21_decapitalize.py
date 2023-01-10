def decapitalize(str1):
    """
    It takes a string, and returns a string with the first letter lowercase

    :param str1: The string to decapitalize
    :return: The first letter of the string is being returned in lowercase, and the rest of the string
    is being returned in its original case.
    """
    return str1[:1].lower() + str1[1:]


print(decapitalize('This Is The New World!'))
