# class variable demo
## Add a class variable to Car that keeps track of numbers of cars created

class Student():
    Total_students = 0

    # constructor
    def __init__(self, name, grade, age):
        self.__name = name
        self.grade = grade
        self.__age = age
        Student.Total_students += 1 # class variable to keep track of number of times class is called
    
    def get_age(self):
        return self.__age
    
    @property # using property decorator we made sure that this variable can't be modified and in case we want to modify we need to define setter
    def get_name(self):
        return self.__name
    
    @staticmethod # Definig static method - basically these are methods which are independent of instances/object of classes
    def school_name():
        return "These students belong to DPS"
    

# Creating objects of class - instances
studen1 = Student("Harry", "6", "22")
studen2 = Student("Zack", "6", "21")
studen3 = Student("Ron", "6", "23")

# to get the total number of student directly call the class variable.
print(Student.Total_students)

# Notel Sometime immediate grabage collection doesn't happens in python and it takes time

# Static Method - 
# A static method is a method that belongs to a class but doesn’t need access to the instance (self) or class (cls).
# It’s used when the logic of the method is related to the class, but doesn’t depend on instance-specific data.

print(Student.school_name())
print(studen1.school_name())

# Property Decorators
## Use a property decorator in the student class to make the name attribute read-only
# studen1.name = "David"
print(studen1.get_name)

# Class Inheritance and isinstance() Function
## Demonstrate the use of isinstance() and check if studen1 is an instance of Student class.

print(isinstance(studen1, Student))

# Multiple Inheritance
## create two classes battery and engine, and let the electriccar class inherit from both, demonstrating multiple inheritance.

# Parent class 1
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Hi, I'm {self.name}."

# Parent class 2
class Learner:
    def study(self):
        return "I'm studying hard!"

# Child class with multiple inheritance
class Student(Person, Learner):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school

    def school_info(self):
        return f"I study at {self.school}."


maya = Student("Maya", "D.A.V")
print(maya.introduce())     # From Person
print(maya.study())         # From Learner
print(maya.school_info())   # From Student
