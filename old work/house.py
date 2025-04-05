import streamlit as st
import pandas as pd

csvlink = pd.read_csv("housedata.csv")
menu = st.sidebar.selectbox("Menu", ["House pricing", "Database"])
if menu == "House pricing":
    st.header("House Budgeting")
    st.write("")
    st.write("")
    name = st.text_input("What is your name?")
    salary = st.number_input("What is your yearly salary", 0)
    budget = ""
    if salary < 100000:
        st.write("You can buy/rent an apartment")
        budget = "Apartment"
    elif salary >= 100000 and salary < 500000:
        st.write("You can buy a bungalow")
        budget = "Bungalow"
    elif salary >= 500000 and salary < 1000000:
        st.write("You can buy a duplex")
        budget = "Duplex"
    elif salary >= 1000000 and salary < 5000000:
        st.write("You can buy a mansion")
        budget = "Mansion"
    elif salary >= 5000000:
        st.write("You can buy an estate")
        budget = "Estate"
    else:
        st.write("Please try again later")
        budget = "error"
    if st.button("Submit"):
        if budget != "error":
            housedict = {"Name":[name], "Salary":[salary], "House Budget":[budget]}
            housetable = pd.DataFrame(housedict)
            bothtables = pd.concat([csvlink, housetable],ignore_index=True)
            bothtables.to_csv("housedata.csv",index=False)
if menu == "Database":
    st.table(csvlink)