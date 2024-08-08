import openai
import streamlit as st

def get_openai_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Streamlit app
st.title("OpenAI ChatBot with Streamlit")

user_input = st.text_input("You: ", )
if st.button("Send"):
    response = get_openai_response(user_input)
    st.write("Bot:", response)
