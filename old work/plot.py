import streamlit as st
import pandas as pd 
import plotly.express as px

csvlink = pd.read_csv('scores.csv')
with st.expander("Click to view table"): 
    st.table(csvlink)
csvcolumns = csvlink.columns
choosecolumns = st.multiselect("Choose columns to plot", csvcolumns)
if choosecolumns:
    avecolumns = csvlink [choosecolumns].mean().reset_index()
    st.table(avecolumns)

    barchart = px.bar (avecolumns,x='index',y=0,labels={'index':'Subject', '0':'Average'}) 
    st.plotly_chart(barchart)
    piechart = px.pie(avecolumns, names='index',values=0,labels={'index':'Subject', '0':'Average'}) 
    st.plotly_chart(piechart)