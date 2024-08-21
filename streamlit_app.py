import os
import streamlit as st
from azure.storage.blob import BlobServiceClient

st.write("Welcome to MyOFreeApp, login to get started. Username: MyOFree, Password: Imfree123. Then you may proceed to other pages.")

# Retrieve your Azure Blob Storage connection string from an environment variable
connection_string = os.environ.get("AZURE_STORAGE_CONNECTION_STRING")

if not connection_string:
    st.success ("Azure Storage connection string not found. Please set the environment variable keep om trying you got this")
else:
    # Specify the container name
    container_name = "data1"

    # Specify the folder (virtual subdirectory) within the container
    folder_name = "Misc"

    # Initialize the BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # List of blob names (replace with your own)
    blob_names = ["Screenshot 2024-08-20 124445.png1.png", "Screenshot 2024-08-20 125408.png", "Screenshot 2024-08-20 125917.png"]

    # Descriptions for each image
    descriptions = ["Description for Image 1", "Description for Image 2", "Description for Image 3"]

    # Retrieve blobs and display images
    for blob_name, description in zip(blob_names, descriptions):
        blob_path = f"{folder_name}/{blob_name}"
        blob_client = blob_service_client.get_blob_client(container_name, blob_path)
        try:
            blob_data = blob_client.download_blob()
            st.image(blob_data.readall(), width=200, caption=blob_name)
            st.write(description)
        except Exception as e:
            st.error(f"Error downloading {blob_name}: {e}")
