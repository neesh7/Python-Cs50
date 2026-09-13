# use hash for single line comment
# Functions - Takes input and gives output (side effects)
"""This is a multi line comment / Doctring
Summary line.

Keyword arguments:
argument -- description
Return: return_description
"""
# Printitng hello world
# print function is used to print something on the screen, and hello world is a string which is argument to the print function
# print("hello world")

user_input = input("What's your name? ") # using input function with assignment operator to store the input in a variable
print("Hello",user_input) # direct usage of comma
print("Hello" + " " + user_input)  # concatenation
print("Hello {0} - using format method".format(user_input)) # format method
print(f"Hello {user_input} - using f-string")  # f-string

# Parameters and Arguments
def hello(to="world"):  # here to is parameter with default value world
    print(f"Hello {to}")
hello("Harry")  # here Harry is argument
hello()  # here no argument is passed so default value will be used
# basically while defining function we use parameters and while calling function we use arguments it's the same thing but different names with different context

# Postional parameters(mandatory) vs named parameters ( Optional parameters) in functions

# Keyword Arguments (Order doesn't matter in keyword arguments) and named parameters
# Positional Arguments(Order matters in positional arguments)
print("hello ", "Zed", sep="-", end="!")  # sep is used to define separator between multiple arguments and end is used to define what to print at the end of the statement

