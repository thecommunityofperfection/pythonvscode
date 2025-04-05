import streamlit as st

num1 = st.number_input("Please input the first number:")
num2 = st.number_input("Please input the second number:")
add = num1+num2
sub = num1-num2
mult = num1*num2
div = num1/num2

if st.button("Addition"):
    operator = "+"
    answers = {"Num1":num1, "Num2":num2, "Operator":"+", "Result":add}
    st.table(answers)
if st.button("Subtraction"):
    operator = "-"
    answers = {"Num1":num1, "Num2":num2, "Operator":operator, "Result":sub}
    st.table(answers)
if st.button("Multiplication"):
    operator = "*"
    answers = {"Num1":num1, "Num2":num2, "Operator":operator, "Result":mult}
    st.table(answers)
if st.button("Division"):
    operator = "+"
    answers = {"Num1":num1, "Num2":num2, "Operator":operator, "Result":add}
    st.table(answers)