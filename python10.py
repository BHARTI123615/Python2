import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load dataset (CSV file)
df = pd.read_csv("data.csv")   # replace with your file path

# 2. Quick overview
print(df.head())        # first 5 rows
print(df.info())        # column info
print(df.describe())    # summary stats

# 3. Data Cleaning
df = df.dropna()        # remove missing values
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())  # fill missing salary

# 4. Feature Engineering
df['Salary_in_Lakhs'] = df['Salary'] / 100000

# 5. Exploratory Data Analysis (EDA)
print(df['Department'].value_counts())   # frequency count

# 6. Visualization
plt.figure(figsize=(6,4))
sns.barplot(x="Department", y="Salary", data=df)
plt.title("Average Salary by Department")
plt.show()

# 7. Simple Statistics
mean_salary = df['Salary'].mean()
max_salary = df['Salary'].max()
print(f"Mean Salary: {mean_salary}, Max Salary: {max_salary}")

# 8. Correlation
print(df.corr())
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.show()
