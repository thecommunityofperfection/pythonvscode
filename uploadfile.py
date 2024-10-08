import streamlit as st
import pandas as pd
#Allow user to upload a csv file
#Allow user to view chart
#Allow user to choose columns to plot
#Alow user to choose arithmetic operation(Sum, Average)
#Allow user to upload and view an image
st.set_page_config(page_title="Upload Files", page_icon="⬆️")
menu = st.sidebar.selectbox("Choose an option:", ["Upload CSV and edit", "Upload Image", "Upload Video", "Upload Audio"])

if menu == "Upload CSV":
    uploadcsv = st.file_uploader("Upload CSV File:", type="csv")

    if uploadcsv:
        csvlink = pd.read_csv(uploadcsv)
        with st.expander("View File"):
            st.table(csvlink)



if menu == "Upload Image":
    uploadimage = st.file_uploader("Upload Image File:", type=["jpg", "jpeg", "png"])

    if uploadimage:
        st.image(uploadimage,use_column_width=True)


    
if menu == "Upload Audio":
    uploadaudio = st.file_uploader("Upload Audio File:", type=["mp3", "wav"])

    if uploadaudio:
        with st.expander("View File"):
            st.audio(uploadaudio,format='audio/mp3')


        
if menu == "Upload Video":
    st.subheader("Upload Youtube Video Link")
    youtubelink = st.text_input("Paste Youtube Video Link")
    if st.button("Play Youtube Video"):
        if youtubelink:
            try:
                st.video(youtubelink)
            except:
                st.error("Sorry cannot play this video link")