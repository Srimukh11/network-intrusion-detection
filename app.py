import streamlit as st
import joblib
import numpy as np

st.title("Heart Disease Prediction")

model = joblib.load("rf_model.pkl")

age = st.number_input("Age", 1, 120)
sex = st.selectbox("Sex (1=Male, 0=Female)", [0, 1])
cp = st.number_input("Chest Pain Type (0–3)")
trestbps = st.number_input("Resting Blood Pressure")
chol = st.number_input("Cholesterol")
thalach = st.number_input("Max Heart Rate")

# IMPORTANT: order must match training
features = np.array([[age, sex, cp, trestbps, chol, thalach]])

if st.button("Predict"):
    prediction = model.predict(features)[0]
    st.success(
        "Heart Disease Detected ❤️" if prediction == 1 else "No Heart Disease 💚"
    )
