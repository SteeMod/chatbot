import streamlit as st
import os

# Ensure the comments directory exists
comments_dir = 'comments'
if not os.path.exists(comments_dir):
    os.makedirs(comments_dir)
    st.write(f"Debug: Created directory {comments_dir}")

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
                file_path = os.path.join(comments_dir, 'comments.txt')
                st.write(f"Debug: Writing to file at {file_path}")
                with open(file_path, 'a') as f:
                    f.write(sanitized_input + '\n')
                st.success("Comment saved successfully!")
                st.write(f"Debug: Successfully wrote to {file_path}")
            else:
                st.warning("Comment cannot be empty.")
                st.write("Debug: Empty comment submitted")
        except FileNotFoundError:
            st.error("The comments directory or file was not found.")
            st.write("Debug: FileNotFoundError occurred")
        except IOError as e:
            st.error(f"An I/O error occurred: {e}")
            st.write(f"Debug: IOError occurred: {e}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
            st.write(f"Debug: Unexpected error occurred: {e}")
