import streamlit as st
import joblib
import pandas as pd

# -------------------------------
# Load model
# -------------------------------
model = joblib.load("final_model.pkl")

st.title("🛡️ Cyber Threat Detection")

# -------------------------------
# Debug (optional - can remove later)
# -------------------------------
st.write("Model keys:", model.keys())

# -------------------------------
# Safely extract components
# -------------------------------
xgb_model = None
features = None
label_map = None
weights = None

# Try different possible keys
if "xgb" in model:
    xgb_model = model["xgb"]
elif "model" in model:
    xgb_model = model["model"]

features = model.get("features", None)
label_map = model.get("label_map", None)
weights = model.get("weights", None)

# -------------------------------
# CASE 1: Features available → Manual Input UI
# -------------------------------
if features is not None:

    st.subheader("Enter Feature Values")

    inputs = {}
    for feature in features:
        inputs[feature] = st.number_input(feature, value=0.0)

    if st.button("Predict"):
        df = pd.DataFrame([inputs])

        # Ensure correct column order
        df = df[features]

        try:
            proba = xgb_model.predict_proba(df)

            if weights is not None:
                proba = weights * proba

            pred = proba.argmax()

            if label_map:
                result = label_map[pred]
            else:
                result = pred

            st.success(f"Prediction: {result}")

        except Exception as e:
            st.error(f"Prediction Error: {e}")

# -------------------------------
# CASE 2: Features NOT available → CSV Upload UI (BEST)
# -------------------------------
else:
    st.warning("⚠️ Features not found in model. Switch to CSV mode.")

    uploaded_file = st.file_uploader("Upload CSV for Prediction")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        st.write("Preview of uploaded data:", df.head())

        try:
            preds = xgb_model.predict(df)

            if label_map:
                preds = [label_map[p] for p in preds]

            st.success("Predictions completed ✅")
            st.write(preds)

        except Exception as e:
            st.error(f"Prediction Error: {e}")