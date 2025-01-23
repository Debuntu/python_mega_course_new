import streamlit as st
import pandas

st.set_page_config(
    page_title="Home",
    page_icon="👋",
)


st.header("The Best Company")

content = """
This is a dummy company created just for creating a dummy website. Just try to write something about the company or what it does.
"""

st.write(content)
st.subheader("Our Team")

df = pandas.read_csv("data.csv", sep=",")

col1, col2, col3 = st.columns(3)

with col1:
    for index, row in df[:4].iterrows():
        st.subheader((row["first name"].title()) + " " + (row["last name"].title()))
        st.write(row["role"].title())
        st.image("images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader((row["first name"].title()) + " " + (row["last name"].title()))
        st.write(row["role"].title())
        st.image("images/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader((row["first name"].title()) + " " + (row["last name"].title()))
        st.write(row["role"].title())
        st.image("images/" + row["image"])
