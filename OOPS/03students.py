# classes - this is more like a blueprint to create our own data type or objects
class Student:
    # Technically Initiallization method - Inititallizes the object
    def __init__(self, name, house): # dunder or constructor method or instance method
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
    

def main():
    student = get_student()
    print(f'{student.name} belongs to {student.house}')

def get_student()   :
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house) # constructor call / instanciate student object
    return student


if __name__=="__main__":
    main()