# classes - this is more like a blueprint to create our own data type or objects
class Student:
    ...
    

def main():
    student = get_student()
    print(f'{student.name} belongs to {student.house}')

def get_student()   :
    student = Student() # creating object of class student basically we are creating student object from Student class mold
    
    # name and house is attribute/instance variables inside an object called student whose type is Student(class)
    student.name = input("Name: ")
    student.house = input("House: ")
    return student


if __name__=="__main__":
    main()