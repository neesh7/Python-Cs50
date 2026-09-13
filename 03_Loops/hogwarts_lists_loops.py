students = ["Hermione", "Harry", "Ron"]

print(students) # prints ['Hermione', 'Harry', 'Ron']
print(students[0]) # prints Hermione
print(students[1]) # prints Harry
print(students[2]) # prints Ron


# for student in students:
#     print(f"{student} is a student at Hogwarts")

for i in range(len(students)):
    print(i+1,f"{students[i]} is a student at Hogwarts",sep=".")