import os

# 1. Create & Write to a file
with open("demo.txt", "w") as f:
    f.write("Hello, this is the first line.\n")
    f.write("Second line of text.\n")

# 2. Read entire file
with open("demo.txt", "r") as f:
    print("Full content:\n", f.read())

# 3. Read file line by line into a list
with open("demo.txt", "r") as f:
    lines = f.readlines()
    print("Lines as list:", lines)

# 4. Append new content
with open("demo.txt", "a") as f:
    f.write("Appended line.\n")

# 5. Find longest word in file
with open("demo.txt", "r") as f:
    words = f.read().split()
    longest = max(words, key=len)
    print("Longest word:", longest)

# 6. Rename file
os.rename("demo.txt", "renamed_demo.txt")
print("File renamed to renamed_demo.txt")

# 7. Delete file
os.remove("renamed_demo.txt")
print("File deleted successfully")
