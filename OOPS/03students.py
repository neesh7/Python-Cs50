# classes - this is more like a blueprint to create our own data type or objects
class Student:
    # Technically Initiallization method - Inititallizes the object
    def __init__(self, name, house, patronus): # dunder or constructor method or instance method
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
        self.patronus = patronus

    # Helps to return the string when object is called directly
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return "Horse"
            case "Otter":
                return "otter"
            case "Jack Russel terrier":
                return "Dog"
            case _:
                return "Magic Wand"

def main():
    student = get_student()
    print(f'{student.name} belongs to {student.house} and have patronus : {student.patronus}')

    # printing the patronus of each student
    print("Expected Patronum!")
    print(student.charm())

def get_student()   :
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")

    student = Student(name, house, patronus) # constructor call / instanciate student object
    # print(student) # it won't print the messege instead it will print the addr of the object.
    print(student) # to make this work we need to define __str__

    return student


if __name__=="__main__":
    main()