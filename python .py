import re
import pandas as pd

# -------------------------------
# OOPS Concept: Class for Data Handling
# -------------------------------
class DataHandler:
    def __init__(self, filename):
        self.filename = filename
    
    # File Handling: Write data to file
    def write_data(self, data):
        try:
            with open(self.filename, 'w') as f:
                f.write(data)
            print("✅ Data written successfully")
        except Exception as e:
            print("⚠️ Error while writing:", e)

    # File Handling: Read data from file
    def read_data(self):
        try:
            with open(self.filename, 'r') as f:
                content = f.read()
            print("📂 File content loaded")
            return content
        except FileNotFoundError:
            print("⚠️ File not found")
            return None
        except Exception as e:
            print("⚠️ Error while reading:", e)
            return None

    # Regular Expression: Extract numbers from text
    def extract_numbers(self, text):
        # Hindi Comment: Regex se sirf numbers nikalna
        numbers = re.findall(r'\d+', text)
        return [int(num) for num in numbers]

    # Data Science Example: Convert extracted numbers to DataFrame
    def to_dataframe(self, numbers):
        try:
            df = pd.DataFrame(numbers, columns=['Numbers'])
            print("📊 Data converted to DataFrame")
            return df
        except Exception as e:
            print("⚠️ Error in DataFrame conversion:", e)
            return None


# -------------------------------
# Main Execution
# -------------------------------
if __name__ == "__main__":
    handler = DataHandler("sample.txt")

    # Step 1: Write data to file
    handler.write_data("Data Science 101: Values = 45, 67, 89, 120")

    # Step 2: Read data from file
    content = handler.read_data()

    if content:
        # Step 3: Extract numbers using Regex
        nums = handler.extract_numbers(content)
        print("🔢 Extracted Numbers:", nums)

        # Step 4: Convert to DataFrame
        df = handler.to_dataframe(nums)
        print(df)

        # Step 5: Exception Handling Example
        try:
            mean_val = df['Numbers'].mean()
            print("📈 Mean Value:", mean_val)
        except Exception as e:
            print("⚠️ Error in calculation:", e)
