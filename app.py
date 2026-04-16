import streamlit as st
import joblib
import pandas as pd

# -----------------------
# Load model
# -----------------------
model = joblib.load("final_model.pkl")

st.title("🛡️ Cyber Threat Detection")

# -----------------------
# Debug (see what's inside model)
# -----------------------
st.write("Model keys:", model.keys())

# -----------------------
# Extract model safely
# -----------------------
if "xgb" in model:
    xgb_model = model["xgb"]
elif "model" in model:
    xgb_model = model["model"]
else:
    st.error("❌ No model found inside .pkl file")
    st.stop()

label_map = model.get("label_map", None)

# -----------------------
# ❌ IMPORTANT: NO model["features"] ANYWHERE
# -----------------------

st.warning("⚠️ Using CSV Upload Mode (features not found)")

# -----------------------
# CSV Upload UI (BEST APPROACH)
# -----------------------
uploaded_file = st.file_uploader("Upload CSV file for prediction")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.write("Preview:", df.head())

    try:
        preds = xgb_model.predict(df)

        if label_map:
            preds = [label_map[p] for p in preds]

        st.success("✅ Predictions completed")
        st.write(preds)

    except Exception as e:
        st.error(f"Prediction Error: {e}")