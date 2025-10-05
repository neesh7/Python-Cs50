# Basic class and object demo

## Create a car class with attribute like brand and model. Then create a instance of the class.
## Add a method to class that displays the full name of the car (brand and Model)


# Class - A blueprint for creating objects. It defines attributes and behaviors.
class Car:
    # Constructor
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # Defining a method inside the class
    def full_details(self):
        return self.brand, self.model

# Object - An instance of a class, neesh_car is an object{Instance of class car} of class car
neesh_car = Car("Toyota", "corolla")
print(neesh_car.brand)
print(neesh_car.full_details())

# Inheritance demo - Allows one class to inherit attributes and methods from another.
## create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.


# ElectricCar is new class we are making which will inherit basic structure from Car class.
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model) # we are accessing constructor from Car class so we have access to those attributes as well
        self.battery_size = battery_size # this is specific property to this class


Tesla = ElectricCar("Tesla", "Model-S", "70 Kwh")
print(Tesla.full_details())
print(f"{Tesla.brand} {Tesla.model} has {Tesla.battery_size} battery")


# Encapsulation Demo - Restrict access to internal variables using naming conventions.
## Modify the Car class to encapsualte the brand attribute, make it private , and a getter method for it.

# to explain the concept of private attribute i am going to use other example
class Student:
    def __init__(self, name, school, age, examResult):
        self.name = name
        self.school = school
        self.__age = age  # private attribute ( use double underscore to make it private)
        self.__examResult = examResult

    # We can access the private attribute inside class using __underscore but to outsiders we design getter method to provide access.
    # get_examResult - A basic getter method
    def get_examResult(self):
        return self.__examResult
    
    @property # Using @property and @<property>.setter are Pythonic tools that make your class interfaces cleaner, more intuitive, and more encapsulated
    def age(self):
        return self.__age

    @age.setter #@<property>.setter, No need of parantheses when calling a getter or method with @property decorator
    def age(self, new_age):
        if new_age > 0:
            self.__age = new_age

# Usage
maya = Student("Maya", "D.A.V", 19, "Passed")
# so at the moment we know name and school of Maya can be accessed directly
# but to access the age we need to call the getter method
print(f"{maya.name} studies at {maya.school} and is {maya.age} years old and she is {maya.get_examResult()} in exam")

# maya.age # calls the getter
maya.age = 22 # calls the setter
print(f"{maya.name} studies at {maya.school} and is {maya.age} years old and she is {maya.get_examResult()} in exam")

# Polymorphism - many forms

## Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviours.

# Parent class - Animal
class Animal():
    def __init__(self, name):
        self.name = name

# child class - Dog
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def speak(self):
        return "woof"

# child class - Cat
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "Meow"


dog = Dog("bruno")
cat = Cat("betty")

# Now we have 2 instances of differnt classes with same methods called speak but with different behaviour.
print(dog.speak())
print(cat.speak())

