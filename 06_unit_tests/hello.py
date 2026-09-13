def main():
    name = input("What's your name ? ")
    return hello(name)


def hello(to = "world"):
    # print("hello",to)
    return f"hello {to}"


if __name__ == "__main__":
    print(main())