# Import essential libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (example: CSV file)
df = pd.read_csv("data.csv")

# Quick overview
print("Shape of dataset:", df.shape)
print("\nFirst 5 rows:\n", df.head())
print("\nData types:\n", df.dtypes)

# Check for missing values
print("\nMissing values:\n", df.isnull().sum())

# Basic statistics
print("\nSummary statistics:\n", df.describe())

# Data cleaning example: fill missing values
df['column_name'] = df['column_name'].fillna(df['column_name'].mean())

# Visualization examples
plt.figure(figsize=(6,4))
sns.countplot(x='category_column', data=df)
plt.title("Category Distribution")
plt.show()

plt.figure(figsize=(6,4))
sns.histplot(df['numeric_column'], bins=20, kde=True)
plt.title("Numeric Column Distribution")
plt.show()

# Correlation heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
