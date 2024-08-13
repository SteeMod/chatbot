import requests
import json
import os
import streamlit as st

# Initialize the OpenAI API client
api_key = os.get("OPENAI_API_KEY")

if not api_key:
    st.error("No OpenAI API key found. Please set the OPENAI_API_KEY environment variable.")
    raise ValueError("No OpenAI API key found. Please set the OPENAI_API_KEY environment variable.")

def generate_response(prompt):
    try:
        url = "https://api.openai.com/v1/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        payload = {
            "model": "text-davinci-003",  # Use the appropriate model
            "prompt": prompt,
            "max_tokens": 150
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        
        if response.status_code == 200:
            response_data = response.json()
            return response_data['choices'][0]['text'].strip()
        else:
            st.error(f"Error generating response: {response.status_code}")
            return "Sorry, I couldn't generate a response."
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return "Sorry, I couldn't generate a response."