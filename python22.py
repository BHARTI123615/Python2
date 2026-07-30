# 📂 File Handling in Python - All in One

# 1. Write to a file
f = open("example.txt", "w")   # 'w' mode → नया लिखना (overwrite)
f.write("Hello, this is Bharti!\n")  # कंटेंट लिखना
f.close()

# 2. Read entire file
f = open("example.txt", "r")   # 'r' mode → पढ़ना
content = f.read()             # पूरा कंटेंट पढ़ना
print("File Content:", content)
f.close()

# 3. Append to a file
f = open("example.txt", "a")   # 'a' mode → जोड़ना
f.write("Adding more lines...\n")  # नया कंटेंट जोड़ना
f.close()

# 4. Read line by line
f = open("example.txt", "r")
for line in f:
    print("Line:", line.strip())   # strip() → extra spaces हटाना
f.close()

# 5. Using 'with' (Best Practice)
with open("example.txt", "r") as f:
    print("Using with:", f.read())  # 'with' auto close करता है

# 6. Write multiple lines at once
lines = ["First line\n", "Second line\n", "Third line\n"]
with open("example.txt", "w") as f:
    f.writelines(lines)  # कई लाइन्स एक साथ लिखना

# 7. Read file into list
with open("example.txt", "r") as f:
    data = f.readlines()  # हर लाइन list में
    print("List of lines:", data)

# 8. Exception Handling (Safe File Access)
try:
    with open("example.txt", "r") as f:
        print("Safe Read:", f.read())
except FileNotFoundError:
    print("⚠️ File नहीं मिला!")
