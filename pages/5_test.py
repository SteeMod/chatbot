import streamlit as st

# Title of the app
st.title("Comment Section")

# Initialize session state for comments and ratings
if "comments" not in st.session_state:
    st.session_state["comments"] = []
if "ratings" not in st.session_state:
    st.session_state["ratings"] = []

# Function to display comments and ratings
def display_comments():
    comments = st.session_state.get("comments", [])
    ratings = st.session_state.get("ratings", [])
    for comment, rating in zip(comments, ratings):
        st.write(f"Comment: {comment}")
        st.write(f"Rating: {'⭐' * rating}")

# Function to add a new comment and rating
def add_comment():
    with st.form(key="comment_form"):
        new_comment = st.text_area("Add your comment")
        new_rating = st.slider("Rate your experience (1-5 stars)", 1, 5, 3)
        submit_button = st.form_submit_button(label="Submit")
        if submit_button and new_comment:
            comments = st.session_state.get("comments", [])
            ratings = st.session_state.get("ratings", [])
            comments.append(new_comment)
            ratings.append(new_rating)
            st.session_state["comments"] = comments
            st.session_state["ratings"] = ratings

# Add a new comment and rating
add_comment()

# Display existing comments and ratings
display_comments()

# Collect feedback with appropriate options
st.feedback(options="thumbs")
