
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (example: CSV file)
data = pd.read_csv("your_dataset.csv")

# Quick overview
print("Shape of dataset:", data.shape)
print("First 5 rows:\n", data.head())

# Basic statistics
print("\nSummary statistics:\n", data.describe())

# Visualization example
plt.figure(figsize=(8,6))
sns.histplot(data['column_name'], kde=True)
plt.title("Distribution of column_name")
plt.show()
