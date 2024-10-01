import streamlit as st
import pandas as pd
#Allow user to upload a csv file
#Allow user to view chart
#Allow user to choose columns to plot
#Alow user to choose arithmetic operation(Sum, Average)
#Allow user to upload and view an image

menu = st.sidebar.selectboxgit init("Choose an option:", ["Upload CSV", "Upload Image"])

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