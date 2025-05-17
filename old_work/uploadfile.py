import streamlit as st
import pandas as pd
import plotly.express as px
#Allow user to upload a csv file
#Allow user to view chart
#Allow user to choose columns to plot
#Alow user to choose arithmetic operation(Sum, Average)
#Allow user to upload and view an image
st.set_page_config(page_title="Upload Files", page_icon="⬆️")
menu = st.sidebar.selectbox("Choose an option:", ["Upload CSV and edit", "Upload Image", "Upload Video", "Upload Audio"])

if menu == "Upload CSV and edit":
    uploadcsv = st.file_uploader("Upload CSV File:", type="csv")

    if uploadcsv:
        readcsv = pd.read_csv(uploadcsv)
        with st.expander("View File"):
            st.table(readcsv)
    
    readcsvcolumns = readcsv.columns #READ ALL COLUMNS IN CSV FILE

    selectcolumns = st.multiselect("Choose columns to plot", readcsvcolumns)
    col1, col2 = st.columns(2)
    with col1:
        selectchart = st.radio("Choose Chart to plot",["Bar Chart", "Pie Chart"], horizontal = True)
    with col2:
        selectoperator = st.radio("Choose Stats Operator",["Average", "Sum", "Count"], horizontal = True)

    if selectcolumns:
        if selectoperator == "Average":
            ave_op = readcsv[selectcolumns].mean().reset_index()
            st.table(ave_op)
            if selectchart == "Bar Chart":
                barchart = px.bar(ave_op, x = "index", y=0, labels = {"index": "Subject","0":"Average"})
                st.plotly_chart(barchart, x="index", y=0)
        
            elif selectchart == "Pie Chart":
                piechart = px.pie(ave_op, names = "index", values = 0, labels = {"index": "Subject","0":"Average"})
                st.plotly_chart(piechart)
               
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