import streamlit as st

# Initialize session state to store comments
if 'comments' not in st.session_state:
    st.session_state['comments'] = []

# Function to add a new comment
def add_comment():
    if st.session_state.new_comment:
        st.session_state.comments.append({
            'username': st.session_state.username,
            'text': st.session_state.new_comment,
            'likes': 0,
            'rating': None
        })
        st.session_state.new_comment = ''

# Input for new comment
st.text_input("Add a comment:", key='new_comment', on_change=add_comment)

# Input for username
st.text_input("Enter your username:", key='username')

# Display the latest comments
st.write("### Latest Comments")
for comment in reversed(st.session_state.comments):
    st.write(f"Username: {comment['username']}")
    st.write(f"Comment: {comment['text']}")
    st.write(f"Likes: {comment['likes']}")
    st.write(f"Rating: {comment['rating']} stars")
    st.write("---")
