class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house


    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name
        
    @property # Getter - gets some value
    def house(self):
        return self._house # if we want to use instance variable in getter, setter without function name colision use _ as indiactor.
    
    @house.setter # Setter - sets some value
    def house(self, house):
        if house not in ["Gryffindor", "hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house

def main():
    student = get_student()
    # student._house = "Ravencla" # Even after this much of gate keeping or security we can override it
    # so basically in python nothing is private everything works on honour system 
    # so if a variable starts with underscore or double underscore it is intended to not to touch it
    print(student)


def get_student()   :
    name = input("Name: ")
    house = input("House: ")

    return Student(name, house)


if __name__=="__main__":
    main()