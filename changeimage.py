import streamlit as st

uploadpfp = st.file_uploader("Choose profile picture: ", type = ["jpg", "png", "jpeg"])
#username = "sam"
if st.button("Press ME!"):
    with open("sam.png", "wb") as writepic:
        writepic.write(uploadpfp.getbuffer())