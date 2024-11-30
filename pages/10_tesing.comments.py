import streamlit as st
import pandas as pd
import os

# Load comments from CSV file
def load_comments(file):
    try:
        comments = pd.read_csv(file)
    except FileNotFoundError:
        comments = pd.DataFrame(columns=['name', 'comment'])
    return comments

# Save comments to CSV file
def save_comments(file, comments):
    comments.to_csv(file, index=False)

# Display comments on the webpage
def display_comments(comments):
    st.write("### Comments")
    for index, row in comments.iterrows():
        st.write(f"**{row['name']}**: {row['comment']}")

# Add new comment to the CSV file
def add_comment(file, name, comment):
    comments = load_comments(file)
    new_comment = pd.DataFrame({'name': [name], 'comment': [comment]})
    comments = pd.concat([comments, new_comment], ignore_index=True)
    save_comments(file, comments)

# Main application
st.title("Comments Section")

# Hardcoded path for the CSV file in the /streamlit/ directory
file_path = '/streamlit/comments.csv'

# Check if the file exists and create if it does not
if not os.path.isfile(file_path):
    save_comments(file_path, pd.DataFrame(columns=['name', 'comment']))

# Load and display existing comments
comments = load_comments(file_path)
display_comments(comments)

# Input fields for new comment
st.write("### Add a new comment")
name = st.text_input("Name")
comment = st.text_area("Comment")

# Button to submit new comment
if st.button("Submit"):
    if name and comment:
        add_comment(file_path, name, comment)
        st.success("Comment added successfully!")
        # Reload comments to display the new ones
        comments = load_comments(file_path)
        display_comments(comments)
    else:
        st.error("Please fill in both fields.")
