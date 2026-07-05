# Collections in Python

# 1. List (Ordered, Mutable)
fruits = ["Apple", "Banana", "Mango"]
fruits.append("Orange")
print("List:", fruits)

# 2. Tuple (Ordered, Immutable)
colors = ("Red", "Green", "Blue")
print("Tuple:", colors)

# 3. Set (Unordered, Unique Values)
numbers = {10, 20, 30, 20, 10}
numbers.add(40)
print("Set:", numbers)

# 4. Dictionary (Key-Value Pair)
student = {
    "Name": "Bharti",
    "Age": 20,
    "Course": "Data Science"
}
student["Age"] = 21
student["City"] = "Mohali"

print("Dictionary:", student)

# Accessing Elements
print("\nAccessing Data")
print("First Fruit:", fruits[0])
print("First Color:", colors[0])
print("Student Name:", student["Name"])
print("Set Elements:", numbers)
