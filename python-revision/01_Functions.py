########### Basics of functions

def hello(name, times=5):
    """This function takes name and no of times as input and prints Hellow world number of times provided.
    
    Keyword arguments:
    argument -- description
    Return: None
    """
    local_variable = 2
    print(weeks)
    print(f"Hello World from {name}\n"*times)

weeks = "7days" # hierarchy matters isliye define this variable before you call the functions
hello("neesh",5)
# print(local_variable) # not reachable here as it is local to hello function not whole code

############ Parameter and Arguments

def say_no(to, reason, greetings="Thank you!"):
    print(f"it is a No from {to} because you are {reason}, {greetings}")

# keyword arg - passing args by name, here order or index doesn't matters
say_no(reason="not eligible", to="BANK")
# postional arg -  here index or orders matters
say_no("BANK","not eligible")
# default arg
say_no("BANK","not eligible") # greeting is default arg which can be overrided like below
say_no("BANK","not eligible","sorry")

# Note: Key points confirmed: Keyword args ignore order, positional match by index, and defaults kick in when omitted or overridden

######### *args and*kwargs ( Arbitrary positional and arbitrary keywords)
# *args (Arbitrary Positional)
# Collects extra positional args into a tuple. Use * before a param name.
def sum_all(*num):
    print(f"The sum of provided inputs (args: {num}) is {sum(num)}")

sum_all(1,2,3,4,5)
# **kwargs (Arbitrary Keyword)
# Collects extra keyword args into a dict. Use ** before a param name.

def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Neesh", age=30, city="Patna")
# name: Neesh
# age: 30
# city: Patna

print_info(role="Trader", experience=5)
# Unnamed keyword args become dict keys/values.

# Combined Use

def flexible(*args, **kwargs):
    print("Positional args:", args)
    print("Keyword args:", kwargs)

flexible(1, 2, name="test", value=42)
# Positional args: (1, 2)
# Keyword args: {'name': 'test', 'value': 42}

# *args first, then **kwargs. Positional can't follow keywords in calls.

# Rules
# *args/**kwargs must be last in param list.

# Can't have two *args or **kwargs.

# Unpack with *list or **dict in calls.

