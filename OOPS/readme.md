## Object Oriented Programming

OOPs stands for Object-Oriented Programming (OOP) — a paradigm that organizes code around objects and classes, rather than just functions and logic. It’s a powerful way to model real-world entities and behaviors in your programs.

- Basic class and object
- class method and self
- Inheritence
- Encapsulation
- class variables
- static methods
- property decorators
- class inheritance and isintance() function
- Multiple inheritance

# 🐍 Python Object-Oriented Programming (OOP) Concepts

Object-Oriented Programming (OOP) is a paradigm that organizes code around **objects** and **classes**, rather than just functions and logic. It helps model real-world entities and behaviors in a modular, reusable, and scalable way.

---

## 📦 1. Basic Class and Object

```python
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def drive(self):
        print(f"{self.brand} drives at {self.speed} km/h")

my_car = Car("Tesla", 120)
my_car.drive()
```
## 🧠 2. Class Method and self

- self refers to the current instance of the class.

- It allows access to instance variables and methods.
```python
class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I'm {self.name}")
```
## 🧬 3. Inheritance
-  Inheritance allows a class to inherit attributes and methods from another class.

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Woof!")

dog = Dog()
dog.speak()  # Woof!
```
## 🔒 4. Encapsulation
-  Encapsulation restricts access to internal variables using naming conventions.

```python
class BankAccount:
    def __init__(self):
        self.__balance = 0  # private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
```
## 🧮 5. Class Variables
-  Class variables are shared across all instances of a class.

```python
class Counter:
    count = 0  # class variable

    def __init__(self):
        Counter.count += 1

print(Counter.count)  # 0
a = Counter()
b = Counter()
print(Counter.count)  # 2

```
## ⚙️ 6. Static Methods
Static methods don’t access instance or class data. Use @staticmethod

```python
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

print(MathUtils.add(5, 3))  # 8
```
## 🧼 7. Property Decorators
Use @property and @<property>.setter for clean, controlled access.

```python
class Student:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value
```
## 🧬 8. Class Inheritance and isinstance()
isinstance() checks if an object is an instance of a class or its subclass.


```python
class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True

```
## 🧩 9. Multiple Inheritance
A class can inherit from multiple parent classes.


```python
class Person:
    def __init__(self, name):
        self.name = name

class Learner:
    def study(self):
        return "Studying..."

class Student(Person, Learner):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school

maya = Student("Maya", "D.A.V")
print(maya.name)         # Maya
print(maya.study())      # Studying...
```