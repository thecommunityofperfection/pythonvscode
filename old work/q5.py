import streamlit as st
import pandas as pd

csvlink = pd.read_csv("math.csv")
st.table(csvlink)
num1 = st.number_input("Chooses a number")
num2 = st.number_input("Choose another number")
add = num1 + num2
subtract = num1 - num2
divide = num1/num2
multiply = num1 * num2
if st.button("Save answers"):
    mathdict = {"FirstNumber":[num1], "SecondNumber":[num2], "Addition":[add], "Subtraction":[subtract], "Multiplication":[multiply], "Division":[divide]}
    mathtable = pd.DataFrame(mathdict)
    st.table(mathtable)
    bothtables = pd.concat([csvlink, mathtable],ignore_index=True)
    bothtables.to_csv("math.csv",index=False)