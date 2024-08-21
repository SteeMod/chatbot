import streamlit as st
from PIL import Image

# Load images from local files
image1 = Image.open("/workspaces/chatbot/images/image.png")
image2 = Image.open("/workspaces/chatbot/images/image2.png")
image3 = Image.open("/workspaces/chatbot/images/image3.png")

# Descriptions of the images
descriptions = [
    "Description 1",
    "Description 2",
    "Description 3"
]

# Create columns with spacing
col1, col2, col3 = st.columns([1, 1, 1], gap="large")

# Display images with descriptions in columns
with col1:
    st.image(image1, caption=descriptions[0], width=300)  # Adjust the width as needed
with col2:
    st.image(image2, caption=descriptions[1], width=300)  # Adjust the width as needed
with col3:
    st.image(image3, caption=descriptions[2], width=300)  # Adjust the width as needed
