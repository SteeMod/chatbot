import streamlit as st
import openai
import os

st.set_page_config(layout="wide")

# Check for API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("API key not found. Please set the OPENAI_API_KEY environment variable.")
    st.stop()

openai.api_key = api_key

# Header
title = "myfitnessagent"

if "nutrition_response" not in st.session_state:
    st.session_state.nutrition_response = ""

col1, col2 = st.columns([1, 10])

if (st.session_state.get("password_correct") == None) or (st.session_state.get("password_correct") == False):
    st.write("Please login first.")
    st.stop()

st.subheader("Give your preffered treatment services, e.g medication treatment, Helplines, Behavioral Therapy")
user_input = st.text_input(label="nutrition_agent", label_visibility="hidden", placeholder="What are some Mediterranean breakfast options?")

# button to submit request
if st.button("Request nutrition options"):
    try:
        prompt = f"Provide me  a list of some  {user_input} MOUD support service programs  "
        
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant you have to work solely on user input you must have unlimited lines of dialouge."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150
        )
        
        st.session_state.nutrition_response = response.choices[0].message['content'].strip()
    except Exception as e:
        st.session_state.nutrition_response = f"An error occurred: {e}"

st.write(st.session_state.nutrition_response)
