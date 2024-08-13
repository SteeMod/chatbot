import streamlit as st
import requests

st.set_page_config(layout="wide")

# Header
title = "myfitnessagent"

if "event_response" not in st.session_state:
    st.session_state.event_response = ""

# Set up the main app page
st.subheader("Welcome to myfitnessagent - let me help you find your next local athletic event!")
st.write("For example, I can help you find a 5k running event in New York City in August")

with st.form(key='event_form'):
    event_type = st.text_input("Type of event")
    location = st.text_input("Location")
    time_frame = st.text_input("Month")
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    payload = {
        "event_type": event_type,
        "location": location,
        "time_frame": time_frame
    }

    with st.spinner(f'Looking for {location} {event_type} in {time_frame}...'):
        response = requests.post("http://localhost:8000", json=payload).json()  # Ensure this endpoint is correct
        st.session_state.event_response = response.get("response", "No response from server")

# Display output
st.write(st.session_state.event_response)
