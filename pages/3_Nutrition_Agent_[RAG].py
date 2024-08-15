import streamlit as st
import openai
import os

def set_page_config():
    st.set_page_config(layout="wide")

def check_api_key():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        st.error("API key not found. Please set the OPENAI_API_KEY environment variable.")
        st.stop()
    openai.api_key = api_key 

def initialize_session_state():
    if "nutrition_response" not in st.session_state:
        st.session_state.nutrition_response = ""

def check_login():
    if (st.session_state.get("password_correct") == None) or (st.session_state.get("password_correct") == False):
        st.write("Please login first.")
        st.stop()

def display_header():
    st.subheader("Give your preferred treatment services, e.g medication treatment, Helplines, Behavioral Therapy")

def get_user_input():
    return st.text_input(label="nutrition_agent", label_visibility="hidden", placeholder="What are some preffered help options?")

def request_nutrition_options(user_input):
    try:
        prompt = f"Provide me a list of some {user_input} OUD support service programs"
        
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant. You have to work solely on user input specific to only what the user says. Do not include MOUD in your output. Include  contacts and links in your output, also take text from those sites and only be very specific based on exact user output. For example, if a user asks for medication treatment, don't give therapy treatment."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150
        )
        
        st.session_state.nutrition_response = response.choices[0]['message']['content'].strip()
    except Exception as e:
        st.session_state.nutrition_response = f"An error occurred: {e}"

def main():
    set_page_config()
    check_api_key()
    initialize_session_state()
    check_login()
    display_header()
    
    user_input = get_user_input()
    
    if st.button("Request nutrition options"):
        request_nutrition_options(user_input)
    
    st.write(st.session_state.nutrition_response)

if __name__ == "__main__":
    main()
