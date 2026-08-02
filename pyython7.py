# -------------------------------
# Python All-in-One Revision Code
# -------------------------------

# ✅ Basics: variables, loops, functions
x = 10
y = 20
print("Sum:", x + y)

def greet(name):
    return f"Hello, {name}!"
print(greet("Bharti"))

# ✅ Exception Handling
try:
    result = x / 0
except ZeroDivisionError as e:
    print("Error:", e)
finally:
    print("Exception handling demo done.")

# ✅ File Handling
with open("demo.txt", "w") as f:
    f.write("Python File Handling Example\n")
with open("demo.txt", "r") as f:
    print("File Content:", f.read())

# ✅ Regular Expressions
import re
text = "My email is test123@example.com"
pattern = r"[a-zA-Z0-9]+@[a-z]+\.[a-z]+"
match = re.search(pattern, text)
if match:
    print("Regex Found:", match.group())

# ✅ Compression
import zlib
data = b"Python compression example! Python compression example!"
compressed = zlib.compress(data)
decompressed = zlib.decompress(compressed)
print("Compressed Size:", len(compressed), "Decompressed:", decompressed.decode())

# ✅ Data Structures
# List
nums = [1, 2, 3, 4]
nums.append(5)
print("List:", nums)

# Tuple
tup = (10, 20, 30)
print("Tuple:", tup)

# Set
unique = {1, 2, 2, 3}
print("Set:", unique)

# Dictionary
student = {"name": "Bharti", "course": "CSE"}
student["year"] = 3
print("Dictionary:", student)

# ✅ End of Script
print("All concepts covered in one code!")
