import streamlit as st
from streamlit_star_rating import st_star_rating

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

# Button to submit the review
if st.button("Submit"):
    if name and review:
        st.session_state.reviews.append({"name": name, "review": review, "rating": rating})
        st.success("Thank you for your review!")
    else:
        st.error("Please enter both your name and review.")

# Display the list of reviews
st.write("### Reviews")
for r in st.session_state.reviews:
    st.write(f"**{r['name']}**: {r['review']} (Rating: {r['rating']} stars)")
