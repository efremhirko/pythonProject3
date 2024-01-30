#1 There are 5280 feet in a mile. Write a Python statement that
# calculates and prints the number of feet in 13 miles
# 1 mile=5280 feet's
# so to know how many feet are there in 13 mile simple we have multiply 5280 feet by 13 mile
# and then simply we can get our result which is equal to 68,640 feet's
miles = float(input("Enter the number of miles: "))

feet_in_miles = miles * 5280

print(f"There are {feet_in_miles:,} feet in {miles:.1f} miles.")

# 1. f-string (f before the string):
#
# It's a type of string formatting introduced in Python 3.6.
# It allows you to create strings with embedded expressions inside curly braces {}.
# This makes it easier to combine text and variables dynamically within a string.
# 2. Curly braces {}:
#
# They serve as placeholders for expressions that you want to insert into the string.
# When the f-string is evaluated, the
# expressions inside the curly braces are calculated and their values are seamlessly integrated into the final string.
print("\nstudent name: Ephrem Hirko\n")
print("ID: RU1360/12")