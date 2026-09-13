## Decorators

A decorator is a function that wraps another function to modify its behavior without changing its code. Think of it as a middleware layer — clean, reusable, and powerful.

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Neesh")
```