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
st.title("Glow")

# Initialize session state
if "phase" not in st.session_state:
    st.session_state.phase = 1
if "responses" not in st.session_state:
    st.session_state.responses = {}

# Phase 1: Greeting and Substance Use History
if st.session_state.phase == 1:
    st.subheader("Phase 1: Initial Assessment")
    st.write("Hello, how are you today?")
    mood = st.radio("Mood", ["Positive", "Neutral", "Negative"])
    
    if mood:
        st.write("Let's proceed with some questions to understand your situation better.")
        st.session_state.responses['mood'] = mood
        st.session_state.phase = 2

# Phase 2: Detailed Questions
if st.session_state.phase == 2:
    st.subheader("Phase 2: Detailed Questions")
    questions = [
        "Have you ever used opioids (prescription or non-prescription)?",
        "Have you ever tried to cut down or stop using opioids but couldn’t?",
        "Do you spend a lot of time obtaining, using, or recovering from the effects of opioids?",
        "Have you continued to use opioids despite knowing it causes problems in your life?",
        "Have you experienced withdrawal symptoms when not using opioids?",
        "Do you need to use more opioids to achieve the same effect?",
        "Have you experienced cravings or a strong desire to use opioids?",
        "Has your opioid use affected your work, school, or home responsibilities?",
        "Have you given up or reduced important social, occupational, or recreational activities because of opioid use?",
        "Have you used opioids in situations where it is physically hazardous (e.g., driving)?",
        "Have you been diagnosed with any mental health conditions (e.g., depression, anxiety)?",
        "Do you use other substances (e.g., alcohol, marijuana) along with opioids?",
        "Have you experienced trauma or significant stress in your life?"
    ]
    
    for question in questions:
        response = st.radio(question, ["Yes", "No"])
        if response:
            st.session_state.responses[question] = response
    
    if st.button("Submit"):
        # Process responses to determine if the user has OUD
        prompt = "Based on the following responses, determine if the user has Opioid Use Disorder (OUD):\n"
        for question, answer in st.session_state.responses.items():
            prompt += f"{question}: {answer}\n"
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant designed to determine if the user has Opioid Use Disorder (OUD) based on their responses."},
                    {"role": "user", "content": prompt}
                ],
            )
            diagnosis = response.choices[0].message['content'].strip()
            st.session_state.responses['diagnosis'] = diagnosis
            
            if "OUD" in diagnosis or "not sure" in diagnosis:
                st.session_state.phase = 3
            else:
                st.write("You are healthy. If you have any concerns, please consult a healthcare professional.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.write(f"Debug info: {str(e)}")

# Phase 3: Location and MOUD Programs
if st.session_state.phase == 3:
    st.subheader("Phase 3: Finding MOUD Programs")
    location = st.text_input("Please provide your location (city and state):")
    
    if location:
        st.session_state.responses['location'] = location
        prompt = f"Find MOUD programs, health professionals, and community-based MOUD programs in {location}."
        
        with st.spinner(f'Searching for MOUD programs in {location}...'):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant designed to find MOUD programs, health professionals, and community-based MOUD programs based on the user's location."},
                        {"role": "user", "content": prompt}
                    ],
                )
                st.session_state.responses['MOUD_programs'] = response.choices[0].message['content'].strip()
            except Exception as e:
                st.error(f"An error occurred: {e}")
                st.write(f"Debug info: {str(e)}")
    
    st.write(st.session_state.responses.get('MOUD_programs', ''))

# Follow-up and Support
if st.session_state.phase == 4:
    st.subheader("Follow-up and Support")
    st.write("Have you contacted any of the MOUD programs or health professionals provided?")
    contacted = st.radio("Contacted", ["Yes", "No"])
    
    if contacted == "Yes":
        st.write("Great! Do you need any further assistance or information?")
    else:
        st.write("Would you like additional resources such as support groups, counseling services, and educational materials?")
    
    st.write("We are here to support you in your journey to recovery.")
