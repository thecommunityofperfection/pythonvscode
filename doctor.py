import streamlit as st
import pandas as pd

ADMIN_PASSWORD = "testpassword"
CSV_FILE_PATH = "appointment.csv"

st.set_page_config(page_title="Book An Appointment", page_icon="🧑‍⚕️")
menu = st.sidebar.selectbox("Menu", ["Book Appointment", "Database"])
csvfile = pd.read_csv(CSV_FILE_PATH)

user_data = {
    "FirstName": None,
    "LastName": None,
    "Gender": None,
    "Birthday": None,
    "Occupation": None,
    "Phone": None,
    "Street1": None,
    "Street2": None,
    "Province": None,
    "City": None,
    "State": None,
}



def admin_page():
    st.title("Admin Page")
    password = st.text_input("Enter admin password: ", type="password")
    if password == ADMIN_PASSWORD:
        st.table(csvfile)

def user_page():
    global user_data

    st.subheader("Doctor Appointment Request Form")
    st.write("Fill the form below and we will get back to you soon for more updates and plan your appointment.")

    left_column, right_column, = st.columns(2)

    with left_column:
        user_data["FirstName"] = st.text_input("First Name:")
        user_data["Birthday"] = st.date_input("Choose your birthday:") 

        st.write("")

        user_data["Gender"] = st.radio("What is your gender", ["Male", "Female"], horizontal=True)
    with right_column:
        user_data["LastName"] = st.text_input("Last Name:")
        user_data["Occupation"] = st.text_input("Enter your occupation:")
        user_data["Phone"] = st.text_input("Phone number")


    user_data["Street1"] = st.text_input("Street Address 1:")
    user_data["Street2"] = st.text_input("Street Address 2:")

    left2, right2 = st.columns(2)

    with left2:
        user_data["City"] = st.text_input("City:")
        request_button = st.button("Request Appointment")
    with right2:
        user_data["State"] = st.text_input("State/Province")

    if request_button:
        user_table = pd.DataFrame([user_data])

        jointables = pd.concat([csvfile, user_table], ignore_index=True)
        jointables.to_csv(CSV_FILE_PATH, index=False)
        st.success("Submission complete!")


if menu == "Database":
    admin_page()
elif menu == "Book Appointment":
    user_page()