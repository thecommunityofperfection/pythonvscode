#streamlit  is a page/framework to run your python app
#how to run code: click + to open new terminal: type streamlit run codename.py
import streamlit as st

st.header("Welcome to my age calculator")

name = st.text_input("Please enter your name here")

current = st.number_input("Please enter your currrent year",2014)

yob = st.number_input("Please enter your year of birth",1850,2014)

age = current - yob

st.write("You will be",age,"years old")