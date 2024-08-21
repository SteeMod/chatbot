import streamlit as st
from PIL import Image

# Load images from local files
image1 = Image.open("images/image2.png")
image2 = Image.open("images/image.png")
image3 = Image.open("images/image3.png")

# Descriptions of the images
descriptions = [
    "Go to the MYOEvent Finder, this page helps you find in person or virtual events (treatment, awareness, Prevention and Support events) about opiod misuse and overdose",
    "MyOSupport Service Finder lets you find support services (medication, behavioral therapy or helplines) based on your preffered treatment service.",
    "MyOTP Finder lets you find Opiod Treatment Programs, facilities and healthcare professionals based on your location."
]

# Display images with descriptions
st.image(image1, caption=descriptions[0], width=300)  # Adjust the width as needed
st.image(image2, caption=descriptions[1], width=300)  # Adjust the width as needed
st.image(image3, caption=descriptions[2], width=300)  # Adjust the width as needed


#Praise GOD

