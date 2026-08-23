# ============================================
# 📊 All-in-One Python Data Science Template
# ============================================

# 1. Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 2. Load Dataset
# Replace 'data.csv' with your file
df = pd.read_csv("data.csv")

# 3. Explore Data
print(df.head())          # First 5 rows
print(df.info())          # Data types
print(df.describe())      # Summary statistics
print(df.isnull().sum())  # Missing values

# 4. Handle Missing Values
df.fillna(df.mean(), inplace=True)

# 5. Encode Categorical Variables
for col in df.select_dtypes(include=['object']).columns:
    df[col] = LabelEncoder().fit_transform(df[col])

# 6. Feature Selection
X = df.drop("target", axis=1)   # Features
y = df["target"]                # Target variable

# 7. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 8. Feature Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 9. Model Training
model = LogisticRegression()
model.fit(X_train, y_train)

# 10. Predictions
y_pred = model.predict(X_test)

# 11. Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# 12. Visualization
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap
