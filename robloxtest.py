import streamlit as st


username = st.text_input("Input Username:")
password = st.text_input("Input Password:", type="password")
gamestatus = "You need to purchase the game first!"
price = 0
if username == "Daniel123" and password == "Daniel'spassword456":
    robloxPurchase = st.radio("Purchase ROBLOX: $150?", ["Options:", "Yes", "No"])
    if robloxPurchase == "Yes":
        price = 150
        gamepass = st.radio("Choose Gamepass", ["Options:", "VIP pass: $50", "Premium pass: 120"])
        outfit = st.radio("Choose Outfit", ["Options:", "Superhero outfit: $40", "Casual outfit: $30", "Work outfit: $25"])
        pet = st.radio("Do you want a pet", ["Options:", "Add Pet: $40", "No Pet: Free"])
        robux = st.radio("Choose robux option:", ["Options:", "800: $10", "2000: $25", "4500: $50"])
        if gamepass == "VIP pass: $50":
            price = price + 50
        if gamepass == "Premium pass: 120":
            price = price + 120
        if outfit == "Superhero outfit: $40":
            price = price + 40
        if outfit == "Casual outfit: $30":
            price = price + 30
        if outfit == "Work outfit: $25":
            price = price + 25
        if pet == "Add pet: $40":
            price = price + 40
        if robux == "800: $10":
            price = price + 10
        if robux == "2000: $25":
            price = price + 25
        if robux == "4500: $50":
            price = price + 50
    st.write("Your total is: $" + str(price))