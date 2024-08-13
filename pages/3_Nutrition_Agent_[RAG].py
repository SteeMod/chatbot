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
    # response = call_chat_model(user_input)
    data = requests.post("http://10.0.0.63:8000/nutrition").json()
    st.session_state.nutrition_response = data["response"]
    
st.write(st.session_state.nutrition_response)
