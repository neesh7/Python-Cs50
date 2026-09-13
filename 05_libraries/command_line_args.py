import sys


# try:
#     print(f"Hello {name}")
# except IndexError:
#     print("Too few arguments")

# checking for errors
if len(sys.argv) < 2:
    sys.exit("Too few args")
# elif len(sys.argv)> 2:
#     sys.exit("Too many args")


# name = sys.argv[1]

for arg in sys.argv[1:]:
    print(f"Hello {arg}")
    