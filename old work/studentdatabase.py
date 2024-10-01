import streamlit as st
import pandas as pd

csvlink = pd.read_csv("scores.csv")
st.table(csvlink)
name = st.text_input("What is your name?")
G1, G2 = st.columns(2)
G3, G4 = st.columns(2)
G5, G6 = st.columns(2)
with G1:
    math_grade = st.number_input("Math grade:",0,100,50)
with G2:
    pe_grade = st.number_input("Physical education grade:",0,100,50)
with G3:
    science_grade = st.number_input("Science grade:",0,100,50)
with G4:
    art_grade = st.number_input("Art grade:",0,100,50)
with G5:
    health_grade = st.number_input("Health grade:",0,100,50)
with G6:
    english_grade = st.number_input("English grade:",0,100,50)
total_grade = math_grade + pe_grade + science_grade + art_grade + health_grade + english_grade
average_grade = total_grade/6
average_grade = round(average_grade)
grade = ""
if average_grade >= 90:
     grade = "A+"
elif average_grade >= 80:
     grade = "A"
elif average_grade >= 70:
     grade = "B"
elif average_grade >= 60:
     grade = "C"
elif average_grade >= 50:
     grade = "D"
elif average_grade < 50:
     grade = "F"
if st.button("Save Grade"):
        #Math,English,Science,Art,PE,Health,Total,Average,Grade
        if average_grade < 50:
                st.error(name + "'s total grade is "+ str(total_grade) + " points. Their average is: " + str(average_grade) + "%, and they FAILED. Their grade is: "+ grade)
        else:
            st.success(name + "'s total grade is "+ str(total_grade) + " points. Their average is: " + str(average_grade) + ", and they PASSED. Their grade is: "+ grade)
        studentdict = {"Name":[name], "Math":[math_grade], "English":[english_grade], "Science":[science_grade], "Art":[art_grade], "PE":[pe_grade], "Health":[health_grade], "Total":[total_grade],"Average":[average_grade], "Grade":[grade]}
        studenttable = pd.DataFrame(studentdict)#pd converts the dict to table format
        st.table(studenttable)#streamlit displays the table
        bothtables = pd.concat([csvlink, studenttable],ignore_index=True)#this joins the new created table after button pressed
        bothtables.to_csv("scores.csv",index=False)