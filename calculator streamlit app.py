import streamlit as st

st.title("🧮 My Calculator")

# Enter two numbers
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

# Select an operation
operation = st.selectbox(
    "Choose an operation",
    ["Addition (+)", "Subtraction (-)",
     "Multiplication (*)", "Division (/)"]
)

# Calculate the result
if st.button("Calculate"):
    if operation == "Addition (+)":
        result = num1 + num2
    elif operation == "Subtraction (-)":
        result = num1 - num2
    elif operation == "Multiplication (*)":
        result = num1 * num2
    elif operation == "Division (/)":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Cannot divide by zero!")
            result = None

    if result is not None:
        st.success(f"Result: {result}")