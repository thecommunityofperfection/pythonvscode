"""
Simple Streamlit calculator for basic arithmetic operations.
"""

import streamlit as st
from typing import Callable

st.title("Streamlit Calculator")

OPERATIONS: dict[str, tuple[str, Callable]] = {
    "Addition": ('`+`', lambda a, b: a + b),
    "Subtraction": ('`-`', lambda a, b: a - b),
    "Multiplication": ('`*`', lambda a, b: a * b),
    "Division": ('`/`', lambda a, b: a / b if b != 0 else "Error: Cannot divide by zero"),
}

# Get input numbers
num1: float = st.number_input("Enter the first number:")
num2: float = st.number_input("Enter the second number:")


# Render buttons in a row
col1, col2, col3, col4 = st.columns(4)
buttons: dict[str, bool] = {
    "Addition": col1.button("➕ Add"),
    "Subtraction": col2.button("➖ Subtract"),
    "Multiplication": col3.button("✖ Multiply"),
    "Division": col4.button("➗ Divide"),
}

# Handle button clicks
for name, clicked in buttons.items():
    if clicked:
        symbol, func = OPERATIONS[name]
        result: int = func(num1, num2)

        st.table({
            "Num 1": [num1],
            "Operator": [symbol],
            "Num 2": [num2],
            "Result": [result],
        })
        break  # Stop after the first button press
    