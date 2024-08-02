import streamlit as st

st.header("Contact Me")

with st.form(key="my_forms"):
    user_email = st.text_input(label="Your email address")
    message = st.text_area(label="Your Message")
    button = st.form_submit_button(label="Submit")

    if button:
        message = message + user_email
        