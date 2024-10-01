import streamlit as st

num_exercise_books = st.number_input("How many exercise books did you buy?", 0)
num_pens = st.number_input("How many pens did you buy?", 0)
num_drawing_books = st.number_input("How many drawing books did you buy?", 0)
num_dictionaries = 2
price_exercise_books = 20
price_drawing_books = 10
price_dictionaries = 50
price_pens = 4
total_price = num_dictionaries*price_dictionaries + num_drawing_books*price_drawing_books + num_exercise_books*price_exercise_books + num_pens*price_pens
st.write("Your total is",total_price,"dollars.")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
#Input 5
name = st.text_input("What is your name?")

red_marbles = st.number_input("How many red marbles do you have?",0)

blue_marbles = st.number_input("How many blue marbles do you have?",0)

green_marbles = st.number_input("How many green marbles do you have?",0)

total_marbles = red_marbles + blue_marbles + green_marbles

st.write("Hi",name + "! You have a total of", total_marbles, "marbles")