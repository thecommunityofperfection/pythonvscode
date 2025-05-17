import streamlit as st

#input 1
name = st.text_input("What is your name?")
favorite_color = st.text_input("What is your favorite color?")
favorite_animal = st.text_input("What is your favorite animal?")
favorite_food = st.text_input("What is your favorite food?")
st.write("Hi " + name + ", your favorite color is " + favorite_color + ", your favorite animal is a " + favorite_animal + ", and your favorite food is " + favorite_food + ".")

#input 2
name = st.text_input("What is your name?")
favorite_sport = st.text_input("What is your favorite sport?")
favorite_team = st.text_input("What is your favorite team?")
favorite_player = st.text_input("What is your favorite player?")
st.write("Hi " + name + ", your favorite sport is " + favorite_sport + ", your favorite team is a " + favorite_team + ", and your favorite player is " + favorite_player + ".")

#input 3
name = st.text_input("What is your name?")
favorite_book = st.text_input("What is your favorite book?")
favorite_character = st.text_input("What is your favorite character?")
favorite_part = st.text_input("What is your favorite part?")
st.write("Hi " + name + ", your favorite book is " + favorite_book + ", your favorite character is a " + favorite_character + ", and your favorite part is " + favorite_part + ".")

#input 4
name = st.text_input("What is your name?")
animal_stickers = st.number_input("How many animal stickers have you collected??")
superhero_stickers = st.number_input("How many superhero stickers have you collected??")
star_stickers = st.number_input("How many star stickers have you collected??")
total_stickers = star_stickers + superhero_stickers + animal_stickers
st.write(name + "you have ", total_stickers)