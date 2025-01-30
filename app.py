import streamlit as st

slider_value = st.slider("Select a value using the slider: ", min_value = 0, max_value = 50, value = 50)
st.write(f"You have selected {slider_value}")
