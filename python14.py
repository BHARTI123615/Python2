
# 1. Class & Object
class Student:
    def __init__(self, name, roll):
        self.name = name        # instance variable
        self.roll = roll

    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll}")

# 2. Inheritance
class Marks(Student):   # inherits Student
    def __init__(self, name, roll, marks):
        super().__init__(name, roll)
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll}, Marks: {self.marks}")

# 3. Polymorphism (same method name, different behavior)
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# 4. Encapsulation (private variable)
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

# 5. Abstraction (using abc module)
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r * self.r


# ---------- Testing ----------
print("=== Class & Object ===")
s1 = Student("Bharti", 101)
s1.display()

print("\n=== Inheritance ===")
m1 = Marks("Raj", 102, 85)
m1.display()

print("\n=== Polymorphism ===")
for animal in [Dog(), Cat(), Animal()]:
    animal.speak()

print("\n=== Encapsulation ===")
acc = BankAccount(1000)
acc.deposit(500)
print("Balance:", acc.get_balance())

print("\n=== Abstraction ===")
c = Circle(5)
print("Circle Area:", c.area())
