import streamlit as st

user_age = st.number_input("Enter your age: ", min_value = 0, max_value = 60, value = 30)

st.write(f"Your age is {user_age}")
