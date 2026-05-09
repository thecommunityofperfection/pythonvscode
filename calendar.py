import streamlit as st
from streamlit_calendar import calendar
import pandas as pd
from datetime import date, time, datetime

st.title("Book an appointment with Sam")

try:
    bookings = pd.read_csv("bookings.csv")
except:
    bookings = pd.DataFrame()

st.sidebar.subheader("Book a meeting")

name = st.sidebar.text_input("Name please")

chooseDate = st.sidebar.date_input("Choose Date")
timeSlots = [f'{i}:00'  for i in range(8,25)]
chooseTime = st.sidebar.selectbox("Choose a timeslot", timeSlots)

if st.sidebar.button("Book slot"):
    bookingDict = {"Name": [name], "Date":[chooseDate], "Time":[chooseTime]}

    newBooking = pd.Dataframe(bookingDict)

    newBooking.to_csv("bookings.csv", mode = 'a', header = bookings.empty)

#calendar interface

events = []

for i in range(len(bookings)):
    get_name = bookings.loc[i, "Name"]
    get_day = bookings.loc[i, "Date"]
    get_time = bookings.loc[i, "Time"]

    start_date = datetime.strftime(f" {get_time} {get_time}", "%Y-%m-%d %H:%M")