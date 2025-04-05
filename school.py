import streamlit as st
import pandas as pd
import random

try:
    csvlink = pd.read_csv("school.csv")
except:
    csvlink = pd.DataFrame()
menu = st.sidebar.selectbox("Menu", ["Registration", "View Info"])
if menu == "Registration":
    st.title("- Student Regstration Form")

    st.divider()
    st.write("**- Student Information**")

    uploadpfp = st.file_uploader("Choose profile picture: ", type = ["jpg", "png", "jpeg"])
    


    c1, c2 = st.columns(2)
    with c1:
        fname = st.text_input("First name:")
        dob = st.date_input("Date of Birth:")
        gender = st.radio("Gender:", ["Male", "Female"], horizontal = True)
    with c2:
        lname = st.text_input("Last name:")
        nation = st.text_input("Nationality:")
        email = st.text_input("Student Email:")
    
    username = fname + lname
    # username = st.text_input("Input Username:")
    #     while username in csvlink["Username"]:
    #         st.error("Username is taken. Please try again.")
    #         username = st.text_input("Input Username:")




    st.divider()
    st.write("**- Parent/Guardian Information**")
    p1, p2 = st.columns(2)
    with p1:
        pName = st.text_input("Parent/guardian Name:")
        pContact = st.text_input("Contact information:")
    with p2:
        relation = st.text_input("Relationship to student:")
        emergency = st.text_input("Emergency contact information:")

    agreement = st.radio("Do you agree to the terms and conditions of enrollment?", ["Yes", "No"])
    if agreement == "Yes":
        if st.button("Save Student Information"):
                
                if uploadpfp and fname and lname:
                    schooldict = {"First Name":[fname], "Last Name":[lname], "Birthday":[dob], "Nationality":[nation], "Gender":[gender], "Email":[email], "Parent Name":[pName], "Parent Relationship":[relation], "Parent Contact":[pContact], "Emergency Contact":[emergency], "Username":[username]}
                    schooltable = pd.DataFrame(schooldict)
                    bothtables = pd.concat([csvlink, schooltable],ignore_index=True)
                    bothtables.to_csv("school.csv",index=False)
                    
                    with open(username+".png", "wb") as writepic:
                        writepic.write(uploadpfp.getbuffer())
                else:
                    st.error("Upload student picture first & Fill all details!")



if menu == "View Info":
    pass