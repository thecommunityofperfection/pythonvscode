import streamlit as st

savings = 250
st.write("You have 250 dollars")
theme_park_cost = st.number_input("How much did you spend on the theme park ticket?",0)
movie_cost = st.number_input("How much did you spend on movies?",0)
snack_cost = st.number_input("How much did you spend on snacks?",0)
bikes_cost = st.number_input("How much did you spend on bike rentals?",0)
beach_cost = st.number_input("How much did you spend on the beach trip?",0)
total_cost = theme_park_cost + movie_cost + snack_cost + bikes_cost + beach_cost
savings = savings - total_cost
if st.button("Check Money Left"):
    if savings >= 0:
        st.write("You have",savings,"dollars left.")
    else:
        st.write("You have spent more than your savings.")