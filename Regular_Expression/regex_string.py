# Strings are of 2 type
import re
import string

# pattern = 'this is a dot \.'
# sr = r'sjdfjksd\.ahfjk'
# 1. Regular string - this treats '\' as an escape charater
# 2. Raw String - this does not treat '\' as an escape charater - This is because the regular expression engine uses \ character for its own escaping purpose.
# \   Used to drop the special meaning of character
#     following it (discussed below)
# []  Represent a character class [123]
# ^   Matches the beginning  -- ^this is begin$
# $   Matches the end
# .   Matches any character except newline
# ?   Matches zero or one occurrence.   x = ac, pattern = ab*c | ab+c, , ac, abc
# |   Means OR (Matches with any of the characters
#     separated by it.
# *   Any number of occurrences (including 0 occurrences)
# +   One or more occurrences
# {}  Indicate number of occurrences of a preceding RE -- (ab{,4}c), ---abbc, abbbbbbbbbc
#     to match.
# ()  Enclose a group of REs
# --------------------------------------------------------------
# 1. \ – Backslash and .


s = '\nthis. is a dot'

# without using \
match = re.search(r'.', s)
print(match)

# using \
match = re.search(r'\.', s)
print(match)

# --------------------------------------------------------------
# 2. [] – Square Brackets , ^ and $, \b, \B

pattern = r'[0, 9]' or r'[0-9]'  # [0123456789]
pattern = r'[a, z]' or r'[a-z]'  # [abcde...xyz]

anti_pattern = r'[^0-3]' or r'[^0123]'
anti_pattern = r'[^a-d]' or r'[^abcd]'

# ^ also means starts with
sentence = 'let us start this car'
start_pattern = r'^let'
end_pattern = r'car$'
result = re.search(start_pattern, sentence)
print(f"Start_pattern - {result}")
result = re.search(end_pattern, sentence)
print(f"End_pattern - {result}")
ps = r'\blet'
result = re.search(ps, sentence)
print(f"ps_pattern - {result}")
pe = r'car\b'
result = re.search(pe, sentence)
print(f"pe_pattern - {result}")

sentence = 'This let us start this car bro'
ps = r'\Bis'
result = re.search(ps, sentence)
print(f"ps_pattern - {result}")
# pe = r'br\B'
# result = re.search(pe, sentence)
# print(f"pe_pattern - {result}")

print('Done')

# --------------------------------------------------------------
# . – Dot, | – Or, ? – Question Mark, * – Star, + – Plus, {m, n} – Braces
# \d, \w
# \d - 0123456789

# \w
# string = 'this is aaaa  aa' \w{2, 4} aaaa, aa
# ------------------------
# Methods - re.findall()
# ------------------------
# \d to find all the number in a string
string_number = "This 12 sequence 1234 and 567, and this is mixed 1423 and  567"
pattern = r'\d{3,4}'  # | r'\d+'
result = re.findall(pattern, string_number)
print(result)

# [3,5]- [3-5]
# ------------------------
# Methods - re.compile(), re.split()
# ------------------------
string_number = "This is increasing 12 sequence 1234 567, and this is mixed 1423 567"
pattern1 = r'\d{3,4}'
pattern2 = r'\d+'
p1 = re.compile(pattern1)
p2 = re.compile(pattern2)
result = p1.findall(string_number)
print(result)
result = p2.findall(string_number)
print(result)

# ------------------------
# Methods - re.split(), re.sub(), re.subn()
# ------------------------
# ------------------------
# Methods - re.search() : This method either returns None (if the pattern doesn’t match), or a re.MatchObject that contains information about the matching part of the string. This method stops after the first match, so this is best suited for testing a regular expression more than extracting data.
# ------------------------

pattern1 = r"[a-zA-Z]+ \d+"
pattern2 = r"(([a-zA-Z]+) (\d+))"  # groups

match = re.search(
    pattern, "India won first cricket world cup in June 1983, jan 2011")

print(f"Search -> pattern match is {match}")
print(f"Search -> pattern group is {match.groups()}")

# ------------------------
# Methods - re.match() : This function attempts to match pattern to whole string. The re.match function returns a match object on success, None on failure.
# ------------------------
sentence = "India won first cricket world cup in June 1983"
pattern = r"(([a-zA-Z]+) (\d+))"
match = re.match(pattern, sentence)
print(f"Match result is {match}")

# ------------------------
# Methods - re.findall() : Return all non-overlapping matches of pattern in string, as a list of strings. The string is scanned left-to-right, and matches are returned in the order found
# ------------------------

print('Done')
