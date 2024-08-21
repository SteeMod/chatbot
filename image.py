import streamlit as st
from PIL import Image

# Load images from local files
image1 = Image.open("/workspaces/chatbot/images/image.png")
image2 = Image.open("/workspaces/chatbot/images/image2.png")
image3 = Image.open("/workspaces/chatbot/images/image3.png")

# Descriptions of the images
descriptions = [
    "Recovery is more effective when individuals come together for treatment. Our focus is on nurturing, educating, and empowering our patients to move towards a brighter future. Let us help you leave this chapter behind and embrace a fresh start.",
    "Successful treatment involves the entire community's support. At MyOFree, we understand the challenges of addiction and the strength that comes from overcoming it. Join us in your journey towards healing and contact us for more details.",
    "Your journey to recovery is unique, just like you. Our tailored services are designed to educate and strengthen you, both mentally and physically. We'll walk alongside you, offering support, motivation, and the reassurance that you're never alone.    "
]

# Display images with descriptions
st.image(image1, caption=descriptions[0], width=300)  # Adjust the width as needed
st.image(image2, caption=descriptions[1], width=300)  # Adjust the width as needed
st.image(image3, caption=descriptions[2], width=300)  # Adjust the width as needed


#Praise GOD

