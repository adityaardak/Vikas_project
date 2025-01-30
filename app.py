import streamlit as st

user_name = st.text_input("Enter your username: ", placeholder = "Type Here...")

if user_name:
  st.write(f"Hello, {user_name}")
