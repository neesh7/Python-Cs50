def main(num):
    return square_no(num)


def square_no(num):
    return num**2

if __name__=="__main__":
    # This is called the main gaurd, it runs the code only it is ran directly and if imported as a module it won't run and avoid uneccessary execution
    # during imports
    print(main(2))