# 1. Write new file
f = open("data.txt", "w")
f.write("Line 1\nLine 2\n")   # नई फाइल में लिखना
f.close()

# 2. Read entire file
f = open("data.txt", "r")
print(f.read())               # पूरा कंटेंट पढ़ना
f.close()

# 3. Append extra content
f = open("data.txt", "a")
f.write("Line 3 appended\n")  # नया कंटेंट जोड़ना
f.close()

# 4. Read line by line
f = open("data.txt", "r")
for line in f:
    print("Line:", line.strip())  # strip() → spaces हटाना
f.close()

# 5. Using 'with' (best practice)
with open("data.txt", "r") as f:
    print("Safe Read:", f.read())  # auto-close

# 6. Read first N characters
with open("data.txt", "r") as f:
    print("First 10 chars:", f.read(10))

# 7. Read single line
with open("data.txt", "r") as f:
    print("First line:", f.readline())

# 8. Read all lines into list
with open("data.txt", "r") as f:
    lines = f.readlines()
    print("List of lines:", lines)

# 9. Binary file handling (image copy)
with open("image.png", "rb") as src:
    with open("copy.png", "wb") as dest:
        dest.write(src.read())   # बाइनरी कॉपी करना

# 10. Exception handling
try:
    with open("nofile.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("फाइल नहीं मिली!")   # Error handle करना
