import streamlit as st
from PIL import Image
st.subheader("Welcome to MYOFree Prototype")
st.write("This app is designed to  empower invididuals, to be OFree (Opiod Free) and live fufilling lives by providing end to end information on opiod misuse/overdose, the app is still in testing phase so please leave a comment. First to use the app you will need to go to the home page through the sidebar, on mobile it looks like this < login to get started. The username is  myofree, Password: imfree123. Then you may proceed to other pages via the side bar.")



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

#praise GOD