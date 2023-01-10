# Python program to check if year is a leap year or not

year = 2001

# To get year (integer input) from the user
# year = int(input("Enter a year: "))

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap yea

if (year % 400 == 0) and (year % 100 == 0):
    print(f"{year} is a leap year")
elif (year % 4 == 0) and (year % 100 != 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
