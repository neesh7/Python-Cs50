# def main():
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print("x raised to y is ", power_num(x,y))

def main():
    x = int(input("Enter the no: "))
    return square(x)

def power_num(x,y):
    return x**y + y


def square(x):
    return x**2


if __name__ == "__main__":
    main()