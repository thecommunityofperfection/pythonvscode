import streamlit as st

#A variable can be used to store one data at a time

puzzle = "Rubik's Cube"

#what happens if we want to store multople games??

#DATA COLLECTIONS: List, Tuple, Dictionary, Set
#Can store more than one item/data in a variable


#List
brands = ["Apple", "Samsung", "LG", "Asus"]
st.write(brands)

#1 SELECTBOX: Used to store multiple items in a box where user can select one from

bestfood = st.selectbox("Choose your favorite food:", ["Pizza", "Pasta", "Burger", "Fries", "Jolof Rice", "Chicken", "Cake"])

st.write("Your favorite food is:", bestfood)

#2 RADIO button: Used to store multiple items in different buttons where user can select one from

game = st.radio("Do you like to play games", ["Yes", "No"])

st.write("You chose", game, "so:")

if game == "Yes":
    st.write("You like to play games")

else:
    st.write("You don't like to play games")
#3 SIDEBAR: This is used to navigate from one page to another

menu = st.sidebar.selectbox("Menu", ["Home", "Shop", "Checkout"])