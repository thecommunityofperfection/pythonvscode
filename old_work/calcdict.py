import streamlit as st
import pandas as pd

csvlink = pd.read_csv("numberCalc.csv")
num1 = st.number_input("Choose a number")
num2 = st.number_input("Choose another number")
if st.button("Submit"):
        numdict = {"Number1":[num1], "Number2":[num2], "Addition":[num1+num2], "Multiplication":[num1*num2]}
        numtable = pd.DataFrame(numdict)
        bothtables = pd.concat([csvlink, numtable],ignore_index=True)
        bothtables.to_csv("numberCalc.csv",index=False)