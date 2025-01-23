import streamlit as st
from send_email import send_email 

st.header("Contact Us")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    raw_message= st.text_area("Your message")
    #message = message + "\n" + user_email
    #to include a subject, we can use a f sring and a backslash

    message = f"""\
Subject: Testing email
From: {user_email}
{raw_message}
"""

    button =st.form_submit_button("Submit")
    print(button)
    if button:
        send_email(message)
        #to show a pop up notification in the app when email is sent.
        st.info("Email is successfully sent")
