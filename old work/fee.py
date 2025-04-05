import streamlit as st
import pandas as pd

st.header("Tuition Calculator")
st.write("")
st.write("")
csvlink = pd.read_csv("studentTuition.csv")
name = st.text_input("What is parents name?")
address = st.text_input("What is your address")
elementaryKidsNum = st.number_input("How many kids do you have in elementary?", 0)
collegeKidsNum = st.number_input("How many kids do you have in college", 0)
elementaryPrice = elementaryKidsNum*15000
collegePrice = collegeKidsNum*25000
totalPrice = collegePrice + elementaryPrice
if st.button("Submit"):
        feedict = {"Name":[name], "Address":[address], "College Kids":[collegeKidsNum], "Elementary Kids":[elementaryKidsNum], "Tuition":[totalPrice]}
        feetable = pd.DataFrame(feedict)
        bothtables = pd.concat([csvlink, feetable],ignore_index=True)
        bothtables.to_csv("studentTuition.csv",index=False)
st.write("Your total Tuition is: $" + str(totalPrice))