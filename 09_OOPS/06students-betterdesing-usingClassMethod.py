class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} is from {self.house}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

def main():
    # if we are using class method we don't even need to initiallize the object we can use classmethod directly
    student = Student.get()
    print(student)


if __name__=="__main__":
    main()