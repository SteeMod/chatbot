import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = 'sk-proj-BaKsrsQ1JWRPXVV5Az6FT3BlbkFJATy78HWXhfTaRalui6dw'

# Function to get response from OpenAI API
def get_openai_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Streamlit app
st.title("OpenAI ChatBot with Streamlit")

user_input = st.text_input("You: ", "Type your message here...")
if st.button("Send"):
    response = get_openai_response(user_input)
    st.write("Bot:", response)
