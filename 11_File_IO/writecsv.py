import csv, pathlib


# Get CWD
base_path = f"{pathlib.Path.cwd()}\\File_IO"
print("basepath= ",f"{base_path}")

# Read Files
# with open(f"{base_path}/sample.csv") as file:
#     for lines in file:
#         row = lines.rstrip().split(",")
#         print(f"{row[0]} current age is {row[1]}")
#         # print(lines,end='')


# sorting existing csv using dictionary
students = []
# Read Files
with open(f"{base_path}/sample.csv") as file:
    for lines in file:
        name, age = lines.rstrip().split(",")
        student = {"name": name, "age": age}
        students.append(student)

# def get_name(student):
#     return student['name']

# def get_age(student):
#     return student['age']


# a short-term function - lambda function
# for student in sorted(students, key=get_name):
# for student in sorted(students, key=get_name, reverse=True):
# for student in sorted(students, key=get_age):
for student in sorted(students, key= lambda student: student['name']): # here sorted function calling get_age by default
    print(f"{student['name']} is in {student['age']}")