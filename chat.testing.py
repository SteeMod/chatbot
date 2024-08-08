import openai
import streamlit as st

def get_openai_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content'].strip()

# Streamlit app
st.title("OpenAI ChatBot with Streamlit")

user_input = st.text_input("You: ", "Type your message here...")
if st.button("Send"):
    response = get_openai_response(user_input)
    st.write("Bot:", response)























    #GOD IS GOOD