
import numpy as np
from sklearn.linear_model import LinearRegression

# Training Data
experience = np.array([1, 2, 3, 4, 5, 6, 7]).reshape(-1, 1)
salary = np.array([30000, 40000, 50000, 60000, 70000, 80000, 90000])

# Create Model
model = LinearRegression()

# Train Model
model.fit(experience, salary)

# Predict Salary
years = np.array([[8]])
predicted_salary = model.predict(years)

print(f"Predicted Salary for 8 years experience: ₹{predicted_salary[0]:,.2f}")

# Model Information
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
print("Accuracy (R² Score):", model.score(experience, salary))
