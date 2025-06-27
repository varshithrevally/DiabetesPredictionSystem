import streamlit as st # type: ignore
from predictor import predict_diabetes

st.title("🩺 Diabetes Prediction System")

fields = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"]
user_input = []

for field in fields:
    val = st.number_input(field, min_value=0.0)
    user_input.append(val)

if st.button("Predict"):
    prediction = predict_diabetes(user_input)
    if prediction == 1:
        st.error("🚨 The person is likely to be **Diabetic**.")
    else:
        st.success("✅ The person is **Non-diabetic**.")
