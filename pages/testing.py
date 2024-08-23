import streamlit as st
import os

# Create a form with a text area in Streamlit
with st.form(key='Comment'):
    text_input = st.text_area(
        label='Enter your comment', 
        value='', 
        placeholder='Include who the message is from and give detailed comments.', 
        max_chars=500
    )
    submit_button = st.form_submit_button(label='Submit')

    # If the form is submitted, write the comment to a file
    if submit_button:
        try:
            # Use __file__ to determine the relative path
            script_dir = os.path.dirname(__file__)
            file_path = os.path.join(script_dir, '/workspaces/chatbot/comments/comments.txt')
            
            with open(file_path, 'a') as f:
                f.write(text_input + '\n')
            st.success("Comment saved successfully!")
        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.error(f"Error details: {str(e)}")
