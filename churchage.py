import streamlit as st 
import pandas as pd

ADMIN_PASSWORD = "testpassword"
CSV_FILE_PATH = "ages.csv"

csvfile = pd.read_csv(CSV_FILE_PATH)
menu = st.sidebar.selectbox("Menu", ["Submit data", "Database"])

# Define age groups
ages = {
    "Kids": [3, 12],
    "Teens": [13, 19],
    "Youth": [20, 35],
    "Adults": [36, 63],
}

def get_age_group(age):
    for group, (min_age, max_age) in ages.items():
        if min_age <= age <= max_age:
            return group
    return "Elders"

def admin_page():
    st.title("Admin Page")
    password = st.text_input("Enter admin password: ", type="password")
    if password == ADMIN_PASSWORD:
        st.table(csvfile)

def user_page():
    username = st.text_input("Choose a username:")
    password = st.text_input("Choose a password:", type="password")
    age = st.number_input("How old are you?",0)
    name = st.text_input("What is your name?")
    gender = st.radio("Gender:", ["Male", "Female"])

    group = get_age_group(age)

    if st.button("Sign up"):
        sign_up(username, password, name, age, gender, group)

def sign_up(username, password, name, age, gender, group):
    user_info = {
        "Username":[username],
        "Password":[password],
        "Name":[name],
        "Age":[age],
        "Gender":[gender],
        "Group":[group]
    }
    user_table = pd.DataFrame(user_info)

    updated_table = pd.concat([csvfile, user_table], ignore_index=True)
    updated_table.to_csv(CSV_FILE_PATH, index=False)

    st.write("Your group is:", group)
    st.success("Submission complete!")
    
if menu == "Submit data":
    user_page()
elif menu == "Database":
    admin_page()