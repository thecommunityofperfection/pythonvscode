"""
Streamlit app to upload and save a profile picture locally.
"""

import streamlit as st
from io import BytesIO
from PIL import Image, UnidentifiedImageError
from pathlib import Path, WindowsPath

PFP_FOLDER: WindowsPath = Path("./profile_pics")
PFP_FILE_NAME: str = "sam.png"

st.title("Upload a Profile Picture")

def open_and_verify_image(image: BytesIO) -> Image.Image:
    """
    Opens and verifies an uploaded image file.

    This function attempts to load the image to ensure it's in a
    valid and readable format. If the file is not a supported image,
    an error is shown in the Streamlit app and execution stops.

    Parameters:
        image (BytesIO): The uploaded file as a byte stream.

    Returns:
        Image.Image: A PIL Image object ready for use.
    """

    try:
        pfp: Image.Image = Image.open(image)
        pfp.load()                  # Verify the image is valid
    except UnidentifiedImageError:
        st.error("Invalid image file.")
        st.stop()
    return pfp

uploaded_file: BytesIO = st.file_uploader(
    "Choose profile picture: ", 
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=False     # Only accept one file
)

if uploaded_file:

    pfp: Image.Image = open_and_verify_image(uploaded_file)

    # Show a preview
    st.image(
        uploaded_file,
        caption="Preview",
        width=150
    )

    if st.button("Save Profile Picture"):
        output_path: WindowsPath = PFP_FOLDER / PFP_FILE_NAME
        output_path.parent.mkdir(exist_ok=True)     # Create the profile picture directory if it does not exist

        # Save the image to disk
        pfp.save(output_path)

        st.success(f"Image saved to: `{output_path}`")