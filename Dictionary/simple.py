companies = {
    'GOOG': 'Google',
    'IBM': 'Internation Business Machine',
    'MSFT': 'Microsoft'
}

# Accessing data in dictionary
print(companies['GOOG'])  # if the key 'GOOG' is not there it throws error

# Better method is
print(companies.get('GOOG', 'Key Not Present'))

# Composite key
toppers = {
    ('class', 'school'): 'Gopal',
    ('Maths', 'Physics'): 'Ram',
    ('Commerce', 'Finance'): "Money",
}

toppers1 = {
    ['class', 'school']: 'Gopal'}

# for key1, key2 in toppers:
#     print(f"Key1 is {key1} and Key2 is {key2}")

for topper in toppers:
    print(f"topper in {topper[0]} is {toppers.get(topper, 'No Value')}")
    print(f"topper in {topper[1]} is {toppers.get(topper, 'No Value')}")
    # print(
    # f"the value of topper of class is {toppers.get(topper,'Class not found')}")
