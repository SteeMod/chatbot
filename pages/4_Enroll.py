import streamlit as st
import my_prompts
import re
from openai import OpenAI
from base_model_utils import call_chat_model

client = OpenAI()

st.set_page_config(layout="wide")

# Header
title = "myfitnessagent"

if (st.session_state.get("password_correct") == None) or (st.session_state.get("password_correct") == False):
    st.write("Please login first.")
    st.stop()

# Initialize internal and external chat history
if "internal_messages" not in st.session_state:
    st.session_state.internal_messages = [{
        "role": "system",
        "content": my_prompts.system_prompt
    }]

if "external_messages" not in st.session_state:
    st.session_state.external_messages = []

# Function to extract tracker tags from response
def parse_messages(text):
    message_pattern = r"<message>(.*?)</message>"

    message = re.findall(message_pattern, text, re.DOTALL)

    return message[0] if message else ""

# Create two columns
col1, col2 = st.columns([1, 1])

with col1:
    st.header("Chat with AI")

    # Create a container for chat messages
    chat_container = st.container()

    # Create a container for the input box
    input_container = st.container()

    # Display chat messages from history on app rerun
    with chat_container:
        for message in st.session_state.external_messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # Accept user input
    with input_container:
        if prompt := st.chat_input("Enter text..."):
            # Add user message to chat history
            st.session_state.internal_messages.append({"role": "user", "content": prompt})
            st.session_state.external_messages.append({"role": "user", "content": prompt})

            with chat_container:
                # Display user message in chat message container
                with st.chat_message("user"):
                    st.markdown(prompt)

                with st.chat_message("assistant"):
                    messages = [{"role": m["role"], "content": m["content"]} for m in st.session_state.internal_messages]

                    completion = call_chat_model(client, messages)

                    response = completion.choices[0].message.content

                    print('***RAW OUTPUTS***')
                    print(response)

                    st.session_state.internal_messages.append({"role": "assistant", "content": response})

                    message = parse_messages(response)

                    st.session_state.external_messages.append({"role": "assistant", "content": message})

                    st.rerun()

with col2:
    st.header("Support and Resources")
    support_container = st.container()
    with support_container:
        st.write("### Follow-up and Support")
        # Add any additional support or resources here
