import streamlit as st

# App title
st.title("Simple Quiz App")

# Question
st.header("Question 1")
st.write("What is the capital of France?")

# Options
answer = st.radio(
    "Choose your answer:",
    ("Berlin", "Madrid", "Paris", "Rome")
)

# Submit button
if st.button("Submit"):
    if answer == "Paris":
        st.success("Correct Answer!")
    else:
        st.error("Wrong Answer. Correct answer is Paris.")