import streamlit as st
import pickle
import numpy as np

# 1. Load the trained model and scaler
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# 2. Set up the web app interface
st.title("Placement Predictor")

iq = st.number_input("Enter IQ of the student", min_value=0.0, max_value=200.0, value=100.0)
cgpa = st.number_input("Enter CGPA of the student", min_value=0.0, max_value=10.0, value=7.0)

# 3. Pure Machine Learning Prediction Logic
if st.button("Predict"):
    # Pass inputs matching your exact training dataframe column order: [[cgpa, iq]]
    raw_features = np.array([[cgpa, iq]])
    
    # Scale the inputs using your exact notebook scaling parameters
    scaled_features = scaler.transform(raw_features)
    
    # Let the model calculate the prediction
    prediction = model.predict(scaled_features)
    
    if prediction[0] == 1:
        st.success("Placement Ho Jaayega 🎉")
    else:
        st.error("Placement Nahi Hoga 😢")