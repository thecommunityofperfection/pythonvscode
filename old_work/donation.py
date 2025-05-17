import streamlit as st
import pandas as pd

st.subheader(":blue[Create donation]")
readcsv = pd.read_csv("donation.csv")
menu = st.sidebar.selectbox("Select Option", ["Create Donation", "", ""])
if menu == "Create Donation":
    cTitle = st.text_input("Campaign Title")
    st.divider()
    email = st.text_input("Email")
    st.write("")
    st.write("")
    st.write("")
    details = st.text_area("Campaign Details", height=200)
    st.write("")
    goal = st.selectbox("Goal amount", ["50", "100", "300", "Custom"])
    if goal == "Custom":
        goal = st.text_input("Custom")
    if st.button("Create"):
        dndict = {"Campaign Title":[cTitle],"Email":[email],"Details":[details],"Goal":[goal]}
        dntable = pd.DataFrame(dndict)
        dnjoin = pd.concat([readcsv, dntable], ignore_index=True)
        dnjoin.to_csv("donation.csv", index=False)
        st.success("Campaign Created!")

if menu == "View Donation":
    st.subheader(":blue[View Donations]")
    st.divider()
    alltitles = readcsv["title"].to_list()
    selecttitle = st.selectbox
    col1, col2 = st.columns(2)
    with col1:
        selecttitle = st.selectbox("Select Donation to View",alltitles)

    filtertitle = readcsv[readcsv["title"] == selecttitle]
    st.write(filtertitle)