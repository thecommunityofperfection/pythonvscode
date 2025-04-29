import streamlit as st
import pandas as pd
adminPassword = "School12457"
try:
    csvlink = pd.read_csv("school.csv")
except:
    csvlink = pd.DataFrame()
menu = st.sidebar.selectbox("Menu", ["Registration", "View Student Info"])
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
    
    studentID = "student" + str(len(csvlink) + 1)




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
                    schooldict = {"First Name":[fname], "Last Name":[lname], "Birthday":[dob],
                                   "Nationality":[nation], "Gender":[gender], "Email":[email],
                                     "Parent Name":[pName], "Parent Relationship":[relation],
                                     "Parent Contact":[pContact], "Emergency Contact":[emergency], "StudentID":[studentID]}
                    schooltable = pd.DataFrame(schooldict)
                    bothtables = pd.concat([csvlink, schooltable],ignore_index=True)
                    bothtables.to_csv("school.csv",index=False)
                    
                    with open(studentID + ".png", "wb") as writepic:
                        writepic.write(uploadpfp.getbuffer())
                    st.success("Saved Student Information!")
                else:
                    st.error("Upload student picture first & Fill all details!")



if menu == "View Student Info":
    studentUser = st.sidebar.text_input("Input student ID: ").lower()
    admin = st.sidebar.text_input("Enter admin password: ", type = "password")
    if st.sidebar.button("View student info"):
        if admin == adminPassword:
            finduser = csvlink[csvlink['StudentID'] == studentUser]
            sImage = studentUser + ".png"
            #st.table(finduser)
            getUserID = finduser["StudentID"].iloc[0]
            getFName = finduser["First Name"].iloc[0]
            getLName = finduser["Last Name"].iloc[0]
            getName = getFName + " " + getLName
            getGender = finduser["Gender"].iloc[0]
            getBirthday = finduser["Birthday"].iloc[0]
            getEmail = finduser["Email"].iloc[0]
            getParent = finduser["Parent Name"].iloc[0]
            getParentContact = finduser["Parent Contact"].iloc[0]
            getRelationship = finduser["Parent Relationship"].iloc[0]
            getEmergency = finduser["Emergency Contact"].iloc[0]
            l1, l2 = st.columns(2)
            with l1:
                st.title(f" :red[{getName}]")
            with l2:
                st.image(sImage)
            st.write()
            side1, side2 = st.columns(2)
            with side1:
                with st.form("col1"):
                    st.subheader("Student Info")
                    st.divider()
                    st.write("User ID: ", getUserID)
                    st.write("Gender: ", getGender)
                    st.write("Birth Date: ", getBirthday)
                    st.write("Email: ", getEmail)
                    if st.form_submit_button(""):
                        pass
            with side2:
                with st.form("col2"):
                    st.subheader("Parent Info")
                    st.divider()
                    st.write("Parent/Guardian: ", getParent)
                    st.write("Parent Contact: ", getParentContact)
                    st.write("Relationship: ", getRelationship)
                    st.write("Emergency Contact: ", getEmergency)
                    if st.form_submit_button(""):
                            pass
        else: 
            st.sidebar.error("Incorrect Password")