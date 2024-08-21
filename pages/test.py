import streamlit as st
import os
from PIL import Image

# Set the path to your image directory
image_directory = '/workspaces/chatbot/images'

# Get a list of all image files in the directory
image_files = [f for f in os.listdir(image_directory) if f.endswith(('png', 'jpg', 'jpeg'))]

# Display images on the Streamlit app
st.title("Image Gallery")

# Display three images in the same column with text under each image
if len(image_files) >= 3:
    col1, col2, col3 = st.columns(3)
    
    with col1:
        image_path = os.path.join(image_directory, image_files[0])
        image = Image.open(image_path)
        st.image(image, caption="Image 1", use_column_width=True)
        st.write("Description for Image 1")
    
    with col2:
        image_path = os.path.join(image_directory, image_files[1])
        image = Image.open(image_path)
        st.image(image, caption="", use_column_width=True)
        st.write("Description for Image 2")
    
    with col3:
        image_path = os.path.join(image_directory, image_files[2])
        image = Image.open(image_path)
        st.image(image, caption="Image 3", use_column_width=True)
        st.write("Description for Image 3")
else:
    st.write("Not enough images in the directory to display.")
