def main():
    num = take_input('Enter a number: ')
    print(f"x is {num}")


# def take_input():
#     # taking right input
#     while True:
#         try:
#             x = int(input('Enter a number: '))
#         except ValueError:
#             print("Please enter right value !")
#         else:
#             # break
#             return x
def take_input(prompt):
    # taking right input
    while True:
        try:
            x = int(input(prompt))
            return x
        except ValueError:
            print("Please enter right value !")

main()