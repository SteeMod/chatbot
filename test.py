import openai
import os
import streamlit as st

# Retrieve the API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    st.error("No OpenAI API key found. Please set the OPENAI_API_KEY environment variable.")
    raise ValueError("No OpenAI API key found. Please set the OPENAI_API_KEY environment variable.")

# Initialize the OpenAI API client
openai.api_key = api_key

def generate_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use the appropriate engine
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return "Sorry, I couldn't generate a response."

def chatbot():
    st.title("Chatbot")
    prompt = st.text_input("Enter your prompt:")
    if prompt:
        response = generate_response(prompt)
        st.write(response)

if __name__ == "__main__":
    chatbot()
