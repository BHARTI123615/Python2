import os

# --- Create & Write ---
with open("demo.txt", "w") as f:
    f.write("Line 1: Hello World\n")
    f.write("Line 2: Python File Handling\n")
    f.write("Line 3: Practice makes perfect\n")

# --- Read Entire File ---
with open("demo.txt", "r") as f:
    print("Full Content:\n", f.read())

# --- Read Line by Line into List ---
with open("demo.txt", "r") as f:
    lines = f.readlines()
    print("Lines as List:", lines)

# --- Append Content ---
with open("demo.txt", "a") as f:
    f.write("Line 4: Appended text\n")

# --- Find Longest Word ---
with open("demo.txt", "r") as f:
    words = f.read().split()
    longest = max(words, key=len)
    print("Longest Word:", longest)

# --- Rename File ---
os.rename("demo.txt", "renamed_demo.txt")
print("File renamed to renamed_demo.txt")

# --- Delete File ---
os.remove("renamed_demo.txt")
print("File deleted successfully")
