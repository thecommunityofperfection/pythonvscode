import streamlit as st

distances = {
    "meter": 1,
    "kilometer": 1000,
    "centimeter": 0.01,
    "millimeter": 0.001,
    "mile": 1609.34,
    "yard": 0.9144,
    "foot": 0.3048,
    "inch": 0.0254
}
weights = {
    "gram": 1,
    "kilogram": 1000,
    "milligram": 0.001,
    "tonne": 1_000_000,        # metric ton
    "ounce": 28.3495,
    "pound": 453.592,
    "stone": 6350.29
}

menu = st.sidebar.selectbox("Choose you conversion", ["Weight", 'Temperature', "Distance"])
if menu == "Distance":
    conv1 = st.selectbox("Choose starting unit:", ["Choose", "meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"])
    conv2 = st.selectbox("Choose resulting unit:", ["Choose", "meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"])
    if conv1 != "Choose" and conv2 != "Choose":
        dist1 = st.number_input(f"What is the original distance in {conv1}s?")
        result = dist1 * distances[conv1] / distances[conv2]
        st.write(f"{dist1} {conv1}s in {conv2}s is: {result}.")
if menu == "Weight":
    conv1 = st.selectbox("Choose starting unit:", ["Choose", "gram", "kilogram", "milligram", "tonne", "ounce", "pound", "stone"])
    conv2 = st.selectbox("Choose resulting unit:", ["Choose", "gram", "kilogram", "milligram", "tonne", "ounce", "pound", "stone"])
    if conv1 != "Choose" and conv2 != "Choose":
        dist1 = st.number_input(f"What is the original distance in {conv1}s?")
        result = dist1 * weights[conv1] / weights[conv2]
        st.write(f"{dist1} {conv1}s in {conv2}s is: {result}.")
if menu == "Temperature":
    conv1 = st.selectbox("Choose your starting unit", ["celsius", "fahrenheit"])
    if conv1 == "celsius":
        cel = st.number_input("What is your temperature in celsius?")
        result = (cel*(9/5))+32
        st.write(f"Your temperature in fahrenheit is: {result}")
    elif conv1 == "fahrenheit":
        fahr = st.number_input("What is your temperature in fahrenheit?")
        result = (fahr-32)*(5/9)
        st.write(f"Your temperature in celsius is: {result}")