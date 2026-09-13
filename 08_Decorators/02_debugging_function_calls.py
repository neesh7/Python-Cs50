# Create a decorator to print the function names and the value of it's arguments every time the function is called.

# Our decorator
def debug(func): # taking functions as a input
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join( f"{key}={value}" for key, value in kwargs.items())
        print(f"calling: {func.__name__} with args {args_value} and kwargs value {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper


@debug
def hello():
    print("Hello !")


@debug
def greet(name, greeting):
    print(f"{greeting}, {name}")

greet("chai",greeting='Hello')