from abc import ABC, abstractmethod

# -------------------------------
# 1. Class & Objects
# -------------------------------
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    
    def display_info(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}")

# -------------------------------
# 2. Inheritance
# -------------------------------
class GraduateStudent(Student):
    def __init__(self, name, roll_no, specialization):
        super().__init__(name, roll_no)
        self.specialization = specialization
    
    def display_info(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, Specialization: {self.specialization}")

# -------------------------------
# 3. Encapsulation
# -------------------------------
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance   # private attribute
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds!")
    
    def get_balance(self):
        return self.__balance

# -------------------------------
# 4. Abstraction
# -------------------------------
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

# -------------------------------
# 5. Polymorphism
# -------------------------------
def print_area(shape):
    print("Area:", shape.area())

-
# Class & Object
s1 = Student("Bharti", 101)
s1.display_info()

# Inheritance
s2 = GraduateStudent("Karan", 102, "Computer Science")
s2.display_info()

# Encapsulation
acc = BankAccount("Bharti", 5000)
acc.deposit(2000)
acc.withdraw(1000)
print("Balance:", acc.get_balance())

# Abstraction + Polymorphism
rect = Rectangle(10, 5)
print_area(rect)
