import streamlit as st
import pandas as pd
import os

# Function to get the absolute path
def get_absolute_path(relative_path):
    base_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)

# Load comments from CSV file
def load_comments(file):
    try:
        comments = pd.read_csv(file)
        st.write(f"Loaded comments from {file}")
    except FileNotFoundError:
        st.write(f"File {file} not found. Initializing empty DataFrame.")
        comments = pd.DataFrame(columns=['name', 'comment'])
    except Exception as e:
        st.error(f"Error loading file {file}: {e}")
    return comments

# Save comments to CSV file
def save_comments(file, comments):
    try:
        comments.to_csv(file, index=False)
        st.write(f"Successfully saved to {file}")
    except Exception as e:
        st.error(f"Error saving to file {file}: {e}")

# Display comments on the webpage
def display_comments(comments):
    st.write("### Comments")
    if comments.empty:
        st.write("No comments yet. Be the first to add one!")
    else:
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

# Use the absolute path to the CSV file
file_path = get_absolute_path('comments.csv')

# Ensure the directory exists
os.makedirs(os.path.dirname(file_path), exist_ok=True)

# Check if the file exists
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
