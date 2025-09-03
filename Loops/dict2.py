# list of dictionaries
students = [
    {   "name": "Hermione", "house": "Gryffindor", "patronus": "Otter"  },
    {   "name": "Harry", "house": "Gryffindor", "patronus": "Stag"  },
    {   "name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"    },
    {   "name": "Draco", "house": "Slytherin", "patronus": None },
    {   "name": "Luna", "house": "Ravenclaw", "patronus": "Hare" }
]
for student in students:
    print(student) # prints each dictionary in the list 
    print(f"{student['name']} is in {student['house']} and their patronus is {student['patronus']}")