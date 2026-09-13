####### 1. Variables and Data types
####### 2. Dynamically typed language

# Name is a variable with data neesh in form of string
# Python is dynamically + Strongly typed language so we don't declare variable type while declaring a variable
# name is basically used as referance here which points to string object neesh in memory and the type is decided on runtime that's why python sometimes lacks on speed front
# 
name = "Neesh"

# Note: not enforced by python, it still checks at runtime . it is for linters/ides and static checkers
name: str = "Neesh" # type hints

# Extra Load on interpreter from this dynamic typing comes, because when we do name='Neesh' or sum = a + b
# The interpreter does the following at runtime
# 1. Track object type (variable types)
# 2. Look up variable binding in dictionaries (scope lookups)
# 3. Decide which operation implemention to call based on the runtime types
# resulting, more pointer chasing, hash table lookups and type checking compared to statically typed language.


######## 3. Compiled vs Interpreted language
# Note: Every operation in CPU handled by microprocessors which have ALU which handles these stuff.
# ALU Understands only instructions set and based on it does the operation. Basically some flipfloff changing their states to achieve a certain results.

# Compiled language
# Source code is compiled --> We get native machine code / executabled or artifacts ( Very low-level code)--> Cpu executes that machine code directly.
# faster execution and , fewer runtime checks

# Interpreted language
# Source code --> some intermediate code (bytecode)(simpler set of instructions)
#                               |
# Interpretor reads every instruction one by one ( adding number, multiplying numbers)
#                               |
# Runs eqivalent c code that implements these instruction on real machine 
# CPU --> Runs Interpreter --> Interpretor --> runs bytecode --> act on data
# + while doing all of this interpretor have to handle dynamic features basically resulting more work per line of code.



###### why to use python ?

# You use dynamically typed languages like Python because they make development 10x faster and more flexible, even if execution is slower.

# Key Advantages
# No type boilerplate: Write name = "ravi" or x = 5 without string name or int x. Less code, fewer mistakes.

# Rapid prototyping: Change types on the fly, experiment quickly without recompiling. Perfect for scripts, data analysis, automation.

# Cleaner, readable code: Focus on logic, not type declarations. Shorter functions, easier collaboration.

# Duck typing/polymorphism: Code works with any object that has the right methods (e.g. len(anything)). No interfaces needed.

# Great for unknown/variable data: JSON APIs, user input, config files—handle mixed types easily.

# Real-world use cases where speed trade-off is worth it
# Scenario	Why dynamic shines	Static alternative
# Data science/ML	Quick scripts, explore datasets	C++ too verbose
# Web scraping/Automation	Throwaway scripts	Java overkill
# Prototypes/Startups	Iterate fast	Go/TypeScript slower dev
# Glue code (integrate tools)	Flexible data handling	Rust too rigid
# The trade-off is deliberate
# Dynamic: 80% of code is dev time (prototyping, maintenance). Performance is secondary—use NumPy/C for hot loops.

# Static: 50% compile time, catches errors early, but slower to write/change.

# Python dominates data science, web dev (Django/Flask), automation because dev speed > raw CPU speed for most tasks. Add type hints + mypy if you need safety.

###### 4. Integer and operators
# + - add
# - - subtract
# * - multiply
# / - divide (output in float)
# % - Modulo Operator it gives remainders
# // - integer division
# ** - power
print(4/2)
print(4//2)
###### 5. Escape Sequences
# Concept of escape sequences
print("hello\nworld")  # \n is used for new line
print("hello\tworld")  # \t is used for tab space
print("hello\\world")  # \\ is used to print single backslash
print('hello "world"')  # using single quote to print double quote
print("hello 'world'")  # using double quote to print single quote
print("hello \"world\"")  # using escape sequence to print double quote inside double quote
print('hello \'world\'')  # using escape sequence to print single quote inside single quote
print(r"hello\nworld")  # r is used to print raw string means escape sequences will not be processed
print("hello\bworld")  # \b is used for backspace
print("hello\rworld")  # \r is used for carriage return
print("hello\fworld")  # \f is used for form feed
print("hello\vworld")  # \v is used for vertical tab
print("hello\aworld")  # \a is used for alert (bell)
print("hello\0world")  # \0 is used for null character
print("hello\100world")  # \100 is used for octal value
print("hello\x40world")  # \x40 is used for hexadecimal value
print("hello\u0040world")  # \u0040 is used for unicode value
print("hello\U00000040world")  # \U00000040 is used for unicode value with 8 digits
print("hello\b\bworld")  # multiple backspace
print("hello\t\tworld")  # multiple tab space
print("hello\n\nworld")  # multiple new line
###### 6. Taking Inputs and Print Method
your_name = input("Please enter your name: ")
your_age = int(input("Please enter your age: "))
if your_name != None and your_age != None:
    if your_age >= 18:
        print(f"Hey {your_name.capitalize()} you are eligible to vote! ")
    else:
        print(f"Hey {your_name.capitalize()} you are not eligible to vote! ")
###### 7. String Methods
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

