import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("final_model.pkl")

st.title("Cyber Threat Detection")

inputs = {}

# Create input fields
for feature in model["features"]:
    inputs[feature] = st.number_input(feature, value=0.0)

# Predict button OUTSIDE loop
if st.button("Predict"):
    df = pd.DataFrame([inputs])

    # 🔥 IMPORTANT: Ensure column order matches training
    df = df[model["features"]]

    # Prediction
    p2 = model["xgb"].predict_proba(df)

    # If weights exist (ensemble case)
    if "weights" in model:
        proba = model["weights"] * p2
    else:
        proba = p2

    pred = proba.argmax()

    st.success(f"Prediction: {model['label_map'][pred]}")