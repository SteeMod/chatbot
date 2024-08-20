import streamlit as st

st.write("Welcome to MyOFreeApp, login to get started username= MyOFree, password=Imfree123, then you may proceed to other pages")

# File uploader
uploaded_files = st.file_uploader("Choose PNG files", type="png", accept_multiple_files=True)

# Descriptions for each image
descriptions = ["Description for Image 1", "Description for Image 2", "Description for Image 3"]

# Display images
if uploaded_files:
    for uploaded_file, description in zip(uploaded_files, descriptions):
        try:
            st.image(uploaded_file, width=200, caption=uploaded_file.name)
            st.write(description)
        except Exception as e:
            st.error(f"Error loading {uploaded_file.name}: {e}")
