import streamlit as st

shop_items = {
    "VIP pass": ["VIP pass: $50", 50],
    "Premium pass": ["Premium pass: 120", 120],
    "Superhero outfit": ["Superhero outfit: $40", 40],
    "Casual outfit": ["Casual outfit: $30", 30],
    "Work outfit": ["Work outfit: $25", 25],
    "Pet": ["Add pet: $40", 40],
    "800 Robux": ["800 Robux: $10", 10],
    "2000 Robux": ["2000 Robux: $25", 25],
    "5000 Robux": ["5000 Robux: $50", 50],
    "10000 Robux": ["10000 Robux: $100", 100],
    "20000 Robux": ["20000 Robux: $200", 200],
}

users = {
    "Daniel123": "Daniel'spassword456",
    "isaac": "isaac"
}
total_price = 0


username = st.text_input("Input Username:")
password = st.text_input("Input Password:", type="password")

def get_item_name(item):
    for name, info in shop_items.items():
        if info[0] == item:
            return name
    return None

def calculate_price(current_price, items):
    new_price = current_price

    for item in items:
        name = get_item_name(item)
        if name is not None:
            new_price += shop_items[name][1]
    
    return new_price

def shop(price):
    robloxPurchase = st.radio("Purchase ROBLOX: $150?", ["Yes", "No"])

    if robloxPurchase == "No":
        return
    
    price += 150

    gamepass = st.radio("Choose Gamepass", [
        "None",
        shop_items["VIP pass"][0],
        shop_items["Premium pass"][0],
    ])
    outfit = st.radio("Choose Outfit", [
        "None",
        shop_items["Superhero outfit"][0],
        shop_items["Casual outfit"][0],
        shop_items["Work outfit"][0],
    ])
    pet = st.radio("Do you want a pet", [
        "None",
        shop_items["Pet"][0]
    ])
    robux = st.radio("Choose robux option:", [
        "None",
        shop_items["800 Robux"][0],
        shop_items["2000 Robux"][0],
        shop_items["5000 Robux"][0],
    ])

    price = calculate_price(price, [gamepass, outfit, pet, robux])

    return price



if username in users and users[username] == password:
    st.write(f"Welcome, {username}!")
    total_price = shop(total_price)
    st.write("Your total is: $" + str(total_price))
else:
    st.write("Invalid username or password.")