
# 1. Class and Object
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    
    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}")

# 2. Inheritance
class GraduateStudent(Student):
    def __init__(self, name, roll_no, degree):
        super().__init__(name, roll_no)
        self.degree = degree
    
    def display(self):
        # Method Overriding (Polymorphism)
        print(f"Graduate Student: {self.name}, Roll No: {self.roll_no}, Degree: {self.degree}")

# 3. Encapsulation
class BankAccount:
    def __init__(self, owner, balance=0):
        self.__balance = balance   # private attribute
        self.owner = owner
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance!")
    
    def get_balance(self):
        return self.__balance

# 4. Abstraction (using abc module)
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

# 5. Polymorphism Example
def print_area(shape):
    print(f"Area: {shape.area()}")


# Object Creation
s1 = Student("Bharti", 101)
s1.display()

s2 = GraduateStudent("Karan", 102, "M.Tech")
s2.display()

# Encapsulation
acc = BankAccount("Bharti", 5000)
acc.deposit(2000)
acc.withdraw(1000)
print(f"Balance: {acc.get_balance()}")

# Abstraction + Polymorphism
rect = Rectangle(10, 5)
print_area(rect)
print(f"Perimeter: {rect.perimeter()}")
