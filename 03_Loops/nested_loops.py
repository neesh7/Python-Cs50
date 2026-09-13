# def main():
#     print_column(3)

# printing vertical of column
# def print_column(height):
#     for _ in range(height):
#         print("#")

# main()

# def main():
#     print_row(3)

# # printig horizontal row of ?
# def print_row(height):
#     print("?"*height)

# main()

# printing star patterns

def main():
    print_star(3)

# def print_star(height):
#     for i in range(height):
#         print("*"*height)
def print_star(height):
    for i in range(height):# this is outer loop refered to rows
        for j in range(height):# this is inner loop refered to columns
            print("#",end="")   # end="" is used to avoid new line after each print
        print()

main()