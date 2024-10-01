import streamlit as st

st.title("Food order App")
st.image("c:/Users/Hollo/Downloads/OIP.jpeg")

bill = 0
st.subheader("Meal")

meal1, meal2, meal3, meal4 = st.columns(4)

with meal1:
    if st.checkbox("Crumpets: $10"):
        st.success("Ok Done.")
        bill += 10

with meal2:
    if st.checkbox("Baked potatoes: $15"):
        st.success("Ok Done.")
        bill += 15

with meal3:
    if st.checkbox("Sausage & Egg: $20"):
        st.success("Ok Done.")
        bill += 20

with meal4:
    if st.checkbox("Shepherd's Pie: $35"):
        st.success("Ok Done.")
        bill += 35

st.subheader("Drinks")

drink1, drink2, drink3, drink4 = st.columns(4)

with drink1:
    if st.checkbox("Water: $1"):
        st.success("Ok Done.")
        bill += 1

with drink2:
    if st.checkbox("Any soft drink: $1.50"):
        soft_drink = st.text_input("What soft drink do you want?")
        st.success("Ok Done ("+ soft_drink + ").")
        bill += 1.50

with drink3:
    if st.checkbox("Juice: $1"):
        juice = st.text_input("What juice do you want?")
        st.success("Ok Done ("+ juice + ").")
        bill += 1

with drink4:
    if st.checkbox("Sparkling water: $1"):
        st.success("Ok Done.")
        bill += 1

if st.button("Check total bill"):
        st.write("Your total bill is",bill,"dollars")
