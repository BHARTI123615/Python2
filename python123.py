

# Step 1: Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load dataset (example: CSV file)
df = pd.read_csv("data.csv")

# Step 3: Quick exploration
print(df.head())        # first 5 rows
print(df.info())        # column info
print(df.describe())    # summary stats

# Step 4: Data cleaning
df = df.dropna()        # remove missing values
df['Category'] = df['Category'].astype('category')

# Step 5: Visualization
sns.countplot(x='Category', data=df)
plt.show()

# Step 6: Simple ML model (Logistic Regression)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X = df[['feature1','feature2']]
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
