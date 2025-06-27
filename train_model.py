import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import joblib
import os

# Load Dataset
df = pd.read_csv('diabetes.csv')

X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train
model = LogisticRegression()
model.fit(X_scaled, y)

# Save model files
os.makedirs('model', exist_ok=True)
joblib.dump(model, 'model/logistic_regression_model.joblib')
joblib.dump(scaler, 'model/scaler.joblib')
joblib.dump(X.columns.tolist(), 'model/column_names.joblib')

print("✅ Model, scaler, and column names saved.")
