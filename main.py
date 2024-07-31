import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/21.jpg", width=380)

with col2:
    st.title("Aryan Bhat")
    content = """
    Hi I am Aryan!, I am upcoming python programmer, and student at Rutgers University.
    """
    st.info(content)
