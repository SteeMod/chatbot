import os
import streamlit as st
from azure.storage.blob import BlobServiceClient

st.write("Welcome to MyOFreeApp, login to get started.")

# Retrieve your Azure Blob Storage connection string from an environment variable
connection_string = os.environ.get("AZURE_STORAGE_CONNECTION_STRING")

# Specify the container name
container_name = "data1"

# Specify the folder (virtual subdirectory) within the container
folder_name = "Misc"

# Initialize the BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# List of blob names (replace with your own)
blob_names = ["Screenshot 2024-08-20 124445.png", "Screenshot 2024-08-20 125408.png", "Screenshot 2024-08-20 125917.png"]

# Descriptions for each image
descriptions = ["Description for Image 1", "Description for Image 2", "Description for Image 3"]

# Retrieve blobs and display images side by side with descriptions
cols = st.columns(len(blob_names))
for col, blob_name, description in zip(cols, blob_names, descriptions):
    blob_path = f"{folder_name}/{blob_name}"
    blob_client = blob_service_client.get_blob_client(container_name, blob_path)
    blob_data = blob_client.download_blob()
    col.image(blob_data.readall(), width=200, caption=description)
    col.write(description)
