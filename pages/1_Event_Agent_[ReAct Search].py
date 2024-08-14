import streamlit as st
from openai import OpenAI
import requests
import os

# Initialize the OpenAI client with your API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("API key not found. Please set the OPENAI_API_KEY environment variable.")
    st.stop()

client = OpenAI(api_key=api_key)

st.set_page_config(layout="wide")

# Header
st.title("myfitnessagent")

if "event_response" not in st.session_state:
    st.session_state.event_response = ""

col1, col2 = st.columns([1, 10])

if not st.session_state.get("password_correct"):
    st.write("Please login first.")
    st.stop()

# Set up the main app page
st.subheader("Welcome to myfitnessagent - let me help you find your next local athletic event!")
st.write("For example, I can help you find a 5k running event in New York City in August")

with st.form(key='event_form'):
    event_type = st.text_input("Type of event")
    location = st.text_input("Location")
    time_frame = st.text_input("Month")
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    # Validate inputs
    if not event_type or not location or not time_frame:
        st.error("Please fill in all fields.")
    else:
        payload = {
            "event_type": event_type,
            "location": location,
            "time_frame": time_frame
        }
        
        with st.spinner(f'Looking for {location} {event_type} in {time_frame}...'):
            try:
                response = requests.post("https://localhost:8507", json=payload)
                response.raise_for_status()  # Check for HTTP errors
                st.session_state.event_response = response.json().get("response", "No response found.")
            except requests.exceptions.RequestException as e:
                st.error(f"An error occurred: {e}")
    
# Display output
st.write(st.session_state.event_response)
