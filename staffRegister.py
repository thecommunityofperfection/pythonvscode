import streamlit as st
import pandas as pd

st.set_page_config(layout = "wide", page_title = "Sam's Staff Register", page_icon = "📖")
try:
        csvlink = pd.read_csv("staff.csv")
except:
        csvlink = pd.DataFrame()
staffID = "staff_"+str(len(csvlink)+1)
menu = st.sidebar.selectbox("Menu", ["Register Staff", "Staff Database", "Staff File"])
st.sidebar.info("Made by Sam🔥")
if menu == "Register Staff":
        st.subheader("Register Staff")
        part1, part2 = st.columns(2)

        with part1:
                fName = st.text_input("First name")        
                email = st.text_input("Email")

        with part2:
                lName = st.text_input("Last Name")
                gender = st.selectbox("Gender", ["Male", "Female"])

        department = st.selectbox("Department", ['Management', 'Accounting', 'Engineering', 'Human Resources', 'Security', 'Medical', 'Transportation'])
        title = st.selectbox("Job Title", ['Board Of Directors', 'Supervisor', 'Senior Staff', 'Junior Staff', 'Paid Intern', 'Unpaid Intern'])

        part3, part4 = st.columns(2)

        with part3:
                status = st.selectbox("Contract Status", ["Select", "Part time","Full time"])
                
        with part4:
                income = st.number_input("Monthly Income", 0)

        degree = st.selectbox("Educational Degree", ['None', 'Associate Degree', 'Bachelor Degree', 'Graduate Degree', 'Professional Degree', 'Doctoral Degree'])
        employmentDate = st.date_input("Employment Date")


        if st.button("Submit Employee Data"):
                with st.spinner("Saving Employee Data"):
                        staffdict = {"Staff_ID":[staffID],"First Name":[fName],"Last Name":[lName],"Gender":[gender],"Employment Date":[employmentDate],"Job Title":[title],"Email":[email],"Department":[department],"Degree":[degree],"Salary":[income],"Contract":[status]}
                        stafftable = pd.DataFrame(staffdict)
                        jointables = pd.concat([csvlink, stafftable], ignore_index=True)
                        jointables.to_csv("staff.csv", index=False)
                        st.success("Submission complete!")

if menu == "Staff Database":
        st.dataframe(csvlink, hide_index = True)

if menu == "Staff File":
        staff1, staff2, staff3 = st.columns(3)
        with staff2:
                st.subheader(":green[Find Staff Info]")
                findStaff  = st.text_input("Enter Staff ID").lower()
                findButton = st.button("Find Staff")

        if findButton:
                findResult = csvlink[csvlink['Staff_ID'] == findStaff]
                #st.table(findResult)

                if findResult.empty:
                        st.error("Staff ID not found. Please double check for accuracy.")
                        st.stop()
                else:
                        #st.divider()
                        getID = findResult["Staff_ID"].iloc[0]
                        getFn = findResult["First Name"].iloc[0]
                        getLn = findResult["Last Name"].iloc[0]
                        getGnd = findResult["Gender"].iloc[0]
                        getEmpDate = findResult["Employment Date"].iloc[0]
                        getTitle = findResult["Job Title"].iloc[0]
                        getMail = findResult["Email"].iloc[0]
                        getDept = findResult["Department"].iloc[0]
                        getDeg = findResult["Degree"].iloc[0]
                        getSal = findResult["Salary"].iloc[0]
                        getCrt = findResult["Contract"].iloc[0]
                        col1, col2, col3 = st.columns(3)
                        with col1:
                                st.info(f":green[{getFn} {getLn}]")
                        st.write()
                        st.subheader("Personal Information")
                        st.divider()
                        sec1,sec2,sec3 = st.columns(3)
                        with sec1:
                                st.write("Email")
                                st.write(getMail)
                        with sec2:
                                st.write("Gender")
                                st.write(getGnd)
                        with sec3:
                                st.write("Degree")
                                st.write(getDeg)
                        st.divider()
                        st.subheader("Job Information")
                        st.divider()
                        sec4,sec5,sec6 = st.columns(3)
                        with sec4:
                                st.write("Department")
                                st.write(getDept)
                        with sec5:
                                st.write("Employee ID")
                                st.write(getID)
                        with sec6:
                                st.write("Date Of Employment")
                                st.write(getEmpDate)
                        st.divider()
                        sec7,sec8 = st.columns(2)
                        with sec7:
                                st.write("Contract Status")
                                st.write(getCrt)
                        with sec8:
                                st.write("Salary")
                                st.write(f"${getSal:,}")                