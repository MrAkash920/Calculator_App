import streamlit as st
import math
# Set page title and favicon
st.set_page_config(
    page_title="Calculator by Akash Singh",
    page_icon="🧮"
)

# Function to perform basic arithmetic operations
def perform_operation(num1, num2, operator):
    if operator == "Addition":
        return num1 + num2
    elif operator == "Subtraction":
        return num1 - num2
    elif operator == "Multiplication":
        return num1 * num2
    elif operator == "Division":
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2

# Function to calculate advanced operations
def calculate_advanced(num, operation):
    if operation == "Square":
        return num ** 2
    elif operation == "Square Root":
        return math.sqrt(num)
    elif operation == "Logarithm":
        return math.log10(num)
    elif operation == "Sine":
        return math.sin(math.radians(num))
    elif operation == "Cosine":
        return math.cos(math.radians(num))
    elif operation == "Tangent":
        return math.tan(math.radians(num))
    elif operation == "Factorial":
        return math.factorial(int(num))

# Main layout
st.title("🧮 Calculator")

calc_mode = st.radio("Select Calculator Mode", ("Basic", "Advanced"))

if calc_mode == "Basic":
    st.header("Basic Calculator")

    num1 = st.text_input("Enter the first number", value="0.0")
    num2 = st.text_input("Enter the second number", value="0.0")
    operation = st.selectbox("Select an operation", ("Addition", "Subtraction", "Multiplication", "Division"))

    if st.button("Calculate"):
        num1 = float(num1)
        num2 = float(num2)
        result = perform_operation(num1, num2, operation)
        st.success(f"Result: {num1} {operation} {num2} = {result}")

else:
    st.header("Advanced Calculator")

    advanced_operation = st.selectbox("Select an advanced operation", ("Square", "Square Root", "Logarithm", "Sine", "Cosine", "Tangent", "Factorial"))
    num_advanced = st.text_input("Enter a number for advanced operations", value="0.0")
    
    if st.button("Calculate Advanced"):
        num_advanced = float(num_advanced)
        result_advanced = calculate_advanced(num_advanced, advanced_operation)
        st.success(f"Result: {advanced_operation}({num_advanced}) = {result_advanced}")

# Optional: Add a history section to display previous calculations
st.sidebar.title("Calculation History")
history = st.sidebar.empty()

# Store calculation history
if "calc_history" not in st.session_state:
    st.session_state.calc_history = []

if st.button("Add to History"):
    if calc_mode == "Basic":
        calculation = f"{num1} {operation} {num2} = {result}"
    else:
        calculation = f"{advanced_operation}({num_advanced}) = {result_advanced}"
    st.session_state.calc_history.append(calculation)
    history.markdown("\n".join(st.session_state.calc_history))

# Reset the history
if st.button("Reset History"):
    st.session_state.calc_history = []
    history.empty()
