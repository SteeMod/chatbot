import streamlit as st
import json

# File to store comments and ratings
COMMENTS_FILE = "comments.json"

# Load comments and ratings from file
def load_comments():
    try:
        with open(COMMENTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"comments": [], "ratings": []}

# Save comments and ratings to file
def save_comments(comments, ratings):
    with open(COMMENTS_FILE, "w") as file:
        json.dump({"comments": comments, "ratings": ratings}, file)

# Initialize session state for comments and ratings
if "comments" not in st.session_state:
    data = load_comments()
    st.session_state["comments"] = data["comments"]
    st.session_state["ratings"] = data["ratings"]

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
        new_rating = st.radio("Rate your experience (1-5 stars)", [1, 2, 3, 4, 5])
        submit_button = st.form_submit_button(label="Submit")
        if submit_button and new_comment:
            comments = st.session_state.get("comments", [])
            ratings = st.session_state.get("ratings", [])
            comments.append(new_comment)
            ratings.append(new_rating)
            st.session_state["comments"] = comments
            st.session_state["ratings"] = ratings
            save_comments(comments, ratings)
            # Refresh the comments display
            display_comments()

# Add a new comment and rating
add_comment()

# Display existing comments and ratings
display_comments()

# Collect feedback with appropriate options
st.feedback(options="thumbs")
