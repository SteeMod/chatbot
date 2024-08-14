import streamlit as st
import requests

st.set_page_config(layout="wide")

# Header
title = "myfitnessagent"

if "nutrition_response" not in st.session_state:
    st.session_state.nutrition_response = ""

col1, col2 = st.columns([1, 10])

if (st.session_state.get("password_correct") == None) or (st.session_state.get("password_correct") == False):
    st.write("Please login first.")
    st.stop()

st.subheader("Let me help you find specific meal options based on your diet (e.g., Mediterranean, Keto, Vegan, etc.)!")
user_input = st.text_input(label="nutrition_agent", label_visibility="hidden", placeholder="What are some Mediterranean breakfast options?")

# button to submit request
if st.button("Request nutrition options"):
    try:
        response = requests.post("https://localhost:8509", json={"query": user_input})
        response.raise_for_status()  # Check if the request was successful
        data = response.json()
        st.session_state.nutrition_response = data.get("response", "No response found.")
    except requests.exceptions.RequestException as e:
        st.session_state.nutrition_response = f"An error occurred: {e}"

st.write(st.session_state.nutrition_response)
