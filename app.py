import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os

# LOAD TRAINED MODEL
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
model = pickle.load(open(model_path, "rb"))

# PAGE SETTINGS
st.set_page_config(page_title="Customer Churn Prediction", layout="centered")
st.title("Customer Churn Prediction")

# USER INPUTS (3 FEATURES ONLY)
tenure = st.number_input(
    "Tenure (months)",
    min_value=0,
    max_value=72,
    step=1
)

monthly = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    step=1.0
)

total = st.number_input(
    "Total Charges",
    min_value=0.0,
    step=1.0
)

# PREDICT BUTTON
if st.button("Predict"):

    data = pd.DataFrame({
        "tenure": [tenure],
        "MonthlyCharges": [monthly],
        "TotalCharges": [total]
    })

    prediction = model.predict(data)[0]

    if prediction == 1:
        st.error("Customer will Churn ❌")
    else:
        st.success("Customer will Stay ✅")


