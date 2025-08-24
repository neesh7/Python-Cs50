# Ask user for name
name = input("What's your name1? ")  # using input function without assignment operator

# Removing whitespaces from both ends in string using strip method
name = name.strip()

"""
Method vs Function
Method is a function which is associated with an object and is called using dot notation
function is a block of code which is called by its name
Method is called on an object and function is called independently

"""

# Capitalize the first letter of the name using capitalize method
# name = name.capitalize()

# title method to capitalize the first letter of each word in the name - ususally used for names
name = name.title()

print(f"Hello, {name}")

#chaining multiple methods at once
# print(f"Hello, {name.strip().title()}")

name2 = input("What's your name2? ") .strip().title()
print(f"Hello, {name2}")


# using split 
name3 = input("What's your name2? ") .strip().title()
first, last = name3.split(" ")  # unpacking the list into two variables
print(f"Hello, {first}")