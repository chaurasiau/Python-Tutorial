from collections import Counter

# Counting the number of times each element appears in the list.
my_list = ['a','a','b','b','b','c','d','d','d','d','d','e','e','f','f']
count = Counter(my_list)

print(count)

print(count['d'])