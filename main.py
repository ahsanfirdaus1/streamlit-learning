import streamlit as st
import pandas as pd

st.write("Hello World")

# capture the input value (text_input)
x = st.text_input("What's your favourite person?")

# showing the one that you've captured
st.write(f"Your favourite person is: {x}")

# create a button
is_clicked = st.button("Click Me Please")

# cretae a heading
st.write("## This is a H2 Title!")

# -----------------------
st.write("data praktikan pengulangan dummy")

data1 = pd.read_csv("data\data1.csv", sep=';')
st.write(data1)

