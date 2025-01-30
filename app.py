import streamlit as st
import pandas as pd

st.header("This is a header")
st.subheader("This is a subheader")

data = {
  "Fruit": ["Apple", "Banana", "Cherry"],
  "Price": [12, 8, 2.5],
  "Quantity": [1, 2, 1]
}

df = pd.DataFrame(data)
st.dataframe(df)

