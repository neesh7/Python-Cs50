students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
    "Luna": "Ravenclaw"

            }
print(students) # prints the whole dictionary
print(students["Hermione"]) # prints Gryffindor
print(students.get("Draco")) # prints Slytherin
print(students.get("Neville")) # prints None

print(students.keys()) # prints all the keys of the dictionary
print(students.values()) # prints all the values of the dictionary
print(students.items()) # prints all the items of the dictionary in the form of tuples

# Looping through a dictionary
for student in students:
    print(f"{student} is in {students[student]}") # prints each student and their house