import streamlit as st

#create a simple church age range project
# This will get the name of the member, get the age too
# also get the gender of the church member (radio button) -submit button
# when you click on submit button:
# Make sure you group members in different category based on their age 
# (Kids(3- 12), Teens(13-19), Youth(20-35), Adult(36-64), Elders(65+) )
group = ""
left, right = st.columns(2)
with left:
    name = st.text_input("What is your name?")
    gender = st.radio("What is your gender?", ["Male", "Female"])
with right:
    age = st.number_input("How old are you?", 0)
    if st.button("Submit"):
        if age >= 3 and age <=12:
            group = "Kids"
        elif age >= 13 and age <=19:
            group = "Teens"
        elif age >= 20 and age <=35:
            group = "Youth"
        elif age >= 36 and age <=64:
            group = "Adult"
        elif age >= 65:
            group = "Elders"
        else:
            group = "Infants"
        st.write(name + ",","your group is:", group + ".")