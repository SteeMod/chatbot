import streamlit as st
import os

# Ensure the comments directory exists
if not os.path.exists('comments'):
    os.makedirs('comments')

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
            # Sanitize input
            sanitized_input = text_input.replace('\n', ' ').strip()
            if sanitized_input:
                # Use a relative path to ensure the file is found
                file_path = os.path.join('comments', 'comments.txt')
                with open(file_path, 'a') as f:
                    f.write(sanitized_input + '\n')
                st.success("Comment saved successfully!")
            else:
                st.warning("Comment cannot be empty.")
        except FileNotFoundError:
            st.error("The comments directory or file was not found.")
        except IOError as e:
            st.error(f"An I/O error occurred: {e}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
