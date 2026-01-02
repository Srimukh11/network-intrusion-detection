import streamlit as st
import pickle
import numpy as np

# Load model & scaler
model = pickle.load(open("rf_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.set_page_config(page_title="Network Intrusion Detection System")

st.title("🔐 AI-Based Network Intrusion Detection System")
st.markdown("Detect whether network traffic is **Normal** or an **Attack** using ML.")

st.divider()

# ---- INPUT FEATURES ----
duration = st.number_input("Duration", min_value=0)
src_bytes = st.number_input("Source Bytes", min_value=0)
dst_bytes = st.number_input("Destination Bytes", min_value=0)
num_failed_logins = st.number_input("Failed Logins", min_value=0)
num_compromised = st.number_input("Compromised Conditions", min_value=0)
count = st.number_input("Connections (last 2 sec)", min_value=0)
srv_count = st.number_input("Same Service Connections", min_value=0)

# Order must match training feature order
input_data = np.array([[duration, src_bytes, dst_bytes,
                        num_failed_logins, num_compromised,
                        count, srv_count]])

if st.button("🚨 Detect Intrusion"):
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)

    if prediction[0] == "attack":
        st.error("⚠️ Intrusion Detected!")
    else:
        st.success("✅ Normal Network Traffic")
