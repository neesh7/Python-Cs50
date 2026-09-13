import pathlib


# Get CWD
base_path = f"{pathlib.Path.cwd()}\\File_IO"
print("basepath= ",f"{base_path}")


# Write/append a file
with open("filename.ext", 'a') as file:
    file.write("content")

# Read a file
with open("filename.txt", 'r') as file:
    for line in file:
        print(line)

# Read a file
with open("filename.txt", 'r') as file:
    for line in file:
        print(line)

with open("names.txt") as file:
    for line in sorted(file):
        print(f"Hello {line.rstrip()}")
