
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
# 1. NumPy Array
arr = np.array([10, 20, 30, 40, 50])
print("Mean:", np.mean(arr), "Std Dev:", np.std(arr))
# 2. Pandas DataFrame
data = {"Name": ["A", "B", "C"], "Marks": [85, 90, 78]}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)
# 3. Matplotlib Visualization
plt.bar(df["Name"], df["Marks"], color="skyblue")
plt.title("Marks of Students")
plt.show()
# 4. Simple ML (Linear Regression)
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])
model = LinearRegression().fit(X, y)
print("\nPrediction for 6:", model.predict([[6]])[0])
