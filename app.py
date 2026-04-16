
import streamlit as st
import joblib
import pandas as pd
model = joblib.load("final_model.pkl")
st.title("Cyber Threat Detection")
inputs = {}
for feature in model["features"]:
    inputs[feature] = st.number_input(feature, value=0.0)
    if st.button("Predict"):
        df = pd.DataFrame([inputs])
        p2 = model["xgb"].predict_proba(df)
        w2 = model["weights"]
        proba = w2*p2
pred = proba.argmax()
st.success(f"Prediction: {model['label_map'][pred]}")