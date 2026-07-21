import streamlit as st
from send_email import send_email 
import pandas

df = pandas.read_csv("./topics.csv")
selections = df["topic"].to_list()

st.header("Contact Us")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")

    option = st.selectbox(
        "What topic do you want to discuss?",
        selections, 
        index=None,
        placeholder="Select topic to discuss",
    )
    
    raw_message= st.text_area("Your message")
    
    message = f"""\
Subject: New Contact Form Submission
From: {user_email}
Topic: {option}
{raw_message}
"""

    button =st.form_submit_button("Submit")
    print(button)
    if button:
        send_email(message)
        #to show a pop up notification in the app when email is sent.
        st.info("Email is successfully sent")
