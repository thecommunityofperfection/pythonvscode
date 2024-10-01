import streamlit as st

st.subheader("Doctor Appointment Form")
st.write("")
left, right, = st.columns(2)
with left:
    firstname = st.text_input("First name*:")
with right:
    lastname = st.text_input("Last name*:")
phone = st.text_input("Phone:")
birthday = st.date_input("Date Of Birth*:") 
street1 = st.text_input("Street Address:")
street2 = st.text_input("Street Address Line 2:")
left2, right2 = st.columns(2)
with left2:
    st.text_input("City:")
    st.text_input("Postal Code:")
with right2:
    st.text_input("Region:")
    st.text_input("Country")
st.text_input("Email:")
st.text_input("Have you previously attended our facility?*")
