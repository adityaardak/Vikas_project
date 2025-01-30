import streamlit as st

slider_value_1 = st.slider("Select a value using the slider: ", min_value = 0, max_value = 50, value = 50)
slider_value_2 = st.slider("Select a value using the slider: ", min_value = 0, max_value = 50, value = 50)
st.write(f"You have selected {slider_value_1 + slider_value_2}")
