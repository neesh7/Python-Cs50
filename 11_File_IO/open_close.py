name = input("What is your name ?")
# file = open("names.txt", "w") # writes the files
file = open("names.txt", "a") # appends the files
file.write(f"{name}\n")
# file.writelines(name)
file.close()