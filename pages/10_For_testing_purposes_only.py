import streamlit as st
from streamlit_star_rating import st_star_rating
from azure.storage.blob import BlobServiceClient
import json

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

# Azure Blob Storage setup
connection_string = "your_connection_string_here"
container_name = "your_container_name_here"
blob_name = "reviews.json"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(container_name)

# Function to save reviews to Azure Blob Storage
def save_reviews(reviews):
    try:
        blob_client = container_client.get_blob_client(blob_name)
        blob_client.upload_blob(json.dumps(reviews), overwrite=True)
        st.success("Reviews saved successfully!")
    except Exception as e:
        st.error(f"Error saving reviews: {e}")

# Function to load reviews from Azure Blob Storage
def load_reviews():
    reviews = []
    try:
        blob_client = container_client.get_blob_client(blob_name)
        blob_data = blob_client.download_blob().readall()
        reviews = json.loads(blob_data)
    except Exception as e:
        st.error(f"Error loading reviews: {e}")
    return reviews

# Load reviews from Azure Blob Storage on startup
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
