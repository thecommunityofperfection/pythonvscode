import streamlit as st
import pandas as pd
import plotly.express as px

uploadcsv = st.file_uploader("Choose CSV file to plot: ", type = "csv")
if uploadcsv:
    csvlink = pd.read_csv(uploadcsv)
    csvcolumns = csvlink.columns
    choicecolumns = st.multiselect("Choose columns to plot:", csvcolumns)
    choicechart = st.radio("Choose chart type: ", ["Bar Chart", "Pie Chart"])
    if choicecolumns:
        avecolumns = csvlink [choicecolumns].mean().reset_index()
        if choicechart == "Bar Chart":
            barchart = px.bar (avecolumns,x='index',y=0,labels={'index':'Subject', '0':'Average'}) 
            st.plotly_chart(barchart)
        if choicechart == "Pie Chart":
            piechart = px.pie(avecolumns, names='index',values=0,labels={'index':'Subject', '0':'Average'}) 
            st.plotly_chart(piechart)