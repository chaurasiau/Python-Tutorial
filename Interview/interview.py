# This is interview question

tup1 = ('2021-01-20', ['abc', 'def'])
tup2 = ('2021-01-20', ['abc', 'def'])
tup3 = tup2

# The == operator is used to test if two objects are the same.
print(tup1 == tup2)
print(tup2 == tup3)
print(tup3 == tup1)

# The “is keyword” is used to test whether two variables belong to the same object. The test will return True if the two objects are the same else it will return False even if the two objects are 100% equal
print(tup2 is tup1)
print(tup3 is tup2)
print(tup3 is tup1)
