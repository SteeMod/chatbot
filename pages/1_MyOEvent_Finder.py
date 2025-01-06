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
    st.write("Please login at the home page the username is myofree and the password is imfree123")
    st.stop()

# Set page configuration
st.set_page_config(layout="wide")

# Header
st.title("Multi Channel Medication Virtual Assistant")

# Initialize session state
if "event_response" not in st.session_state:
    st.session_state.event_response = ""

# Set up the main app page
st.subheader("Welcome to the Multi Channel Medication Virtual Assistant let me help you find the  latest  Opiod related event ")
st.write("For example, I can help you find a Opiod Use Disorder  (OUD) event in Seattle, in the timeframe of September to December in 2024")

# Create a form for user input
with st.form(key='event_form'):
    event_type = st.text_input("Type of event e.g In person/ virtual")
    location = st.text_input("Location, if virtual put country name.")
    time_frame = st.text_input("Timeframe e.g Jan-Feb, put in year")
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
                        {"role": "system", "content": "You are a helpful assistant specially designed to find  events for that discuss Opiod Use Disorder/ Opiod misuse based on  the user's {location} {event_type}, and {time_frame} after that give them the list based in this order, awareness, treatment and so on, also give the number, and email of the event."},
                        {"role": "user", "content": prompt}
                    ],

                )
                st.session_state.event_response = response.choices[0].message['content'].strip()
            except Exception as e:
                st.error(f"An error occurred: {e}")
                st.write(f"Debug info: {str(e)}")

# Display output
st.write(st.session_state.event_response)
