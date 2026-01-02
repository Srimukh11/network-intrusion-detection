import streamlit as st
import pickle
import numpy as np

# Load trained model and scaler
model = pickle.load(open("rf_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.set_page_config(page_title="Network Intrusion Detection System")

st.title("🔐 Network Intrusion Detection System")
st.write("Detect whether the given network traffic is **Normal** or an **Attack**.")

st.divider()

# ---- INPUT FIELDS ----
duration = st.number_input("Duration", min_value=0)
src_bytes = st.number_input("Source Bytes", min_value=0)
dst_bytes = st.number_input("Destination Bytes", min_value=0)
num_failed_logins = st.number_input("Failed Login Attempts", min_value=0)
num_compromised = st.number_input("Compromised Conditions", min_value=0)
count = st.number_input("Connections (last 2 seconds)", min_value=0)
srv_count = st.number_input("Same Service Connections", min_value=0)

if st.button("🚨 Detect Intrusion"):
    input_data = np.array([[duration, src_bytes, dst_bytes,
                            num_failed_logins, num_compromised,
                            count, srv_count]])

    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)

    if prediction[0] == "attack":
        st.error("⚠️ Intrusion Detected!")
    else:
        st.success("✅ Normal Network Traffic")
