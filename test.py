import openai
import os
import streamlit as st

# Retrieve the API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')

st.error("There was an error with the API key")
if not api_key:
    raise ValueError("No OpenAI API key found. Please set the OPENAI_API_KEY environment variable.")

# Initialize the OpenAI API client
openai.api_key = api_key

def generate_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        print(f"Error generating response: {e}")
        return "Sorry, I couldn't generate a response."

def chatbot():
    prompt = "Tell me a joke."
    response = generate_response(prompt)
    print(response)

if __name__ == "__main__":
    chatbot()
