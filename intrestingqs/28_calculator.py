# A dictionary that contains the operators as keys and the functions as values.
import operator

action = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul,
    "**": operator.pow
}

print(action["-"](10, 2))
