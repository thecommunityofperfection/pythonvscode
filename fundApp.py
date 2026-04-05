import streamlit as st
import pandas as pd

st.set_page_config(layout = "wide", page_title = "Sam's Funding Page", page_icon = "💸")
try:
        csvlink = pd.read_csv("fund.csv")
except:
        csvlink = pd.DataFrame()
menu = st.sidebar.selectbox("Select Page", ["Donate", "Create Funding"])
def donate():
    donateList = []
    for i in range(1, len(csvlink)+1):
        findResult = csvlink[csvlink["Fund_ID"] == i]
        title = findResult["Title"].iloc[0]
        donateList.append(title)
    choice = st.selectbox("Which cause would you like to donate to?", donateList)
    findIndex = csvlink[csvlink["Title"] == choice].index[0]
    findResult = csvlink[csvlink["Title"] == choice]
    getRemaining = findResult["Remaining"].iloc[0]
    amount = st.number_input("How much would you like to donate", 0.00, float(getRemaining), 1)
    if getRemaining != 0:
        if st.button("Donate"):
            csvlink.loc[findIndex, "Remaining"] -= amount
            csvlink.to_csv("fund.csv", index=False)
            st.success("Donation successful!")
    else:
        st.error("Cannot donate to this fundraiser.")
if menu == "Donate":
    donate1, donate2, donate3 = st.columns(3)
    with donate1:
        for i in range(1, len(csvlink)+1, 3):
            findResult = csvlink[csvlink["Fund_ID"] == i]
            getTitle = findResult["Title"].iloc[0]
            getDesc = findResult["Description"].iloc[0]
            getGoal = findResult["Goal"].iloc[0]
            getRemaining = findResult["Remaining"].iloc[0]
            if getRemaining != 0:
                st.write(f":blue[{getTitle}]")
                st.write(getDesc)
                st.write(f"Goal: ${getGoal}")
                st.write(f"Remaining: ${getRemaining}")
                st.progress((getGoal - getRemaining) / getGoal)
                if st.checkbox("Donate Now", key = i):
                    donate()
            else:
                st.write(f":blue[{getTitle}]")
                st.write(getDesc)
                st.write(f"Goal: ${getGoal}")
                st.write(f"Remaining: ${getRemaining}")
                st.progress((getGoal - getRemaining) / getGoal)
                st.success("Donation ended! 🎊")
    with donate2:
        for i in range(2, len(csvlink)+1, 3):
            findResult = csvlink[csvlink["Fund_ID"] == i]
            getTitle = findResult["Title"].iloc[0]
            getDesc = findResult["Description"].iloc[0]
            getGoal = findResult["Goal"].iloc[0]
            getRemaining = findResult["Remaining"].iloc[0]
            if getRemaining != 0:
                st.write(f":blue[{getTitle}]")
                st.write(getDesc)
                st.write(f"Goal: ${getGoal}")
                st.write(f"Remaining: ${getRemaining}")
                st.progress((getGoal - getRemaining) / getGoal)
                if st.checkbox("Donate Now", key = i):
                    donate()
            else:
                st.write(f":blue[{getTitle}]")
                st.write(getDesc)
                st.write(f"Goal: ${getGoal}")
                st.write(f"Remaining: ${getRemaining}")
                st.progress((getGoal - getRemaining) / getGoal)
                st.success("Donation ended! 🎊")
    with donate3:
        for i in range(3, len(csvlink)+1, 3):
            findResult = csvlink[csvlink["Fund_ID"] == i]
            getTitle = findResult["Title"].iloc[0]
            getDesc = findResult["Description"].iloc[0]
            getGoal = findResult["Goal"].iloc[0]
            getRemaining = findResult["Remaining"].iloc[0]
            if getRemaining != 0:
                st.write(f":blue[{getTitle}]")
                st.write(getDesc)
                st.write(f"Goal: ${getGoal}")
                st.write(f"Remaining: ${getRemaining}")
                st.progress((getGoal - getRemaining) / getGoal)
                if st.checkbox("Donate Now", key = i):
                    donate()
            else:
                st.write(f":blue[{getTitle}]")
                st.write(getDesc)
                st.write(f"Goal: ${getGoal}")
                st.write(f"Remaining: ${getRemaining}")
                st.progress((getGoal - getRemaining) / getGoal)
                st.sucecss("Donation ended! 🎊")
if menu == "Create Funding":
      fundID = len(csvlink) + 1
      goal = st.number_input("How much funding do you need ($)?")
      title = st.text_input("Choose a title for your funding")
      desc = st.text_area("Describe what you need")
      remaining = goal
      if st.button("Submit"):
            with st.spinner("Saving Employee Data"):
                    funddict = {"Fund_ID":[fundID],"Goal":[goal],"Title":[title],"Description":[desc], "Remaining":[remaining]}
                    fundtable = pd.DataFrame(funddict)
                    jointables = pd.concat([csvlink, fundtable], ignore_index=True)
                    jointables.to_csv("fund.csv", index=False)
                    st.success("Submission complete!")