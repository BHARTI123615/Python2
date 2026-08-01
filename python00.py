# 🚀 Python All-in-One Demo
# Covers: Variables, Data Types, Control Flow, Loops, Functions, OOP,
# File Handling, Exception Handling, Regex, and Pandas (Data Science)

import re
import pandas as pd

# 1. Variables & Data Types
num = 42
text = "Python is powerful"
my_list = [1, 2, 3]
my_tuple = (4, 5, 6)
my_set = {1, 2, 2, 3}   # duplicates auto-removed
my_dict = {"name": "Bharti", "role": "Student"}

print("Variables:", num, text, my_list, my_tuple, my_set, my_dict)

# 2. Control Flow
if num > 40:
    print("Number is greater than 40")
else:
    print("Number is small")

# 3. Loops
for i in range(3):
    print("Loop iteration:", i)

# 4. Functions
def square(x):
    return x * x

print("Square of 5:", square(5))

# 5. Object-Oriented Programming
class Student:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello, I am {self.name}"

s1 = Student("Bharti")
print(s1.greet())

# 6. File Handling + Exception Handling
try:
    with open("demo.txt", "w") as f:
        f.write("Python file handling demo\n")
    with open("demo.txt", "r") as f:
        content = f.read()
    print("File Content:", content)
except Exception as e:
    print("Error:", e)

# 7. Regex
sentence = "My roll number is 12345 and phone is 9876543210"
numbers = re.findall(r"\d+", sentence)
print("Extracted Numbers:", numbers)

# 8. Pandas (Data Science)
data = {"Name": ["A", "B", "C"], "Score": [85, 90, 95]}
df = pd.DataFrame(data)
print("Pandas DataFrame:\n", df)

# 9. Bonus: List Comprehension + Lambda
squares = list(map(lambda x: x*x, range(1,6)))
print("Squares via lambda:", squares)
