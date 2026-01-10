import streamlit as st

gradesAmount = st.number_input("How many grades do you want to input", 0)
gradesList = []
for i in range(0, gradesAmount):
    grade = st.number_input("What was your grade: " + str(i+1), 0, 100)
    if grade >= 75:
        st.write("Grade: A")
    elif grade >= 65:
        st.write("Grade: B")
    elif grade >= 55:
        st.write("Grade: C")
    elif grade >= 45:
        st.write("Grade: D")
    else:
        st.write("Grade: F")
    gradesList.append(grade)
gradesAverage = sum(gradesList)/gradesAmount
st.write(gradesList)
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