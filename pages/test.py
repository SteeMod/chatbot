import streamlit as st
import os
from PIL import Image

# Set the path to your image directory
image_directory = '/workspaces/chatbot/images'

# Get a list of all image files in the directory
image_files = [f for f in os.listdir(image_directory) if f.endswith(('png', 'jpg', 'jpeg'))]

# Display images on the Streamlit app
st.title("Image Display")

# Ensure there are at least 3 images
if len(image_files) >= 3:
    # Select the first three images
    selected_images = image_files[:3]
    
    # Resize images to the same dimensions
    resized_images = []
    for image_file in selected_images:
        image_path = os.path.join(image_directory, image_file)
        image = Image.open(image_path)
        resized_image = image.resize((1200, 900))  # Resize to 1200x900 pixels
        resized_images.append((resized_image, image_path))
    
    # Display images side by side with custom descriptions
    col1, col2, col3 = st.columns([4, 4, 4])  # Adjust column width to make images larger
    descriptions = ["Description 1", "Description 2", "Description 3"]
    
    for idx, (image, image_path) in enumerate(resized_images):
        if idx == 0:
            col1.image(image, use_column_width=True)  # Use column width to make the image larger
            col1.write(descriptions[idx])
        elif idx == 1:
            col2.image(image, use_column_width=True)  # Use column width to make the image larger
            col2.write(descriptions[idx])
        elif idx == 2:
            col3.image(image, use_column_width=True)  # Use column width to make the image larger
            col3.write(descriptions[idx])
else:
    st.write("Not enough images in the directory.")
