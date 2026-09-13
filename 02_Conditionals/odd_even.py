x =  int(input("Enter a number: "))

# if x % 2 == 0:
#     print(f"{x} is even")
# else:
#     print(f"{x} is odd")

# more modular approach

def main(num):
    if is_even(num):
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

def is_even(num):
    # return True if num % 2 == 0 else False # more pythonic way
    return num % 2 == 0 # much more optimized way

main(x)