import streamlit as st

color_list = ["red", "blue", "green"]

fav_color = st.radio("pick any color", option = color_list)

st.write(f"You have selected {fav_color} color")
