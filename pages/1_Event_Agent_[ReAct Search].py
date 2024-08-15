import streamlit as st
import openai
import os
from openai import InvalidRequestError, AuthenticationError, APIConnectionError, OpenAIError

# Set page configuration
st.set_page_config(layout="wide")

# Initialize the OpenAI client with your API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("API key not found. Please set the OPENAI_API_KEY environment variable.")
    st.stop()

openai.api_key = api_key

# Header
st.title("myfitnessagent")

# Initialize session state
if "event_response" not in st.session_state:
    st.session_state.event_response = ""

# Check if the user is logged in
if not st.session_state.get("password_correct"):
    st.write("Please login first.")
    st.stop()

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
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=prompt,
                    max_tokens=150
                )
                st.session_state.event_response = response.choices[0].text.strip()
            except InvalidRequestError as e:
                st.error(f"Invalid request: {e}")
            except AuthenticationError as e:
                st.error(f"Authentication error: {e}")
            except APIConnectionError as e:
                st.error(f"API connection error: {e}")
            except OpenAIError as e:
                st.error(f"An error occurred: {e}")

# Display output
st.write(st.session_state.event_response)
