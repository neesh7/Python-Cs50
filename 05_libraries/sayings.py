def hello(name):
    return "hello " +name

def goodbye(name):
    return "GoodBye " +name

def main(name='world'):
    print(hello(name))
    print(goodbye(name))


if __name__== "__main__":
    main()