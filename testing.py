import streamlit as st

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
            # Use an absolute path to ensure the file is found
            with open('/absolute/path/to/comments.txt', 'a') as f:
                f.write(text_input + '\n')
            st.success("Comment saved successfully!")
        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.error(f"Error details: {str(e)}")
