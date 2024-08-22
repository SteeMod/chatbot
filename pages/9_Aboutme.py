import streamlit as st
from PIL import Image
import os

def show_image(file_path):
    try:
        image_data = Image.open(file_path)
        return image_data
    except Exception as ex:
        st.error(f"Error retrieving image: {ex}")
        return None

# Create two columns
col1, col2 = st.columns(2)

# Use the first column for text
col1.title("About Me")
col1.write(
    "Stephen Modimakwane is a Management Information Systems Specialist with over 18 years of experience in the field. His expertise includes Data Analytics, Data Visualization, AI Infusion, and Strategy Execution. He has a passion for creating technology solutions that help organizations and communities. Email: stephenmodimakwane@gmail.com"
)

# Use the second column for the image
image_path = "images/aboutme.png"  # Adjust file path
image = show_image(image_path)
if image:
    col2.image(image, caption='Stephen Modimakwane', width=200)
