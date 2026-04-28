import streamlit as st
from streamlit_calendar import calendar
import pandas as pd

st.title("Book an appointment with Sam")

try:
    bookings = pd.read_csv("bookings.csv")
except:
    pd.DataFrame()

st.sidebar.subheader("Book a meeting")

name = st.sidebar.text_input("Name please")

choosedate = st.sidebar.date_input("Choose Date")