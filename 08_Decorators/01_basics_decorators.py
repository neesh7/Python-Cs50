import time


# Time function execution

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} function ran in {end-start} time")
        return result
    return wrapper

@timer # we are using timer as toll gate whenever example gets called it will pass through time for sure.
def example(n):
    time.sleep(n)

example(2)