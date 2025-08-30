def main():
    name = input("What's your name? ")  # using input function without assignment operator
    hello(name)
    hello()  # here no argument is passed so default value will be used


def hello(to="world"):  # here to is parameter with default value world
    print(f"Hello, {to}!")

def square(n):
    # return n **n
    return pow(n,2)



main()
print(square(3))