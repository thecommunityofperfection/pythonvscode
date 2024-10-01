import streamlit as st 
import pandas as pd

csvlink = pd.read_csv("ages.csv")
menu = st.sidebar.selectbox("Menu", ["Submit data", "Database"])
if menu == "Database":
    adminpass =  st.sidebar.text_input("Enter password: ", type="password")
    if adminpass == "testpassword":
        st.table(csvlink)
else:
    user = st.text_input("Choose a username:")
    password = st.text_input("Choose a password:", type="password")
    age = st.number_input("How old are you?",0)
    name = st.text_input("What is your name?")
    gender = st.radio("Gender:", ["Male", "Female"])
    if age > 2 and age < 13:
        group = "Kids"
    elif age > 12 and age < 20:
        group = "Teens"
    elif age > 19 and age < 36:
        group = "Youth"
    elif age > 36 and age < 64:
        group = "Adults"
    else:
        group = "Elders"
    if st.button("Sign up"):
        agedict = {"Username":[user],"Password":[password],"Name":[name],"Age":[age],"Gender":[gender], "Group":[group]}
        agetable = pd.DataFrame(agedict)
        jointables = pd.concat([csvlink, agetable], ignore_index=True)
        jointables.to_csv("ages.csv", index=False)
        st.write("Your group is:", group)
        st.success("Submission complete!")