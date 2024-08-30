import streamlit as st
from streamlit_star_rating import st_star_rating
import os

# Title of the app
st.title("Review App")

# Input for user to enter their name
name = st.text_input("Enter your name")

# Input for user to enter their review
review = st.text_area("Enter your review")

# Star rating input
rating = st_star_rating("Rate the app", maxValue=5, defaultValue=3, key="rating")

# Initialize session state to store reviews
if "reviews" not in st.session_state:
    st.session_state.reviews = []

# Define the full path to the reviews.txt file
file_path = os.path.join(os.getcwd(), "reviews.txt")
st.write(f"File path: {file_path}")  # Debug statement

# Function to save reviews to a text file
def save_reviews(reviews):
    try:
        with open(file_path, "w") as f:
            for review in reviews:
                f.write(f"Name: {review['name']}\n")
                f.write(f"Review: {review['review']}\n")
                f.write(f"Rating: {review['rating']} stars\n")
                f.write("\n")
        st.success("Reviews saved successfully!")
    except Exception as e:
        st.error(f"Error saving reviews: {e}")
        st.write(f"Exception: {e}")  # Debug statement

# Function to load reviews from a text file
def load_reviews():
    reviews = []
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()
            for i in range(0, len(lines), 4):
                name = lines[i].strip().split(": ")[1]
                review = lines[i+1].strip().split(": ")[1]
                rating = int(lines[i+2].strip().split(": ")[1].split()[0])
                reviews.append({"name": name, "review": review, "rating": rating})
    except FileNotFoundError:
        pass
    except Exception as e:
        st.error(f"Error loading reviews: {e}")
        st.write(f"Exception: {e}")  # Debug statement
    return reviews

# Load reviews from file on startup
if "reviews_loaded" not in st.session_state:
    st.session_state.reviews = load_reviews()
    st.session_state.reviews_loaded = True

# Button to submit the review
if st.button("Submit"):
    if name and review:
        st.session_state.reviews.append({"name": name, "review": review, "rating": rating})
        save_reviews(st.session_state.reviews)
    else:
        st.error("Please enter both your name and review.")

# Display the list of reviews
st.write("### Reviews")
for r in st.session_state.reviews:
    st.write(f"**{r['name']}**: {r['review']} (Rating: {r['rating']} stars)")
