import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesID


st.set_page_config(page_title = "Image BG removal")
st.info("Image Background Remove")

uploaded_image = st.file_uploader("Upload Image Here", type = ["jpg", "jpeg", "png"])

def image_to_bytes(user_image):
    store_image = BytesID()
    user_image.save(store_image, format = "PNG")

    return store_image.getvalue()

if uploaded_image:
    open_image = Image.open(uploaded_image)

    col1, col2 = st.columns(2)
    with col1:
        st.info("Original image")
        st.image(uploaded_image)
    
    with col2:
        st.info("Removed Background Image")
        removed_bg = remove(open_image)
        st.image(removed_bg)
    
    image_data = image_to_bytes(removed_bg)
    st.download_button("Download Removed BG Image", image_data, "image_no_bg.png", "image/png")