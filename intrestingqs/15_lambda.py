a = [7, 8, 9, 10]
b = [i for i in a if i > 8]

# same using lambda
# b = filter(lambda x: x > 8, a)
c = list(filter(lambda x: x > 8, a))

print(f"b = {b}")
print(f"c = {c}")
