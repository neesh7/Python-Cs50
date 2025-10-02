# names = []

# for _ in range(3):
#     names.append(input("What is your name? "))


# # using with we have capability to autoclose the file - write the file content
# with open("name.txt", "a") as file:
#     for te in names:
#         file.write(f"{te}\n")


# reading the file
# with open("name.txt", 'r') as file:
#     lines = file.readlines()

# for lines in lines:
#     print(lines.rstrip()) # stripping /n from last lines

# Best approach to read files specially text
with open("name.txt", 'r') as f:
    for line in f:
        print(line.rstrip())