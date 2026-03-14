import streamlit as st

st.title("Grade Average Checker")
st.subheader("Input your grades to get the average")
st.write("")
st.write("")
st.write("")

mathGrade = st.number_input("What was your grade in math?", 0, 100)
englishGrade = st.number_input("What was your grade in english?", 0, 100)
scienceGrade = st.number_input("What was your grade in science?", 0, 100)
geographyGrade = st.number_input("What was your grade in geography?", 0, 100)
healthGrade = st.number_input("What was your grade in health?", 0, 100)

gradesList = [mathGrade, englishGrade, scienceGrade, geographyGrade, healthGrade, ]
gradesAverage = sum(gradesList)/5
if st.button("Show grade"):
    st.write("Grade average: ", gradesAverage)
    if gradesAverage >= 75:
        st.write("Grade Average: A")
    elif gradesAverage >= 65:
        st.write("Grade Average: B")
    elif gradesAverage >= 55:
        st.write("Grade Average: C")
    elif gradesAverage >= 45:
        st.write("Grade Average: D")
    else:
        st.write("Grade Average: F")