
import os
import streamlit as st
from azure.storage.blob import BlobServiceClient
st.write(" Welcome to MyOFreeApp, login to get started username= MyOFree, password=Imfree123, then you may proceed to other pages")




# Retrieve your Azure Blob Storage connection string from an environment variable
connection_string = os.environ.get("AZURE_STORAGE_CONNECTION_STRING")

# Specify the container name
container_name = "data1"

# Specify the folder (virtual subdirectory) within the container
folder_name = "Misc"

# Initialize the BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# List of blob names (replace with your own)
blob_names = ["Screenshot 2024-08-20 124445.png1.png", "Screenshot 2024-08-20 125408.png", "Screenshot 2024-08-20 125917.png"]

# Retrieve blobs and display images
for blob_name in blob_names:
    blob_path = f"{folder_name}/{blob_name}"
    blob_client = blob_service_client.get_blob_client(container_name, blob_path)
    blob_data = blob_client.download_blob()
    st.image(blob_data.readall(), width=200, caption=blob_name)

# Text below each image
st.write("Text for Image 1")
st.write("Text for Image 2")
st.write("Text for Image 3")



