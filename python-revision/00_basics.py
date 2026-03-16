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
###### 5. Escape Sequences
###### 6. Taking Inputs and Print Method
###### 7. String Methods
