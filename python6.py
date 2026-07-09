

import pandas as pd

# Step 1: Create a sample dataset
data = {
    'Name': ['Amit', 'Bharti', 'Kiran', 'Ravi'],
    'Marks': [85, 92, 78, 88],
    'Subject': ['Math', 'Science', 'English', 'Math']
}

df = pd.DataFrame(data)

# Step 2: Display the dataset
print("Dataset:\n", df)

# Step 3: Calculate average marks
average_marks = df['Marks'].mean()
print("\nAverage Marks:", average_marks)

# Step 4: Filter students scoring above 85
top_students = df[df['Marks'] > 85]
print("\nTop Students:\n", top_students)

# Step 5: Group by subject and find average
subject_avg = df.groupby('Subject')['Marks'].mean()
print("\nAverage Marks by Subject:\n", subject_avg)
