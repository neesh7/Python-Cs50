import csv
import pathlib


# Get CWD
base_path = f"{pathlib.Path.cwd()}\\File_IO"
print("basepath= ",f"{base_path}")


students = []
# using csv reader below
# with open(f"{base_path}/sample.csv") as file:
#     reader = csv.reader(file)
#     for name, home in reader:
#         students.append({"name": name, "home": home})


# csv Dictreader
with open(f"{base_path}/sample.csv") as file:
    reader = csv.DictReader(file)
    # if your csv includes header then this can be used
    for row in reader:
        students.append({"name": row["Name"], "Age": row["Age"]})

for student in sorted(students, key= lambda students : students["name"]):
    print(f"{student['name']} is from {student['Age']}")