import streamlit as st

name = st.text_input("What is your name?")
gift_cars = st.number_input("How many toy cars did you receive as a gift")
bought_cars = st.number_input("How many toy cars did you buy?")
gave_away_cars = st.number_input("How many toy cars did you give away?")
total_cars = gift_cars + bought_cars
net_cars = total_cars - gave_away_cars
st.write("Hi", name + "! You have a total of", net_cars, "after accounting for the ones you gave away.")