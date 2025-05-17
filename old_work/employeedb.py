import streamlit as st
import pandas as pd

csvlink = pd.read_csv("employee.csv")
sidebar = st.sidebar.selectbox("Menu", ["Register Staff", "Staff Database", "Staff File"])
if sidebar == "Register Staff":
    st.header("Register Employee")

    col1, col2 = st.columns(2)
    with col1:
        fName = st.text_input("First Name:")
        email = st.text_input("Email Address:")
        department = st.selectbox("Department", ['Management', 'Accounting', 'Engineering', 'Human Resources', 'Security', 'Medical', 'Transportation'])
        contract = st.selectbox("Contract Status:", ["Full Time", "Part Time"])
    with col2:
        lName = st.text_input("Last Name:")
        gender = st.selectbox("Gender:",["Male", "Female"])
        title = st.selectbox("Job Title:", ['Board Of Directors', 'Supervisor', 'Senior Staff', 'Junior Staff', 'Paid Intern', 'Unpaid Intern'])
        salary = st.number_input("Monthly Income", 0)
    degree = st.selectbox("Educational Degree:", ['None', 'Associate Degree', 'Bachelor Degree', 'Graduate Degree', 'Professional Degree', 'Doctoral Degree'])
    col3, col4 = st.columns(2)
    with col3:
        employment_date = st.date_input("Employment date:")
    with col4:
        st.write("")
        st.write("")
        if st.button("Submit Employee Data"):
            employeedict = {"First Name":[fName],"Last Name":[lName],"Gender":[gender],"Employment Date":[employment_date],"Job Title":[title],"Email":[email],"Department":[department],"Degree":[degree],"Salary":[salary],"Contract Status":[contract]}
            employeetable = pd.DataFrame(employeedict)
            jointables = pd.concat([csvlink, employeetable], ignore_index=True)
            jointables.to_csv("employee.csv", index=False)
            st.success("Submission complete!")