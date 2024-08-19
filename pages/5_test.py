import streamlit as st

# Title of the app
st.title("Comment Section")

# Initialize session state for comments
if "comments" not in st.session_state:
    st.session_state["comments"] = []

# Function to display comments
def display_comments():
    comments = st.session_state.get("comments", [])
    for comment in comments:
        st.write(comment)

# Function to add a new comment
def add_comment():
    with st.form(key="comment_form"):
        new_comment = st.text_area("Add your comment")
        submit_button = st.form_submit_button(label="Submit")
        if submit_button and new_comment:
            comments = st.session_state.get("comments", [])
            comments.append(new_comment)
            st.session_state["comments"] = comments
            st.experimental_rerun()

# Display existing comments
display_comments()

# Add a new comment
add_comment()

# Collect feedback with appropriate options
st.feedback(options="thumbs")
