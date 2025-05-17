import streamlit as st
import pandas as pd

st.set_page_config(page_title="Book An Appointment", page_icon="🧑‍⚕️")
menu = st.sidebar.selectbox("Menu", ["Book Appointment", "Database"])
csvlink = pd.read_csv("appointment.csv")
if menu == "Database":
    adminpass =  st.sidebar.text_input("Enter admin password: ", type="password")
    #user = st.text_input("Input Username: ")
    #password = st.text_input("Input Password: ", type="password")
    if adminpass == "testpassword":
        st.table(csvlink)
elif menu == "Book Appointment":
    st.subheader("Doctor Appointment Request Form")
    st.write("Fill the form below and we will get back to you soon for more updates and plan your appointment.")

    left, right, = st.columns(2)

    with left:
        firstname = st.text_input("First Name:")
    with right:
        lastname = st.text_input("Last Name:")
    with left:
        birthday = st.date_input("Choose your birthday:") 
    with right:
        occupation = st.text_input("Enter your occupation:")
    with left:
        st.write("")
        gender = st.radio("What is your gender", ["Male", "Female"], horizontal=True)
    with right:
        phone = st.text_input("Phone number")

    street1 = st.text_input("Street Address 1:")
    street2 = st.text_input("Street Address 2:")

    left2, right2 = st.columns(2)

    with left2:
        st.text_input("City:")
    with right2:
        state = st.text_input("State/Province")
    with left2: 
        if st.button("Request Appointment"):
            doctordict = {"FirstName":[firstname],"LastName":[lastname],"Gender":[gender],"Birthday":[birthday],"Occupation":[occupation],"Phone":[phone],"Street1":[street1],"Street1":[street2],"Province":[state]}
            doctortable = pd.DataFrame(doctordict)
            #st.write(doctordict)
            #st.write(doctortable)
            jointables = pd.concat([csvlink, doctortable], ignore_index=True)
            jointables.to_csv("appointment.csv", index=False)
            st.success("Submission complete!")