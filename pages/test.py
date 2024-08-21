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
        resized_image = image.resize((300, 300))  # Resize to 300x300 pixels
        resized_images.append((resized_image, image_path))
    
    # Display images side by side with custom descriptions
    col1, col2, col3 = st.columns(3)
    descriptions = ["Description 1", "Description 2", "Description 3"]
    
    for idx, (image, image_path) in enumerate(resized_images):
        if idx == 0:
            col1.image(image)
            col1.write(descriptions[idx])
        elif idx == 1:
            col2.image(image)
            col2.write(descriptions[idx])
        elif idx == 2:
            col3.image(image)
            col3.write(descriptions[idx])
else:
    st.write("Not enough images in the directory.")
