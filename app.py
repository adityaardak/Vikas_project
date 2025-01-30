import streamlit as st

fav_color = st.radio("pick any color", option = ["red", "blue", "green"])

st.write(f"You have selected {fav_color} color")
