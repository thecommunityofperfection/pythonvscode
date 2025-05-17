import streamlit as st
import pandas as pd

savings = 300
concert_cost = st.number_input("How much did you spend on concert tickets?", 0)
dinner_cost = st.number_input("How much did you spend on dinner?", 0)
shopping_cost = st.number_input("How much did you spend on shopping?", 0)
transportation_cost = st.number_input("How much did you spend on transportation?", 0)
movie_cost = st.number_input("How much did you spend on movie tickets?", 0)
total_cost = concert_cost + dinner_cost + shopping_cost + transportation_cost + movie_cost
savings = savings - total_cost
if savings > 0:
    give_friends = round(savings/3)
st.write("You have $ " + str(savings) + " left. You can give your friends $ " + str(give_friends) + " each.")