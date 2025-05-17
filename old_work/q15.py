import streamlit as st

initial_animals = 50
st.write("You have 50 animals.")
eaten_by_predators = st.number_input("How many animals were eaten?",0)
died_from_disease = st.number_input("How many died from disease?",0)
sold_animals = st.number_input("How many did you sell?",0)
stolen_animals = st.number_input("How many animals were stolen?",0)
initial_animals = initial_animals - eaten_by_predators - died_from_disease - sold_animals - stolen_animals

if st.button("Animals left"):
    if initial_animals > 0:
        st.write("You have", initial_animals, "left")
    else:
        st.write("You lost more animals than you originally had.")
