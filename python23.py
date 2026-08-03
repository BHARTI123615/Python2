# 🚀 Python File Handling – All in One

import csv
import json

# 1️⃣ Create & Write to a File
try:
    with open("demo.txt", "w") as f:
        f.write("Hello, this is a new file.\n")
        f.write("Second line of text.\n")
    print("File created and written successfully.")
except Exception as e:
    print("Error while writing:", e)

# 2️⃣ Read File Content
try:
    with open("demo.txt", "r") as f:
        content = f.read()
    print("\nReading file content:\n", content)
except Exception as e:
    print("Error while reading:", e)

# 3️⃣ Append to File
try:
    with open("demo.txt", "a") as f:
        f.write("Appended line.\n")
    print("\nLine appended successfully.")
except Exception as e:
    print("Error while appending:", e)

# 4️⃣ Read Line by Line
try:
    with open("demo.txt", "r") as f:
        print("\nReading line by line:")
        for line in f:
            print(line.strip())
except Exception as e:
    print("Error while line reading:", e)

# 5️⃣ CSV File Handling
try:
    # Writing CSV
    with open("data.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age"])
        writer.writerow(["Bharti", 21])
        writer.writerow(["John", 25])
    print("\nCSV file written successfully.")

    # Reading CSV
    with open("data.csv", "r") as f:
        reader = csv.reader(f)
        print("\nReading CSV file:")
        for row in reader:
            print(row)
except Exception as e:
    print("Error with CSV:", e)

# 6️⃣ JSON File Handling
try:
    # Writing JSON
    data = {"Name": "Bharti", "Age": 21, "Skills": ["Python", "SQL", "ML"]}
    with open("data.json", "w") as f:
        json.dump(data, f)
    print("\nJSON file written successfully.")

    # Reading JSON
    with open("data.json", "r") as f:
        loaded = json.load(f)
    print("\nReading JSON file:\n", loaded)
except Exception as e:
    print("Error with JSON:", e)

# 7️⃣ Exception Handling Example
try:
    with open("nofile.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("\n⚠️ File not found error handled gracefully.")
