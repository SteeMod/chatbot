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
    st.write("Please login at the home page the username is multichannel and the password is imfree123")
    st.stop()

# Set page configuration
st.set_page_config(layout="wide")

# Header
st.title("Multi Channel Medication Virtual Assistant")

# Initialize session state
if "phase" not in st.session_state:
    st.session_state.phase = 1
if "responses" not in st.session_state:
    st.session_state.responses = {}

# Phase 1: Location and MOUD Programs
if st.session_state.phase == 1:
    st.subheader("Phase 1: Finding Programs")
    location = st.text_input("Please provide your location (city and state):")
    
    if location:
        st.session_state.responses['location'] = location
        prompt = f"Find MOUD programs and fentanyl programs, health professionals, and community-based OUD programs in {location}."
        
        with st.spinner(f'Searching for MOUD programs in {location}...'):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant designed to find OUD programs, health professionals, and community-based OUD programs based on the user's location."},
                        {"role": "user", "content": prompt}
                    ],
                )
                st.session_state.responses['MOUD_programs'] = response.choices[0].message['content'].strip()
            except Exception as e:
                st.error(f"An error occurred: {e}")
                st.write(f"Debug info: {str(e)}")
    
    st.write(st.session_state.responses.get('MOUD_programs', ''))
