import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/my_image1.jpg")

with col2:
    st.title("Debashish Talukder")
    content = """
    Hi, I am Debashish Talukder! I am a Cloud DevOps Engineer who is trying to build a webapp to showcase my projects.
    I love sports and soccer is my favorite game. I love spending my leisure with my family.
    """
    st.info(content)

info_content = """
Contact me for further info
"""
st.write(info_content)
