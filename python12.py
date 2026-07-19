
name = "Bharti"
age = 21
pi = 3.14159
is_student = True

print(f"Name: {name}, Age: {age}, Student: {is_student}")

# 2. Lists, Tuples, Sets, Dicts
my_list = [1, 2, 3, 4]
my_tuple = (10, 20, 30)
my_set = {1, 2, 2, 3}  # duplicates auto-removed
my_dict = {"Python": "Easy", "AI": "Future"}

print(my_list, my_tuple, my_set, my_dict)

# 3. Loops & Conditions
for i in range(1, 6):
    if i % 2 == 0:
        print(f"{i} is Even")
    else:
        print(f"{i} is Odd")

# 4. Functions
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

print("Factorial of 5:", factorial(5))

# 5. Classes & OOP
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
    
    def show(self):
        print(f"Student: {self.name}, Roll: {self.roll}")

s1 = Student("Bharti", 123)
s1.show()

# 6. File Handling
with open("sample.txt", "w") as f:
    f.write("Hello, Python World!\n")

with open("sample.txt", "r") as f:
    print("File Content:", f.read())

# 7. Exception Handling
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero!")

# 8. Libraries (Math, Random, NumPy, Pandas)
import math, random
import numpy as np
import pandas as pd

print("Square root of 16:", math.sqrt(16))
print("Random number:", random.randint(1, 100))

arr = np.array([1, 2, 3, 4])
print("NumPy Array:", arr)

df = pd.DataFrame({"Name": ["A", "B"], "Marks": [90, 85]})
print("Pandas DataFrame:\n", df)

# 9. Simple AI/ML Example (Linear Regression)
from sklearn.linear_model import LinearRegression

X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])

model = LinearRegression()
model.fit(X, y)

print("Prediction for 5:", model.predict([[5]])[0])
