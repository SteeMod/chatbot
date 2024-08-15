import streamlit as st
import openai
import os

# Check for API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("API key not found. Please set the OPENAI_API_KEY environment variable.")
    st.stop()

openai.api_key = api_key

# Check if the user is logged in
if not st.session_state.get("password_correct"):
    st.write("Please login first.")
    st.stop()

# Set page configuration
st.set_page_config(layout="wide")

# Header
st.title("myfitnessagent")

# Initialize session state
if "event_response" not in st.session_state:
    st.session_state.event_response = ""

# Set up the main app page
st.subheader("Welcome to myfitnessagent - let me help you find your next local athletic event!")
st.write("For example, I can help you find a 5k running event in New York City in August")

# Create a form for user input
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
        prompt = f"Find a {event_type} event in {location} in {time_frame}."
        
        with st.spinner(f'Looking for {location} {event_type} in {time_frame}...'):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=150
                )
                st.session_state.event_response = response.choices[0].message['content'].strip()
            except Exception as e:
                st.error(f"An error occurred: {e}")
                st.write(f"Debug info: {str(e)}")

# Display output
st.write(st.session_state.event_response)
