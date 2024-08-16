import streamlit as st
import pickle
import numpy as np

# Load the model and encoders
with open('saved_steps.pkl', 'rb') as file:
    data = pickle.load(file)

model = data["model"]["random_forest"]

# Since ChestPainType, RestingECG, and ST_Slope are categorical, let's define their encodings
chest_pain_mapping = {"ATA": 0, "NAP": 1, "ASY": 2, "TA": 3}
resting_ecg_mapping = {"Normal": 0, "ST": 1, "LVH": 2}  # Assuming these values based on ECG data
st_slope_mapping = {"Up": 0, "Flat": 1, "Down": 2}

def predict(features):
    return model.predict(np.array([features]))

def show_predict_page():
    st.title("Heart Disease Prediction")

    st.write("### Please provide the following details for prediction")

    # Input features
    age = st.slider("Age", 18, 100)
    sex = st.selectbox("Sex", ("Male", "Female"))
    sex_encoded = 1 if sex == "Male" else 0
    chest_pain = st.selectbox("Chest Pain Type", ("ATA", "NAP", "ASY", "TA"))
    chest_pain_encoded = chest_pain_mapping[chest_pain]
    resting_bp = st.slider("Resting Blood Pressure", 80, 200)
    cholesterol = st.slider("Cholesterol", 100, 400)
    fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ("Yes", "No"))
    fasting_bs_encoded = 1 if fasting_bs == "Yes" else 0
    resting_ecg = st.selectbox("Resting ECG", ("Normal", "ST", "LVH"))  # ECG type selection
    resting_ecg_encoded = resting_ecg_mapping[resting_ecg]
    max_hr = st.slider("Max Heart Rate Achieved", 60, 220)
    exercise_angina = st.selectbox("Exercise-induced Angina", ("Yes", "No"))
    exercise_angina_encoded = 1 if exercise_angina == "Yes" else 0
    oldpeak = st.slider("Oldpeak", 0.0, 6.0, step=0.1)
    st_slope = st.selectbox("ST Slope", ("Up", "Flat", "Down"))
    st_slope_encoded = st_slope_mapping[st_slope]

    # Make the prediction
    if st.button("Predict"):
        features = [age, sex_encoded, chest_pain_encoded, resting_bp, cholesterol, fasting_bs_encoded,
                    resting_ecg_encoded, max_hr, exercise_angina_encoded, oldpeak, st_slope_encoded]
        prediction = predict(features)
        st.write(f"Predicted class (1 = Heart Disease, 0 = No Heart Disease): {prediction[0]}")
