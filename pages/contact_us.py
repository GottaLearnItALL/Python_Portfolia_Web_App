import streamlit as st
from sendemail import send_email


st.header("Contact Me")

with st.form(key="my_forms"):
    user_email = st.text_input(label="Your email address")
    raw_message = st.text_area(label="Your Message")
    message = f"""\
Subject: New email from {user_email}
From: {user_email}
{raw_message}
"""
    button = st.form_submit_button(label="Submit")

    if button:
        message = message + user_email
        send_email(receiver=user_email, message=message)
        st.info("Email has been sent successfully")
